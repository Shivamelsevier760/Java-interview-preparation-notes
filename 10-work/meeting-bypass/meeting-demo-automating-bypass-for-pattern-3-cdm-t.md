# Meeting Demo: Automating Bypass for Pattern 3 CDM Tickets from OPEN positions FLM to Sales compensation manager

I've scheduled a meeting, but it's my first task for the CDM. I know most of you are busy, please feel free to skip it from next time if you want.

**Introduction:**

- **Objective:** The objective of this demo is to automate the bypass process for Pattern 3 CDM tickets that have "OPEN" as the first name.
- **Problem: Currently, Front Line Managers (FLMs) for open positions lack approval access, necessitating manual bypass to the Sales Compensation Manager (SCM).**
- **Solution: We propose to implement an automated bypass process to directly route these requests to the Sales Compensation Manager.**

**Code Overview:**

We will demonstrate the key methods used in this automation process.

1. **automaticByPassForFLMOpenPosition():** This method retrieves open position requests starting with "OPEN" and with pattern ID 3. It proceeds with bypassing these requests to the Sales Compensation Manager.
2. **byPassChangeRequestToFlm():** This method handles the bypass process, examines the ChangeRequest, assigns it to the Sales Compensation Manager, updates statuses, and notifications.

**Bypass Logic:**

We will delve into the bypass logic that is the heart of this automation:

- **The ChangeRequest is examined, and approval details are determined.**
- **The request is then assigned to the Sales Compensation Manager.**
- **Statuses and notifications are updated accordingly.**

**Conclusion:**

In conclusion, this automated bypass for Pattern 3 CDM tickets provides the following benefits:

- Eliminates the need for manual bypass to the SCM queue.

This solution is executed through a well-structured code that efficiently handles the bypass, ensuring a smoother and more time-effective process for handling Pattern 3 CDM tickets.

---

**Test Case 1: Negative Test - Assignee "Tiwari, Shivam" (No Escalation)**

- **Scenario:** In this scenario, we have a ChangeRequest assigned to "Tiwari, Shivam," and we do not expect an automatic approval (no escalation).
- **Input:** ChangeRequest assigned to "Tiwari, Shivam."
- **Expected Result:** The system should not perform an automatic bypass to the Sales Compensation Manager (SCM).

**Test Case 2: Negative Test - FLM Last Name Starts with "OPEN" (No Escalation)**

- **Scenario:** In this scenario, we have a ChangeRequest with an FLM whose last name starts with "OPEN." We do not expect an automatic approval (no escalation).
- **Input:** ChangeRequest with FLM whose last name starts with "OPEN."
- **Expected Result:** The system should not perform an automatic bypass to the Sales Compensation Manager (SCM).

**Test Case 3: Negative Test - Pattern ID Not Equal to 3 (No Escalation)**

- **Scenario:** In this scenario, we have a ChangeRequest with a pattern ID that is not equal to 3. We do not expect an automatic approval (no escalation).
- **Input:** ChangeRequest with pattern ID other than 3.
- **Expected Result:** The system should not perform an automatic bypass to the Sales Compensation Manager (SCM).

**Test Case 4: Positive Test - FLM First Name Starts with "OPEN" and Pattern ID 3 (Escalation Occurs)**

- **Scenario:** In this scenario, we have a ChangeRequest with an FLM whose first name starts with "OPEN" and has a pattern ID of 3. We expect an automatic approval and escalation to the Sales Compensation Manager (SCM).
- **Input:** ChangeRequest with FLM whose first name starts with "OPEN" and pattern ID 3.
- **Expected Result:** The system should perform an automatic bypass to the Sales Compensation Manager (SCM).