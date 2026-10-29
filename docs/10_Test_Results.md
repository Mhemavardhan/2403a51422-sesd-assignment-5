# Document 10: Automated Test Results & Verification Log

**Project Title:** Online Food Ordering System — Agile/Scrum Simulation  
**Student Name:** M. Hemavardhan (2403A51422)  
**Course Code:** 24CS301PC311 | Subject: SESD | SR University  
**Execution Timestamp:** 2026-10-29 19:46:45 IST  

---

## 1. Test Execution Summary

The automated unit and integration test suite was executed using Python's standard `unittest` framework on the production database schema and application server logic.

* **Test Runner:** `python3 test_app.py -v`
* **Python Version:** 3.14.5
* **Platform:** Darwin (macOS) / SQLite3
* **Tests Executed:** 6
* **Pass Rate:** 100% (6 Passed, 0 Failed, 0 Skipped)
* **Execution Duration:** 0.008 seconds

---

## 2. Detailed Test Case Execution Log

```
Database initialized successfully with sample restaurants and menus.

test_01_database_tables_exist (__main__.TestFoodOrderingSystem.test_01_database_tables_exist)
Verify all essential schema tables exist ... ok

test_02_password_hashing_security (__main__.TestFoodOrderingSystem.test_02_password_hashing_security)
Verify passwords are salted and hashed securely using SHA-256 ... ok

test_03_default_seeded_restaurants (__main__.TestFoodOrderingSystem.test_03_default_seeded_restaurants)
Verify restaurants and menu items are properly seeded ... ok

test_04_user_registration_and_authentication (__main__.TestFoodOrderingSystem.test_04_user_registration_and_authentication)
Test Sprint 1: Customer Login and Registration (User Story #1) ... ok

test_05_cart_and_mock_checkout (__main__.TestFoodOrderingSystem.test_05_cart_and_mock_checkout)
Test Sprint 2: Shopping Cart and Mock Payment (User Stories #4 & #5) ... ok

test_06_order_tracking_progression (__main__.TestFoodOrderingSystem.test_06_order_tracking_progression)
Test Sprint 3: Order Tracking Lifecycle (User Story #6) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.008s

OK
```

---

## 3. Test Coverage by Backlog Epic

| Test Case Identifier | Associated User Story / Epic | Tested Behavioral Criteria | Result |
| :--- | :--- | :--- | :---: |
| `test_01` | Architecture & Setup | Validates `users`, `restaurants`, `menu_items`, `orders`, `order_items` tables exist | **PASS** |
| `test_02` | Issue #1: Security | Confirms passwords are salted and SHA-256 hashed (64 hex characters) | **PASS** |
| `test_03` | Issue #3: Catalog | Verifies seeded restaurant count $\ge 4$ and menu count $\ge 12$ | **PASS** |
| `test_04` | Issue #1: Login/Register | Verifies valid registration, password authentication, and duplicate email rejection | **PASS** |
| `test_05` | Issue #4 & #5: Cart & Pay | Verifies price calculation, delivery fee addition, and mock order transaction | **PASS** |
| `test_06` | Issue #6: Order Tracking | Validates 5-stage lifecycle state progression from `Placed` to `Delivered` | **PASS** |
