# AWS Directory Services

![Untitled](aws-directory-services/untitled.png)

## Intro

- Database of objects (User Accounts, Computers, Printers, File Shares, Security Groups) on a Windows server. Users can login on any system in the network.
- Objects are organized in **trees**. A group of trees is called **forest**.
- Used to extend the AD network by involving services like EC2 to be a part of the AD to share login credentials.

### AWS Managed Microsoft AD

![Untitled](aws-directory-services/untitled-1.png)

- Login credentials are shared between on-premise and AWS managed AD
- **Manage users on both AD (on-premise and on AWS managed AD)**
- Supports MFA
- Establish trust connections with your on premise AD
- Supports **directory-aware workloads on AWS**

### AD Connector

![Untitled](aws-directory-services/untitled-2.png)

- AD connector will proxy all the requests to the on-premise AD
- **Users are managed on the on-premise AD only**
- Does not support directory-aware workloads on AWS

### Simple AD

- AD-compatible managed directory on AWS (**cannot be joined with on-premise AD**)
- **Users are managed on the AWS AD only**
- Use when you don’t have an on-premise AD