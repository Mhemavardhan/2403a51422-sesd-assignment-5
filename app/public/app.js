/**
 * FoodSwift - Client-Side Controller
 * SESD Assignment 5: Agile/Scrum Simulation
 * Student: M. Hemavardhan (2403A51422) - SR University
 */

const API_BASE = window.location.origin;

// State
let currentUser = null;
let authToken = localStorage.getItem("foodswift_token") || null;
let allRestaurants = [];
let activeRestaurant = null;
let cart = JSON.parse(localStorage.getItem("foodswift_cart") || "[]");
let activeOrderNumber = localStorage.getItem("foodswift_active_order") || null;

// Initial Scrum Backlog Data (Replicating exact items from DOCX screenshots)
const SCRUM_BACKLOG = [
  { id: 1, title: "Customer Login", type: "Parent Issue", status: "In Progress", priority: "High", points: 3, iter: "Iteration 1" },
  { id: 3, title: "Browse Restaurants and Menu", type: "Parent Issue", status: "Todo", priority: "High", points: 5, iter: "Iteration 1" },
  { id: 4, title: "Shopping Cart", type: "Parent Issue", status: "Todo", priority: "High", points: 5, iter: "Iteration 2" },
  { id: 5, title: "Online Payment", type: "Parent Issue", status: "Done", priority: "High", points: 8, iter: "Iteration 2" },
  { id: 6, title: "Order Tracking", type: "Parent Issue", status: "Todo", priority: "Medium", points: 5, iter: "Iteration 3" },
  
  // Sub-issues for Customer Login #1
  { id: 7, title: "Create Login UI", parentId: 1, type: "Sub-issue", status: "In Progress", priority: "High", points: 1, iter: "Iteration 1" },
  { id: 8, title: "Create Username Field", parentId: 1, type: "Sub-issue", status: "Todo", priority: "High", points: 1, iter: "Iteration 1" },
  { id: 9, title: "Create Password Field", parentId: 1, type: "Sub-issue", status: "Todo", priority: "High", points: 1, iter: "Iteration 1" },
  { id: 10, title: "Implement Login Validation", parentId: 1, type: "Sub-issue", status: "Testing", priority: "High", points: 1, iter: "Iteration 1" },
  { id: 11, title: "Display Error Message", parentId: 1, type: "Sub-issue", status: "Todo", priority: "Medium", points: 1, iter: "Iteration 1" },
  { id: 12, title: "Test Login", parentId: 1, type: "Sub-issue", status: "Todo", priority: "High", points: 1, iter: "Iteration 1" },

  // Sub-issues for Browse Restaurants #3
  { id: 13, title: "Create Restaurant Page", parentId: 3, type: "Sub-issue", status: "Todo", priority: "High", points: 1, iter: "Iteration 1" },
  { id: 14, title: "Display Restaurants", parentId: 3, type: "Sub-issue", status: "Todo", priority: "High", points: 1, iter: "Iteration 1" },
  { id: 15, title: "Create Menu Page", parentId: 3, type: "Sub-issue", status: "Todo", priority: "High", points: 1, iter: "Iteration 1" },
  { id: 16, title: "Display Food Items", parentId: 3, type: "Sub-issue", status: "Todo", priority: "High", points: 1, iter: "Iteration 1" },
  { id: 17, title: "Display Food Prices", parentId: 3, type: "Sub-issue", status: "Todo", priority: "Medium", points: 1, iter: "Iteration 1" },
  { id: 18, title: "Test Menu", parentId: 3, type: "Sub-issue", status: "Todo", priority: "High", points: 1, iter: "Iteration 1" }
];

// Document Ready Initialization
document.addEventListener("DOMContentLoaded", () => {
  checkAuth();
  fetchRestaurants();
  renderCart();
  renderScrumBoard();
  if (activeOrderNumber) {
    loadOrderTracking(activeOrderNumber);
  }
});

// Navigation Tab Switching
function switchTab(tabName) {
  document.querySelectorAll(".tab-content").forEach(el => el.classList.remove("active"));
  document.querySelectorAll(".nav-btn").forEach(el => el.classList.remove("active"));

  const targetTab = document.getElementById(`tab-${tabName}`);
  const targetBtn = document.getElementById(`nav-${tabName}`);
  if (targetTab) targetTab.classList.add("active");
  if (targetBtn) targetBtn.classList.add("active");
}

// RESTAURANTS & MENUS
async function fetchRestaurants() {
  const grid = document.getElementById("restaurant-grid");
  try {
    const res = await fetch(`${API_BASE}/api/restaurants`);
    const data = await res.json();
    if (data.success) {
      allRestaurants = data.restaurants;
      renderRestaurants(allRestaurants);
    }
  } catch (err) {
    console.error("Error fetching restaurants:", err);
    grid.innerHTML = `<p class="error-msg">Failed to connect to server backend.</p>`;
  }
}

function renderRestaurants(restaurants) {
  const grid = document.getElementById("restaurant-grid");
  if (!restaurants.length) {
    grid.innerHTML = `<p class="empty-state">No matching restaurants found.</p>`;
    return;
  }

  grid.innerHTML = restaurants.map(r => `
    <div class="restaurant-card" onclick="openMenuModal(${r.id})">
      <div class="rest-card-banner">
        <span>${r.image_emoji || '🍲'}</span>
      </div>
      <div class="rest-card-info">
        <div class="rest-header-row">
          <span class="rest-name">${escapeHtml(r.name)}</span>
          <span class="rest-rating">⭐ ${r.rating}</span>
        </div>
        <div class="rest-cuisine">${escapeHtml(r.cuisine)}</div>
        <div class="rest-footer">
          <span>⏱️ ${r.delivery_time_mins} mins</span>
          <span>🛵 ₹${r.delivery_fee} Delivery</span>
        </div>
      </div>
    </div>
  `).join("");
}

function filterRestaurants() {
  const query = document.getElementById("restaurant-search").value.toLowerCase();
  const filtered = allRestaurants.filter(r => 
    r.name.toLowerCase().includes(query) || 
    r.cuisine.toLowerCase().includes(query)
  );
  renderRestaurants(filtered);
}

function filterCuisine(cuisine, pill) {
  document.querySelectorAll(".filter-pill").forEach(p => p.classList.remove("active"));
  pill.classList.add("active");

  if (cuisine === "all") {
    renderRestaurants(allRestaurants);
  } else {
    const filtered = allRestaurants.filter(r => r.cuisine.toLowerCase().includes(cuisine.toLowerCase()));
    renderRestaurants(filtered);
  }
}

// MENU MODAL
async function openMenuModal(restaurantId) {
  const modal = document.getElementById("menu-modal");
  const list = document.getElementById("menu-items-list");
  list.innerHTML = `<div class="loading-spinner">Loading delicious menu...</div>`;
  modal.classList.add("active");

  try {
    const res = await fetch(`${API_BASE}/api/restaurants/${restaurantId}/menu`);
    const data = await res.json();
    if (data.success) {
      activeRestaurant = data.restaurant;
      document.getElementById("menu-modal-title").innerHTML = `
        <h2>${escapeHtml(activeRestaurant.name)}</h2>
        <p>${escapeHtml(activeRestaurant.cuisine)} • 📍 ${escapeHtml(activeRestaurant.address)}</p>
      `;

      list.innerHTML = data.menu.map(item => `
        <div class="menu-item-row">
          <div class="item-left">
            <span class="veg-icon ${item.is_veg ? '' : 'non-veg'}">
              <span class="veg-dot"></span>
            </span>
            <span class="item-name">${escapeHtml(item.name)}</span>
            <p class="item-desc">${escapeHtml(item.description)}</p>
            <div class="item-price">₹${item.price.toFixed(2)}</div>
          </div>
          <div>
            <button class="btn-add-item" onclick="addToCart(${item.id}, '${escapeHtml(item.name)}', ${item.price}, ${restaurantId})">
              + Add to Cart
            </button>
          </div>
        </div>
      `).join("");
    }
  } catch (err) {
    list.innerHTML = `<p class="error">Failed to load menu items.</p>`;
  }
}

function closeMenuModal() {
  document.getElementById("menu-modal").classList.remove("active");
}

// SHOPPING CART
function addToCart(itemId, name, price, restaurantId) {
  // If cart has items from different restaurant, warn and reset
  if (cart.length > 0 && cart[0].restaurantId !== restaurantId) {
    if (!confirm("Your cart has items from another restaurant. Clear cart and add this item?")) {
      return;
    }
    cart = [];
  }

  const existing = cart.find(i => i.id === itemId);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ id: itemId, name, price, quantity: 1, restaurantId });
  }

  saveCart();
  renderCart();
  showToast(`Added "${name}" to basket!`);
}

function updateCartQty(itemId, delta) {
  const item = cart.find(i => i.id === itemId);
  if (!item) return;

  item.quantity += delta;
  if (item.quantity <= 0) {
    cart = cart.filter(i => i.id !== itemId);
  }
  saveCart();
  renderCart();
}

function saveCart() {
  localStorage.setItem("foodswift_cart", JSON.stringify(cart));
}

function renderCart() {
  const container = document.getElementById("cart-drawer-items");
  const countBadge = document.getElementById("cart-counter");
  const subtotalEl = document.getElementById("cart-subtotal");
  const totalEl = document.getElementById("cart-total-payable");
  const btnCheckout = document.getElementById("btn-checkout");

  const totalCount = cart.reduce((acc, it) => acc + it.quantity, 0);
  countBadge.textContent = totalCount;

  if (cart.length === 0) {
    container.innerHTML = `<div class="empty-cart-msg">Your food basket is empty. Select dishes to get started!</div>`;
    subtotalEl.textContent = `₹0.00`;
    totalEl.textContent = `₹0.00`;
    btnCheckout.disabled = true;
    return;
  }

  btnCheckout.disabled = false;
  let subtotal = 0;

  container.innerHTML = cart.map(it => {
    const itemTotal = it.price * it.quantity;
    subtotal += itemTotal;
    return `
      <div class="cart-item-card">
        <div>
          <strong>${escapeHtml(it.name)}</strong>
          <div class="item-price">₹${itemTotal.toFixed(2)}</div>
        </div>
        <div class="cart-qty-ctrl">
          <button class="qty-btn" onclick="updateCartQty(${it.id}, -1)">−</button>
          <span>${it.quantity}</span>
          <button class="qty-btn" onclick="updateCartQty(${it.id}, 1)">+</button>
        </div>
      </div>
    `;
  }).join("");

  const deliveryFee = 40.0;
  subtotalEl.textContent = `₹${subtotal.toFixed(2)}`;
  totalEl.textContent = `₹${(subtotal + deliveryFee).toFixed(2)}`;
}

function toggleCart() {
  document.getElementById("cart-drawer").classList.toggle("open");
}

// CHECKOUT & MOCK PAYMENT
function openCheckoutModal() {
  if (cart.length === 0) return;
  if (!currentUser) {
    openAuthModal();
    return;
  }

  document.getElementById("cart-drawer").classList.remove("open");
  const modal = document.getElementById("checkout-modal");
  
  let subtotal = cart.reduce((acc, it) => acc + (it.price * it.quantity), 0);
  const delivery = 40.0;
  document.getElementById("modal-subtotal").textContent = `₹${subtotal.toFixed(2)}`;
  document.getElementById("modal-delivery").textContent = `₹${delivery.toFixed(2)}`;
  document.getElementById("modal-grand-total").textContent = `₹${(subtotal + delivery).toFixed(2)}`;

  modal.classList.add("active");
}

function closeCheckoutModal() {
  document.getElementById("checkout-modal").classList.remove("active");
}

async function handleCheckoutSubmit(e) {
  e.preventDefault();
  const address = document.getElementById("checkout-address").value;
  const payMethod = document.querySelector('input[name="paymethod"]:checked').value;
  const restaurantId = cart[0]?.restaurantId || 1;

  const btn = document.getElementById("btn-pay-now");
  btn.disabled = true;
  btn.textContent = "Processing Mock Payment...";

  try {
    const res = await fetch(`${API_BASE}/api/checkout`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${authToken}`
      },
      body: JSON.stringify({
        restaurant_id: restaurantId,
        items: cart,
        payment_method: payMethod,
        delivery_address: address
      })
    });

    const data = await res.json();
    btn.disabled = false;
    btn.textContent = "🔒 Pay & Place Order (Mock Verification)";

    if (data.success) {
      cart = [];
      saveCart();
      renderCart();
      closeCheckoutModal();
      activeOrderNumber = data.order_number;
      localStorage.setItem("foodswift_active_order", activeOrderNumber);

      alert(`✅ Mock Payment Successful!\nOrder #${data.order_number}\nTransaction ID: ${data.transaction_id}\nTotal: ₹${data.total_amount}`);
      
      switchTab("tracking");
      loadOrderTracking(data.order_number);
    } else {
      alert(`Error: ${data.error || "Checkout failed"}`);
    }
  } catch (err) {
    btn.disabled = false;
    btn.textContent = "🔒 Pay & Place Order (Mock Verification)";
    alert("Connection error during checkout");
  }
}

// REAL-TIME ORDER TRACKING
async function loadOrderTracking(orderNumber) {
  const card = document.getElementById("active-order-tracking");
  const noState = document.getElementById("no-tracking-state");

  try {
    const res = await fetch(`${API_BASE}/api/orders/${orderNumber}/track`);
    const data = await res.json();
    if (data.success) {
      noState.classList.add("hidden");
      card.classList.remove("hidden");

      const ord = data.order;
      document.getElementById("track-ord-num").textContent = ord.order_number;
      document.getElementById("track-ord-restaurant").textContent = `${ord.image_emoji || ''} ${ord.restaurant_name}`;
      document.getElementById("track-ord-eta").textContent = `${ord.delivery_time_mins || 30} Mins`;
      document.getElementById("track-ord-amount").textContent = `₹${ord.total_amount.toFixed(2)}`;

      // Update Stepper
      const stages = data.stages;
      const idx = data.current_stage_index;
      const pct = Math.min(100, Math.round((idx / (stages.length - 1)) * 100));
      document.getElementById("step-progress-fill").style.width = `${pct}%`;

      stages.forEach((stage, sIdx) => {
        const node = document.getElementById(`step-${sIdx}`);
        if (!node) return;
        node.classList.remove("completed", "active");
        if (sIdx < idx) {
          node.classList.add("completed");
        } else if (sIdx === idx) {
          node.classList.add("active");
        }
      });

      // Advance button disable if delivered
      const btnAdvance = document.getElementById("btn-advance-status");
      if (ord.order_status === "Delivered") {
        btnAdvance.disabled = true;
        btnAdvance.textContent = "✓ Order Delivered";
      } else {
        btnAdvance.disabled = false;
        btnAdvance.textContent = `⚡ Advance from "${ord.order_status}" to Next Stage`;
      }

      // Render items summary
      const itemsEl = document.getElementById("track-items-summary");
      itemsEl.innerHTML = `
        <h4 style="margin-top: 1.5rem; margin-bottom: 0.5rem;">Order Items:</h4>
        <div style="background: #f8fafc; padding: 1rem; border-radius: 8px;">
          ${ord.items.map(it => `
            <div style="display:flex; justify-content:space-between; margin-bottom:0.25rem; font-size:0.85rem;">
              <span>${it.quantity}x ${escapeHtml(it.item_name)}</span>
              <strong>₹${(it.price * it.quantity).toFixed(2)}</strong>
            </div>
          `).join("")}
          <div style="border-top: 1px dashed #cbd5e1; padding-top: 0.5rem; margin-top: 0.5rem; display: flex; justify-content: space-between; font-weight: bold;">
            <span>Payment Method: ${ord.payment_method} (${ord.payment_status})</span>
            <span>Txn: ${ord.transaction_id || 'MOCK-TXN'}</span>
          </div>
        </div>
      `;
    } else {
      alert("Order not found");
    }
  } catch (err) {
    console.error("Tracking error:", err);
  }
}

function lookupOrderTracking() {
  const val = document.getElementById("track-order-input").value.trim();
  if (val) {
    activeOrderNumber = val;
    loadOrderTracking(val);
  }
}

async function advanceOrderStatus() {
  if (!activeOrderNumber) return;
  try {
    const res = await fetch(`${API_BASE}/api/orders/${activeOrderNumber}/advance`, { method: "POST" });
    const data = await res.json();
    if (data.success) {
      loadOrderTracking(activeOrderNumber);
    }
  } catch (err) {
    alert("Failed to advance order state");
  }
}

// SCRUM DASHBOARD & KANBAN RENDERING
function renderScrumBoard() {
  // Columns
  const colTodo = document.getElementById("cards-todo");
  const colProg = document.getElementById("cards-progress");
  const colTest = document.getElementById("cards-testing");
  const colDone = document.getElementById("cards-done");

  const cardsByStatus = { "Todo": [], "In Progress": [], "Testing": [], "Done": [] };
  SCRUM_BACKLOG.forEach(item => {
    if (cardsByStatus[item.status]) {
      cardsByStatus[item.status].push(item);
    }
  });

  const makeCard = (item) => `
    <div class="kanban-card">
      <div class="card-top">
        <span>#${item.id}</span>
        <span>${item.type}</span>
      </div>
      <div class="card-title">${escapeHtml(item.title)}</div>
      <div class="card-tags">
        <span class="tag-badge ${item.priority === 'High' ? 'tag-high' : 'tag-med'}">${item.priority}</span>
        <span class="tag-badge tag-points">${item.points} pts</span>
        <span class="tag-badge tag-iter">${item.iter}</span>
      </div>
    </div>
  `;

  colTodo.innerHTML = cardsByStatus["Todo"].map(makeCard).join("");
  colProg.innerHTML = cardsByStatus["In Progress"].map(makeCard).join("");
  colTest.innerHTML = cardsByStatus["Testing"].map(makeCard).join("");
  colDone.innerHTML = cardsByStatus["Done"].map(makeCard).join("");

  document.getElementById("count-todo").textContent = cardsByStatus["Todo"].length;
  document.getElementById("count-progress").textContent = cardsByStatus["In Progress"].length;
  document.getElementById("count-testing").textContent = cardsByStatus["Testing"].length;
  document.getElementById("count-done").textContent = cardsByStatus["Done"].length;

  // Table rows
  const tbody = document.getElementById("scrum-table-body");
  tbody.innerHTML = SCRUM_BACKLOG.map(item => `
    <tr>
      <td><strong>#${item.id}</strong></td>
      <td>
        ${item.parentId ? '&nbsp;&nbsp;&nbsp;&nbsp;↳ ' : '<strong>'}${escapeHtml(item.title)}${item.parentId ? '' : '</strong>'}
      </td>
      <td>M. Hemavardhan</td>
      <td><span class="tag-badge" style="background:#e2e8f0; color:#334155;">${item.status}</span></td>
      <td><span class="tag-badge ${item.priority === 'High' ? 'tag-high' : 'tag-med'}">${item.priority}</span></td>
      <td><strong>${item.points}</strong></td>
      <td><span class="tag-badge tag-iter">${item.iter}</span></td>
    </tr>
  `).join("");
}

// AUTHENTICATION
async function checkAuth() {
  if (!authToken) {
    updateAuthUI(null);
    return;
  }
  try {
    const res = await fetch(`${API_BASE}/api/me`, {
      headers: { "Authorization": `Bearer ${authToken}` }
    });
    const data = await res.json();
    if (data.success) {
      currentUser = data.user;
      updateAuthUI(currentUser);
    } else {
      logout();
    }
  } catch (e) {
    updateAuthUI(null);
  }
}

function updateAuthUI(user) {
  const profileBadge = document.getElementById("user-profile-badge");
  const btnAuth = document.getElementById("btn-open-auth");
  const userNameEl = document.getElementById("logged-user-name");

  if (user) {
    profileBadge.classList.remove("hidden");
    btnAuth.classList.add("hidden");
    userNameEl.textContent = user.name;
  } else {
    profileBadge.classList.add("hidden");
    btnAuth.classList.remove("hidden");
  }
}

function openAuthModal() {
  document.getElementById("auth-modal").classList.add("active");
}

function closeAuthModal() {
  document.getElementById("auth-modal").classList.remove("active");
}

function toggleAuthMode(mode) {
  const loginForm = document.getElementById("login-form");
  const regForm = document.getElementById("register-form");
  const tabLogin = document.getElementById("tab-login-btn");
  const tabReg = document.getElementById("tab-register-btn");

  if (mode === "login") {
    loginForm.classList.remove("hidden");
    regForm.classList.add("hidden");
    tabLogin.classList.add("active");
    tabReg.classList.remove("active");
  } else {
    loginForm.classList.add("hidden");
    regForm.classList.remove("hidden");
    tabLogin.classList.remove("active");
    tabReg.classList.add("active");
  }
}

async function handleLogin(e) {
  e.preventDefault();
  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;
  const errBox = document.getElementById("login-error");

  try {
    const res = await fetch(`${API_BASE}/api/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });
    const data = await res.json();
    if (data.success) {
      authToken = data.token;
      currentUser = data.user;
      localStorage.setItem("foodswift_token", authToken);
      updateAuthUI(currentUser);
      closeAuthModal();
      showToast(`Welcome back, ${currentUser.name}!`);
    } else {
      errBox.textContent = data.error || "Login failed";
      errBox.classList.remove("hidden");
    }
  } catch (err) {
    errBox.textContent = "Server communication failure";
    errBox.classList.remove("hidden");
  }
}

async function handleRegister(e) {
  e.preventDefault();
  const name = document.getElementById("reg-name").value;
  const email = document.getElementById("reg-email").value;
  const phone = document.getElementById("reg-phone").value;
  const address = document.getElementById("reg-address").value;
  const password = document.getElementById("reg-password").value;
  const errBox = document.getElementById("register-error");

  try {
    const res = await fetch(`${API_BASE}/api/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, phone, address, password })
    });
    const data = await res.json();
    if (data.success) {
      authToken = data.token;
      currentUser = data.user;
      localStorage.setItem("foodswift_token", authToken);
      updateAuthUI(currentUser);
      closeAuthModal();
      showToast(`Account created! Welcome ${currentUser.name}!`);
    } else {
      errBox.textContent = data.error || "Registration failed";
      errBox.classList.remove("hidden");
    }
  } catch (err) {
    errBox.textContent = "Server communication failure";
    errBox.classList.remove("hidden");
  }
}

function logout() {
  authToken = null;
  currentUser = null;
  localStorage.removeItem("foodswift_token");
  updateAuthUI(null);
  showToast("Logged out successfully");
}

function showToast(msg) {
  const toast = document.createElement("div");
  toast.className = "toast-notification";
  toast.textContent = msg;
  toast.style.cssText = `
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: #0f172a;
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3);
    z-index: 999;
    font-size: 0.9rem;
    font-weight: 600;
  `;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 3000);
}

function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
