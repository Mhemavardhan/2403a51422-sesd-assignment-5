# Online Food Ordering System — Agile/Scrum Simulation

[![SESD Assignment](https://img.shields.io/badge/SESD-Assignment--05%2F12-orange.svg)](docs/09_Assignment_Completion_Report.md)
[![Academic Year](https://img.shields.io/badge/Academic%20Year-2026--2027-blue.svg)](docs/08_Student_Details.md)
[![Student](https://img.shields.io/badge/Student-M.%20Hemavardhan%20(2403A51422)-green.svg)](docs/08_Student_Details.md)
[![Regulation](https://img.shields.io/badge/Regulation-R24-purple.svg)](docs/08_Student_Details.md)
[![Build & Tests](https://img.shields.io/badge/Tests-6%2F6%20Passed-brightgreen.svg)](docs/10_Test_Results.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Academic Metadata & Student Details

* **Student Name:** **M. Hemavardhan**
* **Hall Ticket Number:** **2403A51422**
* **Subject:** Software Engineering and System Design (SESD)
* **Course Code:** **24CS301PC311**
* **Academic Year:** 2026–2027
* **Year / Semester:** III Year / I Semester (III/I SEM)
* **Regulation:** R24
* **Assignment Number:** 05/12
* **University:** SR University
* **Department:** Department of Computer Science & Engineering (CSE)
* **School:** School of Computer Science & Artificial Intelligence (CS&AI)
* **Course Coordinator:** Dr. N. Sharmila Banu
* **Course Instructor:** Dr. Asha S

---

## 🚀 Project Overview

This repository contains the complete implementation, Agile/Scrum project management artifacts, and academic deliverables for **SESD Assignment 5**. Following the official course syllabus and the reference assignment workflow, this project implements **Case Study 1: Online Food Ordering App**.

The system demonstrates:
1. **Customer Login & Registration:** Salted SHA-256 password hashing with session-based authentication.
2. **Browse Restaurants & Menus:** Interactive catalog with real-time cuisine filtering and Veg/Non-Veg indicators.
3. **Shopping Cart Management:** Dynamic slide-out drawer with quantity increment/decrement and live subtotal calculation.
4. **Online Payment (Mock Gateway):** Simulated payment processing for UPI (GPay/PhonePe), Credit/Debit Card, and Cash on Delivery with transaction ID generation.
5. **Real-Time Order Tracking:** 5-stage interactive lifecycle stepper (`Placed` &rarr; `Confirmed` &rarr; `Preparing` &rarr; `Out for Delivery` &rarr; `Delivered`) with an examiner simulation controller.
6. **Agile/Scrum Simulation:** Complete recreation of the GitHub Projects Scrum Board from the reference DOCX, featuring custom fields, 3 timeboxed iterations, and parent/sub-issue breakdowns.

---

## 📋 GitHub Projects & Scrum Board Recreation

The GitHub Project (**[Online Food Ordering - Scrum Project](https://github.com/users/Mhemavardhan/projects/1)**) reproduces the exact Agile/Scrum workflow demonstrated in the reference assignment:

* **Live GitHub Project URL:** [https://github.com/users/Mhemavardhan/projects/1](https://github.com/users/Mhemavardhan/projects/1)
* **Linked Repository:** `Mhemavardhan/2403a51422-sesd-assignment-5`
* **Configured Views:**
  1. `Product Backlog` (Table View — Full backlog with priority and story points)
  2. `Sprint Board` (Board View — Kanban cards distributed across workflow columns)
  3. `Sprint Planning` (Table View — Sprint allocation and estimation)
  4. `Testing` (Board View — Verification stage tracking)

### 1. Custom Metadata Fields
* **Status:** `Todo`, `In Progress`, `Done`, `Testing`
* **Priority:** Single Select (`High`, `Medium`, `Low`)
* **Story Points:** Number ($1, 2, 3, 5, 8$)
* **Iteration:** Timeboxed Sprints
  * **Iteration 1:** Oct 14 – Oct 27 (Foundation: Auth, Catalog, Menu)
  * **Iteration 2:** Oct 28 – Nov 10 (Ordering: Shopping Cart & Mock Payment)
  * **Iteration 3:** Nov 11 – Nov 24 (Tracking: Real-Time Stepper & Quality)

### 2. Backlog Hierarchy (Parent & Sub-Issues)
* **#1 Customer Login** (High Priority, 3 pts, Iteration 1, In Progress)
  * `↳ #2` Create Login UI (1 pt, In Progress)
  * `↳ #3` Create Username Field (1 pt, Todo)
  * `↳ #4` Create Password Field (1 pt, Todo)
  * `↳ #5` Implement Login Validation (1 pt, Testing)
  * `↳ #6` Display Error Message (1 pt, Todo)
  * `↳ #7` Test Login (1 pt, Todo)
* **#8 Browse Restaurants and Menu** (High Priority, 5 pts, Iteration 1, Todo)
  * `↳ #9` Create Restaurant Page (1 pt, Todo)
  * `↳ #10` Display Restaurants (1 pt, Todo)
  * `↳ #11` Create Menu Page (1 pt, Todo)
  * `↳ #12` Display Food Items (1 pt, Todo)
  * `↳ #13` Display Food Prices (1 pt, Todo)
  * `↳ #14` Test Menu (1 pt, Todo)
* **#15 Shopping Cart** (High Priority, 5 pts, Iteration 2, Todo)
  * `↳ #16` Create Cart UI (1 pt, Todo)
  * `↳ #17` Add Items to Cart (1 pt, Todo)
  * `↳ #18` Update Item Quantity (1 pt, Todo)
  * `↳ #19` Remove Items from Cart (1 pt, Todo)
  * `↳ #20` Calculate Total Price (1 pt, Todo)
  * `↳ #21` Test Cart Functionality (1 pt, Todo)
* **#22 Online Payment** (High Priority, 8 pts, Iteration 2, Done)
  * `↳ #23` Create Checkout UI (2 pts, Done)
  * `↳ #24` Implement Order Summary (2 pts, Done)
  * `↳ #25` Implement Mock Payment Flow (2 pts, Done)
  * `↳ #26` Handle Payment Success and Failure (1 pt, Done)
  * `↳ #27` Test Checkout Functionality (1 pt, Done)
* **#28 Order Tracking** (Medium Priority, 5 pts, Iteration 3, Todo)
  * `↳ #29` Create Order Tracking UI (1 pt, Todo)
  * `↳ #30` Generate Order ID (1 pt, Todo)
  * `↳ #31` Display Order Confirmation (1 pt, Todo)
  * `↳ #32` Implement Order Status Updates (1 pt, Todo)
  * `↳ #33` Test Order Tracking (1 pt, Todo)

---

## 🛠️ Quickstart & Local Execution

The project requires **zero external pip dependencies** and runs directly using Python standard libraries:

### 1. Initialize the Database
```bash
python3 app/init_db.py
```

### 2. Start the Server
```bash
python3 app/server.py
```
Open your web browser and navigate to:
```
http://localhost:8080
```

### 3. Run Automated Tests
```bash
python3 app/test_app.py -v
```
All 6 unit and integration test cases pass in under 0.01 seconds.

---

## 📂 Project Repository Structure

```
2403a51422-sesd-assignment-5/
├── .env.example                               # Environment variable template
├── .gitignore                                 # Git ignore patterns
├── README.md                                  # Repository overview and instructions
├── 2403A51422_SESD_Assignment_5_Report.md      # Consolidated academic submission report
├── 2403A51422_SESD_Assignment_5_Report.html    # Formatted HTML report
├── 2403A51422_SESD_Assignment_5_Report.docx    # Editable Word document submission
├── 2403A51422_SESD_Assignment_5_Report.pdf     # Academic PDF submission report
├── app/
│   ├── food_ordering.db                       # Generated SQLite database
│   ├── init_db.py                             # Database schema creation & seeding
│   ├── server.py                              # Python HTTP & REST API server
│   ├── test_app.py                            # Automated unit & integration test suite
│   └── public/
│       ├── app.js                             # Client-side SPA controller & Scrum renderer
│       ├── index.html                         # Responsive web application interface
│       └── styles.css                         # Modern CSS styling system
└── docs/
    ├── 01_Product_Vision.md                   # Product vision, scope, and target persona
    ├── 02_Product_Backlog.md                  # User stories, acceptance criteria, story points
    ├── 03_Sprint_Planning.md                  # 3 Sprint plans, sprint goals, daily scrum
    ├── 04_Sprint_Review_and_Retrospective.md  # Sprint reviews, retrospectives, action items
    ├── 05_Increment_and_Testing.md            # Working increments, DoD verification
    ├── 06_Reflection.md                       # Agile reflection and comparison with Waterfall
    ├── 07_GitHub_Project_Setup.md             # Recreation guide for GitHub Projects & board
    ├── 08_Student_Details.md                  # Official student and course metadata
    ├── 09_Assignment_Completion_Report.md     # Assignment completion checklist & sign-off
    ├── 10_Test_Results.md                     # Actual test execution logs
    ├── 11_Screenshots_Index.md                # Screenshots catalog with detailed captions
    └── 12_Software_Architecture.md            # C4 architecture, ER diagram, REST API specs
```

---

## 📄 Submission Documents

* **Consolidated Academic Report:** [2403A51422_SESD_Assignment_5_Report.md](2403A51422_SESD_Assignment_5_Report.md)
* **Word Document (DOCX):** [2403A51422_SESD_Assignment_5_Report.docx](2403A51422_SESD_Assignment_5_Report.docx)
* **PDF Document:** [2403A51422_SESD_Assignment_5_Report.pdf](2403A51422_SESD_Assignment_5_Report.pdf)
