# Document 05: Potentially Shippable Increments & Testing Strategy

**Project Title:** Online Food Ordering System — Agile/Scrum Simulation  
**Student Name:** M. Hemavardhan (2403A51422)  
**Subject:** Software Engineering and System Design (24CS301PC311)  
**Department of CSE | School of CS&AI | SR University**  

---

## 1. Concept of the Product Increment in Scrum

In Scrum, an **Increment** is the concrete stepping stone toward the Product Goal. Each increment is additive to prior increments and thoroughly verified to ensure all increments work seamlessly together. Crucially, to provide value, the increment must be in usable condition regardless of whether the Product Owner decides to release it immediately.

---

## 2. Iterative Increment Progression

```
+-----------------------------------------------------------------------------------------+
| SPRINT 1 INCREMENT                                                                      |
| Features: Customer Auth + Restaurant Directory + Menu Explorer                           |
| Usability: Users can register, log in, browse restaurants, and view detailed menus.     |
+-----------------------------------------------------------------------------------------+
                                          | (Additive Enhancement)
                                          v
+-----------------------------------------------------------------------------------------+
| SPRINT 2 INCREMENT                                                                      |
| Features: Sprint 1 Base + Shopping Cart Drawer + Checkout + Mock Payment Gateway         |
| Usability: Users can assemble food orders, review pricing, and simulate payment safely. |
+-----------------------------------------------------------------------------------------+
                                          | (Additive Enhancement)
                                          v
+-----------------------------------------------------------------------------------------+
| SPRINT 3 INCREMENT (FINAL PRODUCTION RELEASE)                                           |
| Features: Complete Full-Stack Solution + Real-time 5-Stage Stepper + Embedded Board    |
| Usability: Complete end-to-end food ordering lifecycle with automated test verification.|
+-----------------------------------------------------------------------------------------+
```

---

## 3. Quality Assurance & Test Strategy

Testing was executed at multiple levels to guarantee the Definition of Done was satisfied:
1. **Automated Unit Testing:** Verifying isolated cryptographic functions (SHA-256 password salting), schema integrity, and database constraints.
2. **Integration Testing:** Verifying multi-table operations (User &rarr; Order &rarr; Order Items &rarr; Restaurant relationship).
3. **API Contract Verification:** Validating JSON payload schemas, HTTP status codes (`200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `404 Not Found`).
4. **End-to-End User Experience Verification:** Manual and simulated walkthroughs from user registration to order delivery.

---

## 4. Definition of Done (DoD) Verification Checklist

| Criteria | Verification Method | Status | Evidence |
| :--- | :--- | :---: | :--- |
| **Functional Requirements** | All 5 core case study features operational | Passed | Login, Menu, Cart, Payment, Tracking fully functional |
| **Automated Tests** | `python3 test_app.py` passes 100% | Passed | 6/6 test cases passing in 0.008s |
| **Security Standards** | Salted SHA-256 password hashing | Passed | Verified in `test_02_password_hashing_security` |
| **Cross-browser UI** | Responsive on mobile, tablet, and desktop | Passed | Responsive CSS Grid and Flexbox layouts |
| **Documentation** | Academic reports & architecture specs | Passed | All 12 `docs/*.md` files generated |
| **Version Control** | Clean Git commits and remote push | Passed | Staged, committed, and pushed to GitHub |
| **Student Identity** | Zero references to previous student | Passed | Automated search confirms `M. Hemavardhan (2403A51422)` |
