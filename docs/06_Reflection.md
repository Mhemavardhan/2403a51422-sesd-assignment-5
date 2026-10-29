# Document 06: Student Reflection & Agile Analysis

**Project Title:** Online Food Ordering System — Agile/Scrum Simulation  
**Student Name:** M. Hemavardhan  
**Hall Ticket Number:** 2403A51422  
**Course Code:** 24CS301PC311 (Software Engineering and System Design)  
**Department of CSE | School of CS&AI | SR University**  

---

## 1. Academic Reflection on the Agile/Scrum Simulation

Completing Assignment 5 provided direct, hands-on exposure to implementing the Scrum framework within a real-world software engineering context. Rather than treating Agile merely as a set of theoretical buzzwords, simulating the end-to-end lifecycle of the **Online Food Ordering System** demonstrated how Agile values directly govern day-to-day architectural decisions and code deliveries.

### Key Agile Values Observed:
1. **Individuals and Interactions over Processes and Tools:** While GitHub Projects provided a robust tracking mechanism, clear role definition (Product Owner vs. Developer vs. QA) was essential to maintaining alignment.
2. **Working Software over Comprehensive Documentation:** The focus was placed on producing a genuinely running, testable web application at each sprint boundary rather than writing unvalidated specifications.
3. **Customer Collaboration over Contract Negotiation:** Continuous feedback loops through simulated Sprint Reviews allowed rapid enhancements, such as adding the single-restaurant cart safeguard.
4. **Responding to Change over Following a Plan:** When mock payment integration presented distinct testing requirements, the backlog was adapted dynamically to deliver value without delaying the overall release schedule.

---

## 2. Comparative Analysis: Agile/Scrum vs. Waterfall

| Dimension | Traditional Waterfall Model | Agile / Scrum Framework (Applied in Assignment 5) |
| :--- | :--- | :--- |
| **Requirements Management** | Fixed upfront; difficult and expensive to change later. | Emergent and iterative; prioritized in the Product Backlog. |
| **Delivery Cycle** | Single "Big Bang" release at the end of the project. | Potentially shippable increments delivered every Sprint (2 weeks). |
| **Testing & Quality Assurance** | Executed as a separate, late phase after all development. | Integrated continuously into every sprint via Definition of Done. |
| **Risk Mitigation** | High risk of late discovery of integration bugs. | Low risk; empirical feedback at every Sprint Review. |
| **Stakeholder Visibility** | Low visibility between requirements phase and final delivery. | High transparency through living Kanban boards and Sprint Reviews. |

---

## 3. Estimation & Story Points Reflection

Using **Planning Poker** with the Fibonacci sequence ($1, 2, 3, 5, 8$) forced the development team to think in terms of *relative effort and uncertainty* rather than raw hours. 
* Estimating **Online Payment** at **8 Story Points** reflected both transaction state management and security considerations.
* Breaking down larger user stories into 1-point sub-issues (such as `#7 Create Login UI`, `#8 Create Username Field`, `#9 Create Password Field`) dramatically improved flow through the Kanban board and prevented bottlenecks.

---

## 4. Engineering Takeaways & Professional Growth

1. **Clean Architectural Decoupling:** Separating the frontend UI from the backend REST endpoints enabled independent iteration and automated testing.
2. **Defensive Programming:** Validating prices on the backend rather than trusting client-side payloads is critical in e-commerce and food delivery systems.
3. **Traceability in Git:** Linking Git commit messages to backlog issue numbers ensures complete traceability from requirement to deployment.
