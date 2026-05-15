# Stephane Maarek Test 4

## Wrong

- Q4 - important
    
    **You have configured a Network ACL and a Security Group for the load balancer and Amazon EC2 instances to allow inbound traffic on port 80. However, users are still unable to connect to your website after launch.
    Which additional configuration is required to make the website accessible to all users over the internet?**
    
    - **Add a rule to the Network ACLs to allow outbound traffic on ports 32768 - 61000(Incorrect)**
    - **Add a rule to the Network ACLs to allow outbound traffic on ports 1024 - 65535(Correct)**
    - **Add a rule to the Network ACLs to allow outbound traffic on ports 1025 - 5000**
    - **Add a rule to the Security Group allowing outbound traffic on port 80**
    
    ### **Explanation**
    
    Correct option:
    
    **Add a rule to the Network ACLs to allow outbound traffic on ports 1024 - 65535**
    
    A Network Access Control List (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC.
    
    When you create a custom Network ACL and associate it with a subnet, by default, this custom Network ACL denies all inbound and outbound traffic until you add rules. A network ACL has separate inbound and outbound rules, and each rule can either allow or deny traffic. Network ACLs are stateless, which means that responses to allowed inbound traffic are subject to the rules for outbound traffic (and vice versa).
    
    The client that initiates the request chooses the ephemeral port range. The range varies depending on the client's operating system. Requests originating from Elastic Load Balancing use ports 1024-65535. List of ephemeral port ranges:
    
    1. Many Linux kernels (including the Amazon Linux kernel) use ports 32768-61000.
    2. Requests originating from Elastic Load Balancing use ports 1024-65535.
    3. Windows operating systems through Windows Server 2003 use ports 1025-5000.
    4. Windows Server 2008 and later versions use ports 49152-65535.
    5. A NAT gateway uses ports 1024-65535.
    
    AWS Lambda functions use ports 1024-65535.
    
- Q35 - didn’t understand
    
    **You have a popular three-tier web application that is used by users throughout the globe receiving thousands of incoming requests daily. You have AWS Route 53 policies to automatically distribute weighted traffic to the API resources located at URL api.global.com.
    What is an alternative way of distributing traffic to a web application?**
    
    - **Auto Scaling**
    - **S3**
    - **ELB(Correct)**
    - **CloudFront(Incorrect)**
    
    ### **Explanation**
    
    Correct option:
    
    **ELB**
    
    Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions. Route 53 failover policy is similar to an ELB in that when using failover routing, it lets you route traffic to a resource when the resource is healthy or to a different resource when the first resource is unhealthy.
    
    Incorrect options:
    
    **CloudFront** - Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds.
    
- Q41 - important
    
    **You have uploaded a zip file to AWS Lambda that contains code files written in Node.Js. When your function is executed you receive the following output, 'Error: Memory Size: 10,240 MB Max Memory Used'.
    Which of the following explains the problem?**
    
    - **Your Lambda function ran out of RAM(Correct)**
    - **You have uploaded a zip file larger than 50 MB to AWS Lambda**
    - **The uncompressed zip file exceeds AWS Lambda limits(Incorrect)**
    - **Your zip file is corrupt**
- Q42 - important
    
    **A developer is configuring an Application Load Balancer (ALB) to direct traffic to the application's EC2 instances and Lambda functions.
    Which of the following characteristics of the ALB can be identified as correct? (Select two)**
    
    - [x]  **If you specify targets using IP addresses, traffic is routed to instances using the primary private IP address(Incorrect)**
    - [x]  **An ALB has three possible target types: Instance, IP and Lambda(Correct)**
    - [ ]  **If you specify targets using an instance ID, traffic is routed to instances using any private IP address from one or more network interfaces**
    - [ ]  **You can not specify publicly routable IP addresses to an ALB(Correct)**
    - [ ]  **An ALB has three possible target types: Hostname, IP and Lambda**
    
    ### **Explanation**
    
    Correct options:
    
    **An ALB has three possible target types: Instance, IP and Lambda**
    
    **You can not specify publicly routable IP addresses to an ALB**
    
    When the target type is IP, you can specify IP addresses from specific CIDR blocks only. You can't specify publicly routable IP addresses.
    
    If you specify targets using an instance ID, traffic is routed to instances using the primary private IP address specified in the primary network interface for the instance.
    
    If you specify targets using IP addresses, you can route traffic to an instance using any private IP address from one or more network interfaces. This enables multiple applications on an instance to use the same port.
    
- Q45 - confusing wording
    
    **An order management system uses a cron job to poll for any new orders. Every time a new order is created, the cron job sends this order data as a message to the message queues to facilitate downstream order processing in a reliable way. To reduce costs and improve performance, the company wants to move this functionality to AWS cloud.
    Which of the following is the most optimal solution to meet this requirement?**
    
    - **Use Amazon Simple Notification Service (SNS) to push notifications to Kinesis Data Firehose delivery streams for processing the data for downstream applications**
    - **Configure different Amazon Simple Queue Service (SQS) queues to poll for new orders**
    - **Use Amazon Simple Notification Service (SNS) to push notifications when an order is created. Configure different Amazon Simple Queue Service (SQS) queues to receive these messages for downstream processing(Correct)**
    - **Use Amazon Simple Notification Service (SNS) to push notifications and use AWS Lambda functions to process the information received from SNS(Incorrect)**
- Q46 - important
    
    **You are a manager for a tech company that has just hired a team of developers to work on the company's AWS infrastructure. All the developers are reporting to you that when using the AWS CLI to execute commands it fails with the following exception: You are not authorized to perform this operation. Encoded authorization failure message: 6h34GtpmGjJJUm946eDVBfzWQJk6z5GePbbGDs9Z2T8xZj9EZtEduSnTbmrR7pMqpJrVYJCew2m8YBZQf4HRWEtrpncANrZMsnzk.
    Which of the following actions will help developers decode the message?**
    
    - **AWS STS decode-authorization-message(Correct)**
    - **Use KMS decode-authorization-message**
    - **AWS Cognito Decoder**
    - **AWS IAM decode-authorization-message(Incorrect)**
- Q59 - important
    
    **A company would like to migrate the existing application code from a GitHub repository to AWS CodeCommit.
    As an AWS Certified Developer Associate, which of the following would you recommend for migrating the cloned repository to CodeCommit over HTTPS?**
    
    - **Use Git credentials generated from IAM(Correct)**
    - **Use IAM Multi-Factor authentication**
    - **Use authentication offered by GitHub secure tokens(Incorrect)**
    - **Use IAM user secret access key and access key ID**
    
    ### **Explanation**
    
    Correct option:
    
    **Use Git credentials generated from IAM** - CodeCommit repositories are Git-based and support the basic functionalities of Git such as Git credentials. AWS recommends that you use an IAM user when working with CodeCommit. You can access CodeCommit with other identity types, but the other identity types are subject to limitations.
    
    The simplest way to set up connections to AWS CodeCommit repositories is to configure Git credentials for CodeCommit in the IAM console, and then use those credentials for HTTPS connections. You can also use these same credentials with any third-party tool or individual development environment (IDE) that supports HTTPS authentication using a static user name and password.
    
- Q60 - important
    
    Yo**ur mobile application needs to perform API calls to DynamoDB. You do not want to store AWS secret and access keys onto the mobile devices and need all the calls to DynamoDB made with a different identity per mobile device.
    Which of the following services allows you to achieve this?**
    
    - **Cognito Sync(Incorrect)**
    - **Cognito User Pools**
    - **Cognito Identity Pools(Correct)**
    - **IAM**
- Q62 - important
    
    **An organization recently began using AWS CodeCommit for its source control service. A compliance security team visiting the organization was auditing the software development process and noticed developers making many git push commands within their development machines. The compliance team requires that encryption be used for this activity.
    How can the organization ensure source code is encrypted in transit and at rest?**
    
    - **Enable KMS encryption(Incorrect)**
    - **Use AWS Lambda as a hook to encrypt the pushed code**
    - **Repositories are automatically encrypted at rest(Correct)**
    - **Use a git command line hook to encrypt the code client side**
    
    ### **Explanation**
    
    Correct option:
    
    **Repositories are automatically encrypted at rest**
    
    Data in AWS CodeCommit repositories is encrypted in transit and at rest. When data is pushed into an AWS CodeCommit repository (for example, by calling git push), AWS CodeCommit encrypts the received data as it is stored in the repository.
    

## Doubtful

- Q8 - important
    
    **An Amazon Simple Queue Service (SQS) has to be configured between two AWS accounts for shared access to the queue. AWS account A has the SQS queue in its account and AWS account B has to be given access to this queue.
    Which of the following options need to be combined to allow this cross-account access? (Select three)**
    
    - [x]  **The account A administrator attaches a trust policy to the role that identifies account B as the principal who can assume the role(Correct)**
    - [ ]  **The account A administrator delegates the permission to assume the role to any users in account A**
    - [x]  **The account B administrator delegates the permission to assume the role to any users in account B(Correct)**
    - [x]  **The account A administrator creates an IAM role and attaches a permissions policy(Correct)**
    - [ ]  **The account A administrator attaches a trust policy to the role that identifies account B as the AWS service principal who can assume the role**
    - [ ]  **The account B administrator creates an IAM role and attaches a trust policy to the role with account B as the principal**
    
    ### **Explanation**
    
    Correct options:
    
    **The account A administrator creates an IAM role and attaches a permissions policy**
    
    **The account A administrator attaches a trust policy to the role that identifies account B as the principal who can assume the role**
    
    **The account B administrator delegates the permission to assume the role to any users in account B**
    
    To grant cross-account permissions, you need to attach an identity-based permissions policy to an IAM role. For example, the AWS account A administrator can create a role to grant cross-account permissions to AWS account B as follows:
    
    1. The account A administrator creates an IAM role and attaches a permissions policy—that grants permissions on resources in account A—to the role.
    2. The account A administrator attaches a trust policy to the role that identifies account B as the principal who can assume the role.
    3. The account B administrator delegates the permission to assume the role to any users in account B. This allows users in account B to create or access queues in account A.
- Q18 - important
    
    **A development team had enabled and configured CloudTrail for all the Amazon S3 buckets used in a project. The project manager owns all the S3 buckets used in the project. However, the manager noticed that he did not receive any object-level API access logs when the data was read by another AWS account.
    What could be the reason for this behavior/error?**
    
    - **CloudTrail needs to be configured on both the AWS accounts for receiving the access logs in cross-account access**
    - **The meta-data of the bucket is in an invalid state and needs to be corrected by the bucket owner from AWS console to fix the issue**
    - **The bucket owner also needs to be object owner to get the object access logs(Correct)**
    - **CloudTrail always delivers object-level API access logs to the requester and not to object owner**
    
    ### **Explanation**
    
    Correct option:
    
    **The bucket owner also needs to be object owner to get the object access logs**
    
    If the bucket owner is also the object owner, the bucket owner gets the object access logs. Otherwise, the bucket owner must get permissions, through the object ACL, for the same object API to get the same object-access API logs.
    
- Q30
    
    **A development team is considering Amazon ElastiCache for Redis as its in-memory caching solution for its relational database.
    Which of the following options are correct while configuring ElastiCache? (Select two)**
    
    - [ ]  **While using Redis with cluster mode enabled, asynchronous replication mechanisms are used to keep the read replicas synchronized with the primary. If cluster mode is disabled, the replication mechanism is done synchronously**
    - [x]  **All the nodes in a Redis cluster must reside in the same region(Correct)**
    - [ ]  **You can scale write capacity for Redis by adding replica nodes**
    - [ ]  **If you have no replicas and a node fails, you experience no loss of data when using Redis with cluster mode enabled**
    - [x]  **While using Redis with cluster mode enabled, you cannot manually promote any of the replica nodes to primary(Correct)**
    
    ### **Explanation**
    
    Correct options:
    
    **All the nodes in a Redis cluster must reside in the same region**
    
    All the nodes in a Redis cluster (cluster mode enabled or cluster mode disabled) must reside in the same region.
    
    **While using Redis with cluster mode enabled, you cannot manually promote any of the replica nodes to primary**
    
    While using Redis with cluster mode enabled, there are some limitations:
    
    1. You cannot manually promote any of the replica nodes to primary.
    2. Multi-AZ is required.
    3. You can only change the structure of a cluster, the node type, and the number of nodes by restoring from a backup.
- Q40
    
    **A company has several Linux-based EC2 instances that generate various log files which need to be analyzed for security and compliance purposes. The company wants to use Kinesis Data Streams (KDS) to analyze this log data.
    Which of the following is the most optimal way of sending log data from the EC2 instances to KDS?**
    
    - **Install and configure Kinesis Agent on each of the instances(Correct)**
    - **Use Kinesis Producer Library (KPL) to collect and ingest data from each EC2 instance**
    - **Run cron job on each of the instances to collect log data and send it to Kinesis Data Streams**
    - **Install AWS SDK on each of the instances and configure it to send the necessary files to Kinesis Data Streams**
    
    ### **Explanation**
    
    Correct option:
    
    **Install and configure Kinesis Agent on each of the instances**
    
    Kinesis Agent is a stand-alone Java software application that offers an easy way to collect and send data to Kinesis Data Streams. The agent continuously monitors a set of files and sends new data to your stream. The agent handles file rotation, checkpointing, and retry upon failures. It delivers all of your data in a reliable, timely, and simple manner. It also emits Amazon CloudWatch metrics to help you better monitor and troubleshoot the streaming process.