# Document 03: Sprint Planning & Execution Schedule

**Project Title:** Online Food Ordering System — Agile/Scrum Simulation  
**Student Name:** M. Hemavardhan (2403A51422)  
**Subject:** Software Engineering and System Design (24CS301PC311)  
**Department of CSE | School of CS&AI | SR University**  

---

## 1. Scrum Team Setup & Roles (Academic Simulation)

In accordance with official SESD Assignment 5 guidelines, the simulation plan defines the following specialized Scrum roles:

| Scrum Role | Role Name / Representative | Key Responsibilities |
| :--- | :--- | :--- |
| **Product Owner (PO)** | M. Hemavardhan | Defines product vision, prioritizes Product Backlog, accepts increments |
| **Scrum Master (SM)** | M. Hemavardhan | Facilitates Scrum events, removes impediments, ensures Scrum adherence |
| **Lead Developer** | M. Hemavardhan | Full-stack server, database schema, SQLite REST API implementation |
| **Frontend Engineer** | M. Hemavardhan | Responsive UI, SPA state management, modal controllers, CSS styling |
| **QA / Automation Engineer**| M. Hemavardhan | Automated unit tests, integration test suite, verification against DoD |

---

## 2. Iteration Breakdown & Sprint Schedules

The simulation is planned across three 2-week iterations directly matching the GitHub Projects Iteration settings shown in the reference assignment:

```
+---------------------------------------------------------------------------------------+
|  Iteration 1: Oct 14 - Oct 27 (Foundation: Auth, Catalog, Menu Browsing)             |
|  Iteration 2: Oct 28 - Nov 10 (Ordering: Shopping Cart, Checkout, Mock Payment)      |
|  Iteration 3: Nov 11 - Nov 24 (Tracking & Quality: Real-time Stepper, Tests, Docs)   |
+---------------------------------------------------------------------------------------+
```

---

## 3. Sprint 1 — Foundation & Catalog (Oct 14 – Oct 27)

### Sprint Goal:
*Establish system architecture, user database persistence with secure salted authentication, and a responsive restaurant and menu browsing catalog.*

* **Planned Backlog Items:**
  * `#1` Customer Login and Registration (3 Story Points)
    * `↳ #7` Create Login UI (1 pt)
    * `↳ #8` Create Username Field (1 pt)
    * `↳ #9` Create Password Field (1 pt)
    * `↳ #10` Implement Login Validation (1 pt)
    * `↳ #11` Display Error Message (1 pt)
    * `↳ #12` Test Login (1 pt)
  * `#3` Browse Restaurants and Menu (5 Story Points)
    * `↳ #13` Create Restaurant Page (1 pt)
    * `↳ #14` Display Restaurants List (1 pt)
    * `↳ #15` Create Menu Page (1 pt)
    * `↳ #16` Display Food Items (1 pt)
    * `↳ #17` Display Food Prices (1 pt)
    * `↳ #18` Test Menu Browsing (1 pt)
* **Committed Story Points:** 8 Points (Epic items) / 12 Granular Sub-issue tasks.
* **Sprint Deliverable:** Working web app with live SQLite database, seeded restaurants, interactive menu modal, and working user login/register API.

---

## 4. Sprint 2 — Ordering & Payment (Oct 28 – Nov 10)

### Sprint Goal:
*Implement client-side shopping cart state management, basket modifications, order checkout, and simulated payment gateway processing.*

* **Planned Backlog Items:**
  * `#4` Shopping Cart Management (5 Story Points)
    * Cart drawer UI, quantity modification (`+` / `−`), total calculations, empty state.
  * `#5` Online Payment Mock Gateway (8 Story Points)
    * Payment method selector (UPI, Card, COD), address confirmation, mock transaction generation, database transaction recording.
* **Committed Story Points:** 13 Points.
* **Sprint Deliverable:** Complete checkout workflow where logged-in users can add food to the cart, review totals, simulate payment, and generate a validated order record.

---

## 5. Sprint 3 — Tracking, Quality & Handover (Nov 11 – Nov 24)

### Sprint Goal:
*Deliver real-time milestone order tracking, end-to-end automated test validation, academic assignment reports, and verified GitHub repository publishing.*

* **Planned Backlog Items:**
  * `#6` Real-Time Order Tracking (5 Story Points)
    * 5-stage visual stepper (`Placed` &rarr; `Confirmed` &rarr; `Preparing` &rarr; `Out for Delivery` &rarr; `Delivered`), order tracking lookup API, examiner simulation controller.
  * Quality Assurance & Documentation:
    * Comprehensive `test_app.py` test suite execution.
    * Generation of PDF/DOCX assignment submission reports.
    * GitHub Project and remote repository synchronization.
* **Committed Story Points:** 5 Points (Feature) + QA/Verification milestones.
* **Sprint Deliverable:** Fully tested, production-ready full-stack application and complete academic documentation set.

---

## 6. Daily Scrum Protocol (Simulation Template)

The team adhered to the 15-minute timeboxed Daily Scrum format addressing three core questions:
1. **What did I accomplish yesterday that helped the team meet the Sprint Goal?**
2. **What will I work on today to help the team meet the Sprint Goal?**
3. **What impediments or blockers are in my way?**

### Example Daily Scrum Log (Mid-Sprint 2):
* *Lead Developer:* "Yesterday I completed the SQLite orders schema and `/api/checkout` transaction logic. Today I will link client-side cart checkout with mock UPI transaction generation. Blocker: Need to ensure cart price calculations strictly validate against backend database prices."
* *Scrum Master:* "Action taken: Implemented backend price lookup in `server.py` to prevent client tampering. Blocker resolved."
