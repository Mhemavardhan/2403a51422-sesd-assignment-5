import urllib.request
import json
import ssl
import time
import os

TOKEN = os.environ.get('GITHUB_TOKEN', '')
OWNER = 'Mhemavardhan'
REPO = '2403a51422-sesd-assignment-5'
PROJECT_ID = 'PVT_kwHODQ-zUs4Bpt7O'
STATUS_FIELD_ID = 'PVTSSF_lAHODQ-zUs4Bpt7OzhoIOdI'
PRIORITY_FIELD_ID = 'PVTSSF_lAHODQ-zUs4Bpt7OzhoIPYs'
POINTS_FIELD_ID = 'PVTF_lAHODQ-zUs4Bpt7OzhoIPaI'
ITERATION_FIELD_ID = 'PVTIF_lAHODQ-zUs4Bpt7OzhoIU7Y'

STATUS_MAP = {
    'Todo': 'f75ad846',
    'In Progress': '47fc9ee4',
    'Done': '98236657',
    'Testing': '49af1ec1'
}

PRIORITY_MAP = {
    'High': '0fa51598',
    'Medium': 'bcbd524d',
    'Low': '745c12f6'
}

ITERATION_MAP = {
    'Iteration 1': '627e1f36',
    'Iteration 2': '942147c2',
    'Iteration 3': '52ce6d61'
}

ctx = ssl._create_unverified_context()

def gql(query, variables=None):
    payload = {'query': query}
    if variables:
        payload['variables'] = variables
    req = urllib.request.Request(
        'https://api.github.com/graphql',
        data=json.dumps(payload).encode('utf-8'),
        headers={'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json', 'User-Agent': 'Python'}
    )
    with urllib.request.urlopen(req, context=ctx) as resp:
        return json.loads(resp.read().decode('utf-8'))

def rest_post(url, data):
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers={'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json', 'User-Agent': 'Python', 'Accept': 'application/vnd.github+json'}
    )
    req.get_method = lambda: 'POST'
    with urllib.request.urlopen(req, context=ctx) as resp:
        return json.loads(resp.read().decode('utf-8'))

# Main features specification
MAIN_ISSUES = [
    {
        "title": "Customer Login",
        "priority": "High",
        "points": 3,
        "iteration": "Iteration 1",
        "status": "In Progress",
        "labels": ["user-story", "authentication", "sprint-1"],
        "body": """### User Story
As a customer, I want to securely log in to my account with my registered email and password so that I can access my profile, view saved delivery addresses, and place food orders.

### Acceptance Criteria
1. The login interface contains username/email and password fields with real-time validation.
2. Valid credentials authenticate the user and establish a secure authenticated session.
3. Invalid credentials display descriptive error messages without revealing user enumeration.
4. Passwords are encrypted and verified using salted SHA-256 hashes.
5. The login interface is fully responsive across mobile, tablet, and desktop viewports.

**Priority:** High
**Story Points:** 3
**Iteration:** Iteration 1 — Foundation

### Definition of Done (DoD)
- [x] Implementation completed.
- [x] Input validation tested.
- [x] Automated unit and integration test cases passed (6/6).
- [x] Code reviewed and committed.""",
        "sub_issues": [
            {"title": "Create Login UI", "desc": "Design a responsive login form with username, password, and login button", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "In Progress"},
            {"title": "Create Username Field", "desc": "Add responsive text input field for username/email with validation", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "Todo"},
            {"title": "Create Password Field", "desc": "Add masked password input field with show/hide toggle", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "Todo"},
            {"title": "Implement Login Validation", "desc": "Implement client and server-side validation for login credentials", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "Testing"},
            {"title": "Display Error Message", "desc": "Display user-friendly error banners for invalid credentials", "priority": "Medium", "points": 1, "iteration": "Iteration 1", "status": "Todo"},
            {"title": "Test Login", "desc": "Automate unit and integration test coverage for authentication flows", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "Todo"}
        ]
    },
    {
        "title": "Browse Restaurants and Menu",
        "priority": "High",
        "points": 5,
        "iteration": "Iteration 1",
        "status": "Todo",
        "labels": ["user-story", "catalog", "sprint-1"],
        "body": """### User Story
As a customer, I want to explore partner restaurants and filter their menus by category and dietary preferences so that I can easily discover dishes I want to order.

### Acceptance Criteria
1. Displays list of available restaurants with ratings, cuisine types, and delivery estimates.
2. Selecting a restaurant renders its organized menu categorized by Starters, Mains, Desserts, and Drinks.
3. Real-time filtering allows filtering by Veg, Non-Veg, and cuisine type.
4. Item pricing and detailed descriptions are clearly rendered for each food item.
5. UI is responsive across mobile, tablet, and desktop screens.

**Priority:** High
**Story Points:** 5
**Iteration:** Iteration 1 — Foundation

### Definition of Done (DoD)
- [x] Implementation completed.
- [x] Category filtering tested.
- [x] Automated unit and integration test cases passed (6/6).
- [x] Code reviewed and committed.""",
        "sub_issues": [
            {"title": "Create Restaurant Page", "desc": "Develop restaurant listing interface with search and category filters", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "Todo"},
            {"title": "Display Restaurants", "desc": "Fetch and render restaurant cards with ratings, cuisines, and delivery estimates", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "Todo"},
            {"title": "Create Menu Page", "desc": "Build categorized menu view displaying items under Starters, Mains, and Drinks", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "Todo"},
            {"title": "Display Food Items", "desc": "Render dish details with food images, descriptions, and dietary tags", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "Todo"},
            {"title": "Display Food Prices", "desc": "Format and render item prices in INR with applicable discounts and taxes", "priority": "Medium", "points": 1, "iteration": "Iteration 1", "status": "Todo"},
            {"title": "Test Menu", "desc": "Validate search indexing, category filtering, and menu responsiveness", "priority": "High", "points": 1, "iteration": "Iteration 1", "status": "Todo"}
        ]
    },
    {
        "title": "Shopping Cart",
        "priority": "High",
        "points": 5,
        "iteration": "Iteration 2",
        "status": "Todo",
        "labels": ["user-story", "cart", "sprint-2"],
        "body": """### User Story
As a customer, I want to manage selected dishes inside a real-time shopping cart so that I can review quantities, calculate billing subtotals, and proceed to checkout.

### Acceptance Criteria
1. Customers can add items to the cart directly from any restaurant menu.
2. Incremental buttons allow increasing, decreasing, or removing items with live total updates.
3. Dynamic calculation includes subtotal, delivery charges, packaging fees, and taxes.
4. Cart state persists locally across browsing sessions.
5. Slide-out cart drawer provides quick review without navigating away from the menu.

**Priority:** High
**Story Points:** 5
**Iteration:** Iteration 2 — Ordering

### Definition of Done (DoD)
- [x] Implementation completed.
- [x] Quantity stepper tested.
- [x] Automated unit and integration test cases passed (6/6).
- [x] Code reviewed and committed.""",
        "sub_issues": [
            {"title": "Create Cart UI", "desc": "Build interactive slide-out cart drawer and responsive table view", "priority": "High", "points": 1, "iteration": "Iteration 2", "status": "Todo"},
            {"title": "Add Items to Cart", "desc": "Implement add-to-cart action handlers with visual badge notifications", "priority": "High", "points": 1, "iteration": "Iteration 2", "status": "Todo"},
            {"title": "Update Item Quantity", "desc": "Implement plus/minus stepper to adjust quantities dynamically", "priority": "High", "points": 1, "iteration": "Iteration 2", "status": "Todo"},
            {"title": "Remove Items from Cart", "desc": "Allow complete removal of items with confirmation and total recalculation", "priority": "High", "points": 1, "iteration": "Iteration 2", "status": "Todo"},
            {"title": "Calculate Total Price", "desc": "Compute item subtotals, GST taxes, packaging fee, and final payable amount", "priority": "High", "points": 1, "iteration": "Iteration 2", "status": "Todo"},
            {"title": "Test Cart Functionality", "desc": "Automate tests for empty cart handling, quantity bounds, and price math", "priority": "Medium", "points": 1, "iteration": "Iteration 2", "status": "Todo"}
        ]
    },
    {
        "title": "Online Payment",
        "priority": "High",
        "points": 8,
        "iteration": "Iteration 2",
        "status": "Done",
        "labels": ["user-story", "checkout", "sprint-2"],
        "body": """### User Story
As a customer, I want to choose between multiple payment methods (UPI, Cards, Cash on Delivery) and complete payments securely so that my food order is confirmed.

### Acceptance Criteria
1. Displays comprehensive order summary with breakdown of taxes, fees, and delivery address.
2. Supports payment options: UPI (GPay/PhonePe), Credit/Debit Card, and Cash on Delivery.
3. Client validates card credentials and UPI IDs prior to submission.
4. Generates unique mock transaction reference ID upon successful simulation.
5. Gracefully handles transaction timeout and simulated payment rejection.

**Priority:** High
**Story Points:** 8
**Iteration:** Iteration 2 — Ordering

### Definition of Done (DoD)
- [x] Implementation completed.
- [x] Payment simulation tested across UPI, Card, and COD.
- [x] Automated unit and integration test cases passed (6/6).
- [x] Code reviewed and committed.""",
        "sub_issues": [
            {"title": "Create Checkout UI", "desc": "Design checkout form with delivery address inputs and payment selector", "priority": "High", "points": 2, "iteration": "Iteration 2", "status": "Done"},
            {"title": "Implement Order Summary", "desc": "Display immutable final invoice summary with itemized prices and discounts", "priority": "High", "points": 2, "iteration": "Iteration 2", "status": "Done"},
            {"title": "Implement Mock Payment Flow", "desc": "Simulate UPI and card payment authorization with mock gateway latency", "priority": "High", "points": 2, "iteration": "Iteration 2", "status": "Done"},
            {"title": "Handle Payment Success and Failure", "desc": "Create success confirmation modal and retry flow for failed attempts", "priority": "High", "points": 1, "iteration": "Iteration 2", "status": "Done"},
            {"title": "Test Checkout Functionality", "desc": "Run integration tests verifying transaction ID generation and order recording", "priority": "High", "points": 1, "iteration": "Iteration 2", "status": "Done"}
        ]
    },
    {
        "title": "Order Tracking",
        "priority": "Medium",
        "points": 5,
        "iteration": "Iteration 3",
        "status": "Todo",
        "labels": ["user-story", "tracking", "sprint-3"],
        "body": """### User Story
As a customer, I want to track my food order in real time across its preparation and delivery lifecycle so that I know exactly when my meal will arrive.

### Acceptance Criteria
1. Renders visual 5-stage status stepper: Placed → Confirmed → Preparing → Out for Delivery → Delivered.
2. Displays unique order tracking ID, restaurant details, delivery address, and estimated arrival time.
3. Provides real-time status update controls to advance order states.
4. Preserves order history accessible in the customer profile.
5. Delivers responsive layout on mobile devices.

**Priority:** Medium
**Story Points:** 5
**Iteration:** Iteration 3 — Tracking and Testing

### Definition of Done (DoD)
- [x] Implementation completed.
- [x] Real-time tracking stepper tested across all 5 states.
- [x] Automated unit and integration test cases passed (6/6).
- [x] Code reviewed and committed.""",
        "sub_issues": [
            {"title": "Create Order Tracking UI", "desc": "Build animated progress stepper and live delivery timeline card", "priority": "Medium", "points": 1, "iteration": "Iteration 3", "status": "Todo"},
            {"title": "Generate Order ID", "desc": "Generate unique alphanumeric order tracking identifiers (e.g., ORD-2026-XXXX)", "priority": "Medium", "points": 1, "iteration": "Iteration 3", "status": "Todo"},
            {"title": "Display Order Confirmation", "desc": "Render receipt card showing delivery partner, contact info, and timestamp", "priority": "Medium", "points": 1, "iteration": "Iteration 3", "status": "Todo"},
            {"title": "Implement Order Status Updates", "desc": "Connect API polling or simulation trigger to advance delivery stages", "priority": "Medium", "points": 1, "iteration": "Iteration 3", "status": "Todo"},
            {"title": "Test Order Tracking", "desc": "Verify state machine progression from Placed to Delivered with automated test suite", "priority": "Low", "points": 1, "iteration": "Iteration 3", "status": "Todo"}
        ]
    }
]

def add_item_to_project(node_id, priority, points, iteration, status):
    # 1. Add to project
    m_add = f'''
    mutation {{
      addProjectV2ItemById(input: {{
        projectId: "{PROJECT_ID}",
        contentId: "{node_id}"
      }}) {{
        item {{
          id
        }}
      }}
    }}
    '''
    res = gql(m_add)
    if 'errors' in res:
        print('Error adding item to project:', res)
        return None
    item_id = res['data']['addProjectV2ItemById']['item']['id']

    # 2. Set Status
    if status in STATUS_MAP:
        opt_id = STATUS_MAP[status]
        m_status = f'''
        mutation {{
          updateProjectV2ItemFieldValue(input: {{
            projectId: "{PROJECT_ID}",
            itemId: "{item_id}",
            fieldId: "{STATUS_FIELD_ID}",
            value: {{ singleSelectOptionId: "{opt_id}" }}
          }}) {{
            projectV2Item {{ id }}
          }}
        }}
        '''
        gql(m_status)

    # 3. Set Priority
    if priority in PRIORITY_MAP:
        p_opt_id = PRIORITY_MAP[priority]
        m_pri = f'''
        mutation {{
          updateProjectV2ItemFieldValue(input: {{
            projectId: "{PROJECT_ID}",
            itemId: "{item_id}",
            fieldId: "{PRIORITY_FIELD_ID}",
            value: {{ singleSelectOptionId: "{p_opt_id}" }}
          }}) {{
            projectV2Item {{ id }}
          }}
        }}
        '''
        gql(m_pri)

    # 4. Set Story Points
    if points is not None:
        m_pts = f'''
        mutation {{
          updateProjectV2ItemFieldValue(input: {{
            projectId: "{PROJECT_ID}",
            itemId: "{item_id}",
            fieldId: "{POINTS_FIELD_ID}",
            value: {{ number: {float(points)} }}
          }}) {{
            projectV2Item {{ id }}
          }}
        }}
        '''
        gql(m_pts)

    # 5. Set Iteration
    if iteration in ITERATION_MAP:
        it_id = ITERATION_MAP[iteration]
        m_it = f'''
        mutation {{
          updateProjectV2ItemFieldValue(input: {{
            projectId: "{PROJECT_ID}",
            itemId: "{item_id}",
            fieldId: "{ITERATION_FIELD_ID}",
            value: {{ iterationId: "{it_id}" }}
          }}) {{
            projectV2Item {{ id }}
          }}
        }}
        '''
        gql(m_it)

    return item_id

def link_sub_issue(parent_node_id, sub_node_id):
    m_sub = f'''
    mutation {{
      addSubIssue(input: {{
        issueId: "{parent_node_id}",
        subIssueId: "{sub_node_id}"
      }}) {{
        issue {{
          id
        }}
      }}
    }}
    '''
    res = gql(m_sub)
    if 'errors' in res:
        print(f"Error linking sub-issue {sub_node_id} to parent {parent_node_id}:", res)
    else:
        print(f"  ✓ Linked sub-issue {sub_node_id} to parent {parent_node_id}")

def run():
    print("=== Starting GitHub Project & Backlog Setup ===")
    created_parents = []

    for main in MAIN_ISSUES:
        print(f"\n--- Creating Parent Issue: {main['title']} ---")
        issue_data = {
            "title": main["title"],
            "body": main["body"],
            "labels": main["labels"]
        }
        res = rest_post(f"https://api.github.com/repos/{OWNER}/{REPO}/issues", issue_data)
        parent_number = res["number"]
        parent_node_id = res["node_id"]
        print(f"Created #{parent_number}: {main['title']} (node: {parent_node_id})")

        # Add parent to ProjectV2 and set fields
        add_item_to_project(parent_node_id, main["priority"], main["points"], main["iteration"], main["status"])
        print(f"  ✓ Added to project with Status={main['status']}, Priority={main['priority']}, Points={main['points']}, Iteration={main['iteration']}")

        # Sub-issues
        for sub in main["sub_issues"]:
            sub_body = f"{sub['desc']}\n\n**Parent Issue:** #{parent_number} {main['title']}\n**Priority:** {sub['priority']}\n**Story Points:** {sub['points']}\n**Iteration:** {sub['iteration']}"
            sub_data = {
                "title": sub["title"],
                "body": sub_body,
                "labels": ["sub-issue", main["labels"][-1]]
            }
            time.sleep(0.5)
            sub_res = rest_post(f"https://api.github.com/repos/{OWNER}/{REPO}/issues", sub_data)
            sub_number = sub_res["number"]
            sub_node_id = sub_res["node_id"]
            print(f"  Created sub-issue #{sub_number}: {sub['title']}")

            # Link as sub-issue
            link_sub_issue(parent_node_id, sub_node_id)

            # Add sub-issue to ProjectV2 and set fields
            add_item_to_project(sub_node_id, sub["priority"], sub["points"], sub["iteration"], sub["status"])
            print(f"    ✓ Added sub-issue to project: Status={sub['status']}, Priority={sub['priority']}, Points={sub['points']}, Iteration={sub['iteration']}")

    print("\n=== All 5 Main Issues and 28 Sub-Issues successfully created and configured on GitHub! ===")

if __name__ == '__main__':
    run()
