# Document 01: Product Vision & Scope

**Project Title:** Online Food Ordering System (FoodSwift) — Agile/Scrum Simulation  
**Course Code:** 24CS301PC311 (Software Engineering and System Design)  
**Student Name:** M. Hemavardhan  
**Hall Ticket Number:** 2403A51422  
**Institution:** SR University, School of CS&AI, Department of CSE  
**Academic Year:** 2026–2027 (III Year / I Semester - Regulation R24)  
**Instructor:** Dr. Asha S | **Course Coordinator:** Dr. N. Sharmila Banu  

---

## 1. Executive Summary & Vision Statement

### For:
University students, faculty, and local residents seeking fast, convenient, and reliable dining options.

### Who:
Experience long cafeteria queues, limited dining hours, and inconvenient offline ordering processes.

### The Product:
**FoodSwift** is an intuitive, web-based Online Food Ordering Application developed using an Agile/Scrum framework.

### That Provides:
Instant menu browsing, granular shopping cart customization, seamless mock digital payments (UPI/Card), and real-time order lifecycle tracking from kitchen preparation to doorstep delivery.

### Unlike:
Traditional offline calling, paper menus, or fragmented third-party delivery apps with hidden charges.

### Our Product:
Offers transparent campus-tailored delivery scheduling, real-time status updates, zero latency, and an Agile-driven iterative architecture built to continuously incorporate customer feedback.

---

## 2. Core Business Goals & Target Persona

### Primary Goals:
1. **Frictionless Ordering:** Enable students to browse menus, customize cart items, and complete mock checkout within under 60 seconds.
2. **Operational Transparency:** Provide real-time milestone tracking (Placed &rarr; Confirmed &rarr; Preparing &rarr; Out for Delivery &rarr; Delivered) to eliminate delivery uncertainty.
3. **Agile Engineering Quality:** Demonstrate strict adherence to Scrum principles (Product Backlog grooming, 3 iterative sprints, Definition of Ready/Done, and empirical inspection).

### Target Personas:
* **Campus Student (Aditi):** Rushing between lectures, wants quick ordering from hostel or library with fast UPI checkout.
* **Faculty Member (Prof. Sharma):** Orders lunch delivered directly to the department cabin during short meeting breaks.
* **Local Restaurant Vendor:** Receives validated digital orders with itemized preparation lists and customer contact details.

---

## 3. High-Level System Scope & Boundaries

```
+------------------------------------------------------------------------+
|                          ONLINE FOOD ORDERING SYSTEM                   |
+------------------------------------------------------------------------+
|  [ IN-SCOPE ]                                                          |
|  * Customer authentication with salted SHA-256 cryptographic hashing.   |
|  * Interactive restaurant catalog with cuisine filtering & search.     |
|  * Restaurant-specific menu browsing with Veg/Non-Veg indicators.      |
|  * Dynamic shopping cart with quantity modification & auto-calculation.|
|  * Simulated digital payment gateway supporting UPI, Card, and COD.    |
|  * Interactive 5-stage order tracking stepper with real-time API.       |
|  * Full GitHub Projects Scrum board reproduction with custom fields.   |
+------------------------------------------------------------------------+
|  [ OUT-OF-SCOPE / NON-FUNCTIONAL LIMITS ]                              |
|  * Real monetary transactions (safely mocked for lab demonstration).   |
|  * GPS map turn-by-turn routing (handled via milestone status states). |
|  * Third-party delivery driver telematics.                             |
+------------------------------------------------------------------------+
```

---

## 4. Key Success Metrics (KPIs)
* **User Conversion Rate:** $> 95\%$ successful checkouts without cart abandonment.
* **Average Page Load:** $< 500\text{ ms}$ for restaurant menu rendering.
* **Scrum Team Velocity:** Consistent delivery of 26 total Story Points across 3 planned iterations.
* **Defect Density:** 0 critical defects in core user paths during final increment verification.
