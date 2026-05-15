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