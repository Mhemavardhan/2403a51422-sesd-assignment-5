# Document 02: Product Backlog & User Stories

**Project Title:** Online Food Ordering System — Agile/Scrum Simulation  
**Student Name:** M. Hemavardhan (Hall Ticket: 2403A51422)  
**Course Code:** 24CS301PC311 | Academic Year: 2026–2027  
**Department of CSE | School of CS&AI | SR University**  

---

## 1. Product Backlog Structure & Estimation Overview

The Product Backlog was groomed and estimated using **Planning Poker** with the Fibonacci sequence ($1, 2, 3, 5, 8, 13$). A total of **26 Story Points** across 5 primary epic user stories and 12 granular sub-issues were defined, directly mirroring the GitHub Projects workflow demonstrated in the reference assignment.

### Estimation Scale:
* **1 Point:** Trivial UI component, field, or validation unit test.
* **3 Points:** Self-contained full-stack feature with basic data persistence.
* **5 Points:** Moderate complexity feature with dynamic interactions and database relationships.
* **8 Points:** High complexity module involving multi-state simulation or financial transaction workflow.

---

## 2. Comprehensive Product Backlog Table

| Issue # | Type | Title / User Story | Priority | Story Points | Iteration | GitHub Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **#1** | Parent | **Customer Login and Registration** | High | 3 | Iteration 1 | In Progress |
| ↳ #7 | Sub-issue | Create Login UI | High | 1 | Iteration 1 | In Progress |
| ↳ #8 | Sub-issue | Create Username Field | High | 1 | Iteration 1 | Todo |
| ↳ #9 | Sub-issue | Create Password Field | High | 1 | Iteration 1 | Todo |
| ↳ #10 | Sub-issue | Implement Login Validation | High | 1 | Iteration 1 | Testing |
| ↳ #11 | Sub-issue | Display Error Message | Medium | 1 | Iteration 1 | Todo |
| ↳ #12 | Sub-issue | Test Login (Unit & Integration) | High | 1 | Iteration 1 | Todo |
| **#3** | Parent | **Browse Restaurants and Menus** | High | 5 | Iteration 1 | Todo |
| ↳ #13 | Sub-issue | Create Restaurant Page | High | 1 | Iteration 1 | Todo |
| ↳ #14 | Sub-issue | Display Restaurants List & Ratings | High | 1 | Iteration 1 | Todo |
| ↳ #15 | Sub-issue | Create Menu Page & Categories | High | 1 | Iteration 1 | Todo |
| ↳ #16 | Sub-issue | Display Food Items with Veg/Non-Veg Tag | High | 1 | Iteration 1 | Todo |
| ↳ #17 | Sub-issue | Display Food Prices & Descriptions | Medium | 1 | Iteration 1 | Todo |
| ↳ #18 | Sub-issue | Test Menu Browsing | High | 1 | Iteration 1 | Todo |
| **#4** | Parent | **Shopping Cart Management** | High | 5 | Iteration 2 | Todo |
| **#5** | Parent | **Online Payment (Mock Gateway)** | High | 8 | Iteration 2 | Done |
| **#6** | Parent | **Real-Time Order Tracking** | Medium | 5 | Iteration 3 | Todo |

**Total Estimated Backlog Effort:** 26 Story Points

---

## 3. Detailed User Stories & Acceptance Criteria

### User Story #1: Customer Login and Registration (Parent #1)
* **Narrative:** *As a university student, I want to register and securely log in so that I can personalize my orders, view order history, and save my campus delivery address.*
* **Acceptance Criteria:**
  1. Users can register with valid name, email, phone, and delivery address.
  2. Passwords must be at least 6 characters and stored only after salted SHA-256 hashing.
  3. Duplicate registration attempts using an existing email return an informative HTTP 409 error.
  4. Successful authentication issues an active session token and displays the user's name on the navigation bar.

### User Story #3: Browse Restaurants and Menus (Parent #3)
* **Narrative:** *As a customer, I want to browse available restaurants and view their menu items with prices and descriptions so that I can decide what food to purchase.*
* **Acceptance Criteria:**
  1. Display a responsive grid of restaurants with cuisine tags, ratings, delivery times, and delivery fees.
  2. Provide live search filtering by restaurant name, cuisine type, or dish.
  3. Clicking a restaurant opens its categorized menu list with Veg/Non-Veg icons, prices, and descriptions.
  4. Each item includes a direct "+ Add to Cart" action.

### User Story #4: Shopping Cart Management (Parent #4)
* **Narrative:** *As a hungry student, I want to add, adjust quantities, and remove items in my food basket so that I can review my order total before paying.*
* **Acceptance Criteria:**
  1. Adding an item increments the cart badge counter on the navigation bar.
  2. Quantity can be incremented (`+`) or decremented (`−`), with items automatically removed if quantity reaches 0.
  3. Subtotal, delivery partner fee, and total payable amount calculate automatically.
  4. Preventing mixed orders from different restaurants without user confirmation.

### User Story #5: Online Payment Simulation (Parent #5)
* **Narrative:** *As a buyer, I want to select a payment method (UPI, Card, COD) and complete payment verification so that my order is confirmed instantly.*
* **Acceptance Criteria:**
  1. Checkout form validates delivery address and selected payment mode.
  2. Simulated gateway generates a unique mock transaction reference (`TXN-MOCK-XXXXXXXXXX`).
  3. Order is marked with `Payment Status: Success (Mock Paid)`.
  4. Cart is cleared upon successful order placement and a confirmation alert is displayed.

### User Story #6: Real-Time Order Tracking (Parent #6)
* **Narrative:** *As a customer waiting for food, I want to track my order's live status through progressive milestones so that I know when my meal will arrive.*
* **Acceptance Criteria:**
  1. Order tracking displays Order Number, Restaurant, Estimated Time, and itemized receipt.
  2. Visual 5-stage progress stepper: `Placed` &rarr; `Confirmed` &rarr; `Preparing` &rarr; `Out for Delivery` &rarr; `Delivered`.
  3. REST API `/api/orders/:id/track` provides accurate milestone indices.
  4. Interactive test controller allows examiner/user to advance simulation stages and observe real-time DOM updates.

---

## 4. Scrum Governance Criteria

### Definition of Ready (DoR):
A User Story is Ready to enter a Sprint Backlog when:
* Clearly formulated in standard Persona-Need-Value narrative format.
* Specific, testable Acceptance Criteria are defined.
* Story points are assigned by the Scrum development team.
* External dependencies (e.g., database schema, mock endpoints) are identified.

### Definition of Done (DoD):
A User Story is marked as Done when:
* Code is written, cleanly formatted, and adhering to architectural boundaries.
* Unit and integration test cases pass 100% with no regression failures.
* Code has been committed to Git with descriptive conventional commit messages.
* Feature is verified in the working web application increment.
* Scrum board status is transitioned to `Done`.
