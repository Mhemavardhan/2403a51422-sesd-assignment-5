# Document 07: GitHub Project Setup & Scrum Board Recreation Guide

**Project Title:** Online Food Ordering System — Agile/Scrum Simulation  
**Student Name:** M. Hemavardhan (Hall Ticket: 2403A51422)  
**Course Code:** 24CS301PC311 | Subject: SESD | SR University  

---

## 1. Overview of Workflow Reproduction

This document provides the exhaustive, step-by-step specification for recreating the exact GitHub repository, GitHub Projects board, custom fields, views, iterations, parent issues, and sub-issues demonstrated in the reference assignment document, updated with the student identity of **M. Hemavardhan (2403A51422)**.

---

## 2. Step 1: Repository Creation

* **Repository Name:** `2403a51422-sesd-assignment-5` (or `online-food-ordering-app`)
* **Owner:** `Mhemavardhan`
* **Visibility:** Public
* **Description:** `SESD Assignment 5: Agile/Scrum Simulation for the Online Food Ordering System by M. Hemavardhan, Hall Ticket 2403A51422.`
* **Configuration:** Initialized with README, `.gitignore` for Python, and standard licensing.

---

## 3. Step 2: GitHub Project Creation & Repository Linkage

1. Navigate to GitHub Profile &rarr; **Projects** &rarr; click **New project**.
2. Select **Board** or **Table** template.
3. Name the Project: `Online Food Ordering - Scrum Project` (or `SESD Assignment 5 — Online Food Ordering Scrum Project`).
4. Link repository: Enable **Import items from repository** &rarr; Select `2403a51422-sesd-assignment-5`.

---

## 4. Step 3: Configuring Custom Fields

The project configuration defines four custom metadata fields directly matching the reference screenshots:

| Field Name | Field Type | Configured Values / Options | Purpose |
| :--- | :--- | :--- | :--- |
| **Status** | Single Select | `Todo`, `In Progress`, `Done`, `Testing` | Tracks workflow progression |
| **Priority** | Single Select | `High`, `Medium`, `Low` | Business priority ranking |
| **Story Points** | Number | $1, 2, 3, 5, 8$ | Planning Poker estimation |
| **Iteration** | Iteration | • **Iteration 1:** Oct 14 – Oct 27 (2 weeks)<br>• **Iteration 2:** Oct 28 – Nov 10 (2 weeks)<br>• **Iteration 3:** Nov 11 – Nov 24 (2 weeks) | Timeboxed sprint allocations |

---

## 5. Step 4: Issue Hierarchy & Task Breakdown

### Parent Issues (Core User Stories):
1. **Issue #1:** `Customer Login` (Priority: High, Points: 3, Iteration: Iteration 1)
2. **Issue #3:** `Browse Restaurants and Menu` (Priority: High, Points: 5, Iteration: Iteration 1)
3. **Issue #4:** `Shopping Cart` (Priority: High, Points: 5, Iteration: Iteration 2)
4. **Issue #5:** `Online Payment` (Priority: High, Points: 8, Iteration: Iteration 2)
5. **Issue #6:** `Order Tracking` (Priority: Medium, Points: 5, Iteration: Iteration 3)

### Sub-Issues Breakdown for Issue #1 (Customer Login):
* `#7` `Create Login UI` (Status: In Progress, Points: 1, Priority: High)
* `#8` `Create Username Field` (Status: Todo, Points: 1, Priority: High)
* `#9` `Create Password Field` (Status: Todo, Points: 1, Priority: High)
* `#10` `Implement Login Validation` (Status: Testing, Points: 1, Priority: High)
* `#11` `Display Error Message` (Status: Todo, Points: 1, Priority: Medium)
* `#12` `Test Login` (Status: Todo, Points: 1, Priority: High)

### Sub-Issues Breakdown for Issue #3 (Browse Restaurants and Menu):
* `#13` `Create Restaurant Page` (Status: Todo, Points: 1, Priority: High)
* `#14` `Display Restaurants` (Status: Todo, Points: 1, Priority: High)
* `#15` `Create Menu Page` (Status: Todo, Points: 1, Priority: High)
* `#16` `Display Food Items` (Status: Todo, Points: 1, Priority: High)
* `#17` `Display Food Prices` (Status: Todo, Points: 1, Priority: Medium)
* `#18` `Test Menu` (Status: Todo, Points: 1, Priority: High)

---

## 6. Step 5: Configuring Views

### View 1: Backlog Table View
* **Layout:** Table
* **Visible Columns:** Title, Assignees, Status, Linked pull requests, Sub-issues progress, Priority, Story Points, Iteration.
* **Grouping:** Grouped by `Iteration` or `Status`.

### View 2: Sprint Board (Kanban Board)
* **Layout:** Board
* **Columns:**
  1. `Todo` (Greyscale dot)
  2. `In Progress` (Cyan/blue dot)
  3. `Done` (Purple/green dot)
  4. `Testing` (Yellow/green dot)
* **Card Display:** Shows issue title, repository tag, sub-issues progress bar ($0/6$, $100\%$), priority pill, and story points badge.

---

## 7. Step 6: Scrum Card Movement Demonstration

During the simulation, items flow across the board to illustrate work in progress:
* `#1 Customer Login` &rarr; Moved to `In Progress`.
* `#7 Create Login UI` &rarr; Moved to `In Progress`.
* `#10 Implement Login Validation` &rarr; Moved to `Testing`.
* `#5 Online Payment` &rarr; Moved to `Done`.
* Remaining items reside in `Todo` ready for future sprints.
