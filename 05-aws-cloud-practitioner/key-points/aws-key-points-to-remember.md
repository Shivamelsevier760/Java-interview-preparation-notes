# AWS key points to remember

SET - 4

AWS recommends that customers should scale resources horizontally to increase aggregate system availability. Replacing a large resource with multiple small resources in parallel will reduce the impact of a single failure on the overall system. For example, if a customer wants to convert a large number of binary files to text files or transcode a large number of video files to another format, it is recommended that they use multiple EC2 instances in parallel instead of using one large instance.

Serverless architectures can reduce costs because you do not have to manage or pay for underutilized servers, or provision redundant infrastructure to implement high availability. For example, you can upload your code to the AWS Lambda compute service, and the service can run the code on your behalf using AWS infrastructure. With AWS Lambda, you are charged for every 100ms your code executes and the number of times your code is triggered.

Data protection refers to protecting data while in-transit (as it travels to and from Amazon S3) and at rest (while it is stored on disks in Amazon data centers).

Data in-transit:

You can protect data in transit by using:

1- Secure Socket Layer/Transport Layer Security (SSL/TLS)

2- Client-side encryption.

Data at rest:

Server-Side Encryption and Client-Side Encryption are used to protect data at rest in Amazon S3.

1- Server-Side Encryption – Amazon S3 encrypts your objects automatically before saving it on disks in its data centers and decrypt it when you download the objects.

2- Client-Side Encryption – You can encrypt your data on the client-side and upload the encrypted data to Amazon S3. In this case, you manage the encryption process, the

Amazon Lightsail is designed to be the easiest way to launch and manage a Web server using AWS. Lightsail plans include everything you need to jumpstart your project – a virtual machine, SSD-based storage, data transfer, DNS management, and a static IP address – for a low, predictable price.

Amazon Lightsail is best for Websites built on common applications like WordPress, Joomla, Drupal, Magento. You can get started using Lightsail for your website with just a few clicks. Choose the operating system or application template that‘s best for your website, and your virtual private server is ready in less than a minute. You can easily manage your web server, DNS, and IP addresses directly from the Lightsail console.

The factors that have the greatest impact on cost include: Compute, Storage  and Data Transfer Out. Their pricing differs according to the service you use.

It does not matter how many AWS services you are using. Each AWS service has its own pricing details, and many of them are free to use.

 There is no charge for inbound data transfer (also called Data Transfer IN) across all services in all Regions.

Data transfer from AWS to the internet (Data Transfer OUT) is charged per service, with rates specific to the originating Region.

 IAM and all of its features are free to use.

AWS publishes security bulletins about the latest security and privacy events with AWS services on the Security Bulletins page.

AWS Certificate Manager (ACM) is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources.

The account owner is the entity that has complete control over all resources in their AWS account.

AWS cloud support engineers provide technical support to customers who are having issues with the system. Cloud support engineers are available only for the Business, Enterprise On-Ramp, and Enterprise support plans.

AWS technical account manager (TAM) is a feature offered to AWS customers who have an Enterprise On-Ramp or Enterprise support plan. AWS TAM helps AWS customers craft and execute strategies to drive their adoption and use of AWS services.

The AWS Security Team is an internal AWS team that is responsible for the security of services offered by AWS.

**AWS Organizations**

AWS Organizations helps you to centrally manage billing; control access, compliance, and security; and share resources across your AWS accounts. Using AWS Organizations, you can automate account creation, create groups of accounts to reflect your business needs, and apply policies for these groups for governance. You can also simplify billing by setting up a single payment method for all of your AWS accounts. AWS Organizations is available to all AWS customers at no additional charge.

Key Features of AWS Organizations:

![](https://assets-pt.media.datacumulus.com/aws-clf-pt/assets/pt2-q36-i1.jpg)

via -

[https://aws.amazon.com/organizations/](https://aws.amazon.com/organizations/)

Incorrect options:

**AWS Cost Explorer** - AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time. AWS Cost Explorer includes a default report that helps you visualize the costs and usage associated with your top five cost-accruing AWS services, and gives you a detailed breakdown of all services in the table view. The reports let you adjust the time range to view historical data going back up to twelve months to gain an understanding of your cost trends. You cannot use AWS Cost Explorer to set up consolidated billing and a single payment method for multiple AWS accounts.

**AWS Budgets** - AWS Budgets gives the ability to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount. You can also use AWS Budgets to set reservation utilization or coverage targets and receive alerts when your utilization drops below the threshold you define. Budgets can be created at the monthly, quarterly, or yearly level, and you can customize the start and end dates. You can further refine your budget to track costs associated with multiple dimensions, such as AWS service, linked account, tag, and others. You cannot use AWS Budgets to set up consolidated billing and a single payment method for multiple AWS accounts.

**AWS Secrets Manager** - AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. You cannot use AWS Secrets Manager to set up consolidated billing and a single payment method for multiple AWS accounts.

**Edge Location Management**

Security and Compliance is a shared responsibility between AWS and the customer. The AWS Shared Responsibility Model can help relieve the customer’s operational burden as AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates.

AWS is responsible for security "of" the cloud. This covers their global infrastructure elements including Regions, Availability Zones (AZ), and Edge Locations.

Incorrect options:

**Customer Data**

**Identity and Access Management**

**Server-side Encryption (SSE)**

The customer is responsible for security "in" the cloud. Customers are responsible for managing their data including encryption options and using Identity and Access Management tools for implementing appropriate access control policies as per their organization requirements. For abstracted services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and customers access the endpoints to store and retrieve data. Therefore, these three options fall under the responsibility of the customer according to the AWS shared responsibility model.

Exam Alert:

Please review the AWS Shared Responsibility Model in detail as you can expect multiple questions on this topic in the exam:

![](https://d1.awsstatic.com/security-center/Shared_Responsibility_Model_V2.59d1eccec334b366627e9295b304202faf7b899b.jpg)