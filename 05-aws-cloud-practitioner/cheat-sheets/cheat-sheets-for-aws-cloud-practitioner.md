# Cheat sheets for AWS cloud practitioner

# **AWS Compute Optimizer Cheat Sheet**

- A service that recommends optimal AWS resources to reduce costs and improve performance of your workloads.
- Uses machine learning to analyze historical utilization metrics.
- You can view findings and recommendations across AWS Regions and accounts.
- Generates recommendations for the following resources:
    - Amazon EC2 instances
    - Amazon EC2 Auto Scaling groups
    - Amazon EBS volumes
    - AWS Lambda functions

# **Concepts**

- Recommendation preferences are features that you can activate to enhance or augment the recommendations generated for your resources.
    - **Enhanced infrastructure metrics** – extends the look-back period for utilization metrics analysis to three months.
    - **Inferred workload type** – identify the effort to migrate workloads from x86-based to Arm-based AWS Graviton instances types.
    - **AWS Graviton-based instance recommendations** – provides price and performance impact.
- Delegated Administrator
    - You can delegate a member account in your organization as an administrator.
    - There can only be one delegated administrator per organization.
    - The delegated administrator can do the following:
        - Get and export recommendations
        - Get projected utilization metrics
        - Set recommendation preferences
        - Set member account opt-in status
    - You can use AWS console and CLI to register and remove an account as a delegated administrator.
- The dashboard allows you to view the optimization findings for your AWS resources across all AWS Regions.
- You can also export and share your recommendations to an Amazon S3 bucket.

# **AWS Compute Optimizer Pricing**

- You are charged for the enhanced infrastructure metrics per resource.
- You are charged based on the number of hours the resource runs.

# **AWS Pricing Cheat Sheet**

There are three fundamental drivers of cost with AWS:

- **Compute:** This refers to the cost of server time, typically billed by the second or hour. (e.g., EC2 instance runtime, Lambda function duration/requests).
- **Storage:** This refers to the cost of storing data in the cloud. (e.g., S3 storage in GB/month, EBS volume size).
- **Outbound Data Transfer:** This refers to the cost of data transferred *out* of an AWS Region to the internet.
    - **Data transfer into** AWS is generally free.
    - Data transfer *between* AWS services in the same Region is also generally free.

# **Core Pricing Principles**

AWS pricing is built on a few core principles:

- **Pay-as-you-go:** You pay only for the individual services you need, for as long as you use them. There are no long-term contracts or complex licensing requirements.

![aws pricing](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWS-Pricing.jpg)

- **Pay less when you reserve (Commitment Pricing):** You can receive significant discounts by committing to a certain amount of usage (e.g., 1 or 3 years).
- **Pay less by using more (Volume Discounting):** Many services (like Amazon S3 and data transfer) offer tiered pricing, so the per-unit cost decreases as your usage volume increases.

# **Pricing Models / Purchasing Options**

- **On-Demand:**
    - This is the default pay-as-you-go model. You pay for compute capacity by the hour or second with no long-term commitments. It is ideal for applications with short-term, spiky, or unpredictable workloads.
- **Reserved Instances (RIs):**
    - For certain services, such as [**Amazon EC2](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/), [Amazon EMR](https://tutorialsdojo.com/amazon-emr/),** and [**Amazon RDS**](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/), you can invest in reserved capacity. With Reserved Instances, you can save up to 75% over equivalent on-demand capacity. When you buy Reserved Instances, the larger the upfront payment, the greater the discount.
    - **All Upfront:** You pay for the entire Reserved Instance term with one upfront payment. This option provides you with the largest discount compared to On-Demand instance pricing.
    - **Partial Upfront:** You make a low upfront payment and are then charged a discounted hourly rate for the instance for the duration of the Reserved Instance term.
    - **No Upfront:** This option does not require any upfront payment and provides a discounted hourly rate for the duration of the term.
- **AWS Savings Plans:**
    - This is a **newer, more flexible** commitment-based pricing model that provides discounts up to **72%**.
    - You commit to a consistent dollar amount of usage (e.g., $10/hour) for a 1- or 3-year term, rather than a specific instance type.
    - **Compute Savings Plans:** The most flexible. They automatically apply to EC2, AWS Fargate, and AWS Lambda usage, regardless of instance family, size, or Region.
    - **EC2 Instance Savings Plans:** Offer the highest savings but are less flexible. They apply only to a specific instance family in a chosen Region.
- **Spot Instances:**
    - Allows you to use spare AWS compute capacity at up to a **90% discount** compared to On-Demand prices.
    - Ideal for fault-tolerant, stateless, or non-critical workloads, as AWS can reclaim the instance with a two-minute warning.

# **AWS Free Tier**

For new accounts, the AWS Free Tier is available.

- **12 Months Free:** Offers new AWS customers a free usage allowance for 12 months from the date the account was created. (e.g., 750 hours of EC2, 5GB of S3 storage).
- **Always Free:** These offers are available to all AWS customers without expiration. (e.g., 1 million Lambda requests/month, 10 custom CloudWatch metrics).
- **Trials:** Short-term free trials for specific services, starting from the time of first use.

# **Cost Management Tools**

- [**AWS Pricing Calculator:**](https://calculator.aws/#)
    - A free tool that allows you to estimate your monthly AWS bill.
    - You can estimate the cost of migrating your architecture to the cloud and find the lowest cost for your workload.
- [**AWS Cost Explorer:**](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
    - A free tool to visualize, understand, and manage your AWS costs and usage over time.
    - It includes a default report for the top cost-incurring services and a forecast of your likely spend for the month.
- [**AWS Budgets:**](https://aws.amazon.com/aws-cost-management/aws-budgets)
    - Allows you to set custom budgets (cost or usage) and receive alerts when actual or forecasted costs exceed your defined threshold.
- [**AWS Trusted Advisor:**](https://tutorialsdojo.com/aws-trusted-advisor)
    - Provides real-time guidance to help you provision your resources following AWS best practices.
    - The Cost Optimization pillar (available to all users) provides recommendations for eliminating unused or idle resources.

# **What is the AWS Well-Architected Framework?**

The AWS Well-Architected Framework is basically a body of knowledge that describes the various design principles, key concepts, design and architectural best practices that can help companies design and run highly efficient workloads in the AWS platform. This framework ensures that the company’s cloud architecture is in accordance with the AWS best practices. It also comes with related AWS features, services and tools that you can utilize to measure the overall efficiency of your design. The AWS Well-Architected Framework will empower you to improve your existing IT infrastructure in terms of your overall operations, security, reliability, efficiency, cost optimization, and sustainability.

Having well-architected systems greatly increases the plausibility of business success, which is why AWS created the AWS Well-Architected Framework. This framework is composed of **six pillars** that help you understand the pros and cons of the decisions you make while building cloud architectures and systems on the AWS platform. You will learn the architectural best practices for designing and operating reliable, efficient, cost-effective and secure systems in the cloud by using the framework. This framework also provides a way to consistently measure your architectures against best practices and identify areas for improvement.

### **Use Cases**

- **Measure Architecture:** Use the framework to measure your existing architecture against AWS best practices.
- **Identify Improvements:** Identify areas of risk and specify the necessary improvements to be made.
- **Guide Development:** Apply the framework’s principles during the design phase of a new workload to ensure a strong foundation.
- **Governance:** Establish a common language and set of standards for all development teams in your organization.

# **How do you use the AWS Well-Architected Framework?**

In its raw form, the AWS Well-Architected Framework is simply a body of knowledge that is compiled in a single PDF document or included in the online AWS documentation. It contains specific best practices, design patterns, and other concepts that you can use to review your existing cloud architecture. The AWS Well-Architected Framework contains key architectural questions that can help you verify and measure the quality of your systems.

![Tutorials dojo strip](https://tutorialsdojo.com/wp-content/uploads/2021/02/passyourawsazuregcpbanner.jpg)

Say, for example, you are developing an online solution that handles sensitive financial information. Your system has passed all the integration tests and is finally ready for production deployment any time soon. However, you still want to ensure that your cloud infrastructure in AWS is indeed secure as part of your corporate security compliance.

You can check the security pillar of the AWS Well-Architected Framework that focuses on protecting your data, files, and overall systems. This includes key topics on data integrity, managing user permissions, and establishing controls to detect security incidents.

In essence, you can improve your cloud designs by simply answering the evaluation questions and following the best practices provided by this framework. These questions will shed light on your existing or new architecture in the AWS Cloud. It has questions like:

- “How do you protect your data at rest?”
- “How do you protect your data in transit?”
- “How do you manage identities for people and machines?”
- …and so on and so forth.

Your answer to these questions can show if your cloud architecture is secure or not. If you responded “I don’t know” in the “How do you protect your data at rest?” question, then that means your architecture is not secure and has a high number of security vulnerabilities. This signifies that you don’t employ encryption and tokenization schemes in your system.

The same goes for the “How do you protect your data in transit?” query. If you answer that you do not protect your data in transit, then that indicates your architecture has no firewall rules, network authentication, secure key management, and other mechanisms to keep your sensitive data safe as it traverses through different systems and networks. With this realization, you can now resolve the deficiencies in your system by following the prescriptive guidance provided by the AWS Well-Architected Framework.

# **What are the AWS Well-Architected Framework Pillars?**

![AWS Well-Architected Framework – Six Pillars](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWS-Well-Architected-Framework-%E2%80%93-Six-Pillars.jpg)

### **1. Operational Excellence**

- The ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures.
- There are four best practice areas and tools for operational excellence in the cloud:

- **Organization** – AWS Cloud Compliance, [AWS Trusted Advisor](https://tutorialsdojo.com/aws-trusted-advisor/), [AWS Organizations](https://tutorialsdojo.com/aws-organizations/)
- **Prepare** – [AWS Config](https://tutorialsdojo.com/aws-config/)
- **Operate** – [Amazon CloudWatch](https://tutorialsdojo.com/amazon-cloudwatch/)
- **Evolve** – Amazon OpenSearch Service
- Key AWS service:
    - [**AWS CloudFormation**](https://tutorialsdojo.com/aws-cloudformation/) for creating templates. (See AWS Management Tools Cheat Sheet)

### **2. Security**

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

### **3. Reliability**

- The ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues.
- There are four best practice areas and tools for reliability in the cloud:
    - **Foundations** – IAM, Amazon VPC, AWS Trusted Advisor, AWS Shield
    - **Change Management** – AWS CloudTrail, AWS Config, Auto Scaling, Amazon CloudWatch
    - **Failure Management** – AWS CloudFormation, Amazon S3, AWS KMS, Amazon S3 Glacier
    - **Workload Architecture** – AWS SDK, [AWS Lambda](https://tutorialsdojo.com/aws-lambda/)
- Key AWS service:
    - **Amazon CloudWatch**

### **4. Performance Efficiency**

![Free AWS Courses](https://tutorialsdojo.com/wp-content/uploads/2022/01/td-learn-for-free-now.png)

- The ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve.
- There are four best practice areas for performance efficiency in the cloud:
    - **Selection** – Auto Scaling for Compute, Amazon EBS and S3 for Storage, Amazon RDS and DynamoDB for Database, Route53, VPC, and AWS Direct Connect for Network
    - **Review** – AWS Blog and What’s New section of the website
    - **Monitoring** – Amazon CloudWatch
    - **Tradeoffs** – Amazon Elasticache, Amazon CloudFront, [AWS Snowball](https://tutorialsdojo.com/aws-snowball/), Amazon RDS read replicas.
- Key AWS service:
    - **Amazon CloudWatch**

### **5. Cost Optimization**

- The ability to avoid or eliminate unneeded cost or suboptimal resources.
- There are five best practice areas and tools for cost optimization in the cloud:
    - **Cloud Financial Management** – [Amazon QuickSight](https://tutorialsdojo.com/amazon-quicksight/), AWS Cost and Usage Report (CUR)
    - **Cost-Effective Resources** – Cost Explorer, Amazon CloudWatch and Trusted Advisor, Amazon Aurora for RDS, [AWS Direct Connect](https://tutorialsdojo.com/aws-direct-connect/) with Amazon CloudFront
    - **Matching supply and demand** – Auto Scaling
    - **Expenditure Awareness** – AWS Cost Explorer, AWS Budgets
    - **Optimizing Over Time** – AWS News Blog and the What’s New section on the AWS website, AWS Trusted Advisor

- Key AWS service:
    - **Cost Explore**

### **6. Sustainability**

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

# **What is Cloud Computing?**

# 

Last updated on May 3, 2023

The first time you hear the term Cloud Computing, you probably have asked yourself these questions: “**What exactly is the Cloud in Cloud Computing?**” and “**Why do so many companies use it?**”

Basically, **cloud computing** is an on-demand computing service that you can avail over the Internet to host and run your applications. The “cloud” in cloud computing simply refers to the underlying network or servers that run your web applications, database, and many others. Of course, the term “cloud” does not allude to that white, puffy, and cotton-looking thing in the sky. The physical servers are not hovering above the troposphere either. These servers are actually hosted on data centers around the world and possibly could be situated in one of the buildings in the city that you live in.

In the past, before you could launch a website or an enterprise application, you needed to procure and set up your own physical servers first to deploy your applications. You are also responsible for managing, patching, and troubleshooting your servers and network devices. The problem here is that it takes a lot of time, effort and money just to make your solutions available online.

But with **cloud computing**, all you need to do is avail of the computing services over the Internet and the cloud service provider will be responsible for managing the underlying infrastructure that runs your websites. It’s like you are ‘renting’ a server and after you are done using it, you have the option to end your subscription to stop accumulating unnecessary costs. This empowers you, as well other businesses, to focus on building solutions rather than spending a lot of time setting up and managing servers.

**Cloud Computing** provides a plethora of helpful services that small and big companies can leverage on. Its services include domain registration, Internet of Things (IoT), data analytics, machine learning, gaming, mobile development, Desktop-as-a-Service (DaaS), quantum computing and many more. This is why there are so many companies and even startups leveraging its power to launch their products faster, save on operating costs, and scale globally with ease.

# **Benefits of Cloud Computing**

### **1. Agility**

You have the ability to quickly adapt and deploy services in the most costeffective way in response to changes in business requirements.

### **2. Elasticity**

In the case of varying workloads, it allows your resources to adjust quickly and to scale back and forth as the business capacity and needs change.

### **3. Cost Savings**

Instead of building and managing your own data center and physical servers, you can trade your Capital Expenses for Operational Expenses and pay only the amount you consume.

### **4. Deploy Globally in Minutes**

With just a few clicks, you can quickly deploy your application to different locations and enhance the experience of your users with reduced latency.

# **Types of Cloud Computing**

### **Infrastructure as a Service (IaaS)**

Full control of your infrastructure without the maintenance and operating costs of the servers. IaaS provides access to servers, storage, networking, and operating systems.

### **Platform as a Service (PaaS)**

In this model, you can focus on the deployment and management of your applications. PaaS eliminates the need to manage the underlying infrastructure.

### **Software as a Service (SaaS)**

The software is ready to be used and operated by the service provider. SaaS is also known as end-user applications.

![IaaS PaaS SaaS](https://tutorialsdojo.com/wp-content/uploads/2020/08/IaaS-PaaS-SaaS-1024x597.jpg)

# **Amazon VPC Cheat Sheet**

- Create a virtual network in the cloud dedicated to your AWS account where you can launch AWS resources
- Amazon VPC is the networking layer of [Amazon EC2](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)
- A VPC spans all the Availability Zones in the region. After creating a VPC, you can add one or more subnets in each Availability Zone.

# **Key Concepts**

- A **virtual private cloud** (VPC) allows you to specify an IP address range for the VPC, add subnets, associate security groups, and configure route tables.
- A **subnet** is a range of IP addresses in your VPC. You can launch AWS resources into a specified subnet. Use a **public subnet** for resources that must be connected to the internet, and a **private subnet** for resources that won’t be connected to the internet.
- To protect the AWS resources in each subnet, use **security groups** and **network access control lists (ACLs)**.
- Expand your VPC by adding secondary IP ranges.

# **EC2-VPC vs EC2-Classic**

![Amazon VPC](https://tutorialsdojo.com/wp-content/uploads/2018/12/EC2vsVPC-1024x717.jpg)

# **Default vs Non-Default VPC**

| **Default** | **Non-Default VPC** |
| --- | --- |
| If your account supports the EC2-VPC platform only, it comes with a default VPC that has a default subnet in each Availability Zone. | You can create your own non-default VPC, and configure it as you need. Subnets that you create in your non-default VPC and additional subnets that you create in your default VPC are called non-default subnets. |
| Your default VPC includes an internet gateway, which allows your instances to communicate with the internet, and each default subnet is a public subnet. | Instances can communicate with each other, but can’t access the internet. You can enable internet access for an instance launched into a non-default subnet by attaching an Internet Gateway and associating an Elastic IP address with the instance. |
| Each instance that you launch into a default subnet has a private IPv4 address and a public IPv4 address. | By default, each instance that you launch into a non-default subnet has a private IPv4 address, but no public IPv4 address, unless you specifically assign one at launch, or you modify the subnet’s public IP address attribute. |
| To allow an instance in your VPC to initiate outbound connections to the internet but prevent unsolicited inbound connections from the internet, you can use a network address translation (NAT) device for IPv4 traffic. |  |
| You can optionally associate an Amazon-provided IPv6 CIDR block with your VPC and assign IPv6 addresses to your instances. IPv6 traffic is separate from IPv4 traffic; your route tables must include separate routes for IPv6 traffic. |  |

### **A diagram of default VPC**

![AWS Training Amazon VPC](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWSTrainingAmazonVPC1.jpg)

### **A diagram of non-default VPC**

![AWS Training Amazon VPC](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWSTrainingAmazonVPC2.jpg)

# **Accessing a Corporate or Home Network**

- You can optionally connect your VPC to your own corporate data center using an **IPsec AWS managed VPN connection**, making the AWS Cloud an extension of your data center.
- A **VPN connection** consists of:
    - a **virtual private gateway** (which is the VPN concentrator on the Amazon side of the VPN connection) attached to your VPC.
    - a **customer gateway** (which is a physical device or software appliance on your side of the VPN connection) located in your data center.
    - A diagram of the connection

![Tutorials dojo strip](https://tutorialsdojo.com/wp-content/uploads/2021/02/passyourawsazuregcpbanner.jpg)

![AWS Training Amazon VPC](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWSTrainingAmazonVPC3.jpg)

- **AWS Site-to-Site Virtual Private Network** (VPN) connections can be moved from a virtual private gateway to an **AWS Transit Gateway** without having to make any changes on your customer gateway. Transit Gateways enable you to easily scale connectivity across thousands of Amazon VPCs, AWS accounts, and on-premises networks.
- **AWS PrivateLink** enables you to privately connect your VPC to supported AWS services, services hosted by other AWS accounts (VPC endpoint services), and supported AWS Marketplace partner services. You do not require an internet gateway, NAT device, public IP address, AWS Direct Connect connection, or VPN connection to communicate with the service. Traffic between your VPC and the service does not leave the Amazon network.
- AWS PrivateLink-Supported Services:

| • Amazon IP Gateway | • Amazon Elastic Container Registry |
| --- | --- |
| • Amazon AppStream 2.0 | • Amazon Elastic Container Service |
| • AWS App Mesh | • AWS Glue |
| • Application Auto Scaling | • AWS Key Management Service |
| • Amazon Athena | • Amazon Kinesis Data Firehouse |
| • AWS Auto Scaling | • Amazon Kinesis Data Streams |
| • Amazon Cloud Directory | • Amazon Rekognition |
| • AWS CloudFormation | • Amazon SageMaker and Amazon SageMaker Runtime |
| • AWS CloudTrail | • Amazon SageMaker Notebook |
| • Amazon CloudWatch | • AWS Secrets Manager |
| • Amazon CloudWatch Events | • AWS Security Token Service |
| • Amazon CloudWatch Logs | • AWS Server Migration Service |
| • AWS CodeBuild | • AWS Service Catalog |
| • AWS CodeCommit | • Amazon SNS |
| • AWS CodePipeline | • Amazon SQS |
| • AWS Config | • Amazon Systems Manager |
| • AWS DataSync | • AWS Storage Gateway |
| • Amazon EC2 API | • AWS Transfer for SFTP |
| • Amazon EC2 Auto Scaling | • Amazon WorkSpaces |
| • Amazon Elastic File System | • Endpoint services hosted by other AWS accounts |
| • Elastic Load Balancing | • Supported AWS Marketplace partner services |
| • AWS CloudHSM |  |

- You can create a **VPC peering connection** between your VPCs, or with a VPC in another AWS account, and enable routing of traffic between the VPCs using private IP addresses. You cannot create a VPC peering connection between VPCs that have overlapping CIDR blocks.
- Applications in an Amazon VPC can securely access AWS PrivateLink endpoints across VPC peering connections. The support of VPC peering by AWS PrivateLink makes it possible for customers to privately connect to a service even if that service’s endpoint resides in a different Amazon VPC that is connected using VPC peering.
- AWS PrivateLink endpoints can now be accessed across both intra- and inter-region VPC peering connections.

# **VPC Use Case Scenarios**

- VPC with a Single Public Subnet
- VPC with Public and Private Subnets (NAT)
- VPC with Public and Private Subnets and AWS Managed VPN Access
- VPC with a Private Subnet Only and AWS Managed VPN Access

# **Subnets**

- When you create a VPC, you must specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block (example: 10.0.0.0/16). This is the **primary CIDR block** for your VPC.
- You can add one or more subnets in each Availability Zone of your VPC’s region.
- You specify the CIDR block for a subnet, which is a subset of the VPC CIDR block.
- A CIDR block must not overlap with any existing CIDR block that’s associated with the VPC.
- Types of Subnets
    - Public Subnet – has an internet gateway
    - Private Subnet – doesn’t have an internet gateway
    - VPN-only Subnet – has a virtual private gateway instead
- IPv4 CIDR block size should be between a /16 netmask (65,536 IP addresses) and /28 netmask (16 IP addresses).
- The **first four IP addresses and the last IP address in each subnet CIDR block** are **NOT available** for you to use, and cannot be assigned to an instance.
- You cannot increase or decrease the size of an existing CIDR block.
- When you associate a CIDR block with your VPC, a route is automatically added to your VPC route tables to enable routing within the VPC (the destination is the CIDR block and the target is *local*).
- You have a limit on the number of CIDR blocks you can associate with a VPC and the number of routes you can add to a route table.
- The following rules apply when you add IPv4 CIDR blocks to a VPC that’s part of a **VPC peering connection**:
    - If the VPC peering connection is active, you can add CIDR blocks to a VPC provided they do not overlap with a CIDR block of the peer VPC.
    - If the VPC peering connection is pending-acceptance, the owner of the requester VPC cannot add any CIDR block to the VPC. Either the owner of the accepter VPC must accept the peering connection, or the owner of the requester VPC must delete the VPC peering connection request, add the CIDR block, and then request a new VPC peering connection.
    - If the VPC peering connection is pending-acceptance, the owner of the accepter VPC can add CIDR blocks to the VPC. If a secondary CIDR block overlaps with a CIDR block of the requester VPC, the VPC peering connection request fails and cannot be accepted.
- If you’re using AWS Direct Connect to connect to multiple VPCs through a direct connect gateway, the VPCs that are associated with the direct connect gateway must not have overlapping CIDR blocks.
- The CIDR block is ready for you to use when it’s in the *associated* state.
- You can disassociate a CIDR block that you’ve associated with your VPC; however, you cannot disassociate the primary CIDR block.

# **Subnet Routing**

- Each subnet must be associated with a **route table**, which specifies the allowed routes for **outbound** **traffic** leaving the subnet.
- Every subnet that you create is automatically associated with the main route table for the VPC.
- You can change the association, and you can change the contents of the main route table.
- You can allow an instance in your VPC to initiate outbound connections to the internet over IPv4 but prevent unsolicited inbound connections from the internet using a **NAT gateway or NAT instance**.
- To initiate outbound-only communication to the internet over IPv6, you can use an egress-only internet gateway.

# **Subnet Security**

- Security Groups — control inbound and outbound traffic for your instances
    - You can associate one or more (up to five) security groups to an instance in your VPC.
    - If you don’t specify a security group, the instance automatically belongs to the default security group.
    - When you create a security group, it has no inbound rules. By default, it includes an outbound rule that allows all outbound traffic.
    - Security groups are associated with network interfaces.
- Network Access Control Lists — control inbound and outbound traffic for your subnets
    - Each subnet in your VPC must be associated with a network ACL. If none is associated, automatically associated with the default network ACL.
    - You can associate a network ACL with multiple subnets; however, a subnet can be associated with only one network ACL at a time.
    - A network ACL contains a numbered list of rules that is evaluated in order, starting with the lowest numbered rule, to determine whether traffic is allowed in or out of any subnet associated with the network ACL.
    - The default network ACL is configured to **allow all traffic to flow in and out** of the subnets to which it is associated.
    - For custom ACLs, you need to add a rule for ephemeral ports, usually with the range of 32768-65535. If you have a NAT Gateway, ELB or a Lambda function in a VPC, you need to enable 1024-65535 port range.
- Flow logs — capture information about the IP traffic going to and from network interfaces in your VPC that is published to CloudWatch Logs.
- Flow logs can help you with a number of tasks, such as:
    - Diagnosing overly restrictive security group rules
    - Monitoring the traffic that is reaching your instance
    - Determining the direction of the traffic to and from the network interfaces
- Flow log data is collected outside of the path of your network traffic, and therefore does not affect network throughput or latency. You can create or delete flow logs without any risk of impact to network performance.
- After you’ve created a flow log, it can take several minutes to begin collecting and publishing data to the chosen destinations. Flow logs do not capture real-time log streams for your network interfaces.
- VPC Flow Logs can be sent directly to an Amazon S3 bucket which allows you to retrieve and analyze these logs yourself.
- Amazon security groups and network ACLs don’t filter traffic to or from link-local addresses or AWS-reserved IPv4 addresses. Flow logs do not capture IP traffic to or from these addresses.

| **Security Group** | **Network ACL** |
| --- | --- |
| Operates at the **instance level** | Operates at the **subnet level** |
| Supports **ALLOW rules** only | Supports **ALLOW rules and DENY rules** |
| Is **stateful:** Return traffic is automatically allowed, regardless of any rules | Is **stateless**: Return traffic must be explicitly allowed by rules |
| We evaluate **all rules** before deciding whether to allow traffic | We process **rules in number order** when deciding whether to allow traffic |
| Applies only to EC2 instances and similar services that use EC2 as a backend. | Automatically **applies to all** |
| Security group is specified when launching the instances, or is associated with the instance later on | **Instances in the subnets it’s associated with** |
- Diagram of security groups and NACLs in a VPC

![AWS Training Amazon VPC](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWSTrainingAmazonVPC5.jpg)

# **VPC Networking Components**

- **Network Interfaces**
    - a virtual network interface that can include:
        - a primary private IPv4 address
        - one or more secondary private IPv4 addresses
        - one Elastic IP address per private IPv4 address
        - one public IPv4 address, which can be auto-assigned to the network interface for eth0 when you launch an instance
        - one or more IPv6 addresses
        - one or more security groups
        - a MAC address
        - a source/destination check flag
        - a description
    - Network interfaces can be attached and detached from instances, however, you cannot detach a primary network interface.
- **Route Tables**
    - contains a set of rules, called *routes*, that are used to determine where network traffic is directed.
    - A subnet can only be associated with one route table at a time, but you can associate multiple subnets with the same route table.
    - You cannot delete the main route table, but you can replace the main route table with a custom table that you’ve created.
    - You must update the route table for any subnet that uses gateways or connections.
    - Uses the most specific route in your route table that matches the traffic to determine how to route the traffic (longest prefix match).
- **Internet Gateways**
    - Allows communication between instances in your VPC and the internet.
    - Imposes no availability risks or bandwidth constraints on your network traffic.
    - Provides a target in your VPC route tables for internet-routable traffic, and performs network address translation for instances that have been assigned public IPv4 addresses.
    - The following table provides an overview of whether your VPC automatically comes with the components required for internet access over IPv4 or IPv6.
    - To enable access to or from the Internet for instances in a VPC subnet, you must do the following:
        - Attach an Internet Gateway to your VPC
        - Ensure that your subnet’s route table points to the Internet Gateway.
        - Ensure that instances in your subnet have a globally unique IP address (public IPv4 address, Elastic IP address, or IPv6 address).
        - Ensure that your network access control and security group rules allow the relevant traffic to flow to and from your instance

|  | **Default VPC** | **Non-default VPC** |
| --- | --- | --- |
| Internet gateway | Yes | Yes, if you created the VPC using the first or second option in the VPC wizard. Otherwise, you must manually create and attach the internet gateway. |
| Route table with route to internet gateway for IPv4 traffic (0.0.0.0/0) | Yes | Yes, if you created the VPC using the first or second option in the VPC wizard. Otherwise, you must manually create the route table and add the route. |
| Route table with route to internet gateway for IPv6 traffic (::/0) | No | Yes, if you created the VPC using the first or second option in the VPC wizard, and if you specified the option to associate an IPv6 CIDR block with the VPC. Otherwise, you must manually create the route table and add the route. |
| Public IPv4 address automatically assigned to instance launched into subnet | Yes (default subnet) | No (non-default subnet) |
| IPv6 address automatically assigned to instance launched into subnet | No (default subnet) | No (non-default subnet) |
- **Egress-Only Internet Gateways**
    - VPC component that allows outbound communication over IPv6 from instances in your VPC to the Internet, and prevents the Internet from initiating an IPv6 connection with your instances.
    - An egress-only Internet gateway is stateful.
    - You cannot associate a security group with an egress-only Internet gateway.
    - You can use a network ACL to control the traffic to and from the subnet for which the egress-only Internet gateway routes traffic.
- **NAT**
    - Enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating connections with the instances.
    - NAT Gateways
        - You must specify the **public subnet** in which the NAT gateway should reside.
        - You must specify an **Elastic IP address** to associate with the NAT gateway when you create it.
        - Each NAT gateway is created in a specific Availability Zone and implemented with redundancy in that zone.
        - Deleting a NAT gateway disassociates its Elastic IP address, but does not release the address from your account.
        - A NAT gateway supports the following protocols: TCP, UDP, and ICMP.
        - You cannot associate a security group with a NAT gateway.
        - A NAT gateway can support up to 55,000 simultaneous connections to each unique destination.
        - A NAT gateway cannot send traffic over VPC endpoints, VPN connections, AWS Direct Connect, or VPC peering connections.
        - A NAT gateway uses ports 1024-65535. Make sure to enable these in the inbound rules of your network ACL.
    - NAT Instance vs NAT Gateways

![AWS Training Amazon VPC](https://tutorialsdojo.com/wp-content/uploads/2018/12/Natcomparison.jpg)

- **DHCP Options Sets**
    - **Dynamic Host Configuration Protocol (DHCP)** provides a standard for passing configuration information to hosts on a TCP/IP network.
    - You can assign your own domain name to your instances, and use up to four of your own DNS servers by specifying a special set of DHCP options to use with the VPC.
    - Creating a VPC automatically creates a set of DHCP options, which are domain-name-servers=AmazonProvidedDNS, and domain-name=domain-name-for-your-region, and associates them with the VPC.
    - After you create a set of DHCP options, you can’t modify them. Create a new set and associate a different set of DHCP options with your VPC, or use no DHCP options at all.
- **DNS**
    - AWS provides instances launched in a default VPC with public and private DNS hostnames that correspond to the public IPv4 and private IPv4 addresses for the instance.
    - AWS provides instances launched in a non-default VPC with private DNS hostname and possibly a public DNS hostname, depending on the DNS attributes you specify for the VPC and if your instance has a public IPv4 address.
    - Set VPC attributes *enableDnsHostnames* and *enableDnsSupport* to true so that your instances receive a public DNS hostname and Amazon-provided DNS server can resolve Amazon-provided private DNS hostnames.
        - If you use custom DNS domain names defined in a private hosted zone in Route 53, the *enableDnsHostnames* and *enableDnsSupport* attributes must be set to true.
- VPC Peering
    - A networking connection between two VPCs that enables you to route traffic between them privately. Instances in either VPC can communicate with each other as if they are within the same network.
- **Elastic IP Addresses**
    - A **static, public IPv4 address**.
    - You can associate an Elastic IP address with any instance or network interface for any VPC in your account.
    - You can mask the failure of an instance by rapidly remapping the address to another instance in your VPC.
    - Your Elastic IP addresses remain associated with your AWS account until you explicitly release them.
    - AWS imposes a small hourly charge when EIPs aren’t associated with a running instance, or when they are associated with a stopped instance or an unattached network interface.
    - You’re limited to five Elastic IP addresses.
- **VPC Endpoints**
    - Privately connect your VPC to supported AWS services and VPC endpoint services powered by PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
    - Endpoints are virtual devices.
    - Two Types
        - **Interface Endpoints**
            - An elastic network interface with a private IP address that serves as an entry point for traffic destined to a supported service.
            - Can be accessed through AWS VPN connections or AWS Direct Connect connections, through intra-region VPC peering connections from Nitro instances, and through inter-region VPC peering connections from any type of instance.
            - For each interface endpoint, you can choose only one subnet per Availability Zone. Endpoints are supported within the same region only.
            - You can add endpoint policies to interface endpoints. The Amazon VPC endpoint policy defines which principal can perform which actions on which resources. An endpoint policy does not override or replace IAM user policies or service-specific policies. It is a separate policy for controlling access from the endpoint to the specified service.
            - An interface endpoint supports IPv4 TCP traffic only.
- **Gateway Endpoints**
    - A gateway that is a target for a specified route in your route table, used for traffic destined to a supported AWS service.
    - You can create multiple endpoints in a single VPC, for example, to multiple services. You can also create multiple endpoints for a single service, and use different route tables to enforce different access policies from different subnets to the same service.
    - You can modify the endpoint policy that’s attached to your endpoint, and add or remove the route tables that are used by the endpoint.
    - Endpoints are supported within the same region only. You cannot create an endpoint between a VPC and a service in a different region.
    - Endpoints support IPv4 traffic only.
    - You must enable DNS resolution in your VPC, or if you’re using your own DNS server, ensure that DNS requests to the required service (such as S3) are resolved correctly to the IP addresses maintained by AWS.
- You can create your own application in your VPC and configure it as an AWS PrivateLink-powered service (referred to as an *endpoint service*). You are the *service provider*, and the AWS principals that create connections to your service are *service consumers*.

# **VPN Connections**

| **VPN connectivity option** | **Description** |
| --- | --- |
| AWS managed VPN | You can create an IPsec VPN connection between your VPC and your remote network. On the AWS side of the VPN connection, a *virtual private gateway* provides two VPN endpoints (tunnels) for automatic failover. You configure your *customer gateway* on the remote side of the VPN connection. |
| AWS VPN CloudHub | If you have more than one remote network, you can create multiple AWS-managed VPN connections via your virtual private gateway to enable communication between these networks. |
| Third-party software VPN appliance | You can create a VPN connection to your remote network by using an Amazon EC2 instance in your VPC that’s running a third-party software VPN appliance. AWS does not provide or maintain third-party software VPN appliances; however, you can choose from a range of products provided by partners and open source communities. |
| AWS Direct Connect | You can also use AWS Direct Connect to create a dedicated private connection from a remote network to your VPC. You can combine this connection with an AWS-managed VPN connection to create an IPsec-encrypted connection. |
- Specify a private Autonomous System Number (ASN) for the virtual private gateway. If you don’t specify an ASN, the virtual private gateway is created with the default ASN (64512). You cannot change the ASN after you’ve created the virtual private gateway.
- When you create a VPN connection, you must:
    - Specify the type of routing that you plan to use (static or dynamic)
    - Update the route table for your subnet
- If your VPN device supports Border Gateway Protocol (BGP), specify **dynamic routing** when you configure your VPN connection. If your device does not support BGP, specify **static routing**.
- VPG uses path selection to determine how to route traffic to your remote network. Longest prefix match applies.
- Each VPN connection has two tunnels, with each tunnel using a unique virtual private gateway public IP address. It is important to configure both tunnels for redundancy.

# **VPC Traffic Mirroring**

- Allows you to replicate the network traffic from EC2 instances within your VPC to security and monitoring appliances for content inspection, threat monitoring, troubleshooting, and more.
- Both Nitro and non-Nitro instances are supported.

# **Advanced VPC Management & Networking**

- **Amazon VPC Lattice**Definition: A fully managed application networking service that simplifies connecting, securing, and monitoring services across multiple accounts and VPCs.Why use it: It handles complexity like network address translation (NAT) and overlapping IP addresses automatically, removing the need for sidecar proxies or manual route table management.Traffic Management: Supports granular traffic controls (request-level routing, weighted targets) useful for blue/green and canary deployments.
- **IP Address Manager (IPAM)**Definition: A centralized resource to plan, track, and monitor IP addresses across your entire AWS Organization.Capabilities: Automates IP assignment to VPCs and subnets, tracks IP history (who used what IP and when), and helps identify IP overlaps.Public IP Insights: A free feature within IPAM that provides a unified view of all public IPv4 addresses in use across your organization to help optimize costs.
- **Network Access & Reachability Analyzers**Reachability Analyzer: A static configuration analysis tool that enables you to perform connectivity testing between resources without sending actual packets.Network Access Analyzer: Helps you identify unintended network access to your resources to help you meet security and compliance requirements.

# **Amazon VPC Pricing**

- NAT Gateway
    - Charged per NAT Gateway-hour.
    - Data processing charge per GB processed.
    - Standard AWS data transfer charges still apply.
- VPN Connection
    - Charged per VPN Connection-hour.
- Elastic IP (EIP) hourly charge for all public IPv4 addresses, whether attached to a running instance or not. Additional fees apply for remapping more than 100 times per month.
- VPC Lattice charged per service-hour plus data processing (GB) and request volume.
- IP Address Manager (IPAM)
    - Advanced Tier billed hourly per active IP address managed.
    - Traffic MirroringHourly charge per ENI with mirroring enabled.
- Reachability Analyzer
    - Pay-per-use fee for each connectivity analysis run.

# **Amazon Redshift Cheat Sheet**

- A fully managed, **petabyte-scale data warehouse** service.
- Redshift extends data warehouse queries to your data lake. You can run analytic queries against petabytes of data stored locally in Redshift, and directly against exabytes of data stored in S3.

![Tutorials dojo strip](https://tutorialsdojo.com/wp-content/uploads/2021/02/passyourawsazuregcpbanner.jpg)

- RedShift is an OLAP type of DB.
- Currently, Redshift only supports Single-AZ deployments.
- Features
    - Redshift uses **columnar storage**, data compression, and zone maps to reduce the amount of I/O needed to perform queries.
    - It uses a **massively parallel processing** data warehouse architecture to parallelize and distribute SQL operations.
    - Redshift uses machine learning to deliver high throughput based on your workloads.
    - Redshift uses **result caching** to deliver sub-second response times for repeat queries.
    - Redshift automatically and continuously backs up your data to [S3](https://tutorialsdojo.com/amazon-s3/). It can asynchronously replicate your snapshots to S3 in another region for disaster recovery.

# **Components**

- **Cluster** – a set of **nodes**, which consists of a leader node and one or more compute nodes.
    - Redshift creates one database when you provision a cluster. This is the database you use to load data and run queries on your data.
    - You can scale the cluster in or out by adding or removing nodes. Additionally, you can scale the cluster up or down by specifying a different node type.
    - Redshift assigns a 30-minute maintenance window at random from an 8-hour block of time per region, occurring on a random day of the week. During these maintenance windows, your cluster is not available for normal operations.
    - Redshift supports both the [EC2](https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/)–[VPC](https://tutorialsdojo.com/amazon-vpc/) and EC2-Classic platforms to launch a cluster. You create a **cluster subnet group** if you are provisioning your cluster in your VPC, which allows you to specify a set of subnets in your VPC.

- **Redshift Nodes**
    - The *leader node* receives queries from client applications, parses the queries, and develops query execution plans. It then coordinates the parallel execution of these plans with the compute nodes and aggregates the intermediate results from these nodes. Finally, it returns the results back to the client applications.
    - *Compute nodes* execute the query execution plans and transmit data among themselves to serve these queries. The intermediate results are sent to the leader node for aggregation before being sent back to the client applications.
    - Node Type
        - **Dense storage (DS)** node type – for large data workloads and use hard disk drive (HDD) storage.
        - **Dense compute (DC)** node types – optimized for performance-intensive workloads. Uses SSD storage.
- **Parameter Groups – a group of parameters that apply to all of the databases that you create in the cluster. The default parameter group has preset values for each of its parameters, and it cannot be modified.**
- **Database Querying Options**
    - Connect to your cluster and run queries on the AWS Management Console with the Query Editor.
    - You can use the Query editor with Redshift clusters enabled and with enhanced VPC routing. Leverage [AWS Secrets Manager](https://tutorialsdojo.com/aws-secrets-manager/) to store your cluster credentials and use that with the Query Editor.
    - Connect to your cluster through a SQL client tool using standard ODBC and JDBC connections.
- **Enhanced VPC Routing**
    - By using Enhanced VPC Routing, you can use VPC features to manage the flow of data between your cluster and other resources.
    - You can also use VPC flow logs to monitor *COPY* and *UNLOAD* traffic.
- **RedShift Spectrum**
    - Enables you to run queries against exabytes of data in S3 without having to load or transform any data.
    - Redshift Spectrum supports Enhanced VPC Routing.
    - If you store data in a columnar format, Redshift Spectrum scans only the columns needed by your query, rather than processing entire rows.
    - If you compress your data using one of Redshift Spectrum’s supported compression algorithms, less data is scanned.
- **RedShift Streaming Ingestion**
    - Allows you to consume and process data directly from a streaming source to a Redshift cluster using SQL.
    - Streaming ingestion eliminates the need for staging data in Amazon S3, which gives you a low-latency, high-speed ingestion.
    - Valid data source:
- [Amazon Kinesis](https://tutorialsdojo.com/amazon-kinesis/) Data Streams
- [Amazon Managed Streaming for Apache Kafka (MSK)](https://tutorialsdojo.com/amazon-managed-streaming-for-apache-kafka-amazon-msk/)
- **Redshift ML**
    - Allows you to train and deploy machine learning models using the data stored in your Amazon Redshift cluster through a simple **CREATE MODEL** SQL statement.
    - You can make in-database local inferences using SQL, eliminating the need to move data between Redshift and other storage services like Amazon S3.
    - Redshift ML uses [Amazon SageMaker](https://tutorialsdojo.com/amazon-sagemaker/) Autopilot behind the scenes to find the best model based on your input data.
- **Redshift Data Sharing**
    - Redshift Data Sharing is a secure way to share live data across Redshift clusters within an AWS account, without the need to copy or move data.
    - Data Sharing provides live access to the data so that your users always see the most up-to-date and consistent information as it is updated in the data warehouse.
    - Can be used on Redshift RA3 clusters at no additional cost.
- **Redshift Cross-Database Query**
    - Redshift Cross-database queries provide the ability to query across databases in a Redshift cluster, regardless of which database you are connected to.
    - Available on Redshift RA3 node types at no additional cost.
- **Cluster Snapshots**
    - Point-in-time backups of a cluster. There are two types of snapshots: automated and manual. Snapshots are stored in S3 using SSL.
    - Redshift periodically takes incremental snapshots of your data every 8 hours or 5 GB per node of data change.
    - Redshift provides free storage for snapshots that is equal to the storage capacity of your cluster until you delete the cluster. After you reach the free snapshot storage limit, you are charged for any additional storage at the normal rate.
    - Automated snapshots are enabled by default when you create a cluster. These snapshots are deleted at the end of a retention period, which is one day, but you can modify it. You cannot delete an automated snapshot manually.
    - By default, manual snapshots are retained indefinitely, even after you delete your cluster.
    - You can share an existing manual snapshot with other AWS accounts by authorizing access to the snapshot.
    - You can configure Amazon Redshift to automatically copy snapshots (automated or manual) for a cluster to another AWS Region. For automated snapshots, you can also specify the retention period to keep them in the destination AWS Region. The default retention period for copied snapshots is seven days.
    - If you store a copy of your snapshots in another AWS Region, you can restore your cluster from recent data if anything affects the primary AWS Region. You can configure your cluster to copy snapshots to only one destination AWS Region at a time.

# **Amazon Redshift Monitoring**

- Use the *database audit logging* feature to track information about authentication attempts, connections, disconnections, changes to database user definitions, and queries run in the database. The logs are stored in S3 buckets.
- Redshift tracks events and retains information about them for a period of several weeks in your AWS account.
- Redshift provides performance metrics and data so that you can track the health and performance of your clusters and databases. It uses [CloudWatch](https://tutorialsdojo.com/amazon-cloudwatch/) metrics to monitor the physical aspects of the cluster, such as CPU utilization, latency, and throughput.
- *Query/Load performance data* helps you monitor database activity and performance.
- When you create a cluster, you can optionally configure a CloudWatch alarm to monitor the average percentage of disk space that is used across all of the nodes in your cluster, referred to as the *default disk space* alarm.

# **Amazon Redshift Security**

- By default, an Amazon Redshift cluster is only accessible to the AWS account that creates the cluster.
- Use [IAM](https://tutorialsdojo.com/aws-identity-and-access-management-iam/) to create user accounts and manage permissions for those accounts to control cluster operations.
- If you are using the EC2-Classic platform for your Redshift cluster, you must use Redshift security groups.
- If you are using the EC2-VPC platform for your Redshift cluster, you must use VPC security groups.
- When you provision the cluster, you can optionally choose to encrypt the cluster for additional security. Encryption is an immutable property of the cluster.
- Snapshots created from the encrypted cluster are also encrypted.

# **Amazon Redshift Pricing**

- You pay a per-second billing rate based on the type and number of nodes in your cluster.
- You pay for the number of bytes scanned by RedShift Spectrum
- You can reserve instances by committing to using Redshift for a 1 or 3-year term and save costs.

### **Deep Dive and Best Practices for Amazon Redshift:**

### **Validate Your Knowledge**

### **Question 1**

A financial services company based in Australia uses Amazon Redshift for its data-warehousing solutions. They have expanded recently in Singapore and is designing a solution that would integrate queries between data from an Amazon RDS for PostgreSQL database in Singapore with data from the Redshift cluster in Sydney.

Which solution will best simplify the integration between these data sources?

1. Configure cross-regional snapshots with Redshift cluster and restore a new cluster with the latest snapshot in Singapore. Export the PostgreSQL tables to an S3 bucket and load it to the new Amazon Redshift cluster.
2. Configure cross-regional snapshots with Redshift cluster and restore a new cluster with the latest snapshot in Singapore. Export the PostgreSQL tables to an S3 bucket. Create an external schema and external tables from the S3 files and use Redshift Spectrum to query from S3 and the new Redshift cluster.
3. Set up connectivity from your Amazon Redshift cluster to your Amazon RDS PostgreSQL cluster. Create an external schema from the PostgreSQL database and use federated queries to access both sources.
4. Export the RDS PostgreSQL tables to an S3 bucket. Create an external schema and external tables from the S3 files and use Redshift Spectrum to query from S3 and the new Redshift cluster.

[**Show me the answer!**](https://tutorialsdojo.com/amazon-redshift/?src=udemy#e4f1673b291f92237)

### **Question 2**

A Database Specialist manages an Amazon Redshift cluster for the company’s data warehousing solution. Keeping track of the maintenance tasks that run on the cluster, the Database Manager wants to receive e-mail notifications as soon as the cluster goes into and outside of maintenance mode and is advised if the maintenance was customer-initiated.

How should the Database Specialist meet this requirement with the least operational effort?

1. Using the Redshift console, create an event subscription that sends a notification for `Management` events.
2. Work with Amazon Redshift’s performance data metrics and create an alarm whenever the `Maintenance Mode` unit value is `1`. Use Amazon SNS to send an e-mail.
3. Write an AWS Lambda function to trigger on AWS CloudTrail API calls. Filter on specific Redshift API calls and create an Amazon SNS topic to send the notifications.
4. Create an Amazon EventBridge rule with the operations that need to be tracked on the Redshift Cluster. Create an AWS Lambda function to act on these rules and use Amazon SNS to send an e-mail.

[**Show me the answer!**](https://tutorialsdojo.com/amazon-redshift/?src=udemy#39f209f6c5dd8e52f)

# **AWS Global Infrastructure Cheat Sheet**

**Amazon Web Services** offers the **most extensive global footprint** among cloud providers and expands into new regions more quickly than its competitors.

# **AWS Global Cloud Infrastructure**

- AWS provides the most extensive global footprint compared to any other cloud provider in the market, and it opens up new regions faster than others.
- AWS maintains numerous geographic regions around the globe, from North America, South America, Europe, Asia Pacific, and the Middle East.
- AWS serves over a million active customers in more than 190 countries.
- AWS is able to support this massive workload thanks to its Global Cloud Infrastructure, which consists of the following:
    - Availability Zones
    - Regions
    - Edge Networks
    - Local Zones and Wavelength Zones
- The AWS Global Cloud Infrastructure is the most secure, extensive, and reliable cloud platform in the industry today, offering a wide range of cloud services.
- It is the top choice for small and medium enterprises to deploy their application workloads globally and distribute content closer to their end-users with low latency. It provides you with a **highly available and fault-tolerant** cloud infrastructure where and when you need it.

### **Data Centers**

![Tutorials dojo strip](https://tutorialsdojo.com/wp-content/uploads/2021/02/passyourawsazuregcpbanner.jpg)

- AWS owns and operates thousands of servers and networking devices that are running and located in various data centers worldwide.
- A data center is a physical facility that houses hundreds of computer systems, network devices, and storage appliances.
- You can run your applications in two or more data centers to achieve high availability, so if there is an outage in one of the data centers, you still have other servers running in another data center.
- A data center can also deliver cached content to your global end-users, improving response times.

At its core, the AWS Global Infrastructure utilizes multiple data centers, which are grouped into Availability Zones, Regions, and Edge Locations. Let’s discuss these components one by one:

# **AWS Region**

- An AWS Region comprises **multiple Availability Zones** and currently has **120 Availability Zones across 38 geographic Regions** globally. AWS has various regions available in North America, South America, Europe, Asia, and other parts of the globe. Since a single AZ consists of multiple data centers, your system can achieve a higher level of fault-tolerance by running it in two or more AZs. This enables companies to build highly available, fault-tolerant, and scalable cloud architectures, rather than running their applications on a single data center.
- The Availability Zones of a single AWS Region are typically within hundreds of kilometers or miles of each other.
- These AZs (Availability Zones) are still within a specific country to comply with **data sovereignty** requirements, ensuring that sensitive data is stored only in a designated location.
- To improve the **durability** of your data, you can also replicate it in two or more regions. This is helpful for **disaster recovery** and backups.

# **AWS Availability Zones**

- An Availability Zone, or “**AZ**” for short, consists of one or more data centers, each with redundant power, networking, and connectivity.
- The data centers of a single AZ are typically within 100 kilometers or 60 miles of each other. Think of it as a cluster of interconnected data centers in a specific geographic zone that can help your applications become highly available – hence the name, Availability Zone.
- AZs are physically separated by a meaningful distance to prevent a single event (like a fire or flood) from impacting all of them.
- Since a single AZ consists of one or more data centers, deploying your application to **multiple AZs** in a single Region enables companies to build a highly available, fault-tolerant, and scalable cloud architecture.

# **AWS Edge Networks**

The other component of the AWS Global Cloud Infrastructure is the edge networks of **Point-of-Presence** or **PoP**.

- It consists of Edge Locations and Regional Edge Caches, which enable you to distribute your content with low-latency (pronounced: *Laaay-tancy*) to your global users. Basically, a PoP functions as an access point that allows two distinct networks to communicate with each other.
- By using these global edge networks (over **700+ Points of Presence**), a user request doesn’t need to travel far back to your origin to fetch data. The cached contents can quickly be retrieved from regional edge caches that are closer to your end-users. This is also referred to as a Content Delivery Network (CDN).
    - For example, you have high-resolution images stored on a server in California. You can cache these media files at an edge location in the Philippines, India, or Singapore to enable your customers in Asia to retrieve these photos more quickly. The images will be loaded promptly because they are fetched from an edge server near your users, rather than being retrieved from their origin server in California.

As mentioned above, the AWS Global infrastructure is built around **Regions** and **Availability Zones** (AZs):

![](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWS-Overview-1024x584.png)

**Regions** provide multiple, physically separated, and isolated **Availability Zones**, which are connected via low-latency, high-throughput, and highly redundant networking. **Availability Zones** offer high availability, fault tolerance, and scalability. It consists of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities. An Availability Zone is represented by a **region code** followed by a **letter identifier**, such as `us-east-1a`.

You can visualize the hierarchy of the Availability Zone and AWS Region in this diagram:

![AWS Regions and Availability Zones](https://tutorialsdojo.com/wp-content/uploads/2018/11/AWS-Regions-and-Availability-Zones.jpg)

- An **AWS Local Region** is a single data center designed to complement an existing AWS Region.
- An **AWS Local Zone** places AWS compute, storage, database, and other select services closer to large populations, industries, and IT centers where no AWS Region currently exists. To deliver low-latency content to users worldwide, AWS has established **Points of Presence**, which are either edge locations or edge caches. These points are used by [CloudFront](https://tutorialsdojo.com/amazon-cloudfront/) and [Lambda](https://tutorialsdojo.com/aws-lambda/)@Edge services.
- **Edge locations** are locations that CloudFront uses to cache copies of your content for faster delivery to users at any location.

# **Specialized Infrastructure Offerings**

- **AWS Local Zone:** A specialized infrastructure that places AWS compute, storage, database, and other select services **closer to large populations, industry, and IT centers** to provide ultra-low latency.
- **AWS Wavelength Zones:** Embed AWS compute and storage services within the **5G networks** of telecom carriers to deliver ultra-low latency applications to mobile end-users.
- **AWS Outposts:** Enables customers to run **AWS infrastructure and services on-premises**, providing a truly consistent hybrid cloud experience.

View the Interactive AWS Global Infrastructure Map [here](https://www.infrastructure.aws/).

![](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWS-Overview-3-1024x497.png)

# **What is the AWS Cloud Adoption Framework?**

The AWS Cloud Adoption Framework, or AWS CAF for short, is simply a framework provided by AWS to assist you in adopting cloud computing for your enterprise infrastructure. It is a framework that contains various perspectives that are based on years of extensive experience and best practices in AWS. This can help you digitally transform and accelerate your digital transformation as well as business outcomes through the innovative use of the AWS Cloud.

AWS CAF zeroes in on specific organizational capabilities that are vital in successful cloud transformations. The capabilities and perspectives of this framework provide best-practice guidance that assists companies in improving their total cloud readiness.

# **What are the different Perspectives of the AWS Cloud Adoption Framework?**

The AWS Cloud Adoption Framework groups its many capabilities in 6 different perspectives namely:

- Business

![Tutorials dojo strip](https://tutorialsdojo.com/wp-content/uploads/2021/02/passyourawsazuregcpbanner.jpg)

- People
- Governance
- Platform
- Security
- Operations

Each of these perspectives consists of a set of capabilities that particular stakeholders own or manage in the company’s cloud transformation journey.  These perspectives can identify and prioritize transformation opportunities, evaluate and improve your company’s cloud readiness as well and evolve your transformation roadmap iteratively.

# **Capabilities of AWS CAF**

- **Business**: This perspective ensures that your investments in the cloud propel your digital transformation goals and business results.
- **People**: This perspective acts as a link between technology and business, speeding up the cloud journey to help organizations quickly evolve into a culture of continuous growth and learning, where change is the norm. It focuses on culture, organizational structure, leadership, and workforce.
- **Governance**: This perspective helps coordinate cloud initiatives while maximizing organizational benefits and minimizing risks associated with transformation.
- **Platform**: This perspective helps construct an enterprise-grade, scalable, hybrid cloud platform, modernize existing workloads, and implement new cloud-native solutions.
- **Security**: This perspective helps achieve the confidentiality, integrity, and availability of data and cloud workloads.
- **Operations**: This perspective helps ensure that cloud services are delivered at a level that meets the business needs.

Using AWS CAF, businesses can identify and prioritize transformation opportunities, evaluate and improve cloud readiness, and iteratively evolve their transformation roadmap.

# **Benefits of Using AWS CAF**

- **Risk Reduction**: It reduces the risk profile through improved reliability, increased performance, and enhanced security.
- **Improve environmental, social, and governance performance**: It uses insights to improve sustainability and corporate transparency.
- **Revenue Growth**: Businesses can create new products and services, reach new customers, and enter new market segments.
- **Increased Operational Efficiency**: It reduces operating costs, increases productivity, and improves the employee and customer experience.

These benefits make AWS CAF a valuable tool for organizations looking to adopt cloud practices.

# **Cloud Transformation Phases in AWS CAF**

1. **Envision**: This phase involves identifying and prioritizing transformation opportunities that align with strategic objectives. Transformation initiatives are associated with key stakeholders and measurable business outcomes to demonstrate value as the business progresses through the transformation journey.
2. **Align**: In this phase, capability gaps and cross-organizational dependencies are identified. This helps in creating strategies for improving cloud readiness, ensuring stakeholder alignment, and facilitating relevant organizational change management activities.
3. **Launch**: This phase involves delivering pilots in production and demonstrating incremental business value. Pilots should be highly impactful, and when successful, they influence future direction. Learning from pilots helps businesses adjust their approach before scaling to full production.
4. **Scale**: In this phase, pilots and business value are expanded to the desired scale. This ensures that the business benefits associated with cloud investments are realized and sustained.

# **AWS CAF Use Cases**

- **Technology**: This involves migrating and modernizing legacy infrastructure, applications, and data and analytics platforms.
- **Process**: This involves digitizing, automating, and optimizing business operations. This may include leveraging new data and analytics platforms to create actionable insights or using machine learning (ML) to improve your customer service experience, employee productivity and decision-making, business forecasting, fraud detection and prevention, and industrial operations.
- **Organization**: This involves reimagining how business and technology teams create customer value and meet strategic intent. Organizing teams around products and value streams while leveraging agile methods to rapidly iterate and evolve will help businesses become more responsive and customer-centric.
- **Product**: This involves reimagining the business model by creating new value propositions and revenue models.

# **Related AWS Certified Cloud Practitioner CLF-C02 Resources:**

Are you preparing for your AWS Certified Cloud Practitioner CLF-C02 Exam?

Get Actual AWS Hands-On Labs, Full 65-Question Timed Practice Test, Flashcards plus many more with our highly-visual [AWS Certified Cloud Practitioner CLF-C02 Video course](https://portal.tutorialsdojo.com/courses/aws-certified-cloud-practitioner-clf-c01-video-course/) — all for a price of lunch!

# **AWS Billing and Cost Management Cheat Sheet**

- **Cost Explorer** tracks and analyzes your AWS usage. It is free for all accounts.
- Use **Budgets** to manage budgets for your account.
- Use **Bills** to see details about your current charges.
- Use **Payment History** to see your past payment transactions.
- AWS Billing and Cost Management closes the billing period at midnight on the last day of each month and then calculates your bill.
- At the end of a billing cycle or at the time you choose to incur a one-time fee, AWS charges the credit card you have on file and issues your invoice as a downloadable PDF file.

![Tutorials dojo strip](https://td-mainsite-cdn.tutorialsdojo.com/wp-content/uploads/2021/02/passyourawsazuregcpbanner.jpg)

- With [CloudWatch](https://tutorialsdojo.com/amazon-cloudwatch/), you can create billing alerts that notify you when your usage of your services exceeds the thresholds that you define.
- Use **cost allocation tags** to track your AWS costs on a detailed level. AWS provides two types of cost allocation tags, an *AWS generated tags* and *user-defined tags*.

# **AWS Cost Anomaly Detection**

- This is an AWS Cost Management feature that uses machine learning models to detect and alert on anomalous spend patterns in your AWS workloads.
- With this, you can receive alerts individually in aggregated reports via an email message. Amazon SNS can be configured to send Slack message notifications.
- Your team can evaluate your spending patterns using machine learning methods to reduce the number of false positive alerts. Your cost data can be evaluated on a weekly or monthly basis as well as other custom timeframes.
- Billing group is a set of accounts within your consolidated billing family – in the pro forma billing domain only – that share a common end customer. That end customer maintains the “Primary Account” and can see the cost and usage that accrues across its group.

# **AWS Billing Conductor**

- A feature that simplifies the billing and reporting process of your AWS account with customizable pricing and cost visibility.
- Allows you to assign accounts to a specific billing group to provide both you and your primary accounts an aggregated view of the monthly cost and usage data of your entire AWS workloads across various accounts.
- Uses Billing Groups. A billing group is a set of accounts within your consolidated billing family that share a common end customer.
- You can set up your account where the end customer maintains the “Primary Account” and can view all the costs and usage that accrues across its business group.

# **AWS Free Tier**

- When you create an AWS account, you’re automatically signed up for the free tier for **12 months**.
- You can use a number of AWS services for free, as long as you haven’t surpassed the allocated usage limit.
- To help you stay within the limits, you can track your free tier usage and set a **billing alarm with AWS Budgets** to notify you if you start incurring charges.

# **AWS Cost and Usage Reports**

- The AWS Cost and Usage report provides information about your use of AWS resources and estimated costs for that usage.
- The AWS Cost and Usage report is a .csv file or a collection of .csv files that are stored in an [S3](https://tutorialsdojo.com/amazon-s3/) bucket. Anyone who has permission to access the specified S3 bucket can see your billing report files.
- You can use the Cost and Usage report to track your Reserved Instance Utilization, charges, and allocations.
- For time granularity, you can choose one of the following:
    - **Hourly** if you want your items in the report to be aggregated by the hour.
    - **Daily** if you want your items in the report to be aggregated by the day.
    - **Monthly** if you want your items in the report to be aggregated by month.
- Report can be automatically uploaded into [AWS Redshift](https://tutorialsdojo.com/amazon-redshift/) and/or [AWS QuickSight](https://tutorialsdojo.com/amazon-quicksight/) for analysis.

# **AWS Cost Explorer**

- Cost Explorer includes a default report that helps you visualize the costs and usage associated with your TOP FIVE cost-accruing AWS services, and gives you a detailed breakdown of all services in the table view.
- You can view data for up to the last 12 months, forecast how much you’re likely to spend for the next three months and get recommendations on what Reserved Instances to purchase.
- Cost Explorer must be enabled before it can be used. You can enable it only if you’re the owner of the AWS account and you signed in to the account with your root credentials.

![Cost Explorer](https://td-mainsite-cdn.tutorialsdojo.com/wp-content/uploads/2018/12/Cost-Explorer.png)

- If you’re the owner of a management account in an organization, enabling Cost Explorer enables Cost Explorer for all of the organization accounts. You can’t grant or deny access individually.
- You can create forecasts that predict your AWS usage and define a time range for the forecast.
- Other default reports available are:
    - The **EC2 Monthly Cost and Usage report** lets you view all of your AWS costs over the past two months, as well as your current month-to-date costs.
    - The **Monthly Costs by Linked Account report** lets you view the distribution of costs across your organization.
    - The **Monthly Running Costs report** gives you an overview of all of your running costs over the past three months and provides forecasted numbers for the coming month with a corresponding confidence interval.

# **AWS Budgets**

- Set custom budgets that alert you when your costs or usage exceed or are forecasted to exceed your budgeted amount.
- With Budgets, you can view the following information:
    - How close your plan is to your budgeted amount or to the free tier limits
    - Your usage to date, including how much you have used of your Reserved Instances and purchased Savings Plans.
    - Your current estimated charges from AWS and how much your predicted usage will incur in charges by the end of the month
    - How much of your budget has been used

![](https://td-mainsite-cdn.tutorialsdojo.com/wp-content/uploads/2018/12/AWS-Budgets.png)

- Budget information is updated up to three times a day.
- Types of Budgets:
    - **Cost budgets** – Plan how much you want to spend on a service.
    - **Usage budgets** – Plan how much you want to use one or more services.
    - **RI utilization budgets** – Define a utilization threshold and receive alerts when your RI usage falls below that threshold.
    - **RI coverage budgets** – Define a coverage threshold and receive alerts when the number of your instance hours that are covered by RIs fall below that threshold.
- Budgets can be tracked at the daily, monthly, quarterly, or yearly levels, and you can customize the start and end dates.
- Budget alerts can be sent via email and/or Amazon SNS topic.
- The first two budgets created are free of charge.

# **Amazon EC2 Cheat Sheet**

- A Linux-based/Windows-based/Mac-based virtual server that you can provision.
- You are limited to running On-Demand Instances per your vCPU-based On-Demand Instance limit, purchasing 20 Reserved Instances, and requesting Spot Instances per your dynamic Spot limit per region.
- **Amazon Elastic Compute Cloud (Amazon EC2)** is a web service that provides secure, resizable compute capacity in the cloud.
- It simplifies web-scale cloud computing for developers and offers complete control over your computing resources, allowing you to run on Amazon’s proven computing environment.

### **Key Highlights**

- **Global Reach:** Deploy across 30+ Regions and Local Zones.
- **Secure:** Verified boot with NitroTPM and network isolation via VPC.
- **Flexible:** Choice of processors (Intel, AMD, Graviton) and purchase models (Spot, On-Demand, Savings Plans).

# **Amazon EC2 Features**

- The **AWS Nitro System** is the underlying platform of the next generation of EC2 instances. Traditionally, hypervisors protect the physical hardware and bios, virtualize the CPU, storage, networking, and provide a rich set of management capabilities. With the Nitro System, these functions are offloaded to dedicated hardware and software, thereby reducing the costs of your instances in the process. Hence, the Nitro Hypervisor delivers performance that is indistinguishable from bare metal and performs better than its predecessor: the Xen Hypervisor.
- **Instances:** Server environments.
- **Amazon Machine Images (AMIs): Package OS and additional installations in a reusable template.**
- Various configurations of CPU, memory, storage, and networking capacity for your instances, known as **instance types**
    - `t-type` and `m-type` for general purpose
    - `c-type` for compute optimized
    - `r-type`, `x-type`, and `z-type` for memory-optimized
    - `d-type`, `h-type`, and `i-type` for storage optimized
    - `f-type`, `g-type`, `p-type`, `trn-type` (Trainium), and `inf-type` (Inferentia) for accelerated computing
- **EC2 Instance Attestation:** A security feature that uses **NitroTPM** to cryptographically verify the identity and software integrity of your EC2 instance (Attestable AMIs). It shifts security from a “trust me” to a “verify me” model.
- **EC2 Instance Connect:** Simple and secure way to connect to your instances using SSH (Linux) or RDP (Windows) without managing SSH keys.
- Secure login information for your instances using **key pairs**
- Storage volumes for temporary data that are deleted when you STOP or TERMINATE your instance, known as **instance store volumes.** Take note that you can stop an EBS-backed instance but not an Instance Store-backed instance. You can only either start or terminate an Instance Store-backed instance.
- Persistent storage volumes for your data using **Elastic Block Store volumes** (see AWS storage services).
- Multiple physical locations for deploying your resources, such as instances and [EBS](https://tutorialsdojo.com/amazon-ebs/) volumes, known as **regions** and **Availability Zones** (see AWS overview)**.**
- A firewall that enables you to specify the protocols, ports, and source IP ranges that can reach your instances using **security groups** (see aws networking and content delivery).
- Static IPv4 addresses for dynamic cloud computing, known as **Elastic IP addresses** (see aws networking and content delivery).
- Metadata, known as **tags**, that you can create and assign to your EC2 resources
- Virtual networks you can create that are logically isolated from the rest of the AWS cloud, and that you can optionally connect to your own network, known as [**virtual private clouds**](https://tutorialsdojo.com/amazon-vpc/) or **VPC**s (see aws networking and content delivery).
- Add a script that will be run on instance boot called **user-data**.
- **Host Recovery for Amazon EC2** automatically restarts your instances on a new host in the event of an unexpected hardware failure on a Dedicated Host.
- **EC2 Hibernation** is available for On-Demand and Reserved Instances running on freshly launched M3, M4, M5, C3, C4, C5, R3, R4, and R5 instances running Amazon Linux and Ubuntu 18.04 LTS. You can enable hibernation for your EBS-backed instances at launch. You can then hibernate and resume your instances through the AWS Management Console, or through the AWS SDK and CLI using the existing stop-instances and start-instances commands. Hibernation requires an EC2 instance to be an encrypted EBS-backed instance.
- You can allow automatic connection of one or more EC2 instances to an [RDS](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/) database.

# **Instance states**

- **Start** – run your instance normally. You are continuously billed while your instance is running.
- **Stop** – is just a normal instance shut down. You may restart it again anytime. All EBS volumes remain attached, but data in instance store volumes are deleted. You won’t be charged for usage while instance is stopped. You can attach or detach EBS volumes. You can also create an AMI from the instance, and change the kernel, RAM disk, and instance type while in this state.
- **Hibernate** – When an instance is hibernated, it writes the in-memory state to a file in the root EBS volume and then shuts itself down. The AMI used to launch the instance must be encrypted, and also the root EBS volume of the instance. The encryption ensures proper protection for sensitive data when it is copied from memory to the EBS volume. While the instance is in hibernation, you pay only for the EBS volumes and Elastic IP Addresses attached to it; there are no hourly charges.
- **Terminate** – instance performs a normal shutdown and gets deleted. You won’t be able to restart an instance once you terminate it. The root device volume is deleted by default, but any attached EBS volumes are preserved by default. Data in instance store volumes are deleted.
- To prevent accidental termination, enable termination protection.
- By enabling instance stop protection, you can prevent an instance from being accidentally stopped.

# **Root Device Volumes**

- The root device volume contains the image used to boot the instance.
- You can replace the root volume of a running EC2 instance using the following:
    - Initial launch state
    - Snapshot
    - AMI
- Instance Store-backed Instances
    - Any data on the instance store volumes are deleted when the instance is terminated (instance store-backed instances do not support the Stop action) or if it fails (such as if an underlying drive has issues).
    - You should also back up critical data from your instance store volumes to persistent storage on a regular basis.
- [Amazon EBS](https://tutorialsdojo.com/amazon-ebs/)backed Instances
    - An Amazon EBS-backed instance can be stopped and later restarted without affecting data stored in the attached volumes.
    - When in a stopped state, you can modify the properties of the instance, change its size, or update the kernel it is using, or you can attach your root volume to a different running instance for debugging or any other purpose.
    - By default, the root device volume for an AMI backed by Amazon EBS is deleted when the instance terminates.
    - Previously, to launch an encrypted EBS-backed EC2 instance from an unencrypted AMI, you would first need to create an encrypted copy of the AMI and use that to launch the EC2 instance. Now, you can [**launch encrypted EBS-backed EC2 instances](https://aws.amazon.com/about-aws/whats-new/2019/05/launch-encrypted-ebs-backed-ec2-instances-from-unencrypted-amis-in-a-single-step/)** from unencrypted AMIs directly.

# **Amazon EC2 – AMI**

- Includes the following:
    - A template for the root volume for the instance (OS, application server, and applications)
    - Launch permissions that control which AWS accounts can use the AMI to launch instances
    - A block device mapping that specifies the volumes to attach to the instance when it’s launched

![AWS Training Amazon EC2 2](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWS-Training-Amazon-EC2-2.jpg)

- Backed by Amazon EBS – root device for an instance launched from the AMI is an Amazon EBS volume. AMIs backed by Amazon EBS snapshots can use EBS encryption.
- Backed by Instance Store – root device for an instance launched from the AMI is an instance store volume created from a template stored in [S3](https://tutorialsdojo.com/amazon-s3/).

| **Characteristic** | **Amazon EBS-backed AMI** | **Amazon instance store-backed AMI** |
| --- | --- | --- |
| **Boot time for an instance** | Usually less than 1 minute. | Usually less than 5 minutes. |
| **Size limit for a root device** | 64 TiB** | 10 GiB |
| **Root device volume** | EBS volume | Instance store volume |
| **Data persistence** | By default, the root volume is deleted when the instances terminates.* Data on any other EBS volumes persists after instance termination by default. | Data on any instance store volumes persists only during the life of the instance. |
| **Modifications** | The instance type, kernel, RAM disk and user data can be changed while the instances is stopped. | Instance attributes are fixed for the life of an instance. |
| **Charges** | You’re charged for instance usage, EBS volume usage, and storing your AMI as an EBS snapshot. | You’re charged for instance usage and storing your AMI in Amazon S3. |
| **AMI creation/bundling** | Uses a single command/call. | Requires installation and use of AMI tools. |
| **Stopped state** | Can be in a stopped state. Even when the instance is stopped and not running, the root volumes persisted in Amazon EBS. | Cannot be in stopped state; instances are running or terminated. |
- You can copy AMIs to different regions.
- Recycle Bin
    - You can restore deleted AMIs using recycle bin.
    - You can set lock retention rules to protect against modifications and deletions.
- Check the *LastLaunchedTime* timestamp to see when your AMI was last used to launch an instance.
- By default, a public AMI is deprecated after 2-years from the creation date.
    - In the EC2 console, public AMIs owned by Amazon or a verified Amazon partner is marked as a verified provider.
- When an AMI changes state, an event is automatically generated, and you can use Amazon EventBridge to detect and respond to these events.
- With UEFI Secure Boot, you can ensure that an instance only boots software signed with cryptographic keys.
- You can configure an AMI to use Instance Metadata Service Version 2 (IMDSv2) when requesting instance metadata.
- If an AMI has been shared with your AWS account, you can remove your account from the AMI’s launch permissions.

# **Amazon EC2 Image Builder**

- A fully managed AWS service that automates the creation, management, and deployment of your Amazon Machine Images (AMIs)
- The AWS Management Console, AWS Command Line Interface, or AWS APIs can be used to create custom images in your AWS account.
- The customized images that Image Builder creates in your account are owned by you, and you can configure pipelines to automate updates as well as system patching for the images in your AWS account.
- Amazon EC2 Image Builder also provides a stand-alone command to create an AMI with the configuration resources that you have defined.

# **Amazon EC2 Pricing**

- **Savings Plans:** Flexible pricing (up to 72% off) for committing to a consistent amount of usage (e.g., $10/hour) for 1 or 3 years. Applies to EC2, Fargate, and Lambda.
- **On-Demand:** Pay for the instances that you use by the second, with no long-term commitments or upfront payments.
- **Reserved:** Make a low, one-time, up-front payment for an instance, reserve it for a *one*– or *three*year term, and pay a significantly lower hourly rate for these instances. It has two offering classes: Standard and Convertible.
    - The Standard class provides the most significant discount but you can only modify some of its attributes during the term. It can also be sold in the Reserved Instance Marketplace.
    - The Convertible class provides a lower discount than Standard Reserved Instances, but can be exchanged for another Convertible Reserved Instance with different instance attributes. However, this one cannot be sold in the Reserved Instance Marketplace.

|  | **Standard RI** | **Convertible RI** |
| --- | --- | --- |
| **Terms**
(average discount off On-Demand) | 1 year (40%)
3 years (60%) | 1 year (31%)
3 years (54%) |
| Change Availability Zone, Instance size (for Linux OS), Networking type | Yes | Yes |
| Change instance families, operating system, tenancy, and payment option |  | Yes |
| Benefit from Price Reductions |  | Yes |
- When purchasing a Reserved Instance, you’ll need to determine its scope (regional or zonal).

|  | **Regional RI** | **Zonal RI** |
| --- | --- | --- |
| Ability to Reserve Capacity | No | Yes |
| Availability Zone Flexibility | The discount is valid for instance usage in any Availability Zone within the specified Region. | The discount only applies to instance usage in the specified Availability Zone. |
| Instance Size Flexibility | The discount applies to instance usage within the instance family. | The discount only applies to instance usage for the specified instance type and size. |
| Queuing A Purchase | Yes | No |
- **Spot:** Request unused EC2 instances, which can lower your costs significantly. Spot Instances are available at up to a 90% discount compared to On-Demand prices.
    - Spot Instances with a defined duration (also known as **Spot blocks**) are designed not to be interrupted and will run continuously for the duration you select. This makes them ideal for jobs that take a finite time to complete, such as batch processing, encoding and rendering, modeling and analysis, and continuous integration.
    - A **Spot Fleet** is a collection of Spot Instances and optionally On-Demand Instances. The service attempts to launch the number of Spot Instances and On-Demand Instances to meet your specified target capacity. The request for Spot Instances is fulfilled if there is available capacity and the maximum price you specified in the request exceeds the current Spot price. The Spot Fleet also attempts to maintain its target capacity fleet if your Spot Instances are interrupted.
    - A **Spot Capacity pool** is a set of unused EC2 instances with the same instance type, operating system, Availability Zone, and network platform.
    - You can start and stop your Spot Instances backed by Amazon EBS at will.
    - You can modify instance types and weights for a running EC2 Fleet or Spot Fleet without having to recreate it.
    - Allocation strategy for Spot Instances
        - **LowestPrice** – The Spot Instances come from the pool with the lowest price. This is the default strategy.
        - **Diversified** – The Spot Instances are distributed across all pools.
        - **CapacityOptimized** – The Spot Instances come from the pool with optimal capacity for the number of instances that are launching.
        - **InstancePoolsToUseCount** – The Spot Instances are distributed across the number of Spot pools that you specify. This parameter is valid only when used in combination with the lowest Price.

|  | **Spot Instances** | **On-Demand Instances** |
| --- | --- | --- |
| **Launch time** | Can only be launched immediately if the Spot Request is active and capacity is available. | Can only be launched immediately if you make a manual launch request and capacity is available. |
| **Available capacity** | If capacity is not available, the Spot Request continues to automatically make the launch request until capacity becomes available. | If Capacity is not available when you make a launch request, you get an Insufficient Capacity Error (ICE). |
| **Hourly price** | The hourly price for Spot Instances varies based on demand. | The hourly price for On-Demand instance is static |
| **Rebalance recommendation** | The signal that Amazon EC2 emits for a running Spot Instance when the instance is at an elevated risk of interruption. | You determine when an On-Demand Instance is interrupted (stopped, hibernated, or terminated). |
| **Instance interruption** | You can stop and start an Amazon EBS-backed Spot Instance. In addition, the Amazon EC2 Spot service can interrupt an individual Spot Instance if capacity is no longer available, the spot price exceeds your maximum price, or demand for Spot Instances increases. | You determine when an On-demand Instance is interrupted (stopped, hibernated, or terminated). |
- **Dedicated Hosts:** Pay for a physical host that is fully dedicated to running your instances, and bring your existing per-socket, per-core, or per-VM software licenses to reduce costs.
- **Dedicated Instances:** Pay, by the hour, for instances that run on single-tenant hardware.
- **On-Demand Capacity Reservations:** Reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration.
    - Unlike Reserved instances, you don’t need to have a one-year or three-year term commitment.
    - When you create a Capacity Reservation, you specify:
        - The Availability Zone in which to reserve the capacity
        - The number of instances for which to reserve capacity
        - The instance attributes, including the instance type, tenancy, and platform/OS
    - Your Savings Plans and regional Reserved Instances can be applied with your capacity reservations to receive discounts. Without these, your capacity reservations do not have billing discounts.
    - Capacity Reservations can be created in placement groups
    - Capacity Reservations can’t be used with Dedicated Hosts
    - Your capacity reservation usage metrics can be monitored in Amazon Cloudwatch.
- There is a data transfer charge when copying AMI from one region to another
- EBS pricing is different from instance pricing. (see AWS storage services)
- AWS imposes a small hourly charge if an Elastic IP address is not associated with a running instance, or if it is associated with a stopped instance or an unattached network interface.
- You are charged for any additional Elastic IP addresses associated with an instance.
- If data is transferred between these two instances, it is charged at “Data Transfer Out from EC2 to Another AWS Region” for the first instance and at “Data Transfer In from Another AWS Region” for the second instance.

# **Amazon Elastic Compute Cloud Security**

- Use [IAM](https://tutorialsdojo.com/aws-identity-and-access-management-iam/) to control access to your instances (see AWS Security and Identity Service).
    - IAM policies
    - IAM roles
- Restrict access by only allowing trusted hosts or networks to access ports on your instance.
- A **security group** acts as a virtual firewall that controls the traffic for one or more instances.
    - Create different security groups to deal with instances that have different security requirements.
    - You can add rules to each security group that allows traffic to or from its associated instances.
    - You can modify the rules for a security group at any time.
    - New rules are automatically applied to all instances that are associated with the security group.
    - Evaluates all the rules from all the security groups that are associated with an instance to decide whether to allow traffic or not.
    - By default, security groups allow **all outbound traffic**.
    - Security group rules are **always permissive**; you can’t create rules that deny access.
    - Security groups are **stateful**
- If you don’t specify a security group when you launch an instance, the instance is automatically associated with the **default security group** for the VPC, which has the following rules:
    - Allows all inbound traffic from other instances associated with the default security group
    - Allows all outbound traffic from the instance.
- Disable password-based logins for instances launched from your AMI, since passwords can be cracked or found.
- You can replicate the network traffic from an EC2 instance within your Amazon VPC and forward that traffic to security and monitoring appliances for content inspection, threat monitoring, and troubleshooting.
- When creating a new key pair, you can specify the key format (.pem & .ppk).
- Querying of the public key and creation date of an EC2 key pair is supported.
- For EC2 Instance Connect and EC2 Serial Console, ED25519 keys are now supported.

# **Amazon EC2 Networking**

- An **Elastic IP address** is a static IPv4 address designed for dynamic cloud computing. With it, you can mask the failure of an instance or software by rapidly remapping the address to another instance in your account.
- If you have not enabled auto-assign public IP address for your instance, you need to associate an Elastic IP address with your instance to enable communication with the internet.
- An Elastic IP address is for use in a specific region only.
- By default, all AWS accounts are limited to five (5) Elastic IP addresses per region, because public (IPv4) internet addresses are a scarce public resource.
- You can transfer Elastic IP addresses from one AWS account to another.
- By default EC2 instances come only with a private IP when created in a private subnet, and public and private IP when created in a public subnet.
- An elastic **network interface** is a logical networking component in a VPC that represents a virtual network card, which directs traffic to your instance
- Every instance in a VPC has a default network interface, called the **primary network interface** (eth0). You cannot detach a primary network interface from an instance.
- You can create and attach additional network interfaces. The maximum number of network interfaces that you can use varies by instance type.
- You can attach a network interface to an instance in a different subnet as long as its within the same AZ
- Default interfaces are terminated with instance termination.
- Scale with **EC2 Scaling Groups** and distribute traffic among instances using **Elastic Load Balancer**.
- You can configure EC2 instances as **bastion hosts** (aka jump boxes) in order to access your VPC instances for management, using SSH or RDP protocols
- **Enhanced Networking – It provides higher bandwidth, higher packet per second (PPS) performance, and consistent lower inter-instance latencies, which are being used in Placement Groups. It uses single root I/O virtualization (SR-IOV) to provide high-performance networking capabilities. SR-IOV is a method of device virtualization that provides higher I/O performance and lower CPU utilization when compared to traditional virtualized network interfaces.**
- **Elastic Fabric Adapter (EFA) –** This is a network device that you can attach to your EC2 instance to significantly accelerate machine learning applications and High Performance Computing (HPC). It empowers your computing resources to achieve the application performance of an on-premises HPC cluster, with the elasticity and scalability provided by AWS. Compared with a TCP transport that is traditionally used in cloud-based HPC systems, EFA provides lower and more consistent latency and higher throughput as it enhances the performance of inter-instance communication.

# **Amazon EC2 Monitoring**

- EC2 items to monitor
    - CPU utilization, Network utilization, Disk performance, Disk Reads/Writes using EC2 metrics
    - Memory utilization, disk swap utilization, disk space utilization, page file utilization, log collection using a monitoring agent/CloudWatch Logs
- Automated monitoring tools include:
    - System Status Checks – monitor the AWS systems required to use your instance to ensure they are working properly. These checks detect problems with your instance that require AWS involvement to repair.
    - Instance Status Checks – monitor the software and network configuration of your individual instance. These checks detect problems that require your involvement to repair.
    - [Amazon CloudWatch](https://tutorialsdojo.com/amazon-cloudwatch/) Alarms – watch a single metric over a time period you specify, and perform one or more actions based on the value of the metric relative to a given threshold over a number of time periods.
    - Amazon CloudWatch Events – automate your AWS services and respond automatically to system events.
    - Amazon CloudWatch Logs – monitor, store, and access your log files from Amazon EC2 instances, [AWS CloudTrail](https://tutorialsdojo.com/aws-cloudtrail/), or other sources.
- Monitor your EC2 instances with CloudWatch. By default, EC2 sends metric data to CloudWatch in 5-minute periods.
- You can also enable detailed monitoring to collect data in 1-minute periods.

# **Instance Metadata and User Data**

- **Instance metadata** is data about your instance that you can use to configure or manage the running instance.
- Instance metadata and user data are not protected by cryptographic methods.
- View all categories of instance metadata from within a running instance at [**http://169.254.169.254/latest/meta-data/**](http://169.254.169.254/latest/meta-data/)
- You can pass two types of user data to EC2: shell scripts and cloud-init directives.
- User data is limited to 16 KB.
- If you stop an instance, modify its user data, and start the instance, the updated user data is not executed when you start the instance.
- Retrieve user data from within a running instance at [**http://169.254.169.254/latest/user-data**](http://169.254.169.254/latest/user-data)
- An instance tag can be accessed from the instance metadata.
- When using Auto Scaling groups, the instance metadata contains information about an instance’s target lifecycle state.

# **Placement Groups**

- You can launch or start instances in a **placement group**, which determines how instances are placed on underlying hardware.
    - Cluster – clusters instances into a low-latency group in a single Availability Zone. Recommended for applications that benefit from low network latency, high network throughput, or both, and if the majority of the network traffic is between the instances in the group.
    - Spread – spreads instances across underlying hardware. Recommended for applications that have a small number of critical instances that should be kept separate from each other. Note: A spread placement group can span multiple Availability Zones, and you can have a maximum of seven running instances per Availability Zone per group.
- Partition placement groups is an Amazon EC2 placement strategy that helps reduce the likelihood of correlated failures for large distributed and replicated workloads such as HDFS, HBase, and Cassandra running on EC2.
- Partition placement groups spread EC2 instances across logical partitions and ensure that instances in different partitions do not share the same underlying hardware. In addition, partition placement groups offer visibility into the partitions and allow topology aware applications to use this information to make intelligent data replication decisions, increasing data availability and durability.

# **Amazon EC2 Rules**

- The name you specify for a placement group must be unique within your AWS account for the region.
- You can’t merge placement groups.
- An instance can be launched in one placement group at a time; it cannot span multiple placement groups.
- Instances with a tenancy of host cannot be launched in placement groups.

# **Amazon EC2 Storage**

### 

![AWS Training Amazon EC2 5](https://tutorialsdojo.com/wp-content/uploads/2018/12/AWS-Training-Amazon-EC2-5.jpg)

- **EBS** (see AWS Storage Services)
    - Provides durable, block-level storage volumes that you can attach to a running instance.
    - Use as a primary storage device for data that requires frequent and granular updates.
    - To keep a backup copy of your data, create a snapshot of an EBS volume, which is stored in S3. You can create an EBS volume from a snapshot, and attach it to another instance.
- **Instance Store**
    - Provides temporary block-level storage for instances.
    - The data on an instance store volume persists only during the life of the associated instance; if you stop or terminate an instance, any data on instance store volumes is lost.
- [**Elastic File System](https://tutorialsdojo.com/amazon-efs/) (EFS)** (see AWS Storage Services)
    - Provides scalable file storage for use with Amazon EC2. You can create an EFS file system and configure your instances to mount the file system.
    - You can use an EFS file system as a common data source for workloads and applications running on multiple instances.
- **FSx**
    - [Amazon FSx](https://tutorialsdojo.com/amazon-fsx/) for Windows File Server is a fully-managed file storage built on Windows Server.
    - Amazon FSx for Lustre is a fully-managed file storage built on the world’s most popular high-performance file system, Lustre.
    - Amazon FSx for NetApp ONTAP is a fully managed shared storage solution based on NetApp’s ONTAP file system.
    - Amazon FSx for OpenZFS is a fully managed shared storage solution that is based on the OpenZFS file system.
- **S3** (see AWS Storage Services)
    - Provides access to reliable and inexpensive data storage infrastructure.
    - Storage for EBS snapshots and instance store-backed AMIs.
- With torn write prevention (block storage feature), you can improve the performance of your I/O-intensive relational database workloads and reduce latency without compromising data resiliency.
- **Resources and Tagging**
    - EC2 resources include images, instances, volumes, and snapshots. When you create a resource, AWS assigns the resource a *unique resource ID*.
    - Some resources can be used in all regions (global), and some resources are specific to the region or Availability Zone in which they reside.

| **Resource** | **Type** | **Description** |
| --- | --- | --- |
| AWS account | Global | You can use the same AWS account in all regions. |
| Key pairs | Global or Regional | The key pairs that you create using EC2 are tied to the region where you created them. You can create your own RSA key pair and upload it to the region in which you want to use it; therefore, you can make your key pair globally available by uploading it to each region. |
| Amazon EC2 resource identifiers | Regional | Each resource identifier, such as an AMI ID, instance ID, EBS volume ID, or EBS snapshot ID, is tied to its region and can be used only in the region where you created the resource. |
| User-supplied resource names | Regional | Each resource name, such as a security group name or key pair name, is tied to its region and can be used only in the region where you created the resource. Although you can create resources with the same name in multiple regions, they aren’t related to each other. |
| AMIs | Regional | An AMI is tied to the region where its files are located within S3. You can copy an AMI from one region to another. |
| Elastic IP addresses | Regional | An Elastic IP address is tied to a region and can be associated only with an instance in the same region. |
| Security groups | Regional | A security group is tied to a region and can be assigned only to instances in the same region. You can’t enable an instance to communicate with an instance outside its region using security group rules. |
| EBS snapshots | Regional | An EBS snapshot is tied to its region and can only be used to create volumes in the same region. You can copy a snapshot from one region to another. |
| EBS volumes | Availability Zone | An EBS volume is tied to its Availability Zone and can be attached only to instances in the same Availability Zone. |
| Instances | Availability Zone | An instance is tied to the Availability Zones in which you launched it. However, its instance ID is tied to the region. |
- You can optionally assign your own metadata to each resource with **tags**, which consist of a key and an optional value that you both define.