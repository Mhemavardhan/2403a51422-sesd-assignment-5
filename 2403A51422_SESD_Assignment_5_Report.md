# SR UNIVERSITY
### SCHOOL OF COMPUTER SCIENCE & ARTIFICIAL INTELLIGENCE
### DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING

---

# SOFTWARE ENGINEERING AND SYSTEM DESIGN (SESD)
## LAB / RECITATION ASSIGNMENT 05 / 12
### AGILE / SCRUM SIMULATION: ONLINE FOOD ORDERING SYSTEM

---

### STUDENT INFORMATION & SUBMISSION METADATA

* **Student Name:** **M. Hemavardhan**
* **Hall Ticket Number:** **2403A51422**
* **Course Code:** **24CS301PC311**
* **Course Title:** Software Engineering and System Design
* **Academic Year:** 2026–2027
* **Year & Semester:** III Year / I Semester (III/I SEM)
* **Regulation:** R24
* **Assignment Number:** 05/12
* **Date of Assignment:** 08-09-2026
* **Date of Submission:** 29-10-2026
* **Course Coordinator:** Dr. N. Sharmila Banu
* **Course Instructor:** Dr. Asha S
* **GitHub Repository:** `https://github.com/Mhemavardhan/2403a51422-sesd-assignment-5`

---

## 1. Title Page & Official Metadata

This laboratory submission report represents the comprehensive technical and Agile project management deliverables for Assignment 5 of the Software Engineering and System Design course at SR University. The assignment simulates a full industry-grade Scrum lifecycle for **Case Study 1: Online Food Ordering Application**, encompassing product backlog creation, Planning Poker relative story point estimation, 3-sprint timeboxed iteration planning, custom fields implementation in GitHub Projects, working full-stack software development, automated testing, sprint retrospectives, and empirical process reflections.

---

## 2. Assignment Objectives

The key learning and operational objectives of Assignment 5 include:
1. **Agile Methodological Competence:** Master the application of Scrum ceremonies, artifacts, and roles in software development.
2. **Backlog Grooming & User Story Formulation:** Decompose complex functional requirements into clear, testable User Stories adhering to the INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable) with explicit Acceptance Criteria.
3. **Agile Estimation:** Apply Planning Poker and relative sizing using the Fibonacci sequence to quantify development effort and team velocity.
4. **Tool Mastery via GitHub Projects:** Recreate and optimize a modern GitHub Projects Scrum board featuring customized workflows, iteration sprints, Kanban views, and sub-issue task hierarchies.
5. **Software Engineering Delivery:** Build, test, and package a working, secure, potentially shippable full-stack increment.

---

## 3. Problem Statement

### Case Study 1 — Online Food Ordering App
> *"Design an application that allows users to browse restaurants, add food items to a cart, pay online, and track their orders in real time.*  
> *Deliverables: Backlog with features like Login, Browse Menu, Cart, Payment, Order Tracking."*

In modern university campuses and urban communities, students and staff encounter significant inefficiencies in dining operations, including extended physical queues during peak meal breaks, fragmented communication with kitchen vendors, lack of transparent order status updates, and unreliable payment processing. The objective of this project is to simulate and engineer **FoodSwift**, a streamlined, responsive, full-stack food ordering solution that guarantees rapid meal discovery, customized ordering, secure simulated digital payments, and real-time order lifecycle visibility.

---

## 4. Product Vision

* **For:** University students, faculty, and local campus community members.
* **Who:** Require fast, reliable, and convenient food ordering without waiting in dining lines.
* **The Product:** **FoodSwift** is an intuitive, web-based Online Food Ordering System.
* **That Provides:** Instant menu exploration, dynamic cart customization, simulated UPI/Card digital payment verification, and real-time 5-stage order progression tracking.
* **Unlike:** Traditional offline calling, paper menus, or complex commercial applications with heavy overhead.
* **Our Product:** Offers zero latency, campus-tailored delivery scheduling, full pricing transparency, and an Agile iterative architecture designed to continuously incorporate customer feedback.

---

## 5. Functional Requirements

1. **User Authentication & Profile Management:**
   - User registration with name, email, phone number, and campus delivery address.
   - Secure authentication utilizing salted SHA-256 cryptographic password hashing.
   - Session-based state persistence and profile display on the application header.
2. **Restaurant Directory & Menu Browsing:**
   - Categorized restaurant listings with cuisine tags, delivery ratings, estimated delivery times, and delivery fees.
   - Real-time search and filter capabilities by dish name, restaurant, or cuisine category.
   - Modal menu explorer highlighting dietary tags (Vegetarian / Non-Vegetarian), item descriptions, and transparent pricing.
3. **Shopping Cart Management:**
   - Add dishes directly to a persistent cart drawer.
   - Dynamic quantity increment (`+`) and decrement (`−`) controls with automatic zero-quantity removal.
   - Real-time subtotal, delivery fee, and grand total recalculation.
   - Cross-restaurant cart safeguards with user prompt confirmation.
4. **Simulated Payment Gateway:**
   - Multi-option payment selector supporting simulated UPI (GPay/PhonePe/Paytm), Mock Credit/Debit Card, and Cash on Delivery.
   - Server-side order verification with unique transaction ID generation (`TXN-MOCK-XXXXXXXXXX`).
   - Order confirmation with automatic cart clearing.
5. **Real-Time Order Tracking:**
   - Visual 5-stage progress stepper: `Placed` &rarr; `Confirmed` &rarr; `Preparing` &rarr; `Out for Delivery` &rarr; `Delivered`.
   - REST API tracking endpoint (`/api/orders/:id/track`) returning live milestone status and itemized receipts.
   - Examiner/user simulation controller to advance delivery stages interactively during evaluation.

---

## 6. User Stories and Acceptance Criteria

### User Story 1: Customer Login and Registration (Issue #1)
* **Narrative:** *As a student customer, I want to register and log in to the food ordering platform so that I can manage my orders and save my delivery details.*
* **Priority:** High | **Story Points:** 3 | **Iteration:** Iteration 1
* **Acceptance Criteria:**
  - System accepts valid student email addresses and passwords with a minimum of 6 characters.
  - Passwords are salted and stored exclusively as SHA-256 hashes.
  - Duplicate registration attempts return an HTTP 409 conflict response.
  - Successful authentication grants an active session and displays the user's name on the navigation bar.

### User Story 2: Browse Restaurants and Menus (Issue #3)
* **Narrative:** *As a customer, I want to browse restaurants and view their categorized food menus so that I can select meals that match my preferences and dietary restrictions.*
* **Priority:** High | **Story Points:** 5 | **Iteration:** Iteration 1
* **Acceptance Criteria:**
  - Displays restaurant cards featuring ratings, cuisine tags, and delivery time.
  - Clicking a restaurant opens its categorized menu list with clear Veg/Non-Veg indicators.
  - Search filter instantly narrows displayed restaurants and dishes.
  - Each dish includes a direct "+ Add to Cart" action.

### User Story 3: Shopping Cart Management (Issue #4)
* **Narrative:** *As a hungry user, I want to add dishes to a slide-in food cart and adjust quantities so that I can verify my selections before placing an order.*
* **Priority:** High | **Story Points:** 5 | **Iteration:** Iteration 2
* **Acceptance Criteria:**
  - Cart counter badge updates synchronously across the entire application interface.
  - Quantities can be adjusted dynamically with instantaneous total recalculations.
  - Empty cart state disables the checkout trigger and prompts the user to add food items.
  - Items are persisted in local storage across browser refreshes.

### User Story 4: Online Payment Simulation (Issue #5)
* **Narrative:** *As a customer, I want to select a payment method and submit payment details so that my order is verified and confirmed immediately.*
* **Priority:** High | **Story Points:** 8 | **Iteration:** Iteration 2
* **Acceptance Criteria:**
  - Validates delivery address and payment mode selection.
  - Generates a unique mock transaction identifier.
  - Records the order in the database with status `Success (Mock Paid)`.
  - Clears the cart and displays a confirmation dialog with order details.

### User Story 5: Real-Time Order Tracking (Issue #6)
* **Narrative:** *As an expectant customer, I want to view my order's live preparation and delivery status so that I know exactly when to receive my meal.*
* **Priority:** Medium | **Story Points:** 5 | **Iteration:** Iteration 3
* **Acceptance Criteria:**
  - Displays an interactive 5-stage progress stepper reflecting current status.
  - Highlights active milestones with primary accent coloring and completed milestones with green checkmarks.
  - Displays order number, restaurant details, delivery address, and itemized receipt.
  - Allows immediate stage advancement via an embedded evaluation simulation button.

---

## 7. Product Backlog Table

| Issue # | Type | Item Title / User Story | Priority | Points | Iteration | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **#1** | Epic | **Customer Login and Registration** | High | 3 | Iteration 1 | In Progress |
| ↳ #7 | Task | Create Login UI | High | 1 | Iteration 1 | In Progress |
| ↳ #8 | Task | Create Username Field | High | 1 | Iteration 1 | Todo |
| ↳ #9 | Task | Create Password Field | High | 1 | Iteration 1 | Todo |
| ↳ #10 | Task | Implement Login Validation | High | 1 | Iteration 1 | Testing |
| ↳ #11 | Task | Display Error Message | Medium | 1 | Iteration 1 | Todo |
| ↳ #12 | Task | Test Login (Unit & Integration) | High | 1 | Iteration 1 | Todo |
| **#3** | Epic | **Browse Restaurants and Menus** | High | 5 | Iteration 1 | Todo |
| ↳ #13 | Task | Create Restaurant Page | High | 1 | Iteration 1 | Todo |
| ↳ #14 | Task | Display Restaurants List & Ratings | High | 1 | Iteration 1 | Todo |
| ↳ #15 | Task | Create Menu Page & Categories | High | 1 | Iteration 1 | Todo |
| ↳ #16 | Task | Display Food Items with Veg/Non-Veg Tag | High | 1 | Iteration 1 | Todo |
| ↳ #17 | Task | Display Food Prices & Descriptions | Medium | 1 | Iteration 1 | Todo |
| ↳ #18 | Task | Test Menu Browsing | High | 1 | Iteration 1 | Todo |
| **#4** | Epic | **Shopping Cart Management** | High | 5 | Iteration 2 | Todo |
| **#5** | Epic | **Online Payment (Mock Gateway)** | High | 8 | Iteration 2 | Done |
| **#6** | Epic | **Real-Time Order Tracking** | Medium | 5 | Iteration 3 | Todo |

**Total Estimated Backlog Velocity:** 26 Story Points

---

## 8. Sprint Planning and Task Allocation

The project was planned across three 2-week timeboxed iterations:

### Sprint 1: Foundation & Discovery (Oct 14 – Oct 27)
* **Goal:** Deliver user authentication, core relational schema, and restaurant catalog browsing.
* **Scope:** Issue `#1` (Sub-issues `#7`–`#12`) and Issue `#3` (Sub-issues `#13`–`#18`).
* **Velocity Committed:** 8 Epic Points / 12 Sub-issue tasks.

### Sprint 2: Ordering & Payment (Oct 28 – Nov 10)
* **Goal:** Deliver shopping cart management, price verification, checkout, and simulated payment processing.
* **Scope:** Issue `#4` (Shopping Cart) and Issue `#5` (Online Payment Mock Gateway).
* **Velocity Committed:** 13 Story Points.

### Sprint 3: Tracking & Quality Assurance (Nov 11 – Nov 24)
* **Goal:** Deliver 5-stage order tracking, automated test coverage, and documentation sign-off.
* **Scope:** Issue `#6` (Order Tracking) and comprehensive end-to-end regression testing.
* **Velocity Committed:** 5 Story Points.

---

## 9. GitHub Repository and Project Setup

The repository and project board were structured to recreate and improve the reference workflow:
* **Repository:** `2403a51422-sesd-assignment-5`
* **Visibility:** Public
* **Owner:** `Mhemavardhan`
* **Associated GitHub Project:** `Online Food Ordering - Scrum Project`
* **Views Configured:**
  1. *View 1 (Backlog Table View):* Displays columns for Title, Assignees, Status, Sub-issues progress, Priority, Story Points, and Iteration.
  2. *Sprint Board (Kanban View):* Grouped by workflow columns `Todo`, `In Progress`, `Testing`, and `Done`.

---

## 10. Kanban Board and Custom Fields

Four custom metadata fields were configured to govern the Scrum workflow:
1. **Status:** Single select field with states `Todo`, `In Progress`, `Testing`, and `Done`.
2. **Priority:** Single select field with levels `High`, `Medium`, and `Low`.
3. **Story Points:** Numerical field representing relative effort values based on the Fibonacci sequence ($1, 2, 3, 5, 8$).
4. **Iteration:** Timeboxed Sprint field featuring 2-week sprints:
   - *Iteration 1:* Oct 14 – Oct 27
   - *Iteration 2:* Oct 28 – Nov 10
   - *Iteration 3:* Nov 11 – Nov 24

---

## 11. Implementation Details & Architecture

The application is engineered using a robust Three-Tier architecture with zero external third-party package dependencies:
* **Presentation Tier:** Single Page Application (SPA) built with semantic HTML5, modern CSS3 variables and grid layouts, and modular vanilla JavaScript.
* **Application / Logic Tier:** Lightweight Python HTTP REST API server (`app/server.py`) handling user authentication, session security, price verification, and order state progression.
* **Data Storage Tier:** SQLite relational database (`app/food_ordering.db`) with tables for `users`, `restaurants`, `menu_items`, `orders`, and `order_items`.

---

## 12. Screenshots and Captions Index

* **Figure 1:** *GitHub Repository Initialization* — Displays repository name `2403a51422-sesd-assignment-5`, description, and public configuration.
* **Figure 2:** *GitHub Project Creation* — Creation of "Online Food Ordering - Scrum Project" linked to repository.
* **Figure 3:** *Parent Issue Creation* — Issue `#1 Customer Login` with structured User Story narrative and Acceptance Criteria.
* **Figure 4:** *Sub-Issues Breakdown* — Issue `#1` decomposed into 6 sub-issues (`#7` to `#12`).
* **Figure 5:** *Custom Field Configuration (Priority & Story Points)* — Single select and numerical field setup.
* **Figure 6:** *Iteration Field Configuration* — Definition of 3 consecutive two-week sprint schedules.
* **Figure 7:** *Backlog Table View (View 1)* — Complete backlog table populated with all 18 parent and sub-issue tasks.
* **Figure 8:** *Kanban Sprint Board View* — Cards distributed across `Todo`, `In Progress`, `Testing`, and `Done`.
* **Figure 9:** *Web Application Homepage* — Restaurant catalog, student metadata banner, search bar, and cuisine filter pills.
* **Figure 10:** *Menu Explorer Modal* — Categorized menu items with Veg/Non-Veg indicators and Add to Cart action.
* **Figure 11:** *Shopping Cart Drawer* — Slide-in drawer with item quantity controls and live price calculations.
* **Figure 12:** *Checkout & Mock Payment Dialog* — Address input and payment method selection (UPI/Card/COD).
* **Figure 13:** *Real-Time 5-Stage Order Tracking Stepper* — Live progress bar showing active order milestone and simulation controller.

---

## 13. Testing and Results

Automated unit and integration testing was executed using Python's `unittest` framework:
* **Command:** `python3 app/test_app.py -v`
* **Test Suite Duration:** 0.008 seconds
* **Pass Rate:** 100% (6 of 6 tests passed successfully)

```
Database initialized successfully with sample restaurants and menus.
test_01_database_tables_exist (__main__.TestFoodOrderingSystem.test_01_database_tables_exist) ... ok
test_02_password_hashing_security (__main__.TestFoodOrderingSystem.test_02_password_hashing_security) ... ok
test_03_default_seeded_restaurants (__main__.TestFoodOrderingSystem.test_03_default_seeded_restaurants) ... ok
test_04_user_registration_and_authentication (__main__.TestFoodOrderingSystem.test_04_user_registration_and_authentication) ... ok
test_05_cart_and_mock_checkout (__main__.TestFoodOrderingSystem.test_05_cart_and_mock_checkout) ... ok
test_06_order_tracking_progression (__main__.TestFoodOrderingSystem.test_06_order_tracking_progression) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.008s

OK
```

---

## 14. Increment Summary

Across the three simulated sprints, the team delivered three cumulative, potentially shippable increments:
* **Increment 1 (Sprint 1):** Functional customer authentication and restaurant/menu browsing catalog.
* **Increment 2 (Sprint 2):** Integrated shopping cart drawer with quantity modification and mock payment checkout.
* **Increment 3 (Sprint 3):** Real-time 5-stage order tracking stepper, embedded Scrum board viewer, and automated test suite.

---

## 15. Sprint Review and Retrospective

* **Sprint 1 Retrospective:** Highlighted the benefits of early database schema normalization and identified the need for client-side password length enforcement.
* **Sprint 2 Retrospective:** Led to the addition of single-restaurant cart safeguards to prevent conflicting vendor dispatches.
* **Sprint 3 Retrospective:** Confirmed that empirical Scrum governance and test-driven development yielded a zero-defect final deliverable.

---

## 16. Reflection and Conclusion

This simulation demonstrated that Agile/Scrum is far superior to traditional Waterfall methodologies for web applications subject to evolving user requirements. Timeboxing work into 2-week sprints, estimating complexity with Planning Poker, visualizing progress on Kanban boards, and verifying quality against an explicit Definition of Done ensured steady development velocity and high software reliability.

---

## 17. GitHub Links & Verification

* **GitHub Repository URL:** `https://github.com/Mhemavardhan/2403a51422-sesd-assignment-5`
* **Student Identifier:** M. Hemavardhan (Hall Ticket: 2403A51422)
* **Status:** Verified and Complete
