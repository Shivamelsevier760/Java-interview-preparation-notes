# AWS Cloud Practitioner — Interview Q&A

> Auto-extracted from the notes in [`05-aws-cloud-practitioner/`](../05-aws-cloud-practitioner/) by [`scripts/extract_qa.mjs`](../scripts/extract_qa.mjs).
> Do not edit by hand — regenerate with `node scripts/extract_qa.mjs`.

**22 answered questions** · **60 question prompts without recorded answers**

---

## 1. What is the AWS Well-Architected Framework?

*Source: [`05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md`](../05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md)*

The AWS Well-Architected Framework is basically a body of knowledge that describes the various design principles, key concepts, design and architectural best practices that can help companies design and run highly efficient workloads in the AWS platform. This framework ensures that the company’s cloud architecture is in accordance with the AWS best practices. It also comes with related AWS features, services and tools that you can utilize to measure the overall efficiency of your design. The AWS Well-Architected Framework will empower you to improve your existing IT infrastructure in terms of your overall operations, security, reliability, efficiency, cost optimization, and sustainability.

Having well-architected systems greatly increases the plausibility of business success, which is why AWS created the AWS Well-Architected Framework. This framework is composed of **six pillars** that help you understand the pros and cons of the decisions you make while building cloud architectures and systems on the AWS platform. You will learn the architectural best practices for designing and operating reliable, efficient, cost-effective and secure systems in the cloud by using the framework. This framework also provides a way to consistently measure your architectures against best practices and identify areas for improvement.

**Use Cases**

- **Measure Architecture:** Use the framework to measure your existing architecture against AWS best practices.
- **Identify Improvements:** Identify areas of risk and specify the necessary improvements to be made.
- **Guide Development:** Apply the framework’s principles during the design phase of a new workload to ensure a strong foundation.
- **Governance:** Establish a common language and set of standards for all development teams in your organization.

---

## 2. How do you use the AWS Well-Architected Framework?

*Source: [`05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md`](../05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md)*

In its raw form, the AWS Well-Architected Framework is simply a body of knowledge that is compiled in a single PDF document or included in the online AWS documentation. It contains specific best practices, design patterns, and other concepts that you can use to review your existing cloud architecture. The AWS Well-Architected Framework contains key architectural questions that can help you verify and measure the quality of your systems.

Say, for example, you are developing an online solution that handles sensitive financial information. Your system has passed all the integration tests and is finally ready for production deployment any time soon. However, you still want to ensure that your cloud infrastructure in AWS is indeed secure as part of your corporate security compliance.

You can check the security pillar of the AWS Well-Architected Framework that focuses on protecting your data, files, and overall systems. This includes key topics on data integrity, managing user permissions, and establishing controls to detect security incidents.

In essence, you can improve your cloud designs by simply answering the evaluation questions and following the best practices provided by this framework. These questions will shed light on your existing or new architecture in the AWS Cloud. It has questions like:

- “How do you protect your data at rest?”
- “How do you protect your data in transit?”
- “How do you manage identities for people and machines?”
- …and so on and so forth.

Your answer to these questions can show if your cloud architecture is secure or not. If you responded “I don’t know” in the “How do you protect your data at rest?” question, then that means your architecture is not secure and has a high number of security vulnerabilities. This signifies that you don’t employ encryption and tokenization schemes in your system.

The same goes for the “How do you protect your data in transit?” query. If you answer that you do not protect your data in transit, then that indicates your architecture has no firewall rules, network authentication, secure key management, and other mechanisms to keep your sensitive data safe as it traverses through different systems and networks. With this realization, you can now resolve the deficiencies in your system by following the prescriptive guidance provided by the AWS Well-Architected Framework.

---

## 3. What are the AWS Well-Architected Framework Pillars?

*Source: [`05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md`](../05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md)*

**1. Operational Excellence**

- The ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures.
- There are four best practice areas and tools for operational excellence in the cloud:

- **Organization** – AWS Cloud Compliance, [AWS Trusted Advisor](https://tutorialsdojo.com/aws-trusted-advisor/), [AWS Organizations](https://tutorialsdojo.com/aws-organizations/)
- **Prepare** – [AWS Config](https://tutorialsdojo.com/aws-config/)
- **Operate** – [Amazon CloudWatch](https://tutorialsdojo.com/amazon-cloudwatch/)
- **Evolve** – Amazon OpenSearch Service
- Key AWS service:
    - [**AWS CloudFormation**](https://tutorialsdojo.com/aws-cloudformation/) for creating templates. (See AWS Management Tools Cheat Sheet)

**2. Security**

- The ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies.
- There are six best practice areas and tools for security in the cloud:
    - **Security** – [AWS Shared Responsibility Model](https://tutorialsdojo.com/aws-shared-responsibility-model/), AWS Config, AWS Trusted Advisor
    - [**Identity and Access Management**](https://tutorialsdojo.com/aws-identity-and-access-management-iam/) – IAM, Multi-Factor Authentication, [AWS Organizations](https://tutorialsdojo.com/aws-organizations/)
    - **Detective Controls** – [AWS CloudTrail](https://tutorialsdojo.com/aws-cloudtrail/), AWS Config, [Amazon GuardDuty](https://tutorialsdojo.com/amazon-guardduty/)
    - **Infrastructure Protection** – [Amazon VPC](https://tutorialsdojo.com/amazon-vpc/), [Amazon CloudFront](https://tutorialsdojo.com/amazon-cloudfront/) with [AWS Shield](https://tutorialsdojo.com/aws-shield/), [AWS WAF](https://tutorialsdojo.com/aws-waf/)
    - **Data Protection** – [ELB](https://tutorialsdojo.com/aws-elastic-load-balancing-elb/), Amazon Elastic Block Store ([Amazon EBS](https://tutorialsdojo.com/amazon-ebs/)), [Amazon S3](https://tutorialsdojo.com/amazon-s3/), and [Amazon Relational Database Service](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/) (Amazon RDS) encryption, [Amazon Macie](https://tutorialsdojo.com/amazon-macie/), [AWS Key Management Service (AWS KMS)](https://tutorialsdojo.com/aws-key-management-service-aws-kms/)
    - **Incident Response** – IAM, Amazon EventBridge
- Key AWS service:
    - **AWS Identity and Access Management (IAM)**

**3. Reliability**

- The ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues.
- There are four best practice areas and tools for reliability in the cloud:
    - **Foundations** – IAM, Amazon VPC, AWS Trusted Advisor, AWS Shield
    - **Change Management** – AWS CloudTrail, AWS Config, Auto Scaling, Amazon CloudWatch
    - **Failure Management** – AWS CloudFormation, Amazon S3, AWS KMS, Amazon S3 Glacier
    - **Workload Architecture** – AWS SDK, [AWS Lambda](https://tutorialsdojo.com/aws-lambda/)
- Key AWS service:
    - **Amazon CloudWatch**

**4. Performance Efficiency**

- The ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve.
- There are four best practice areas for performance efficiency in the cloud:
    - **Selection** – Auto Scaling for Compute, Amazon EBS and S3 for Storage, Amazon RDS and DynamoDB for Database, Route53, VPC, and AWS Direct Connect for Network
    - **Review** – AWS Blog and What’s New section of the website
    - **Monitoring** – Amazon CloudWatch
    - **Tradeoffs** – Amazon Elasticache, Amazon CloudFront, [AWS Snowball](https://tutorialsdojo.com/aws-snowball/), Amazon RDS read replicas.
- Key AWS service:
    - **Amazon CloudWatch**

**5. Cost Optimization**

- The ability to avoid or eliminate unneeded cost or suboptimal resources.
- There are five best practice areas and tools for cost optimization in the cloud:
    - **Cloud Financial Management** – [Amazon QuickSight](https://tutorialsdojo.com/amazon-quicksight/), AWS Cost and Usage Report (CUR)
    - **Cost-Effective Resources** – Cost Explorer, Amazon CloudWatch and Trusted Advisor, Amazon Aurora for RDS, [AWS Direct Connect](https://tutorialsdojo.com/aws-direct-connect/) with Amazon CloudFront
    - **Matching supply and demand** – Auto Scaling
    - **Expenditure Awareness** – AWS Cost Explorer, AWS Budgets
    - **Optimizing Over Time** – AWS News Blog and the What’s New section on the AWS website, AWS Trusted Advisor

- Key AWS service:
    - **Cost Explore**

**6. Sustainability**

- The ability to increase efficiency across all components of a workload by maximizing the benefits from the provisioned resources.
- There are six best practice areas for sustainability in the cloud:
    - **Region Selection** – [AWS Global Infrastructure](https://tutorialsdojo.com/aws-global-infrastructure/)
    - **User Behavior Patterns** – Auto Scaling, Elastic Load Balancing
    - **Software and Architecture Patterns** – AWS Design Principles
    - **Data Patterns** – Amazon EBS, [Amazon EFS](https://tutorialsdojo.com/amazon-efs/), Amazon FSx, Amazon S3
    - **Hardware Patterns** – [Amazon EC2](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/), AWS Elastic Beanstalk
    - **Development and Deployment Process** – AWS CloudFormation
- Key AWS service:
    - **Amazon EC2 Auto Scaling**

---

## 4. What is Cloud Computing?

*Source: [`05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md`](../05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md)*

# 

Last updated on May 3, 2023

The first time you hear the term Cloud Computing, you probably have asked yourself these questions: “**What exactly is the Cloud in Cloud Computing?**” and “**Why do so many companies use it?**”

Basically, **cloud computing** is an on-demand computing service that you can avail over the Internet to host and run your applications. The “cloud” in cloud computing simply refers to the underlying network or servers that run your web applications, database, and many others. Of course, the term “cloud” does not allude to that white, puffy, and cotton-looking thing in the sky. The physical servers are not hovering above the troposphere either. These servers are actually hosted on data centers around the world and possibly could be situated in one of the buildings in the city that you live in.

In the past, before you could launch a website or an enterprise application, you needed to procure and set up your own physical servers first to deploy your applications. You are also responsible for managing, patching, and troubleshooting your servers and network devices. The problem here is that it takes a lot of time, effort and money just to make your solutions available online.

But with **cloud computing**, all you need to do is avail of the computing services over the Internet and the cloud service provider will be responsible for managing the underlying infrastructure that runs your websites. It’s like you are ‘renting’ a server and after you are done using it, you have the option to end your subscription to stop accumulating unnecessary costs. This empowers you, as well other businesses, to focus on building solutions rather than spending a lot of time setting up and managing servers.

**Cloud Computing** provides a plethora of helpful services that small and big companies can leverage on. Its services include domain registration, Internet of Things (IoT), data analytics, machine learning, gaming, mobile development, Desktop-as-a-Service (DaaS), quantum computing and many more. This is why there are so many companies and even startups leveraging its power to launch their products faster, save on operating costs, and scale globally with ease.

---

## 5. What is the AWS Cloud Adoption Framework?

*Source: [`05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md`](../05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md)*

The AWS Cloud Adoption Framework, or AWS CAF for short, is simply a framework provided by AWS to assist you in adopting cloud computing for your enterprise infrastructure. It is a framework that contains various perspectives that are based on years of extensive experience and best practices in AWS. This can help you digitally transform and accelerate your digital transformation as well as business outcomes through the innovative use of the AWS Cloud.

AWS CAF zeroes in on specific organizational capabilities that are vital in successful cloud transformations. The capabilities and perspectives of this framework provide best-practice guidance that assists companies in improving their total cloud readiness.

---

## 6. What are the different Perspectives of the AWS Cloud Adoption Framework?

*Source: [`05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md`](../05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md)*

The AWS Cloud Adoption Framework groups its many capabilities in 6 different perspectives namely:

- Business

- People
- Governance
- Platform
- Security
- Operations

Each of these perspectives consists of a set of capabilities that particular stakeholders own or manage in the company’s cloud transformation journey.  These perspectives can identify and prioritize transformation opportunities, evaluate and improve your company’s cloud readiness as well and evolve your transformation roadmap iteratively.

---

## 7. Why Cloud Computing?

*Source: [`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*

- IT assets becoming programmable resources
- Global availability and unlimited capacity
- High-level managed services, incl call center functionality, text to voice, machine learning, etc
- Security built in (AWS manages security)

---

## 8. What’s free?

*Source: [`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*

1. Amazon VPC
2. Elastic Beanstalk (services it provisions are not free)
3. CloudFormation (services it provisions not free)
4. Identity Access Management (IAM)
5. Auto Scaling (EC2 instances it uses are not free)
6. Opsworks
7. Consolidated Billing (add all AWS accounts into one bill)

---

## 9. What determines price?

*Source: [`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*

1. Clock hours of server time (time server is running)
2. Machine configuration (more resources consumed = more paid)
3. Machine purchase type (some instance types cost more)
4. Number of instances
5. Load balancing
6. Detailed monitoring (monitor EC2 by minute instead of 5-min intervals)
7. Auto scaling (EC2 instances cost money)
8. Elastic IP Addresses
9. Operating systems (Windows) and software packages
- Elastic Compute Cloud can reserve instances ahead of time, even cheaper if you pay upfront

---

## 10. S3 – What determines price?

*Source: [`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*

1. Storage class (Standard or IA)
2. Storage amount
3. Number of requests
4. Data transfer (data transfer out)

---

## 11. RDS – What determines price?

*Source: [`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*

1. Number of hours RDS is running
2. Database characteristics (licensed?)
3. Database purchase type (huge, nano?)
4. Number of instances
5. Provisioned storage (how big?)
6. Requests made to database
7. Deployment type (multi A-Z, read replicas)
8. Data transfer out

---

## 12. Cloudfront – What determines price?

*Source: [`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*

1. Traffic distribution
2. Requests
3. Data transfers out

---

## 13. What is a Microservice REALLY?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

- A **microservice** is an **independently deployable**, **loosely coupled**, and **domain-driven component** that handles one business responsibility.
- A real microservice:
    - Has its own **data storage**
    - Communicates with others through **well-defined APIs**
    - Can fail **without breaking** the entire system
    - Can be **deployed independently**

Common misconception:

> "Just splitting code and putting it in different folders or deploying it in different Docker containers doesn’t mean you’ve implemented microservices."
> 

---

---

## 14. When You Use What?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

- Entity: Only for persistence (DB operations)
- DTO: Only for API request/response
- POJO: Anywhere for simple data holding or business logic

---

---

## 15. What makes a class immutable?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

An **immutable class** is one whose instances cannot be changed after creation. Once the object is created, its state (field values) cannot be modified.

Key rules for making a class immutable:

1. **Mark the class as `final`** → Prevents subclassing, which could add mutability.
2. **Make all fields `private`**  **and `final`** → `private` prevents direct access, `final` ensures they can’t be reassigned.
3. **No setters** → Do not provide methods that change field values after object creation.
4. **Initialize all fields in the constructor** → Ensures the object’s state is fully set at creation time.
5. **Defensive copies for mutable fields** → If your class has fields like `Date` or `List` , don’t expose them directly. Example: return a copy in the getter, and copy inputs in the constructor.
6. **Don’t allow methods to modify state**  → Every method should return a new object instead of altering the current one.

---

**Example of an immutable class:**

---

```java
public final class Person {
    private final String name;
    private final int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // No setters
    public String getName() { return name; }
    public int getAge() { return age; }

    // If change needed, return new object
    public Person withAge(int newAge) {
        return new Person(this.name, newAge);
    }
}
```

---

## 16. Why use an interceptor?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

- **Centralized error handling** → No need to repeat `catchError` in every service.
- **Automatic retries** → Can handle transient network issues globally.
- **Request/response modifications** → e.g., adding auth tokens or headers.

Register in `app.module.ts`:

```java
providers: [
  { provide: HTTP_INTERCEPTORS, useClass: ApiInterceptor, multi: true }
]
```

6. **Consuming API in Components**

```java
@Component({...})
export class UserListComponent implements OnInit {
  users: User[] = [];
  errorMsg = '';

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.userService.getUsers().subscribe({
      next: data => this.users = data,
      error: err => this.errorMsg = err.message
    });
  }
}
```

**Observable subscription** → Essential because `HttpClient`  returns Observables.

**Handles success & error** → Makes the UI reactive to API results.

**Runs in `ngOnInit()`**  → Ensures data is fetched **after component initialization**.

---

---

## 17. Why Deploy Frontend and Backend in Separate Pods?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

Deploying **Angular frontend** and **Spring Boot backend** in separate pods is standard practice in Kubernetes/microservices for several reasons:

---

**1. Independent Scaling**

- Frontend and backend often have **different resource requirements**.
    - Example:
        - Angular frontend (static assets served via Nginx) → CPU/memory light
        - Spring Boot backend → CPU-heavy for business logic and DB calls
- **Separate pods allow scaling individually** using Kubernetes **replicas or HPA**.

```java
Frontend: 3 replicas (static content, high user load)
Backend: 5 replicas (heavy API processing)
```

**2. Independent Deployment & Updates**

- Frontend and backend are **built separately** and **released independently**.
- Example:
    - Update Angular UI → deploy frontend pods only
    - Update Spring Boot API → deploy backend pods only
- Reduces risk and downtime.

---

**3. Isolation and Fault Tolerance**

- If **frontend crashes**, backend continues running and serving API (for other clients or apps).
- If backend crashes, frontend pods can still serve cached or static content.
- Limits blast radius of failures.

---

**4. Technology/Runtime Differences**

- Frontend → served via **Nginx / HTTP server / CDN**
- Backend → runs **Java JVM**
- Running them in the **same container/pod** would require multiple processes in one pod, which is **against Kubernetes best practices**.

**5. Resource Management**

- Separate pods allow **fine-grained resource limits and requests** in Kubernetes.
    - Frontend: `cpu: 100m` , `memory: 128Mi`
    - Backend: `cpu: 500m` , `memory: 1Gi`
- Sharing a pod would force compromises.

---

**6. Better Observability & Monitoring**

- Separate pods → separate **logs, metrics, and alerts**
- Easier to troubleshoot frontend vs backend issues

---

**7. Supports Microservices Architecture**

- Backend often consists of **multiple microservices**.
- Frontend can communicate with **many backend services** via APIs.
- Each service in its own pod → **loose coupling**, easier CI/CD, better maintainability.

---

**Summary Table**

| Reason+++ | Benefit+ |
| --- | --- |
| Independent Scaling+ | Scale frontend & backend separately |
| Independent Deployment+ | Faster UI updates without touching backend |
| Isolation / Fault Tolerance+ | Crashes in one pod don’t affect the other |
| Runtime Differences+ | Frontend (Nginx) vs Backend (JVM) |
| Resource Management+ | Allocate CPU/memory efficiently |
| Observability+ | Separate logs and monitoring |
| Microservices Alignment+ | Backend services independently managed |

---

**Key principle:**

> In Kubernetes, each container/pod should ideally run **a single responsibility**
> 
> 
> **Frontend and backend have different responsibilities, lifecycles, and resource needs,  so they are deployed separately.**
> 

**How would you debug if frontend pod cannot reach backend pod?**

---

## 18. Why not always rely on ngOnChanges?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

- `ngOnChanges` only runs when the **reference of an `@Input()`** property changes.
- If you mutate a complex object/array **without replacing its reference**, `ngOnChanges` won’t trigger.

---

## 19. First, what is <ng-content>?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

- `<ng-content>` is Angular’s way of **content projection** (like a placeholder).
- It lets a parent pass custom HTML into a child component’s template.

```java
@Component({
  selector: 'card',
  template: `
    <div class="card">
      <ng-content></ng-content>
    </div>
  `
})
export class CardComponent {}
```

Parent

```java
<card>
  <p>This is projected into the card!</p>
</card>
```

Rendered:

```java
<div class="card">
  <p>This is projected into the card!</p>
</div>
```

---

## 20. Where does ngAfterContentInit fit?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

- When Angular first inserts that `<p>` into `<ng-content>` ,
- It calls **`ngAfterContentInit()`** inside the `CardComponent` .
- This ensures you can now safely access or manipulate the projected content.

Example

```java
@Component({
  selector: 'child-comp',
  template: `
    <div>
      <h3>Child component:</h3>
      <ng-content></ng-content>
    </div>
  `
})
export class ChildComponent implements AfterContentInit {
  ngAfterContentInit() {
    console.log('ngAfterContentInit: projected content is ready');
  }
}
```

Parent:

```java
<child-comp>
  <p>Hello from parent!</p>
</child-comp>
```

Console output:

```java
ngAfterContentInit: projected content is ready
```

---

## 21. What is ngAfterContentChecked()?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

- A lifecycle hook in Angular.
- Called **every time Angular runs change detection** and checks the **projected content** (`<ng-content>` ).
- It runs **after**:
    1. `ngAfterContentInit()` (first time only)
    2. On **every subsequent change detection cycle** thereafter.

**Example with <ng-content>**

Child component:

```java
@Component({
  selector: 'child-comp',
  template: `
    <div>
      <h3>Child component:</h3>
      <ng-content></ng-content>
    </div>
  `
})
export class ChildComponent implements AfterContentInit, AfterContentChecked {
  ngAfterContentInit() {
    console.log('ngAfterContentInit: content projected first time');
  }

  ngAfterContentChecked() {
    console.log('ngAfterContentChecked: content checked in CD cycle');
  }
}
```

Parent:

```java
<child-comp>
  <p>{{message}}</p>
</child-comp>

<button (click)="message = 'Updated message!'">Update</button>
```

**What happens in console:**

Initial load:

```java
ngAfterContentInit: content projected first time
ngAfterContentChecked: content checked in CD cycle
```

Click the button (change detection runs again):

```java
ngAfterContentChecked: content checked in CD cycle
```

**Key difference from ngAfterContentInit**

- `ngAfterContentInit` → Runs **once**, when content is first projected.
- `ngAfterContentChecked` → Runs **every time** change detection re-checks that projected content (may happen many times).

---

**Use case**

- When you need to react **every time the projected content changes**.
- Example: updating calculations, logging, validating, or triggering child logic when parent-projected content updates.

---

**Analogy**

- **`ngAfterContentInit`** → "The guest (content) has arrived for the first time."
- **`ngAfterContentChecked`** → "I keep checking on the guest every time there’s an update in the house."

**Summary**:

- `ngAfterContentChecked` is called **after every check of projected content** during change detection.
- It pairs with `ngAfterContentInit` :
    - Init → runs once
    - Checked → runs on every cycle

---

## 22. So how is ngDoCheck() different from ngAfterContentChecked()?

*Source: [`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

- **`ngDoCheck()`**
    - Called very early in the cycle, after Angular’s default input check.
    - Meant for **custom change detection logic** (e.g., deep object comparisons).
    - Doesn’t care whether it’s about content, view, or inputs — it’s global to the component.
- **`ngAfterContentChecked()`**
    - Called **after Angular has finished checking projected content** (`<ng-content>` ).
    - Runs in every change detection cycle too, but specifically signals: “Angular has checked the **content projection area**.”
    - Useful if you need to run logic that depends on the **final projected content state**.

---

---

## Question bank (no recorded answers)

Prompts collected from the notes that have no written answer yet:

- “How do you protect your data at rest?” — *[`05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md`](../05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md)*
- “How do you protect your data in transit?” — *[`05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md`](../05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md)*
- “How do you manage identities for people and machines?” — *[`05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md`](../05-aws-cloud-practitioner/cheat-sheets/cheat-sheets-for-aws-cloud-practitioner.md)*
- Database characteristics (licensed?) — *[`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*
- Database purchase type (huge, nano?) — *[`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*
- Provisioned storage (how big?) — *[`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*
- What are resource groups? Group resources based on tags — *[`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*
- What is the benefit of consolidated billing? — *[`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*
- What’s the benefit of AWS Quick Starts? — *[`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*
- Do you have the ability to stop something from happening? If you dont have the ability to stop it, it’s Amazon’s responsibility — *[`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*
- Cost Optimization (do you have an EC2 with nothing happening on it or an empty DB?) — *[`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*
- Fault Tolerance (are you using multiple avail zones?) — *[`05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md`](../05-aws-cloud-practitioner/printable/need-to-print-this-cloud-practitioner-notes.md)*
- Ask: “Can I deploy this service independently?” — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- Maybe call it a POJO, maybe a DTO… who knows? — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- When do you use it? Inside the Repository and Service layer to interact with the database. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- Why not return this in API? It leaks password and internal fields (like isAdmin) Any DB schema change will break your API — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- When do you use it? — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- Where is it used? — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- When do you use it? Anywhere internally when you just need a plain object for calculations, caching, or logic. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- Response body — is it JSON as expected? — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- Did request reach the controller? — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- Any exceptions thrown in service or repository layer? — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What makes a class immutable and why use immutability?What to listen for: final fields, no setters, defensive copies. Benefits: thread-safety, simpler reasoning. Outline: final class/fields, private fields, constructor initialization, no setters, return copies for mutable internals. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What are checked vs unchecked exceptions? When would you use each?What to listen for: compile-time enforcement vs runtime; API design tradeoffs. Outline: Checked must be declared/handled (e.g., IOException ), unchecked extend RuntimeException . Use checked for recoverable problems; unchecked for programming errors. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you profile and diagnose a Java performance issue in production?What to listen for: metrics, thread dumps, heap dumps, profilers, replicating issue, safe production sampling. Outline: gather metrics (CPU, memory, GC), capture thread/heap dump, analyze with tools (jstack, jmap, VisualVM, async-profiler), add tracing/metrics, make targeted fix. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What does Spring Boot auto-configuration do and how does it work?What to listen for: @EnableAutoConfiguration , spring.factories /spring-boot-autoconfigure . Outline: Boot scans classpath and applies sensible defaults via auto-configuration classes; override with properties or user config. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you structure a Spring Boot microservice for maintainability?What to listen for: layered packages, DTOs, service interfaces, domain vs infra separation, config management. Outline: separate controllers/services/repositories, use DTOs and mappers, externalize config, small single-responsibility services. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you manage service-to-service communication (sync vs async)?What to listen for: tradeoffs of HTTP/REST/gRPC vs messaging (Kafka/RabbitMQ), consistency patterns. Outline: sync for simple req/resp (REST, gRPC), async for decoupling/capacity (message brokers), consider retry/backoff, idempotency. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What are circuit breakers, and why use them?What to listen for: resilience patterns to avoid cascading failures, example frameworks (Resilience4j, Hystrix legacy). Outline: detect failing downstream, open circuit to fail fast, reset after interval; metrics/control via Resilience4j. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How would you secure microservices (auth/authz, tokens)?What to listen for: OAuth2/JWT, token validation, scopes/roles, API gateway as enforcement point. Outline: use JWT/OAuth2 for identity, validate tokens in each service or via gateway, rotate keys, use TLS, least privilege. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you handle configuration across environments in Spring Boot?What to listen for: profiles, externalized config, config servers (Spring Cloud Config), secrets management. Outline: use application-{profile}.yml , env vars, HashiCorp Vault or cloud secret managers, central config server for many services. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How would you design and test database transactions in distributed microservices?What to listen for: distributed transactions not recommended, SAGA pattern, compensation, idempotency. Outline: avoid 2PC; use SAGA (choreography or orchestration), design compensating actions, ensure idempotent operations. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you manage state in a medium-sized Angular app?What to listen for: when to use services vs NgRx vs simpler local state, pros/cons. Outline: use services + RxJS for lightweight, NgRx or Akita for complex state and time-travel/debugging, avoid over-engineering. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do change detection strategies work and when to use OnPush ?What to listen for: default vs OnPush, immutability benefits, performance gains. Outline: default checks whole tree; OnPush checks only on input change or observable emits—use with immutable data to improve perf. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you optimize frontend performance (Angular)?What to listen for: lazy loading, AOT, bundle splitting, trackBy, minimize bindings. Outline: AOT compilation, lazy load modules, use trackBy in ngFor , avoid heavy watchers, prune third-party libs. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you test Angular components & services?What to listen for: unit tests (Karma/Jest), TestBed, component harnesses, e2e (Cypress/Playwright). Outline: unit tests with TestBed, mocks for services, e2e for flows; use component harnesses and snapshot testing where useful. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- When would you use SSR (Angular Universal) or not?What to listen for: SEO, first paint improvements vs added complexity. Outline: SSR for SEO or perceived perf on initial load; otherwise client-side rendering for simpler apps. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you optimize slow SQL queries?What to listen for: use EXPLAIN, indexes, avoid SELECT , proper joins, query rewrite, caching. Outline: EXPLAIN plan, add indexes, rewrite queries, denormalize when required, caching layer for hot reads. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- When to use NoSQL vs relational DB for parts of a full-stack app?What to listen for: data shape, consistency needs, query patterns. Outline: use relational for transactional/ACID needs; NoSQL for large-scale, schema-less, denormalized read-heavy workloads. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How would you set up CI/CD for a Java + Angular microservices project?What to listen for: build, test, containerization, artifact repo, deployment pipelines. Outline: pipeline: lint → unit tests → build (Maven/Gradle + Angular CLI) → build Docker images → push to registry → run integration tests → deploy via Helm/Argo/Flux; gating and rollbacks. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you design integration and contract tests between frontend and backend?What to listen for: contract testing (Pact), API mocks, integration test environments. Outline: use contract testing to ensure API compatibility, run integration tests in CI with staging services or test containers. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What logging and monitoring would you put in place for production?What to listen for: structured logs, correlation IDs, metrics, alerting, dashboards. Outline: JSON logs to ELK/EFK, metrics to Prometheus, tracing via OpenTelemetry, alert rules in PagerDuty/opsgenie, dashboards in Grafana. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you prioritize technical debt vs feature delivery?What to listen for: risk-based approach, ROI, incremental refactor, scheduling tech debt sprints. Outline: quantify risk & cost, allocate % of sprint to debt, backlog grooming, quick wins vs large refactors with feature flagging. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- Describe a time you had to debug a production incident — what steps did you take?What to listen for: calm, methodical incident response, RCA, postmortem. Outline: gather facts, mitigate impact, restore service, capture evidence (logs/metrics), root cause analysis, preventive actions. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you evaluate whether a candidate is a good full-stack hire in a 45-minute loop?What to listen for: balance between depth and breadth, practical coding task, system-design conversation. Outline: 15 min live coding focused on backend/frontend, 15 min architecture/design, 10 min testing/ops, 5 min culture/communication. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How does an Angular application typically communicate with a Spring Boot backend?Listen for: REST APIs, JSON over HTTP, HttpClient in Angular, CORS configuration. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What is CORS and how would you resolve CORS errors during integration?Listen for: browser restriction, configuring @CrossOrigin in Spring Boot, using proxy in Angular during dev. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you handle different environments (dev, test, prod) when making API calls from Angular to backend?Listen for: environment.ts in Angular, externalized config in Spring Boot, avoiding hardcoded URLs. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What are common security challenges when integrating frontend and backend?Listen for: protecting APIs, JWT/OAuth2, CSRF, HTTPS, token expiration handling on frontend. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How would you design authentication flow between Angular frontend and Spring Boot backend?Listen for: login endpoint → JWT issued → store in local/session storage → attach token in Authorization header → backend validates → refresh tokens. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you propagate errors from the backend to frontend gracefully?Listen for: structured error responses (status codes + messages), Angular interceptors, user-friendly UI messages. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What strategies do you use for API versioning and how does it affect the frontend?Listen for: /api/v1/... , backward compatibility, frontend adapting to breaking changes. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you ensure consistent data contracts between Angular and Spring Boot?Listen for: DTOs, shared OpenAPI/Swagger specs, contract testing (e.g., Pact). — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you handle pagination and filtering in an integrated system?Listen for: backend provides paginated endpoints with params (?page=1&size=10 ), frontend builds UI with results + metadata (total count). — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you secure API keys or sensitive configurations in Angular apps?Listen for: never store secrets in frontend, backend proxies calls, use environment variables only for non-sensitive info. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What challenges occur with session management in SPAs like Angular when backend is stateful?Listen for: stateless JWT preferred, session cookies issues, handling expiry & re-login flow. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you manage file uploads from Angular to Spring Boot?Listen for: multipart/form-data , Angular FormData , Spring Boot MultipartFile , handling large file sizes, validation. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How would you implement real-time updates between Angular and Spring Boot?Listen for: WebSockets (SockJS, STOMP), Server-Sent Events, polling fallback, challenges with scalability. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- What’s your approach when the frontend shows stale data but backend is updated?Listen for: cache invalidation, ETag/If-Modified-Since headers, websockets, refreshing strategy in frontend. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*
- How do you debug integration issues between Angular and Spring Boot?Listen for: using browser dev tools, Postman/Insomnia to test APIs separately, checking Spring Boot logs, enabling CORS logs, proxy debugging. — *[`05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md`](../05-aws-cloud-practitioner/tutorials-dojo/aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)*

