# Document 04: Sprint Review & Retrospective

**Project Title:** Online Food Ordering System — Agile/Scrum Simulation  
**Student Name:** M. Hemavardhan (2403A51422)  
**Subject:** Software Engineering and System Design (24CS301PC311)  
**Department of CSE | School of CS&AI | SR University**  

---

## 1. Overview of Scrum Empirical Process Control

Scrum relies on three pillars of empirical process control:
1. **Transparency:** Backlog items, board statuses, and increments are visible to the entire team and stakeholders.
2. **Inspection:** Regular cadence of Sprint Reviews and Retrospectives to inspect deliverables and processes.
3. **Adaptation:** Immediate adjustment of future sprint planning based on empirical findings.

---

## 2. Sprint 1 Review & Retrospective

### Sprint 1 Review (Demo to Product Owner)
* **Date:** End of Iteration 1 (Oct 27)
* **Demonstrated Increment:**
  * User registration and login flow with salted SHA-256 password hashing.
  * Restaurant catalog displaying 4 distinct restaurants with cuisine tags, delivery times, and ratings.
  * Menu modal displaying categorized dishes with Veg/Non-Veg indicators and item prices.
* **Product Owner Feedback:**
  * "The catalog displays cleanly and fast. Ensure the UI clearly shows the logged-in student's name on the header navigation bar."
* **Velocity Achieved:** 8 Story Points completed.

### Sprint 1 Retrospective (Team Inspection)
* **What Went Well:**
  * Choosing SQLite and Python standard library eliminated dependency conflicts and ensured instant local startup.
  * Decomposing User Story #1 and #3 into 6 granular sub-issues each simplified Git issue tracking.
* **What Could Be Improved:**
  * Initial password validation did not enforce length constraints on the frontend.
* **Action Items for Next Sprint:**
  * Add client-side and server-side minimum length validations ($ \ge 6 $ characters).
  * Build an active session management store so authentication persists across page refreshes.

---

## 3. Sprint 2 Review & Retrospective

### Sprint 2 Review (Demo to Product Owner)
* **Date:** End of Iteration 2 (Nov 10)
* **Demonstrated Increment:**
  * Interactive slide-in shopping cart drawer with live subtotal, delivery fee, and grand total calculations.
  * Mock payment gateway supporting simulated UPI, Credit/Debit Card, and Cash on Delivery.
  * Instant generation of unique mock transaction reference ID (`TXN-MOCK-XXXXXXXXXX`).
* **Product Owner Feedback:**
  * "Mock payment flow is intuitive and meets academic demonstration standards without risky live gateways. The cart needs protection against mixing dishes from different restaurants simultaneously."
* **Velocity Achieved:** 13 Story Points completed.

### Sprint 2 Retrospective (Team Inspection)
* **What Went Well:**
  * Backend price verification prevented any client-side price tampering during order creation.
  * Smooth modal dialog animations and cart counter badge updates enhanced user experience.
* **What Could Be Improved:**
  * Multi-restaurant cart handling needed an explicit user confirmation prompt before clearing older items.
* **Action Items for Next Sprint:**
  * Added single-restaurant cart validation prompt in `app.js`.
  * Prepare test scripts to verify cart calculations with multi-item quantities.

---

## 4. Sprint 3 Review & Retrospective

### Sprint 3 Review (Final Increment Demonstration)
* **Date:** End of Iteration 3 (Nov 24)
* **Demonstrated Increment:**
  * Real-time 5-stage order tracking stepper (`Placed` &rarr; `Confirmed` &rarr; `Preparing` &rarr; `Out for Delivery` &rarr; `Delivered`).
  * Interactive examiner simulation controller allowing immediate state progression demonstration.
  * Complete test suite passing 100% of unit and integration test cases.
  * Integrated Agile/Scrum Project viewer tab embedded directly within the web application.
* **Stakeholder / Instructor Acceptance:**
  * "All 5 core assignment features (Login, Browse Menu, Cart, Payment, Order Tracking) are demonstrably implemented, tested, and published to GitHub with complete academic documentation."
* **Velocity Achieved:** 5 Story Points completed (Total: 26 Story Points across 3 Sprints).

### Sprint 3 Retrospective (Project-Wide Reflection)
* **What Went Well:**
  * Zero-dependency architecture ensured reproducible execution across standard development environments.
  * All 6 automated tests execute in under 0.01 seconds.
* **Key Takeaway:**
  * Agile iterative development allowed continuous refinement of user experience while maintaining robust software engineering standards.
