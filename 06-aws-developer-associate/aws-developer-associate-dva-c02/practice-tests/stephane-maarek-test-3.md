# Stephane Maarek Test 3

## Wrong

- Q9
    
    **A development team uses shared Amazon S3 buckets to upload files. Due to this shared access, objects in S3 buckets have different owners making it difficult to manage the objects.
    As a developer associate, which of the following would you suggest to automatically make the S3 bucket owner, also the owner of all objects in the bucket, irrespective of the AWS account used for uploading the objects?**
    
    - **Use S3 CORS to make the S3 bucket owner, the owner of all objects in the bucket**
    - **Use Bucket Access Control Lists (ACLs) to control access on S3 bucket and then define its owner(Incorrect)**
    - **Use S3 Access Analyzer to identify the owners of all objects and change the ownership to the bucket owner**
    - **Use S3 Object Ownership to default bucket owner to be the owner of all objects in the bucket(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    **Use S3 Object Ownership to default bucket owner to be the owner of all objects in the bucket**
    
    S3 Object Ownership is an Amazon S3 bucket setting that you can use to control ownership of new objects that are uploaded to your buckets. By default, when other AWS accounts upload objects to your bucket, the objects remain owned by the uploading account. With S3 Object Ownership, any new objects that are written by other accounts with the bucket-owner-full-control canned access control list (ACL) automatically become owned by the bucket owner, who then has full control of the objects.
    
- Q13
    
    **As a Senior Developer, you manage 10 Amazon EC2 instances that make read-heavy database requests to the Amazon RDS for PostgreSQL. You need to make this architecture resilient for disaster recovery.
    Which of the following features will help you prepare for database disaster recovery? (Select two)**
    
    - [x]  **Use cross-Region Read Replicas(Correct)**
    - [ ]  **Use database cloning feature of the RDS DB cluster**
    - [ ]  **Enable the automated backup feature of Amazon RDS in a multi-AZ deployment that creates backups in a single AWS Region(Correct)**
    - [ ]  **Use RDS Provisioned IOPS (SSD) Storage in place of General Purpose (SSD) Storage**
    - [x]  **Enable the automated backup feature of Amazon RDS in a multi-AZ deployment that creates backups across multiple Regions(Incorrect)**
    
    ### **Explanation**
    
    Correct option:
    
    **Use cross-Region Read Replicas**
    
    In addition to using Read Replicas to reduce the load on your source DB instance, you can also use Read Replicas to implement a DR solution for your production DB environment. If the source DB instance fails, you can promote your Read Replica to a standalone source server. Read Replicas can also be created in a different Region than the source database. Using a cross-Region Read Replica can help ensure that you get back up and running if you experience a regional availability issue.
    
    **Enable the automated backup feature of Amazon RDS in a multi-AZ deployment that creates backups in a single AWS Region**
    
    Amazon RDS provides high availability and failover support for DB instances using Multi-AZ deployments. Amazon RDS uses several different technologies to provide failover support. Multi-AZ deployments for MariaDB, MySQL, Oracle, and PostgreSQL DB instances use Amazon's failover technology.
    
    The automated backup feature of Amazon RDS enables point-in-time recovery for your database instance. Amazon RDS will backup your database and transaction logs and store both for a user-specified retention period. If it’s a Multi-AZ configuration, backups occur on the standby to reduce I/O impact on the primary. Automated backups are limited to a single AWS Region while manual snapshots and Read Replicas are supported across multiple Regions.
    
- Q14
    
    **You are a developer working with the AWS CLI to create Lambda functions that contain environment variables. Your functions will require over 50 environment variables consisting of sensitive information of database table names.
    What is the total set size/number of environment variables you can create for AWS Lambda?**
    
    - **The total size of all environment variables shouldn't exceed 8 KB. There is no limit on the number of variables(Incorrect)**
    - **The total size of all environment variables shouldn't exceed 8 KB. The maximum number of variables that can be created is 50**
    - **The total size of all environment variables shouldn't exceed 4 KB. The maximum number of variables that can be created is 35**
    - **The total size of all environment variables shouldn't exceed 4 KB. There is no limit on the number of variables(Correct)**
- Q27 - important
    
    **Your web application architecture consists of multiple Amazon EC2 instances running behind an Elastic Load Balancer with an Auto Scaling group having the desired capacity of 5 EC2 instances. You would like to integrate AWS CodeDeploy for automating application deployment. The deployment should re-route traffic from your application's original environment to the new environment.
    Which of the following options will meet your deployment criteria?**
    
    - **Opt for Immutable deployment(Incorrect)**
    - **Opt for Rolling deployment**
    - **Opt for Blue/Green deployment(Correct)**
    - **Opt for In-place deployment**
    
    ### **Explanation**
    
    Correct option:
    
    **Opt for Blue/Green deployment** - A Blue/Green deployment is used to update your applications while minimizing interruptions caused by the changes of a new application version. CodeDeploy provisions your new application version alongside the old version before rerouting your production traffic. 
    
    Incorrect options:
    
    **Opt for Immutable deployment** - This deployment type is present for AWS Elastic Beanstalk and not for EC2 instances directly.
    
- Q36 - important
    
    **The development team at a social media company is considering using Amazon ElastiCache to boost the performance of their existing databases.
    As a Developer Associate, which of the following use-cases would you recommend as the BEST fit for ElastiCache? (Select two)**
    
    - [x]  **Use ElastiCache to improve performance of Extract-Transform-Load (ETL) workloads(Incorrect)**
    - [ ]  **Use ElastiCache to improve performance of compute-intensive workloads(Correct)**
    - [x]  **Use ElastiCache to improve latency and throughput for read-heavy application workloads(Correct)**
    - [ ]  **Use ElastiCache to run highly complex JOIN queries**
    - [ ]  **Use ElastiCache to improve latency and throughput for write-heavy application workloads**
    
    ### **Explanation**
    
    Correct option:
    
    **Use ElastiCache to improve latency and throughput for read-heavy application workloads**
    
    **Use ElastiCache to improve performance of compute-intensive workloads**
    
    Amazon ElastiCache can be used to significantly improve latency and throughput for many read-heavy application workloads (such as social networking, gaming, media sharing, and Q&A portals) or compute-intensive workloads (such as a recommendation engine) by allowing you to store the objects that are often read in the cache.
    
    Incorrect options:
    
    **Use ElastiCache to improve latency and throughput for write-heavy application workloads** - As mentioned earlier in the explanation, Amazon ElastiCache can be used to significantly improve latency and throughput for many read-heavy application workloads. Caching is not a good fit for write-heavy applications as the cache goes stale at a very fast rate.
    
    **Use ElastiCache to improve performance of Extract-Transform-Load (ETL) workloads** - ETL workloads involve reading and transforming high volume data which is not a good fit for caching. You should use AWS Glue or Amazon EMR to facilitate ETL workloads.
    
    **Use ElastiCache to run highly complex JOIN queries** - Complex JSON queries can be run on relational databases such as RDS or Aurora. ElastiCache is not a good fit for this use-case.
    
- Q47 - important
    
    **A mobile gaming company is experiencing heavy read traffic to its Amazon Relational Database Service (RDS) database that retrieves player’s scores and stats. The company is using RDS database instance type db.m5.12xlarge, which is not cost-effective for their budget. They would like to implement a strategy to deal with the high volume of read traffic, reduce latency, and also downsize the instance size to cut costs.
    As a Developer, which of the following solutions do you recommend?**
    
    - **Setup ElastiCache in front of RDS(Correct)**
    - **Move to Amazon Redshift**
    - **Switch application code to AWS Lambda for better performance**
    - **Setup RDS Read Replicas(Incorrect)**
    
    ### **Explanation**
    
    Correct option:
    
    **Setup ElastiCache in front of RDS**
    
    Amazon ElastiCache is an ideal front-end for data stores such as Amazon RDS, providing a high-performance middle tier for applications with extremely high request rates and/or low latency requirements. The best part of caching is that it’s minimally invasive to implement and by doing so, your application performance regarding both scale and speed is dramatically improved.
    
    Incorrect options:
    
    **Setup RDS Read Replicas** - Adding read replicas would further add to the database costs and will not help in reducing latency when compared to a caching solution. So this option is ruled out.
    
- Q49
    
    **A multi-national enterprise uses AWS Organizations to manage its users across different divisions. Even though CloudTrail is enabled on the member accounts, managers have noticed that access issues to CloudTrail logs across different divisions and AWS Regions is becoming a bottleneck in troubleshooting issues. They have decided to use the organization trail to keep things simple.
    What are the important points to remember when configuring an organization trail? (Select two)**
    
    - [x]  **Member accounts will be able to see the Organization trail, but cannot modify or delete it(Correct)**
    - [ ]  **By default, CloudTrail event log files are not encrypted**
    - [x]  **There is nothing called Organization Trail. The master account can, however, enable CloudTrail logging, to keep track of all activities across AWS accounts(Incorrect)**
    - [ ]  **By default, CloudTrail tracks only bucket-level actions. To track object-level actions, you need to enable Amazon S3 data events(Correct)**
    - [ ]  **Member accounts do not have access to organization trail, neither do they have access to the Amazon S3 bucket that logs the files**
    
    ### **Explanation**
    
    Correct option:
    
    If you have created an organization in AWS Organizations, you can also create a trail that will log all events for all AWS accounts in that organization. This is referred to as an organization trail.
    
    **By default, CloudTrail tracks only bucket-level actions. To track object-level actions, you need to enable Amazon S3 data events** - This is a correct statement. AWS CloudTrail supports Amazon S3 Data Events, apart from bucket Events. You can record all API actions on S3 Objects and receive detailed information such as the AWS account of the caller, IAM user role of the caller, time of the API call, IP address of the API, and other details. All events are delivered to an S3 bucket and CloudWatch Events, allowing you to take programmatic actions on the events.
    
    **Member accounts will be able to see the organization trail, but cannot modify or delete it** - Organization trails must be created in the master account, and when specified as applying to an organization, are automatically applied to all member accounts in the organization. Member accounts will be able to see the organization trail, but cannot modify or delete it. By default, member accounts will not have access to the log files for the organization trail in the Amazon S3 bucket.
    
- Q51 - info
    
    **A developer is configuring an Amazon API Gateway as a front door to expose backend business logic. To keep the solution cost-effective, the developer has opted for HTTP APIs.
    Which of the following services are not available as an HTTP API via Amazon API Gateway?**
    
    - **Amazon Cognito(Incorrect)**
    - **AWS Lambda**
    - **AWS Web Application Firewall (AWS WAF)(Correct)**
    - **AWS Identity and Access Management (IAM)**
- Q62
    
    **A development team has created a new IAM user that has `s3:putObject` permission to write to an S3 bucket. This S3 bucket uses server-side encryption with AWS KMS managed keys (SSE-KMS) as the default encryption. Using the access key ID and the secret access key of the IAM user, the application received an access denied error when calling the `PutObject` API.
    As a Developer Associate, how would you resolve this issue?**
    
    - **Correct the ACL of the S3 bucket to allow the IAM user to upload encrypted objects**
    - **Correct the bucket policy of the S3 bucket to allow the IAM user to upload encrypted objects**
    - **Correct the policy of the IAM user to allow the `kms:GenerateDataKey` action(Correct)**
    - **Correct the policy of the IAM user to allow the `s3:Encrypt` action(Incorrect)**
- Q65 - important
    
    **A telecom service provider stores its critical customer data on Amazon Simple Storage Service (Amazon S3).
    Which of the following options can be used to control access to data stored on Amazon S3? (Select two)**
    
    - [ ]  **Query String Authentication, Permissions boundaries**
    - [x]  **Permissions boundaries, Identity and Access Management (IAM) policies(Incorrect)**
    - [x]  **Bucket policies, Identity and Access Management (IAM) policies(Correct)**
    - [ ]  **Query String Authentication, Access Control Lists (ACLs)(Correct)**
    - [ ]  **IAM database authentication, Bucket policies**
    
    ### **Explanation**
    
    Correct options:
    
    **Bucket policies, Identity and Access Management (IAM) policies**
    
    **Query String Authentication, Access Control Lists (ACLs)**
    
    Customers may use four mechanisms for controlling access to Amazon S3 resources: Identity and Access Management (IAM) policies, bucket policies, Access Control Lists (ACLs), and Query String Authentication.
    
    IAM enables organizations with multiple employees to create and manage multiple users under a single AWS account. With IAM policies, customers can grant IAM users fine-grained control to their Amazon S3 bucket or objects while also retaining full control over everything the users do.
    
    With bucket policies, customers can define rules which apply broadly across all requests to their Amazon S3 resources, such as granting write privileges to a subset of Amazon S3 resources. Customers can also restrict access based on an aspect of the request, such as HTTP referrer and IP address.
    
    With ACLs, customers can grant specific permissions (i.e. READ, WRITE, FULL_CONTROL) to specific users for an individual bucket or object.
    
    With Query String Authentication, customers can create a URL to an Amazon S3 object which is only valid for a limited time. Using query parameters to authenticate requests is useful when you want to express a request entirely in a URL. This method is also referred as presigning a URL.
    

## Doubtful

- Q11
    
    **A telecommunications company that provides internet service for mobile device users maintains over 100 c4.large instances in the us-east-1 region. The EC2 instances run complex algorithms. The manager would like to track CPU utilization of the EC2 instances as frequently as every 10 seconds.
    Which of the following represents the BEST solution for the given use-case?**
    
    - **Open a support ticket with AWS**
    - **Create a high-resolution custom metric and push the data using a script triggered every 10 seconds(Correct)**
    - **Enable EC2 detailed monitoring**
    - **Simply get it from the CloudWatch Metrics**
- Q20
    
    **To meet compliance guidelines, a company needs to ensure replication of any data stored in its S3 buckets.
    Which of the following characteristics are correct while configuring an S3 bucket for replication? (Select two)**
    
    - [ ]  **Replicated objects do not retain metadata**
    - [ ]  **Once replication is enabled on a bucket, all old and new objects will be replicated**
    - [x]  **S3 lifecycle actions are not replicated with S3 replication(Correct)**
    - [x]  **Same-Region Replication (SRR) and Cross-Region Replication (CRR) can be configured at the S3 bucket level, a shared prefix level, or an object level using S3 object tags(Correct)**
    - [ ]  **Object tags cannot be replicated across AWS Regions using Cross-Region Replication**
- Q21
    
    **As part of employee skills upgrade, the developers of your team have been delegated few responsibilities of DevOps engineers. Developers now have full control over modeling the entire software delivery process, from coding to deployment. As the team lead, you are now responsible for any manual approvals needed in the process.
    Which of the following approaches supports the given workflow?**
    
    - **Create deeply integrated AWS CodePipelines for each environment**
    - **Use CodePipeline with Amazon Virtual Private Cloud**
    - **Create one CodePipeline for your entire flow and add a manual approval step(Correct)**
    - **Create multiple CodePipelines for each environment and link them using AWS Lambda**
- Q24 - important
    
    **An organization is moving its on-premises resources to the cloud. Source code will be moved to AWS CodeCommit and AWS CodeBuild will be used for compiling the source code using Apache Maven as a build tool. The organization wants the build environment should allow for scaling and running builds in parallel.
    Which of the following options should the organization choose for their requirement?**
    
    - **Run CodeBuild in an Auto Scaling group**
    - **CodeBuild scales automatically, the organization does not have to do anything for scaling or for parallel builds(Correct)**
    - **Choose a high-performance instance type for your CodeBuild instances**
    - **Enable CodeBuild Auto Scaling**
- Q29 - important
    
    **A development team has deployed a REST API in Amazon API Gateway to two different stages - a test stage and a prod stage. The test stage is used as a test build and the prod stage as a stable build. After the updates have passed the test, the team wishes to promote the test stage to the prod stage.
    Which of the following represents the optimal solution for this use-case?**
    
    - **API performance is optimized in a different way for prod environments. Hence, promoting test to prod is not correct. The promotion should be done by redeploying the API to the prod stage**
    - **Deploy the API without choosing a stage. This way, the working deployment will be updated in all stages**
    - **Delete the existing prod stage. Create a new stage with the same name (prod) and deploy the tested version on this stage**
    - **Update stage variable value from the stage name of test to that of prod(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    **Update stage variable value from the stage name of test to that of prod**
    
    After creating your API, you must deploy it to make it callable by your users. To deploy an API, you create an API deployment and associate it with a stage. A stage is a logical reference to a lifecycle state of your API (for example, dev, prod, beta, v2). API stages are identified by the API ID and stage name. They're included in the URL that you use to invoke the API. Each stage is a named reference to a deployment of the API and is made available for client applications to call.
    
    Stages enable robust version control of your API. In our current use-case, after the updates pass the test, you can promote the test stage to the prod stage. The promotion can be done by redeploying the API to the prod stage or updating a stage variable value from the stage name of test to that of prod.
    
    Incorrect options:
    
    **Deploy the API without choosing a stage. This way, the working deployment will be updated in all stages** - An API can only be deployed to a stage. Hence, it is not possible to deploy an API without choosing a stage.
    
    *Delete the existing prod stage. Create a new stage with the same name (prod) and deploy the tested version on this stage** - This is possible, but not an optimal way of deploying a change. Also, as prod refers to real production system, this option will result in downtime.
    
    **API performance is optimized in a different way for prod environments. Hence, promoting test to prod is not correct. The promotion should be done by redeploying the API to the prod stage** - For each stage, you can optimize API performance by adjusting the default account-level request throttling limits and enabling API caching. And these settings can be changed/updated at any time.
    
- Q38
    
    **You have been asked by your Team Lead to enable detailed monitoring of the Amazon EC2 instances your team uses. As a Developer working on AWS CLI, which of the below command will you run?**
    
    - **aws ec2 run-instances --image-id ami-09092360 --monitoring Enabled=true**
    - **aws ec2 monitor-instances --instance-id i-1234567890abcdef0**
    - **aws ec2 run-instances --image-id ami-09092360 --monitoring State=enabled**
    - **aws ec2 monitor-instances --instance-ids i-1234567890abcdef0(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    **`aws ec2 monitor-instances --instance-ids i-1234567890abcdef0`** - This enables detailed monitoring for a running instance.
    
- Q45 - important
    
    **A large firm stores its static data assets on Amazon S3 buckets. Each service line of the firm has its own AWS account. For a business use case, the Finance department needs to give access to their S3 bucket's data to the Human Resources department.
    Which of the below options is NOT feasible for cross-account access of S3 bucket objects?**
    
    - **Use Resource-based policies and AWS Identity and Access Management (IAM) policies for programmatic-only access to S3 bucket objects**
    - **Use IAM roles and resource-based policies delegate access across accounts within different partitions via programmatic access only(Correct)**
    - **Use Cross-account IAM roles for programmatic and console access to S3 bucket objects**
    - **Use Access Control List (ACL) and IAM policies for programmatic-only access to S3 bucket objects**
    
    ### **Explanation**
    
    Correct option:
    
    **Use IAM roles and resource-based policies delegate access across accounts within different partitions via programmatic access only** - This statement is incorrect and hence the right choice for this question. IAM roles and resource-based policies delegate access across accounts only within a single partition. For example, assume that you have an account in US West (N. California) in the standard `aws` partition. You also have an account in China (Beijing) in the `aws-cn` partition. You can't use an Amazon S3 resource-based policy in your account in China (Beijing) to allow access for users in your standard AWS account.
    
    Incorrect options:
    
    **Use Resource-based policies and AWS Identity and Access Management (IAM) policies for programmatic-only access to S3 bucket objects** - Use bucket policies to manage cross-account control and audit the S3 object's permissions. If you apply a bucket policy at the bucket level, you can define who can access (Principal element), which objects they can access (Resource element), and how they can access (Action element). Applying a bucket policy at the bucket level allows you to define granular access to different objects inside the bucket by using multiple policies to control access. You can also review the bucket policy to see who can access objects in an S3 bucket.
    
    **Use Access Control List (ACL) and IAM policies for programmatic-only access to S3 bucket objects** - Use object ACLs to manage permissions only for specific scenarios and only if ACLs meet your needs better than IAM and S3 bucket policies. Amazon S3 ACLs allow users to define only the following permissions sets: READ, WRITE, READ_ACP, WRITE_ACP, and FULL_CONTROL. You can use only an AWS account or one of the predefined Amazon S3 groups as a grantee for the Amazon S3 ACL.
    
    **Use Cross-account IAM roles for programmatic and console access to S3 bucket objects** - Not all AWS services support resource-based policies. This means that you can use cross-account IAM roles to centralize permission management when providing cross-account access to multiple services. Using cross-account IAM roles simplifies provisioning cross-account access to S3 objects that are stored in multiple S3 buckets, removing the need to manage multiple policies for S3 buckets. This method allows cross-account access to objects that are owned or uploaded by another AWS account or AWS services. If you don't use cross-account IAM roles, the object ACL must be modified.