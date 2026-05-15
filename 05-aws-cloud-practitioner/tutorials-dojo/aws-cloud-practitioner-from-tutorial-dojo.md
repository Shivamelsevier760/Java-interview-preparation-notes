# AWS cloud practitioner from tutorial DoJO

Question 1:

A startup plans to migrate its product's infrastructure from on-premises to AWS. Doing this will turn their fixed infrastructure costs into variable costs. They intend to commit to utilizing AWS services in the long term for 1 or 3 years.

Which AWS pricing model or offering will meet these requirements in the MOST cost-effective way?

**AWS Free Tier**

**Pay-as-you-go pricing**

**Your answer is correct**

**~~Savings Plans~~**

**AWS Billing Conductor**

**Overall explanation**

**Savings Plans** is an offering of AWS that grants a flexible pricing model for those customers who want to significantly reduce their AWS bill in exchange for long-term commitment for one (1) or three (3) years. AWS Savings Plans may reduce costs by up to 76% compared to on-demand prices.

The Savings Plans feature is available in 3 different payment options. The No Upfront option does not require any upfront payment, and your commitment will be charged purely on a monthly basis. The Partial Upfront option offers lower prices on Savings Plans. With this option, you will be charged at least half of your commitment upfront, and the remaining will be charged on a monthly basis. With the All Upfront option, you will receive the lowest prices, and your entire commitment will be charged in one payment.

![](https://media.tutorialsdojo.com/public/EC2_Savings_Plan_03OCT2023.png)

AWS offers three types of Savings Plans:

**Compute Savings Plans** provide the most flexibility and help to reduce your costs by up to 66%. These plans automatically apply to EC2 instance usage regardless of instance family, size, AZ, region, OS or tenancy, and also apply to Fargate and Lambda usage.

**EC2 Instance Savings Plans** provide the lowest prices, offering savings of up to 72% in exchange for a commitment to the usage of individual instance families in a region (e.g., M5 usage in N. Virginia). This automatically reduces your cost on the selected instance family in that region regardless of AZ, size, OS, or tenancy. EC2 Instance Savings Plans give you the flexibility to change your usage between instances within a family in that region.

**Amazon SageMaker Savings Plans** is a flexible pricing model for Amazon SageMaker, in exchange for a commitment to a consistent amount of usage (measured in $/hour) for a one- or three-year term. Amazon SageMaker Savings Plans provide the most flexibility and help to reduce your costs by up to 64%. These plans automatically apply to eligible SageMaker ML instance usages.

Hence, the correct answer is: **Savings Plans**

**Pay-as-you-go pricing** is incorrect because this is just the default pricing model of AWS. Like paying electricity or water bills, AWS's pay-as-you-go pricing model will bill customers on-demand for the individual resources they use.

**AWS Free Tier** is incorrect. Although this is the most cost-effective option as you don't have to pay a single cent, this offering remains inadequate because it expires or limits how much compute capacity or resources a customer can utilize for free. It is an offering suited for customers trying to get started and learn AWS services without incurring costs, which is not fit for this scenario where the services will be used for the long term since the Free Tier has certain time and usage limitations.

**AWS Billing Conductor** is incorrect because this option does not change the way a customer is billed by AWS each month. The AWS Billing Conductor is just a financial management service that enables customers to manage billing separately on different accounts within their organization. This allows the customer to create custom bill versions without separating from the organization's management or payer account but not provide any discounts like the Savings Plans option.

Question 2:

Which of the following are general design principles described in the AWS Well-Architected Framework? (Select TWO.)

**Your selection is correct**

**Drive architectures using data.**

**Correct selection**

**Test systems at production scale.**

**Your selection is incorrect**

**Intelligently guess your capacity needs.**

**Test recovery procedures.**

**Stick to one cloud architecture.**

**Overall explanation**

The AWS Well-Architected Framework serves primarily as a guide to ensure that applications and workloads deployed on AWS are robust, secure, and efficient. By adhering to this framework, organizations can make informed decisions about their infrastructure, optimize costs, enhance performance, and maintain excellent security that meets their needs.

![](https://media.tutorialsdojo.com/public/TD_aws-well-architected-map.png)

The AWS Well-Architected Framework upholds six (6) general design principles. The following are:

- Stop guessing your capacity needs.
- Test systems at production scale.
- Automate to make architectural experimentation easier.
- Allow for evolutionary architectures.
- Drive architectures using data.
- Improve through game days.

The AWS Well-Architected Framework's general design principles guide users in optimizing cloud resources and architectures. By discouraging capacity guessing, it promotes dynamic resource scaling. It emphasizes the importance of real-world testing, advocates for automation to simplify architectural experiments, and supports the continuous evolution of cloud structures. Making data-driven architectural decisions and regularly simulating real-world events (game days) ensures that architectures remain resilient, efficient, and aligned with business needs.

Hence, the correct answers are:

- **Test systems at production scale.**
- **Drive architectures using data.**

The option that says: **Test recovery procedures** is incorrect because it only falls under the **Reliability Pillar**, not a general design principle of the AWS Well-Architected Framework.

The option that says: **Intelligently guess your capacity needs** is incorrect because when working in the AWS Cloud, guessing is no longer needed to compute your existing workloads approximately. There is a design principle called "Stop guessing your capacity needs." in which AWS gives you the power to basically scale up and down with as little capacity as you need on-demand — avoiding any wasted resources and performance issues.

The option that says: **Stick to one cloud architecture** is incorrect because this will be detrimental when your application scales. As business requirements change, sticking to the same architecture will hinder the application's ability to perform and adapt. The "Allow for evolutionary architectures" design principle simply states that you should leverage AWS's capability to automate and test on demand, lowering the risk of impact from design changes. This allows systems to evolve over time so that businesses can take advantage of innovations as a standard practice.

Question 3:

A company recently audited the usage of its Amazon EC2 instances, which are used by its various applications. The company discovered a lot of these instances are under-utilized and over-provisioned. They then decide to rightsize their set of Amazon EC2 instances to optimize the performance of their computing resources.

Which configuration change will meet this requirement with the LEAST operational overhead?

**Your answer is incorrect**

**Deploy an Auto Scaling Group behind an Elastic Load Balancer.**

**Correct answer**

**Utilize the AWS Compute Optimizer and apply the recommended reconfigurations.**

**Reserve compute capacity for Amazon EC2 instances through On-Demand Capacity Reservations.**

**Change the instance purchasing option of the Amazon EC2 Instances from On-Demand to EC2 Instance Savings Plans.**

**Overall explanation**

**AWS Compute Optimizer** allows you to rightsize your AWS resources. In the context of the cloud, rightsizing is the process of reconfiguring compute resources to match workload performance at the lowest possible cost. With AWS Compute Optimizer, rightsizing has been made easier and straightforward.

![](https://media.tutorialsdojo.com/public/AWS_Compute_Optimizer_03OCT2023.png)

This service scans through your current infrastructure configuration and its respective utilization metrics. After this, it gives recommendations on the necessary reconfigurations to optimize your infrastructure in performance and cost.

Hence, the answer is: **Utilize the AWS Compute Optimizer and apply the recommended reconfigurations.**

The option that says: **Deploy an Auto Scaling Group behind an Elastic Load Balancer** is incorrect. Keep in mind that an Autoscaling group does not necessarily rightsize EC2 instances. If the compute capacity of your current launch template for your EC2 instances is too high for the current workload of your infrastructure, then no Auto Scaling action would occur; hence, that sole EC2 instance you have would be over-provisioned. On the other hand, if the compute capacity of the current launch template of your EC2 instances is too low for the current workload, then there's a possibility that the last Auto Scaling action would spin up a new EC2 instance that is under-utilized and over-provisioned. Without AWS Compute Optimizer, finding the suitable configuration and determining the instance type would take a lot of operational overhead.

The option that says: **Change the instance purchasing option of the Amazon EC2 instances from On-Demand to EC2 Instance Savings Plans** is incorrect. Although this option will reduce costs, the performance of the EC2 Instances is not at all optimized. The compute workload will still have a mix of Amazon EC2 instances that are under-utilized and over-provisioned. The only benefit of this option is that you would pay less than the On-Demand price.

The option that says: **Reserve compute capacity for Amazon EC2 instances through On-Demand Capacity Reservations** is incorrect because rightsizing is not at all evident here. This tool allows you to reserve computing capacity based on the number of EC2 instances, instance type, and the Availability Zone in which you want to reserve the capacity. Reserving an instance type without knowledge of the current workload can be prone to an over-provisioned or under-provisioned infrastructure.

Question 4:

Which AWS Well-Architected Framework pillar supports the design principle of performing operations as code?

**Cost Optimization**

**Security**

**Performance Efficiency**

**Your answer is correct**

**Operational Excellence**

**Overall explanation**

The **AWS Well-Architected Framework** helps you understand the pros and cons of the decisions you make while building systems on AWS. Using the Framework enables you to learn architectural best practices for designing and operating secure, reliable, efficient, cost-effective, and sustainable workloads in the AWS Cloud.

The AWS Well-Architected Framework is based on a set of pillars — operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

![](https://media.tutorialsdojo.com/public/AWS_WA_Tool_Operational_Excellence_16AUG2023.png)

The Operational Excellence pillar includes supporting the development and running workloads effectively, gaining insight into their operations, and continuously improving supporting processes and procedures to deliver business value.

There are five design principles for operational excellence in the cloud:

- **Perform operations as code**: In the cloud, you can apply the same engineering discipline that you use for application code to your entire environment. You can define your entire workload (applications, infrastructure) as code and update it with code.
- **Make frequent, small, reversible changes**: Design workloads to permit components to be updated regularly.
- **Refine operations procedures frequently**: As you use operations procedures, look for opportunities to improve them.
- **Anticipate failure**: Perform “pre-mortem” exercises to identify potential sources of loss so that they can be removed or mitigated.
- **Learn from all operational failures**: Drive improvement through lessons learned from all operational events and failures. Share what is learned across teams and through the entire organization.

Hence, the correct answer is: **Operational Excellence**

The option that says: **Performance Efficiency** is incorrect because this pillar's purpose is to ensure that the computing resources are efficiently utilized to meet system requirements and to maintain that efficiency as demand changes and technologies evolve.

The option that says: **Security** is incorrect because this pillar simply focuses on protecting your data, systems, and assets by taking advantage of various cloud features and technologies. It doesn't support the design principle of performing operations as code, unlike Operational Excellence.

The option that says: **Cost Optimization** is incorrect because this pillar's primary concern is to optimize your cloud workloads to deliver business value at the lowest price point.

[Code Decode Case studies and there answers](aws-cloud-practitioner-from-tutorial-dojo/code-decode-case-studies-and-there-answers.md)

[Again Tutorials DOJO notes](aws-cloud-practitioner-from-tutorial-dojo/again-tutorials-dojo-notes.md)

Question 4:

Which AWS Well-Architected Framework pillar supports the design principle of performing operations as code?

**Cost Optimization**

**Security**

**Performance Efficiency**

**Your answer is correct**

**Operational Excellence**

**Overall explanation**

The **AWS Well-Architected Framework** helps you understand the pros and cons of the decisions you make while building systems on AWS. Using the Framework enables you to learn architectural best practices for designing and operating secure, reliable, efficient, cost-effective, and sustainable workloads in the AWS Cloud.

The AWS Well-Architected Framework is based on a set of pillars — operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

![](https://media.tutorialsdojo.com/public/AWS_WA_Tool_Operational_Excellence_16AUG2023.png)

The Operational Excellence pillar includes supporting the development and running workloads effectively, gaining insight into their operations, and continuously improving supporting processes and procedures to deliver business value.

There are five design principles for operational excellence in the cloud:

- **Perform operations as code**: In the cloud, you can apply the same engineering discipline that you use for application code to your entire environment. You can define your entire workload (applications, infrastructure) as code and update it with code.
- **Make frequent, small, reversible changes**: Design workloads to permit components to be updated regularly.
- **Refine operations procedures frequently**: As you use operations procedures, look for opportunities to improve them.
- **Anticipate failure**: Perform “pre-mortem” exercises to identify potential sources of loss so that they can be removed or mitigated.
- **Learn from all operational failures**: Drive improvement through lessons learned from all operational events and failures. Share what is learned across teams and through the entire organization.

Hence, the correct answer is: **Operational Excellence**

The option that says: **Performance Efficiency** is incorrect because this pillar's purpose is to ensure that the computing resources are efficiently utilized to meet system requirements and to maintain that efficiency as demand changes and technologies evolve.

The option that says: **Security** is incorrect because this pillar simply focuses on protecting your data, systems, and assets by taking advantage of various cloud features and technologies. It doesn't support the design principle of performing operations as code, unlike Operational Excellence.

The option that says: **Cost Optimization** is incorrect because this pillar's primary concern is to optimize your cloud workloads to deliver business value at the lowest price point.

Question 5:

A company is migrating its on-premises workloads to a new architecture that is distributed between the AWS Cloud and its local data center.

**Correct answer**

**On-premises to Hybrid**

**Hybrid to On-premises**

**Hybrid to Cloud Native**

**Your answer is incorrect**

**On-premises to Cloud Native**

**Overall explanation**

Hybrid cloud is an IT infrastructure design that integrates a company’s internal IT resources with third-party cloud provider infrastructure and services. With hybrid cloud, you can store your data and run your applications across multiple environments. Your hybrid cloud environment helps you provision, scale, and centrally manage your compute resources.

Hybrid cloud infrastructure emerged with the increasing adoption of cloud technology. Companies had to integrate their existing systems with modern cloud resources.

![](https://media.tutorialsdojo.com/aws_hyrbid_cloud_8AUG2023.png)

In addition to cloud migration and modernization efforts, there are myriad other reasons to adopt a hybrid cloud, such as low-latency needs, local data processing, and data residency. Hybrid cloud solutions let you use the best of every cloud option. With more granular control over IT resources, you can optimize spend. Hybrid cloud also helps you modernize applications faster, and connect cloud services to data in a secure manner that delivers new value. Other reasons to adopt hybrid cloud include differentiated end-user experiences and adherence to data regulations.

Hence, the correct answer is: **On-premises to Hybrid**

The option that says: **Hybrid to On-premises** is incorrect because this is the complete opposite of what the scenario describes. The company has on-premises workloads that they want to integrate with AWS Cloud, which means that this is an on-premises to Hybrid migration.

The option that says: **Hybrid to Cloud Native** is incorrect because, in the first place, the company is not using a hybrid deployment model for its workloads as it is only using its local data center originally. In addition, Cloud Native is simply a software approach to building, deploying, and managing modern applications in cloud computing environments.

The option that says: **On-premises to Cloud Native** is incorrect. Although it is true that the current setup of the company is using on-premises only, it is still wrong to say that the company is moving to a Cloud Native architecture since the scenario didn't mention anything about Kubernetes. Moreover, a Cloud Native approach doesn't usually have on-premises workloads associated with them.

Question 6:

A startup plans to improve the security of its Amazon EC2 instances by applying security rules to subnets of the default VPC.

Which is the MOST suitable AWS service or tool that should be used to meet this requirement?

**AWS Network Firewall**

**Correct answer**

**Network Access Control Lists**

**Your answer is incorrect**

**Security Groups**

**AWS Firewall Manager**

**Overall explanation**

**Network Access Control Lists** allow or deny inbound or outbound traffic that operates at the subnet level. These are basically stateless firewalls that do not track a connection's state. Stateless firewalls, like Network Access Control Lists, process each incoming packet in isolation without considering the packets that came before it.

![](https://media.tutorialsdojo.com/public/Network_ACL_11OC2023.png)

Hence, the correct answer is: **Network Access Control Lists.**

The option that says: **Security Groups** is incorrect because, unlike Network Access Control Lists, they operate at the resource level and not the subnet level. These are basically attached through an Elastic Network Interface (ENI) of a resource such as an EC2 or RDS instance. Furthermore, these are stateful firewalls that maintain context about active sessions and remember past packets.

The option that says: **AWS Firewall Manager** is incorrect because this is basically a service that centralizes the management of security rules across multiple accounts and services. This service does not even manage subnet rules at all as it primarily focuses on managing higher-level security policies for AWS WAF (Web Application Firewall), AWS Shield Advanced, and AWS Network Firewall.

The option that says: **AWS Network Firewall** is incorrect. Although this service can apply security rules to the subnets of your default VPC, using the AWS Network Firewall is not the most suitable one to use as it is primarily used as a stateful firewall that operates at the entire VPC level and not just for subnets. AWS Network Firewall also entails a significant cost compared with Network ACLs. This firewall allows you to filter traffic at the perimeter of your VPC and inspect traffic flows using features such as inbound encrypted traffic inspection, stateful inspection, protocol detection, and others.

Question 7:

Which AWS service allows machine learning models to be trained using SQL commands and enables the integration of trained models within a data warehouse for forecasting purposes?

**Amazon Aurora PostgreSQL**

**Amazon MemoryDB for Redis**

**Amazon SageMaker**

**Your answer is correct**

**Amazon Redshift ML**

**Overall explanation**

**Amazon Redshift ML** is a cutting-edge machine learning tool enabling data analysts and developers to build and deploy machine learning models using SQL. With Redshift ML, you can train and deploy models directly from your Redshift data warehouse, making it much more efficient and seamless to build predictive models at scale. The best part about Redshift ML is that it is built on Amazon SageMaker, providing access to a vast range of pre-built algorithms and the ability to develop custom models using your code.

![](https://media.tutorialsdojo.com/public/Amazon-Redshift-ML-07-24-2023.jpg)

This tool is perfect for businesses looking to enhance their data analysis and gain valuable insights from their data. With Amazon Redshift ML, you can seamlessly integrate machine learning into your business workflows, giving you the ability to make data-driven decisions that can impact your bottom line.

Hence, the correct answer is: **Amazon Redshift ML.**

The option that says: **Amazon SageMaker** is incorrect because this service only focuses on the end-to-end machine learning workflow, which includes data preparation, building and training machine learning models in a separate environment, and deployment. It is not specifically designed to create and train models for data warehouses.

The option that says: **Amazon Aurora PostgreSQL** is incorrect because although it supports machine learning integrations with services like Amazon SageMaker, it is primarily a relational database and does not provide the same level of integration for training and running ML models directly within a data warehouse using SQL commands.

The option that says: **Amazon MemoryDB for Redis** is incorrect because this service does not have Machine Learning capabilities that leverages on SQL to train ML models. Amazon MemoryDB for Redis is just a durable database with microsecond reads, low single-digit millisecond writes, scalability, and enterprise security.

Question 8:

A manufacturing company plans to host a business-critical application on a single Amazon EC2 instance.

What is the best way to increase the application's resilience with the LEAST operational overhead?

**Launch multiple EC2 instances of the application using CloudFormation StackSets in different AWS accounts.**

**Your answer is correct**

**Launch multiple EC2 instances of the application in multiple Availability Zones.**

**Launch multiple EC2 instances of the application in multiple subnets.**

**Launch multiple EC2 instances of the application in multiple VPCs.**

**Overall explanation**

Resiliency is the ability of a workload to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions, such as misconfigurations or transient network issues.

AWS Regions consist of AWS Availability Zones (AZs). Each AZ represents one or more distinct data centers with redundant power, networking, and connectivity within an AWS Region. A single AWS Region can contain three or more AZs. While each AZ is set at a considerable distance from others to ensure physical separation, they all lie within 100 km (60 miles) of one another.

![](https://media.tutorialsdojo.com/public/Regions_and_AZs_02OCT2023.png)

To enhance the resilience and availability of your application, you should deploy your application across multiple AZs. This approach ensures that even if one AZ experiences issues, your application remains operational in the other AZs.

You can also deploy your enterprise applications across multiple AWS Regions and AWS Accounts to further improve the availability, resiliency, and fault tolerance of your systems. However,

Hence, the correct answer is: **Launch multiple EC2 instances of the application in multiple Availability Zones.**

The option that says: **Launch multiple EC2 instances of the application using CloudFormation StackSets in different AWS Accounts** is incorrect. While deploying an application in a separate AWS Account can potentially enhance its resilience, the context provided doesn't guarantee this. If the EC2 instances from different AWS Accounts reside in the same AWS Region and Availability Zone as the primary account, the application's resilience won't necessarily improve. Moreover, even if you launch the EC2 instances in a different Availability Zone or Region in another AWS Account, this approach might be excessive for the given context and require a lot of operational overhead than simply deploying across multiple AZs in a single account.

The option that says: **Launch multiple EC2 instances of the application in multiple VPCs** is incorrect because the primary purpose of a VPC is to provide network isolation, not to increase resilience. A Virtual Private Cloud (VPC) in AWS primarily provides a virtual network environment that allows users to define and control the network architecture, including IP address ranges, subnets, and route tables. Managing multiple VPCs also adds unnecessary operational complexity compared to just managing multiple AZs.

The option that says: **Launch multiple EC2 instances of the application in multiple subnets** is incorrect. While deploying an application in multiple subnets can potentially enhance its resilience, the context provided does not guarantee this. A subnet is a range of IP addresses in a VPC. You launch AWS resources, such as EC2 instances, in subnets where a single subnet resides in a single Availability Zone. However, it is essential to remember that multiple subnets can reside in a single AZ. In the given context, launching an application in multiple subnets does not increase resilience if these subnets reside in a single AZ. A business-critical application must at least reside in multiple subnets in multiple AZs to ensure resiliency.

Question 9:

Which of the following are the relevant stakeholders in the Platform perspective of the AWS Cloud Adoption Framework (AWS CAF)? (Select TWO.)

**Your selection is correct**

**Technology Leaders**

**Chief Financial Officers (CFOs)**

**Chief information security officer (CISO)**

**Correct selection**

**IT Architects**

**Your selection is incorrect**

**Chief information officers (CIOs)**

**Overall explanation**

The **AWS Cloud Adoption Framework (AWS CAF)** leverages AWS experience and best practices to help you digitally transform and accelerate your business outcomes through the innovative use of AWS. AWS CAF groups its capabilities in six perspectives: Business, People, Governance, Platform, Security, and Operations. Each perspective comprises a set of capabilities that functionally related stakeholders own or manage in the cloud transformation journey

![](https://media.tutorialsdojo.com/td_aws_cloud_adoption_framework_aws_caf_24_AUG_2023.png)

The ***Platform*** perspective focuses on accelerating the delivery of cloud workloads via an enterprise-grade, scalable, hybrid cloud environment. It comprises seven capabilities shown in the following figure. Common stakeholders include CTO, technology leaders, architects, and engineers.

Hence, the correct answers are:

- **Technology Leaders**
- **IT Architects**

The option that says: **Chief Financial Officers (CFOs)** is incorrect because they correspond only to the Business perspective, where they help ensure that the cloud investments accelerate the digital transformation ambitions and business outcomes.

The option that says: **Chief Information Officers (CIOs)** is incorrect because they belong to different perspectives, such as the Business, People, and Governance perspectives.

The option that says: **Chief Information Security officer (CISO)** is incorrect because they are the relevant stakeholders of the Security perspective that helps achieve the confidentiality, integrity, and availability of the data and cloud workloads.

Question 10:

Which AWS service uses machine learning to continuously monitor and detect unusual cloud expenditures in terms of cost and usage?

**AWS Cost Explorer**

**Your answer is incorrect**

**AWS Billing Conductor**

**Correct answer**

**AWS Cost Anomaly Detection**

**AWS Trusted Advisor**

**Overall explanation**

**AWS Cost Anomaly Detection** is an AWS cost management feature that uses machine learning to continually monitor your cost and usage to detect unusual spending. It can reduce cost surprises and enhance control without slowing innovation.

The AWS Cost Anomaly Detection feature leverages advanced Machine Learning technologies to identify anomalous spend and root causes, so you can quickly take action. With three simple steps, you can create your own contextualized monitor and receive alerts when any anomalous spend is detected.

![](https://media.tutorialsdojo.com/public/AWS_Cost_Anomaly_Detection_14Nov2024.JPG)

Using AWS Cost Anomaly Detection includes the following benefits:

- You receive alerts individually in aggregated reports in an email message or an Amazon SNS topic.
- You can evaluate your spending patterns using machine learning methods to minimize false positive alerts. For example, you can determine weekly or monthly seasonality and natural growth.
- You can investigate the root cause of the anomaly, such as the AWS account, service, Region, or usage type that's driving the cost increase.
- You can configure how to evaluate your costs. Choose whether you want to analyze all of your AWS services independently or analyze specific member accounts, cost allocation tags, or cost categories.

Hence, the correct answer is: **AWS Cost Anomaly Detection**

The option that says: **AWS Billing Conductor** is incorrect because this service just simplifies the process of billing and reporting by offering flexible pricing options and clear cost visibility. Moreover, this service does not have machine learning capabilities to monitor and detect unusual spending.

The option that says: **AWS Cost Explorer** is incorrect because it only helps visualize and analyze cost and usage data over time. While it provides detailed insights into spending patterns, it does not use machine learning to automatically detect cost anomalies. Instead, it allows users to manually explore cost and usage data and identify trends, but it does not proactively monitor or detect unusual expenditures.

The option that says: **AWS Trusted Advisor** is incorrect because it simply provides recommendations for best practices, including cost optimization. It does not use machine learning for anomaly detection in spending.

Question 11:

A company plans to streamline its native iOS application development process and harness the AWS cloud's capabilities for enhancing its build activities.

Which of the following should the company use to achieve these requirements?

**Correct answer**

**Amazon EC2 M1 Mac instances**

**AWS Device Farm**

**AWS Amplify**

**Your answer is incorrect**

**AWS App Runner**

**Overall explanation**

**Amazon EC2 M1 Mac instances** allow you to run on-demand macOS workloads in the AWS cloud. With EC2 Mac instances, developers creating apps for iPhone, iPad, Mac, Apple Watch, Apple TV, and Safari can now provision and access macOS environments within minutes, dynamically scale capacity as needed, and benefit from AWS's pay-as-you-go pricing.

![](https://media.tutorialsdojo.com/public/EC2_M2_Mac_Instance_12OCT2023.jpg)

Building native IOS applications are compatible with these type of instances. Instead of relying on other third-party APIs and services on the internet, Amazon EC2 M1 Mac instances provide developers the flexibility, elasticity, and scale of AWS to increase their focus on core innovation, such as developing creative and functional apps while spending less time managing infrastructure.

Hence, the correct answer is: **Amazon EC2 M1 Mac instances.**

**AWS Device Farm** is incorrect primarily because this service is not at all used for developing building applications. This application testing service lets you improve the quality of your web and mobile apps by testing them across an extensive range of desktop browsers and real mobile devices without having to provision and manage any testing infrastructure.

**AWS Amplify** is incorrect this service is not capable of supporting native IOS development and build activities. The closest offering of this service to IOS applications is a backend hosting service for cross-platform applications with real-time and offline functionality.

**AWS App Runner** is incorrect primarily because it isn't for developing and building native iOS applications. Instead, it's a container-native service managed by AWS, designed to help developers swiftly build, deploy, and scale web applications and APIs.

**References:**

Question 12:

A company plans to migrate its multi-tier application to the AWS Cloud. The company wants to ensure that each tier (web, application, and database) can communicate with each other while also preventing unauthorized access through the use of security groups.

Which particular task can be performed by using security groups in AWS?

**Your answer is incorrect**

**Apply a stateful firewall to an Amazon S3 bucket.**

**Correct answer**

**Enable exclusive access to Amazon EC2 instances inside an Amazon VPC via a specific port.**

**Enhance the security of cached data managed by Amazon CloudFront.**

**Prevent unauthorized access from malicious IP addresses at each tier's subnet.**

**Overall explanation**

**Security groups** are stateful firewalls that operate at the resource level. These are basically attached through an Elastic Network Interface (ENI) of a resource such as an Amazon EC2 or Amazon RDS instance. Security groups can allow access to an Amazon EC2 instance through a specific port.

![](https://media.tutorialsdojo.com/public/Security_Group_11OCT2023.jpg)

Furthermore, security groups in AWS can reference other security groups, allowing for layered security. For instance, if the application tier references the web tier's security group, it will only permit traffic from the web tier. Any incoming traffic to the application tier not originating from the web tier gets denied.

Additionally, you can specify allowed ports within these security groups. So, even if the database tier correctly references the application tier's security group, access will be denied if it attempts to connect to an unconfigured port in the database tier's security group.

Hence, the correct answer is: **Enable exclusive access to Amazon EC2 instances inside an Amazon VPC via a specific port.**

The option that says: **Prevent unauthorized access from malicious IP addresses at each tier's subnet** is incorrect because this task is only accomplished using Network Access Control Lists, not security groups. Network Access Control Lists operate at the subnet level, while security groups operate at the resource level.

The option that says: **Enhance the security of cached data managed by Amazon CloudFront** is incorrect because security groups are not at all used to protect the data being cached in Amazon CloudFront. As stated before, security groups operate at the resource level through ENIs attached to resources such as EC2 and RDS instances. The AWS Web Application Firewall (WAF) is a more appropriate service to protect your CloudFront distributions.

The option that says: **Apply a stateful firewall to an Amazon S3 bucket** is incorrect. Although a security group does act as a stateful firewall in AWS, this feature is not used at all in Amazon S3. Note that Amazon S3 uses different security features such as S3.

Question 13:

A company plans to migrate its existing on-premises infrastructure to the AWS Cloud. The current business workflows heavily rely on legacy systems. The company aims to evaluate AWS Cloud readiness first and prioritize business transformation opportunities before starting migration activities.

Which AWS service or tool can help achieve these requirements?

**Correct answer**

**AWS Cloud Adoption Framework (AWS CAF)**

**Your answer is incorrect**

**AWS Migration Hub**

**AWS Support**

**AWS Prescriptive Guidance**

**Overall explanation**

The **AWS Cloud Adoption Framework (AWS CAF)** is a tool that aids companies or organizations in assessing their current capabilities that are critical to successful cloud adoption. Companies and organizations may utilize this tool to identify and prioritize transformation opportunities, evaluate and improve their cloud readiness, and iteratively evolve their transformation roadmap. Along with the guided concepts and ideologies the AWS Cloud Adoption Framework provides, a cloud readiness assessment is also available for companies and organizations to utilize.

![](https://media.tutorialsdojo.com/public/AWS_CAF.png)

AWS CAF groups its capabilities in six perspectives: Business, People, Governance, Platform, Security, and Operations. Each perspective comprises a set of capabilities that functionally related stakeholders own or manage in your cloud transformation journey.

This assessment might give them a better understanding of their capabilities and be cognizant of what they need to improve when adopting the cloud.

Hence, the correct answer is: **AWS Cloud Adoption Framework (AWS CAF).**

**AWS Support** is incorrect because this is simply a service by AWS that offers a range of plans that provide access to tools and expertise that support the success and operational health of the customer's AWS solutions. Although it allows technical assistance for cloud migration, the overall task of assessing a customer, business, or institution of being cloud-ready is outside the scope of this service.

**AWS Prescriptive Guidance** is incorrect because this service is just a collection of articles that provides time-tested strategies, guides, and patterns curated by AWS experts to help accelerate your cloud migration, modernization, and optimization projects. Like the previous option, this service allows for technical assistance for cloud migration but still lacks in assessing cloud readiness adoption.

**AWS Migration Hub** is incorrect because this service is primarily used by customers when migration is already happening and not in the planning phase. This service provides a single place to discover your existing servers, plan migrations, and track the status of each application migration. In the context of the provided scenario, the company needs to assess its cloud readiness before committing to a complete migration, which is not a suitable use case for the AWS Migration Hub service.

Question 14:

A company plans to migrate its operations to AWS and wants to justify the value of the cloud migration. The company seeks to define its measurable business outcomes by identifying and prioritizing transformation opportunities using the AWS Cloud Adoption Framework (AWS CAF).

Which phase of the cloud transformation journey do these plans belong to?

**Scale**

**Launch**

**Your answer is incorrect**

**Align**

**Correct answer**

**Envision**

**Overall explanation**

The **AWS Cloud Adoption Framework (AWS CAF)** leverages AWS experience and best practices to help you digitally transform and accelerate your business outcomes through innovative use of AWS. AWS CAF identifies specific organizational capabilities that underpin successful cloud transformations.

You can use the AWS CAF to identify and prioritize transformation opportunities, evaluate and improve your cloud readiness, and iteratively evolve your transformation roadmap.

![](https://media.tutorialsdojo.com/public/AWS_CAF_Cloud_Transformation_Journey_4OCT2023.png)

Adopting an iterative approach will help you maintain momentum and evolve your roadmap as you learn from experience. The AWS CAF recommends four iterative and incremental cloud transformation phases:

- Envision
- Align
- Scale
- Launch

The **Envision phase** focuses on demonstrating how the cloud will help accelerate your business outcomes. It does so by identifying and prioritizing transformation opportunities across each of the four transformation domains in line with your strategic business objectives. Associating your transformation initiatives with key stakeholders (senior individuals capable of influencing and driving change) and measurable business outcomes will help you demonstrate value as you progress through your transformation journey.

Hence, the correct answer is **Envision.**

**Align** is incorrect because it primarily focuses on identifying capability gaps and cross-organizational dependencies, which will improve your cloud readiness and ensure stakeholder alignment.

**Scale** is incorrect because it only focuses on expanding production pilots and business value of your cloud infrastructure. This phase in the AWS CAF cloud journey ensures that the business benefits associated with your cloud investments are realized and sustained. sustained.

**Launch** is incorrect because this is simply delivering pilots in production and demonstrating incremental business value rather than identifying measurable business outcomes.

Question 15:

Which of the following AWS services automates the creation, management, testing, and deployment of customized Amazon EC2 server images?

**Your answer is correct**

**EC2 Image Builder**

**AWS Well-Architected Tool**

**AWS Compute Optimizer**

**AWS Launch Wizard**

**Overall explanation**

**EC2 Image Builder** is a fully managed AWS service that helps you to automate the creation, management, and deployment of customized, secure, and up-to-date server images. You can use the AWS Management Console, AWS Command Line Interface, or APIs to create custom images in your AWS account.

![](https://media.tutorialsdojo.com/public/AWS_EC2_Image_Builder.PNG)

With this service, you can own the customized images that Image Builder creates in your account. You can configure pipelines to automate updates and system patching for the photos that you own, as well as run a stand-alone command to create an image with the configuration resources that you've defined.

Hence, the correct answer is: **EC2 Image Builder**

The option that says: **AWS Well-Architected Tool** is incorrect because this is simply a tool that provides a consistent process for measuring your architecture using AWS best practices and against the AWS Well-Architected Framework. It does not help in creating, designing, testing, or managing custom Amazon EC2 images.

The option that says: **AWS Compute Optimizer** is incorrect because it only focuses on analyzing the configuration and utilization metrics of your AWS resources which both are not applicable for handling the customized images.

The option that says: **AWS Launch Wizard** is incorrect because this service primarily guides the way of sizing, configuring, and deploying AWS resources for third-party applications. It is not capable of automating the creation or management of custom EC2 images, unlike the EC2 Image Builder service.