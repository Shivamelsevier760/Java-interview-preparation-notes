# AWS Practice mock results :

### 1) Automated Regression Failure Analysis & Jira Ticket Creation

I want to build a system that monitors regression test executions running in **Jenkins**.

- The system should track regression packs and analyze failures from Jenkins pipelines.
- Based on the failure, it should automatically create a **Jira ticket**.
- The Jira ticket should include:
    - Which **microservices** encountered the issue
    - The **root cause** of the failure
    - Suggested **fixes or remediation steps**
    - Details from a **daily reminder bug scan**
    - How long the issue has been occurring (issue aging)
- The system should automatically:
    - Analyze the **previous commit history**
    - Identify if the issue started after a specific commit
    - Detect if a **dependency was deprecated** or upgraded
    - Highlight if the code is no longer supported due to dependency or version incompatibility

---

### 2) Centralized Microservices Health & Technology Stack Reporting

I want to build a **dashboard or website** that provides visibility across all microservices.

- It should generate **daily, weekly, or bi-weekly reports** showing:
    - Bug scan results across all microservices
    - Current health status of each service
- The platform should display:
    - Technology stack used by each microservice (e.g. Java version, Spring Boot version)
    - Frontend stack (Angular version, etc.)
    - Email or messaging integrations
    - Any other major frameworks or tools used
- The system should:
    - Track **end-of-life (EOL)** dates for technologies
    - Example: If Angular 18 or a Java version is approaching EOL
    - Send **email alerts** to the business and engineering teams
    - Automatically create **Jira tickets** requesting review or upgrade
    - Clearly mention risks of continuing with unsupported technologies and recommend upgrades to avoid future issues

---

### 3) UI Accessibility Scanner Using Vibe Coding

I want to build an **accessibility scanner** for any UI website (for example, an Elsevier UI application).

- The scanner should:
    - Check whether the website follows **accessibility guidelines** (WCAG standards)
    - Identify accessibility gaps if guidelines are not met
- For each issue, it should:
    - Explain what accessibility rule is being violated
    - Provide **clear suggestions** on how to fix the issue
    - Recommend improvements in UI components, ARIA labels, contrast, keyboard navigation, etc.

---

### 4) Chatbot Integration for CDM OrgFinder (Angular UI)

In the **CDM OrgFinder** application (which is built using Angular), I want to add a **chatbot on the UI**.

- When a user logs in:
    - The chatbot should identify the user based on their **AD group**
    - Display all **pending Jira tickets** assigned to that user
- The chatbot should act as a reminder:
    - Encourage users to close pending tickets first
    - Show priorities directly on the main page
-