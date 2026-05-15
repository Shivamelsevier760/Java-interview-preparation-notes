# AWS cloud practitioner notes for the Examination

# **AWS Cloud Practitioner Certification Cheat Sheet**

![](https://miro.medium.com/v2/resize:fit:1050/1*GWfhS7elA5DByj0zDiwZjA.png)

A summary of AWS for AWS Cloud Practitioner Certification. This is a short brief that I took notes and read before going to the exam. Good Luck!

# **IAM (Identity and Access Management)**

- **Users** — Mapped to a physical user, has a password for AWS Console
- **Groups** — Contains users only
- **Policies** — JSON document that outlines permissions for users or groups
- **Roles** — For EC2 instants or AWS services
- **Security** — MFA + Password Policy
- **AWS CLI** — Manage your AWS services using the command-line
- **AWS SDK** — Manage your AWS services using a programming language
- **Access Keys** — Access AWS using the CLI or SDK
- **Audit — IAM** Credential Reports & IAM Access Advisor

# **EC2 (Elastic Compute Cloud)**

- **EC2 Instance** — AMI(OS) + Instance Size (CPU + RAM) + Storage + Security Group + EC2 User Data
- **Security Groups** — Firewall attached to the EC2 instance
- **EC2 User Data** — Script launched at the first start of an instance
- **SSH** — Start terminal into our EC2 Instances (port 22)
- **EC2 Instance Role** — Link to IAM roles
- **Purchasing Options** — On-demand, Spot, Reserved (Standard + Convertible), Dedicated Host, Dedicated Instance

# **EC2 Instance Storage**

- **EBS Volumes**○ Network drives attached to one EC2 instance at a time○ Mapped to an Availability Zones○ Can use EBS Snapshots for backups/transferring EBS volumes across AZ
- **AMI** — Create ready-to-use EC2 instance with our customizations
- **EC2 Image Builder** — Automatically build, test, and distribute AMIs
- **EC2** Instance Store○ High-performance hardware disk attached to our EC2 instance○ Lost if our instance is stopped/terminated
- **EFS** — Network file system, can be attached to 100s of instances in a region
- **EFS-IA** — Cost-optimized storage class of infrequent access file
- **FSx for Windows** — Network File System for Windows servers
- **FSx for Lustre** — High-Performance Computing Linux file system

# **ELB & ASG**

- **High Availability** vs **Scalability** (vertical and horizontal) vs **Elasticity** vs **Agility** in the Cloud
- **Elastic Load Balancers (ELB)**○ Distribute traffic across backend EC2 instances, can be Multi-AZ○ Supports health checks○ 4 types: Classic (old), Application (HTTP-L7), Network (TCP-L4), Gateay (L3)
- **Auto Scaling Groups (ASG)**○ Implement Elasticity for your application, across multiple AZ○ Scale EC2 instances based on the demand on your system, and replace unhealthy○ Integrated with the ELB

> ELB: Elastic Load Balancing
> 
> 
> ASG: Auto Scaling Group
> 

# **Amazon S3**

- **Buckets vs Objects** — global unique name, tied to a region
- **S3 Security** — IAM policy, S3 Bucket Policy (public access), S3 Encryption
- **S3 Websites** — Host a static website on Amazon S3
- **S3 Versioning** — Multiple versions for files, prevent accidental deletes
- **S3 Replication** — Same-region or cross-region, must enable versioning
- **S3 Storage Classes** — Standard, IA, 1Z-IA, Intelligent, Glacier (Instant, Flexible, Deep)
- **Snow Family** — Import data onto S3 through a physical device, edge computing○ **SnowCone & SnowCone SSD** — Storage capacity → 8TB HDD, 14TB SSD, Storage capacity → 8TBsize up to 24TB, online and offline○ **Snowball Edge & Storage Optimized** — Storage capacity → 80TB usable, Storage capacity → up to Petabytes, offline○ **SnowMobile** — Storage capacity → < 100PB, Storage capacity → up to Exabytes, offline
- **OpsHub** — Desktop application to manage Snow Family devices
- **Storage Gateway** — Hybrid solution to extend on-premises storage to S3

> IA: Infrequency Access
> 

![](https://miro.medium.com/v2/resize:fit:1050/0*wDp3rB0g9nfu0a7V.jpg)

via — [https://aws.amazon.com/s3/storage-classes/](https://aws.amazon.com/s3/storage-classes/)

# **Databases & Analytics**

- **Relational Databases-OLTP** — RDS & Aurora (SQL)
- **Differences between Multi-AZ, Read Replicas, Multi-Region**
- **In-memory Database** — ElasticCache
- **Key/Value Database**
    
    — DynamoDB (serverless) & DAX (cache for DynamoDB)
    
- **Warehouse-OLAP** — Redshift (SQL)
- **Hadoop Cluster** — EMR
- **Athena** — Query data on Amazon S3 (serverless & SQL)
- **QuckSight** — Dashboard on your data (serverless)
- **DocumentDB** — “Aurora for MongoDB” (JSON- NoSQL database)
- **Amazon QLDB** — Financial Transactions Ledger (immutable journal, cryptographically verifiable)
- **Amazon Managed Blockchain** — managed Hyperledger Fabric & Ethereum blockchains
- **Glue** — Managed ETL (Extract Transform Load) and Data Catalog service
- **Database Migration** — DMS
- **Neptune** — Graph Database (Social Network)

> OLAP: Online Analytics Processing
> 

![](https://miro.medium.com/v2/resize:fit:1050/0*KWdQJtVKbZOA7wS-.jpg)

# **Other Compute**

- **Docker** — Container technology to run applications
- **ECS** (Elastic Container Service)— Run docker containers on EC2 instance
- **Fargate**○ Run Docker containers without provisioning the infrastructure○ Serverless offering (no EC2 instances)
- **ECR** (Elastic Container Registry) — Private Docker Image Repository
- **Batch** — Run batch jobs on AWS across managed EC2 instance
- **Lightsail** — Predictable & low pricing for simple applications & DB

# **Lambda**

- **Lamba** — Serverless, Function as a Service, seamless scaling, reactive
- **Lambda Billings**○ By the time run x by the RAM Provisioned○ By the number of invocations
- **Language Support** — Many programming languages except (arbitrary) Docker
- **Invocation time** — up to 15 minutes
- **Use cases**○ Create Thumbnails for images uploaded onto S3○ Run a Serverless cron job
- **API Gateway** — Expose Lambda functions as HTTP API

# **Deployment**

- **CloudFormation** (AWS only)○ Infrastructure as Code, works with almost all AWS resources○ Repeat across Regions & accounts
- **Beanstalk** (AWS only)○ Platform as a Service (PaaS), limited to certain programming languages or Docker○ Deploy code consistently with a known architecture: ex, ALB+BC+RDS
- **CodeDeploy** (Hybrid) — Deploy & upgrade any application onto servers
- **Systems Manager** (Hybrid) — Patch, configure, and run commands at scale
- **OpsWorks** (Hybrid) — Managed Chef and Puppet in AWS
- **CodeCommit** — Store code in private git repository (version controlled)
- **CodeBuild** — Build & Test code in AWS
- **CodeDeploy** — Deploy code onto servers
- **CodePipeline** — Orchestration of pipeline (from code to build to deploy)
- **CodeArtifact** — Store software packages/dependencies on AWS
- **CodeStar** — Unified view for allowing developers to do CI/CD and code
- **Cloud9** — Cloud IDE with collab
- **AWS CDK** (Cloud Development Kit) — Defined your cloud infrastructure using a programming language

# **Leveraging the AWS Global Application**

- **Global DNS: Rute 53**○ It is great to route users to the closet deployment with the least latency○ Great for disaster recovery strategies
- **Global Content Delivery Network (CDN): CloudFront**○ Replicate part of your application to AWS Edge Locations — decrease latency○ Cache common requests — improved user experience and decreased latency
- **S3 Transfer Acceleration**○ Accelerate global uploads & download into Amazon S3
- **AWS Global Accelerator**○ Improve global application availability and performance using the AWS global network
- **AWS Outposts**○ Deploy Outposts Racks in your own Data Centers to extend AWS services
- **AWS WaveLenth**○ Brings AWS services to the edge of the 5G networks○ Ultra-low latency applications
- **AWS Local Zones**○ Brings AWS resources (compute, database, storage, …) closer to your users○ Good for latency-sensitive applications

# **Cloud Integration**

- **SQS** (Simple Queue Service)○ Queue service in AWS○ Multiple Producers, messages are kept up to 14 days○ Multiple Consumers share the read and delete message○ Used to **decouple** applications in AWS
- **SNS** (Simple Notification Service)○ Notification service in AWS○ Subscribers: Email, Lambda, SQS, HTTP, Mobile, …○ Multiple Subscribers, send all messages to all of them○ No message retention
- **Kinesis** — Real-time data streaming, persistence, and analysis
- **Amazon MQ** — Managed message broker for ActiveMQ and RabbitMQ in the cloud (MQTT, AMQP…protocols)

# **Cloud Monitoring**

- **CloudWatch**○ **Metrics** — Monitor the performance of AWS services and billing metrics○ **Alarms** — Automate notification, perform EC2 action, notify to SNS based on metrics○ **Logs** — Collect log files from EC2 instances, servers, Lambda functions…○ **Events** (or EventBridge) — React to events in AWS, or trigger a rule on a schedule
- **CloudTrail** — Audit API calls made within your AWS account
- **CloudTrail Insights** — Automated analysis of your CloudTrail Events
- **X-Ray** — Trace requests made through your distributed applications
- **AWS Health Dashboard** — Status of all AWS services across all regions
- **AWS Account Health Dashboard** — AWS events that impact your infrastructure
- **Amazon CodeGuru** — Automated code reviews and application performance recommendations

# **AWS Security & Compliance**

- **Share Responsibility on AWS**
- **Sheild** — Automatic DDoS Protection + 24/7 support for advanced
- **WAF** — Firewall to filter incoming requests based on rules
- **KMS** — Encryption keys managed by AWS
- **CloudHSM** — Hardware encryption, we manage encryption keys
- **AWS Certificate Manager** — Provision, manage, and deploy SSL/TLS certificates
- **Artifact** — Get access to compliance reports such as PCI, ISO, etc …
- **GuardDuty** — Find malicious behavior with VPC, DNS & CloudTrail Logs
- **Inspector** — Find software vulnerabilities in EC2, ECR images, and Lambda functions
- **Network Firewall** — Protect VPC against network attacks
- **Config** — Track config changes and compliance against rules
- **Macie** — Find sensitive data (e.g. PII data) in Amazon S3 buckets
- **CloudTrail** — Track API calls made by users within an account
- **Amazon Detective** — Find the root cause of security issues or suspicious activities
- **AWS Abuse** — Report AWS resources used for abusive or illegal purposes
- **Root user privilege**s○ Change account setting○ Close your AWS account○ Change or cancel your AWS Support plan○ Register as a seller in the Reserved Instance Marketplace

# **AWS Machine Learning**

- **Rekognition** — Face detection, labeling, celebrity recognition
- **Transcribe** — Audio to Text (e.g. subtitles)
- **Polly** — Text to Audio
- **Translate** — Translations
- **Lex** — Build conversation bots (e.g. chatbots), (like Alexa)
- **Connect** — Cloud contact center
- **Comprehend** — Natural Language Processing
- **SageMaker** — Machine Learning for every developer and data scientist
- **Forecast** — Build highly accurate forecasts
- **Kendra** — ML-powered search engine
- **Personalize** — Real-time personalized recommendations
- **Textact** — Detect text and data in documents

# **AWS VPC & Network**

- **VPC** — Virtual Private Cloud
- **Subnets** — Tied to an AZ, network partition of the VPC
- **Internet Gateway** — At the VPC level, provide Internet Access
- **NAT Gateway / Instances** — Give internet access to private subnets
- **NACL** — Stateless, subnet rules for inbound and outbound
- **Security Groups** — Stateful, operate at the EC2 instance level or ENI
- **VPC Peering** — Connect two VPC with non-overlapping IP ranges, nontransitive
- **Elastic IP** — Fixed public IPv4, ongoing cost if not in-use
- **VPC Endpoints** — Provide Private access to AWS Services within VPC
- **PrivateLink** — Privately connect to a service in a 3rd party VPC
- **VPC Flow Logs** — network traffic logs
- **Site to Site VPN** — VPN over public internet between op-premises DC and AWS
- **Client VPN** — OpenVPN connection from your computer into your VPC
- **Direct Connect** — Direct private connection to AWS
- **Transit Gateway** — Connect thousands of VPC and on-premises networks together

# **Account Best Practices**

- Operate multiple accounts using **Organizations**
- Use **SCP** (service control policies) to restrict account power
- Easily setup multiple accounts with best-practices with **AWS Control Tower**
- **Use Tags & Cost Allocation Tags** for easy management & billing
- **IAM guidelines** — MFA, least-privilege, password policy, password rotation
- **Cofig** To record all resources configurations & compliance over time
- **CloudFormation** to deploy stack across accounts and regions
- **Trusted Advisor** to get insights, Support Plan adapted to your needs
- **If your Account is compromised** — change the root password, delete and rotate all passwords/keys, contact the AWS support
- Allow users to create pre-defined stacks defined by admins using **AWS Service Catalog**

# **Billing and Costing Tools**

- **Compute Optimizer** — Recommends resources’ configuration to reduce cost
- **Pricing Calculator** — Cost of services on AWS
- **Billing Dashboard** — High-level overview + free tier dashboard
- **Cost Allocation Tags** — Tag resources to create detailed reports
- **Cost and Usage Reports** — The most comprehensive billing dataset
- **Cost Explorer** — View current usage (detailed) and forecast usage
- **Billing Alarms** — in us-east-1 — track overall and per-service billing
- **Budges** — More advanced — track usage, costs, RI, and get alerts
- **Saving Plans** — Easy way to save based on long-term usage of AWS
- **Cost Anomaly Detection** — Detect unusual spends using Machine Learning
- **Service Quotas** — Notify you when you’re close to the service quota threshold

# **Advanced Identity**

- **IAM**○ Identity and Access Management inside your AWS account○ For users that you trust and belong to your company
- **Organizations** — Manage multiple accounts
- **Security Token Service (STS)** — temporary, limited-privileges credentials to access AWS resources
- **Cognito** — Create a database of users for your mobile & web applications
- **Directory Services** — Integrate Microsoft Active Directory in AWS
- **IAM Identify Center** — One login for multiple AWS accounts & applications

# **AWS Support Plan**

There are four AWS support plans available:

- **Basic** — billing and account support only (access to forums only).
- **Developer** — business hours support via email.
- **Business** — 24×7 email, chat, and phone support.
- **Enterprise** — 24×7 email, chat, and phone support.

![](https://miro.medium.com/v2/resize:fit:1050/0*IoFRfh0fZF7o99Pz.png)

![](https://miro.medium.com/v2/resize:fit:1050/0*-Ygdk5l4SyWOo9Of.png)

# **AWS Well-Architected and the Six Pillars**

The AWS Well-Architected Framework describes key concepts, design principles, and architectural best practices for designing and running workloads in the cloud. By answering a few foundational questions, learn how well your architecture aligns with cloud best practices and gain guidance for making improvements.

![](https://miro.medium.com/v2/resize:fit:1050/0*CIN9GQdKLwJt_tK4.jpg)

- **Operational Excellence Pillar** — Includes the ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures
- **Performance Efficiency Pillar** — The performance efficiency pillar focuses on the structured and streamlined allocation of IT and computing resources. Key topics include selecting resource types and sizes optimized for workload requirements, monitoring performance, and maintaining efficiency as business needs evolve.
- **Reliability Pillar** — The reliability pillar focuses on workloads performing their intended functions and how to recover quickly from failure to meet demands. Key topics include distributed system design, recovery planning, and adapting to changing requirements.
- **Security Pillar** — The security pillar focuses on protecting information and systems. Key topics include confidentiality and integrity of data, managing user permissions, and establishing controls to detect security events.
- **Cost Optimization Pillar** — The cost optimization pillar focuses on avoiding unnecessary costs. Key topics include understanding spending over time and controlling fund allocation, selecting resources of the right type and quantity, and scaling to meet business needs without overspending.
- **Sustainability Pillar** — The sustainability pillar focuses on minimizing the environmental impacts of running cloud workloads. Key topics include a shared responsibility model for sustainability, understanding impact, and maximizing utilization to minimize required resources and reduce downstream impacts.

## **AWS Cloud Adoption Framework (AWS CAF)**

![](https://miro.medium.com/v2/resize:fit:1050/0*FMZm6iwa6Bu8YmH0.png)

# **Other Services**

- **Amazon WorkSpace**○ Managed Desktop as a Service (DaaS) solution to easily **provision Windows or Linux desktops**○ **Great to eliminate management of on-premiseVDI** (Virtual Desktop Infrastructure)○ Fast and quickly scalable to thousands of users○ Secured data – integrates with KMS○ Pay-as-you-go service with monthly or hourly rates
- **Amazon AppSteam 2.0**○ Desktop Application Streaming Service○ Deliver to any computer, without acquiring, provisioning infrastructure○ **The application is delivered from within a web browser**
- **AWS IoT Core**○ AWS IoT Core allows you to easily connect IoT devices to the AWS Cloud○ **Serverless, secure & scalable** to billions of devices and trillions of messages○ Your applications can communicate with your devices even when they aren’t connected
- **Amazon Elastic Transcoder**○ ElasticTranscoder is used to **convert media files stored in S3 into media files in the formats required by consumer playback devices** (phones etc..)
- **AWS AppSync**○ Store and sync data across mobile and web apps in real-time○ **Makes use of GraphQL** (mobile technology from Facebook)
- **AWS Amplify —** A set of tools and services that helps you develop and deploy scalable full-stack web and mobile applications
- **AWS Device Farm** — Fully-managed service that tests your web and mobile apps against desktop browsers, real mobile devices, and tablets
- **AWS Backup** — Fully-managed service to centrally manage and automate backups across AWS services
- **Disaster Strategy**○ Backup and Restore○ Pilot Light○ Warm Standby○ Multi-site/Hot-site

![](https://miro.medium.com/v2/resize:fit:1050/0*HI8EzgiOc8wd-6iT.jpg)

- **Amazon Elastic Disaster Recovery (DRS) —** Quickly and easily recover your physical, virtual, and cloud-based servers into AWS
- **AWS DataSync**○ Move large amounts of data from on-premises to AWS○ Replication tasks can be scheduled hourly, daily, weekly○ The replication tasks are ***incremental*** after the first full load
- **AWS Application Discovery Service**○ Plan migration projects by gathering information about on-premises data centers○ Server utilization data and dependency mapping are important for migrations○ **Agentless Discovery** (AWS Agentless Discovery Connector) → VM inventory, configuration, and performance history such as CPU, memory, and disk usage○ **Agent-based Discovery** (AWS Application Discovery Agent) → System configuration, system performance, running processes, and details of the network connections between systems○ Resulting data can be viewed within AWS Migration Hub
- AWS Application Migration Service (MNG)
- AWS Migration Evaluator
- **AWS Migration Hub**○ Central location to collect servers and applications inventory data for the assessment, planning, and tracking of migrations to AWS○ Helps accelerate your migration to AWS, automate lift-and-shift○ **AWS Migration Hub Orchestrator** — provides pre-built templates to save time and effort migrating enterprise apps (e.g., SAP, Microsoft SQL Server…)○ Supports migrations status updates from A**pplication Migration Service (MGN)** and **Database Migration Service (DMS)**
- **AWS Fault Injection Simulator (FIS)**○ A fully managed service for running fault injection experiments on AWS workloads○ Based on Chaos Engineering — stressing an application by creating disruptive events (e.g., a sudden increase in CPU or memory), observing how the system responds, and implementing improvements**AWS Step Functions**○ Build a serverless visual workflow to orchestrate your Lambda functions○Use cases: order fulfillment, data processing, web applications, any workflow
- **AWS Ground Station**○ Fully managed service that lets you control satellite communications, process data, and scale your satellite operations○ Use cases: weather forecasting, surface imaging, communications, video broadcasts
- **Amazon Pinpoint**○ Scalable 2-ways (inbound/outbound) marketing communication service○ Supports email, SMS, push, voice, and in-app messaging○ Use cases: run campaigns by sending marketing, bulk, and transactional SMS messages

other people notes medium

https://medium.com/@austinwolff/my-aws-cloud-practitioner-notes-d3131f4c68a
- [https://medium.com/@kanani-nirav/aws-cloud-practitioner-exam-short-notes-a-study-guide-b8dcbebb292e](https://medium.com/@kanani-nirav/aws-cloud-practitioner-exam-short-notes-a-study-guide-b8dcbebb292e)
- [https://0xneel.medium.com/aws-certified-cloud-practitioner-notes-a0608e1ea6f4](https://0xneel.medium.com/aws-certified-cloud-practitioner-notes-a0608e1ea6f4)