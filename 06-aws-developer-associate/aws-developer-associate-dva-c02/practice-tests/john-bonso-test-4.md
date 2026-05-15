# John Bonso Test 4

## Wrong

- Q7
    
    **You work for a software development company where the teams are divided into distinct projects. The management wants to have separation on their AWS resources, which will have a detailed report on the costs of each project.
    Which of the following options is the recommended way to implement this?**
    
    - **Create separate AWS accounts for each project and use consolidated billing.(Correct)**
    - **Tag resources by projects and use Detailed Billing Reports to show costing per tag.(Incorrect)**
    - **Tag resources by IAM group assigned for each project and use Detailed Billing reports to show costing.**
    - **Create separate AWS accounts for each project and generate Detailed Billing for each account.**
    
    ### **Explanation**
    
    The consolidated billing feature in AWS Organizations allows you to consolidate payment for multiple AWS accounts or multiple AISPL accounts. Each organization in AWS Organizations has a master account that pays the charges for all the member accounts. If you have access to the master account, you can see a combined view of the AWS charges that are incurred by the member accounts. You also can get a cost report for each member account. Hence the correct answer is to *create separate AWS accounts for each project and use consolidated billing*.
    
    The options that say *"tag resources by projects and use Detailed Billing Reports to show costing per tag"* and *"tag resources by IAM group assigned for each project and use Detailed Billing reports to show costing"* are both incorrect because although these are possible, you will have to manage the Tags for all AWS resources and you can’t achieve separation of resources of each project. In addition, AWS recommends using Cost and Usage Reports instead of using the Detailed Billing Reports.
    
- Q11
    
    **A developer is planning to add a global secondary index in a DynamoDB table. This will allow the application to query a specific index that can span all of the data in the base table, across all partitions.
    Which of the following should the developer consider when using this type of index? (Select TWO.)**
    
    - [ ]  **Queries or scans on this index consume read capacity units from the base table.**
    - [x]  **Queries or scans on this index consume capacity units from the index, not from the base table.(Correct)**
    - [ ]  **For each partition key value, the total size of all indexed items must be 10 GB or less.**
    - [ ]  **Queries on this index support eventual consistency only.(Correct)**
    - [x]  **When you query this index, you can choose either eventual consistency or strong consistency.(Incorrect)**
- Q16
    
    **You are configuring the task definitions of your ECS Cluster in AWS to make sure that the tasks are scheduled on instances with enough resources to run them. It should also follow the constraints that you specified both implicitly or explicitly.
    Which of the following options should you implement to satisfy the requirement which requires the LEAST amount of configuration?**
    
    - **Use a `random` task placement strategy.(Correct)**
    - **Use a `binpack` task placement strategy.**
    - **Use a `spread` task placement strategy with custom placement constraints.(Incorrect)**
    - **Use a `spread` task placement strategy which uses the `instanceId` and `host` attributes.**
    
    ### **Explanation**
    
    By default, tasks are randomly placed with RunTask or spread across Availability Zones with CreateService. Spread is typically used to achieve high availability by making sure that multiple copies of a task are scheduled across multiple instances based on attributes such as Availability Zones.
    
    A **task placement strategy** is an algorithm for selecting instances for task placement or tasks for termination. Task placement strategies can be specified when either running a task or creating a new service.
    
    The *Random* task placement strategy is fairly straightforward as it doesn’t require further parameters. The two other strategies, such as binpack and spread, take opposite actions. Binpack places tasks on as few instances as possible, helping to optimize resource utilization, while spread places tasks evenly across your cluster to help maximize availability. By default, ECS uses spread with the *ecs.availability-zone* attribute to place tasks.
    
    *Random* places tasks on instances at random yet still honors the other constraints that you specified, implicitly or explicitly. Specifically, it still makes sure that tasks are scheduled on instances with enough resources to run them.
    
- Q19
    
    **You are a developer for a global technology company, which heavily uses AWS with regional offices in San Francisco, Manila, and Bangalore. Most of the clients of your company are using serverless computing in which you are responsible for ensuring that their applications are working efficiently.
    Which of the following options are valid considerations in improving the performance of your Lambda function? (Select TWO.)**
    
    - [ ]  **The concurrent execution limit is enforced against the sum of the concurrent executions of all function.(Correct)**
    - [ ]  **You have to install the X-Ray daemon in Lambda to enable active tracing.**
    - [x]  **You can throttle all incoming executions and stop processing any invocations to your function by setting concurrency to `false`.(Incorrect)**
    - [ ]  **Lambda automatically creates Elastic IP's that enable your function to connect securely to other resources within your private VPC.**
    - [x]  **An increase in memory size triggers an equivalent increase in CPU available to your function.(Correct)**
    
- Q28 - confusing wording
    
    **A developer is managing an application hosted in EC2, which stores data in an S3 bucket. To comply with the new security policy, the developer must ensure that the data is encrypted at rest using an encryption key that is provided and managed by the company. The change should also provide AES-256 encryption to their data.
    Which of the following actions could the developer take to achieve this? (Select TWO.)**
    
    - [x]  **Use SSL to encrypt the data while in transit to Amazon S3.(Incorrect)**
    - [x]  **Implement Amazon S3 server-side encryption with customer-provided keys (SSE-C).(Correct)**
    - [ ]  **Encrypt the data on the client-side before sending to Amazon S3 using their own master key.(Correct)**
    - [ ]  **Implement Amazon S3 server-side encryption with AWS KMS-Managed Keys (SSE-KMS).**
    - [ ]  **Implement Amazon S3 server-side encryption with Amazon S3-Managed Encryption Keys.**
- Q36
    
    **A company has recently developed a containerized application that uses a multicontainer Docker platform which supports multiple containers per instance. They need a service that automatically handles tasks such as provisioning of the resources, load balancing, auto-scaling, monitoring, and placing the containers across the cluster.
    Which of the following services provides the EASIEST way to accomplish the above requirement?**
    
    - **ECS(Incorrect)**
    - **EKS**
    - **Lambda**
    - **Elastic Beanstalk(Correct)**
    
    ### **Explanation**
    
    **ECS** is incorrect. Although it can host Docker applications, it doesn't automatically handle all the details such as resource provisioning, balancing load, auto-scaling, monitoring, and placing your containers across your cluster, unlike Elastic Beanstalk. Take note that even though you can use Service Auto Scaling in ECS, you still have to enable and configure it. Elastic Beanstalk still provides the easiest way to accomplish the requirements.
    
- Q40
    
    **A company is currently in the process of integrating their on-premises data center to their cloud infrastructure in AWS. One of the requirements is to integrate the on-premises Lightweight Directory Access Protocol (LDAP) directory service to their AWS VPC using IAM.
    Which of the following provides the MOST suitable solution to implement if the identity store that they are using is not compatible with SAML?**
    
    - **Set up an IAM policy that references the LDAP identifiers and AWS credentials.(Incorrect)**
    - **Implement the AWS Single Sign-On (SSO) service to enable single sign-on between AWS and your LDAP.**
    - **Create IAM roles to rotate the IAM credentials whenever LDAP credentials are updated.**
    - **Create a custom identity broker application in your on-premises data center and use STS to issue short-lived AWS credentials.(Correct)**
    
    ### **Explanation**
    
    If your identity store is not compatible with SAML 2.0, then you can build a custom identity broker application to perform a similar function. The broker application authenticates users, requests temporary credentials for users from AWS, and then provides them to the user to access AWS resources.
    
    The application verifies that employees are signed into the existing corporate network's identity and authentication system, which might use LDAP, Active Directory, or another system. The identity broker application then obtains temporary security credentials for the employees.
    
    To get temporary security credentials, the identity broker application calls either **`AssumeRole`** or **`GetFederationToken`** to obtain temporary security credentials, depending on how you want to manage the policies for users and when the temporary credentials should expire. The call returns temporary security credentials consisting of an AWS access key ID, a secret access key, and a session token. The identity broker application makes these temporary security credentials available to the internal company application. The app can then use the temporary credentials to make calls to AWS directly. The app caches the credentials until they expire, and then requests a new set of temporary credentials.
    
    ![](https://docs.aws.amazon.com/IAM/latest/UserGuide/images/enterprise-authentication-with-identity-broker-application.diagram.png)
    
    Hence, the correct answer is to ***create a custom identity broker application in your on-premises data center and use STS to issue short-lived AWS credentials**.*
    
    ***Setting up an IAM policy that references the LDAP identifiers and AWS credentials*** is incorrect because using an IAM policy is not enough to integrate your LDAP service to IAM. You need to use SAML, STS or a custom identity broker instead.
    
- Q42
    
    **A web application is currently using an on-premises Microsoft SQL Server 2019 Enterprise Edition database. Your manager instructed you to migrate the application to Elastic Beanstalk and the database to RDS. For additional security, you must configure your database to automatically encrypt data before it is written to storage, and automatically decrypt data when the data is read from storage.
    Which of the following services will you use to achieve this?**
    
    - **Enable Transparent Data Encryption (TDE).(Correct)**
    - **Use IAM DB Authentication.**
    - **Enable RDS Encryption.(Incorrect)**
    - **Use Microsoft SQL Server Windows Authentication.**
    
    ### **Explanation**
    
    Amazon RDS supports using **Transparent Data Encryption (TDE)** to encrypt stored data on your DB instances running Microsoft SQL Server. TDE automatically encrypts data before it is written to storage, and automatically decrypts data when the data is read from storage.
    
    The option that says: **Enable RDS Encryption** **is incorrect because this simply encrypts your Amazon RDS DB instances and snapshots at rest. It doesn't automatically encrypt data before it is written to storage, nor automatically decrypt data when it is read from storage.
    
- Q50
    
    **A developer uses AWS X-Ray to create a trace on an instrumented web application to identify any performance bottlenecks. The segment documents being sent by the application contain annotations that the developer wants to utilize in order to identify and filter out specific data from the trace.
    Which of the following should the developer do in order to satisfy this requirement with minimal configuration? (Select TWO.)**
    
    - [ ]  **Use filter expressions via the X-Ray console.(Correct)**
    - [x]  **Fetch the trace IDs and annotations using the `GetTraceSummaries` API.(Correct)**
    - [ ]  **Send trace results to an S3 bucket then query the trace output using Amazon Athena.**
    - [ ]  **Configure Sampling Rules in the AWS X-Ray Console.**
    - [x]  **Fetch the data using the `BatchGetTraces` API.(Incorrect)**
    
    ### **Explanation**
    
    A subset of segment fields are indexed by X-Ray for use with filter expressions. You can search for segments associated with specific information in the X-Ray console or by using the `GetTraceSummaries` API.
    
    **Fetching the data using the `BatchGetTraces` API** is incorrect because this API simply retrieves a list of traces specified by ID. It does not support filter expressions nor returns the annotations.
    

## Doubtful

- Q14
    
    **A web application hosted in Elastic Beanstalk has a configuration file named `.ebextensions/debugging.config` which has the following content:
    
    `1. option_settings: 
    2.  aws:elasticbeanstalk:xray: 
    3.   XRayEnabled: true`
    
    For its database tier, it uses RDS with Multi-AZ deployments configuration and Read Replicas. There is a new requirement to record calls that your application makes to RDS and other internal or external HTTP web APIs. The tracing information should also include the actual SQL database queries sent by the application, which can be searched using the filter expressions in the X-Ray Console.
    Which of the following should you do to satisfy the above task?**
    
    - **Add metadata in the subsegment section of the segment document.**
    - **Add metadata in the segment document.**
    - **Add annotations in the subsegment section of the segment document.(Correct)**
    - **Add annotations in the segment document.**
    
    ### **Explanation**
    
    A trace segment is a JSON representation of a request that your application serves. A trace segment records information about the original request, information about the work that your application does locally, and subsegments with information about downstream calls that your application makes to AWS resources, HTTP APIs, and SQL databases.
    
    **Adding annotations in the segment document** is incorrect. Although the use of annotations is correct, you have to add this in the ***subsegment*** section of the *segment* document since you want to trace the downstream call to RDS and not the actual request to your application.
    
- Q21
    
    **The company that you are working for recently decided to migrate and transform their monolithic application on-premises to a Lambda application. It is your responsibility to ensure that application works effectively in AWS.
    Which of the following are the best practices in developing Lambda functions? (Select TWO.)**
    
    - [ ]  **Use recursive code.**
    - [ ]  **Include the core logic in the Lambda handler.**
    - [x]  **Take advantage of Execution Context reuse to improve the performance of your function.(Correct)**
    - [x]  **Use AWS Lambda Environment Variables to pass operational parameters to your function.(Correct)**
    - [ ]  **Use Amazon Inspector for troubleshooting.**
    
    ### **Explanation**
    
    Below are some of the best practices in working with AWS Lambda Functions:
    
    - Separate the Lambda handler (entry point) from your core logic.
    
    - Take advantage of Execution Context reuse to improve the performance of your function
    
    - Use AWS Lambda Environment Variables to pass operational parameters to your function.
    
    - Control the dependencies in your function's deployment package.
    
    - Minimize your deployment package size to its runtime necessities.
    
    - Reduce the time it takes Lambda to unpack deployment packages
    
    - Minimize the complexity of your dependencies
    
    - Avoid using recursive code
    
    Hence, the correct answers in this scenario are:
    
    - ***Take advantage of Execution Context reuse to improve the performance of your function***
    - ***Use AWS Lambda Environment Variables to pass operational parameters to your function***
    
    ***Using recursive code*** is incorrect because this is a situation wherein the function automatically calls itself until some arbitrary criteria is met. This could lead to an unintended volume of function invocations and escalated costs.
    
    ***Including the core logic in the Lambda handler*** is incorrect because you have to separate the Lambda handler (entry point) from your core logic instead.
    
    ***Using Amazon Inspector for troubleshooting*** is incorrect because this service is primarily used for EC2 and not for Lambda. You have to use X-Ray instead of troubleshooting your functions.
    
- Q34
    
    **You are working as an IT Consultant for a top investment bank in Europe which uses several serverless applications in their AWS account. They just launched a new API Gateway service with a Lambda proxy integration and you were instructed to test out the new API. However, you are getting a `Connection refused` error whenever you use this Invoke URL `http://779protaw8.execute-api.us-east-1.amazonaws.com/tutorialsdojo/` of the API Gateway.
    Which of the following is the MOST likely cause of this issue?**
    
    - **You are not using FTP in invoking the API.**
    - **You are not using HTTP/2 in invoking the API.**
    - **You are not using HTTPS in invoking the API.(Correct)**
    - **You are not using WebSocket in invoking the API.**
    
    ### **Explanation**
    
    All of the APIs created with Amazon API Gateway expose **HTTPS** endpoints only.
    
- Q39
    
    **A developer is building an AI-based traffic monitoring application using Lambda in AWS. Due to the complexity of the application, the developer must do certain modifications such as the way Lambda runs the function's setup code and how the invocation events are read from the Lambda runtime API.
    In this scenario, which feature of Lambda should you take advantage of to meet the above requirement?**
    
    - **Lambda@Edge**
    - **DLQ**
    - **Layers**
    - **Custom Runtime(Correct)**
- Q49
    
    **You have created an SWF workflow to coordinate the tasks of your media processing cluster, which processes the videos, and a separate media publishing cluster, which publishes the processed videos. Since the media processing cluster converts a single video multiple times, you need to record how many times a video is converted before another action is executed.
    Which of the following SWF options can be used to record such events?**
    
    - **Tags**
    - **Signals**
    - **Timers**
    - **Markers(Correct)**
    
    ### **Explanation**
    
    You can use ***markers*** to record events in the workflow execution history for application specific purposes. Markers are useful when you want to record custom information to help implement decider logic. For example, you could use a marker to count the number of loops in a recursive workflow.
    
- Q59
    
    **A company has an application hosted in an ECS Cluster that heavily uses an RDS database. A developer needs to closely monitor how the different processes on a DB instance use the CPU, such as the percentage of the CPU bandwidth or the total memory consumed by each process to ensure application performance.
    Which of the following is the MOST suitable solution that the developer should implement?**
    
    - **Develop a shell script that collects and publishes custom metrics to CloudWatch which tracks the real-time CPU Utilization of the RDS instance.**
    - **Track the `CPU%` and `MEM%` metrics which are readily available in the Amazon RDS console.**
    - **Use Enhanced Monitoring in RDS.(Correct)**
    - **Use CloudWatch to track the CPU Utilization of your database.**
    
    ### **Explanation**
    
    Amazon RDS provides metrics in real-time for the operating system (OS) that your DB instance runs on. You can view the metrics for your DB instance using the console or consume the Enhanced Monitoring JSON output from CloudWatch Logs in a monitoring system of your choice. By default, Enhanced Monitoring metrics are stored in the CloudWatch Logs for 30 days. To modify the amount of time the metrics are stored in the CloudWatch Logs, change the retention for the `RDSOSMetrics` log group in the CloudWatch console.
    
    ![](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/metrics2.png)
    
    Take note that there are certain differences between CloudWatch and Enhanced Monitoring Metrics. CloudWatch gathers metrics about CPU utilization from the hypervisor for a DB instance, and Enhanced Monitoring gathers its metrics from an agent on the instance. As a result, you might find differences between the measurements, because the hypervisor layer performs a small amount of work.
    
- Q60 - tricky
    
    **A startup has recently launched a high-quality photo sharing portal using Amazon Lightsail and S3. They noticed that there are other external websites which are linking and using their photos without permission. This has caused an increase on their data transfer cost and potential revenue loss.
    Which of the following is the MOST effective method to solve this issue?**
    
    - **Configure the S3 bucket to remove public read access and use pre-signed URLs with expiry dates.(Correct)**
    - **Use a CloudFront web distribution to serve the photos.**
    - **Block the IP addresses of the offending websites using Network Access Control List.**
    - **Enable cross-origin resource sharing (CORS) which allows cross-origin GET requests from all origins.**
- Q63 - important
    
    **An aerospace engineering company has recently migrated to AWS for their cloud architecture. They are using CloudFormation and AWS SAM as deployment services for both of their monolithic and serverless applications. There is a new requirement where you have to dynamically install packages, create files, and start services on your EC2 instances upon the deployment of the application stack using CloudFormation.
    Which of the following helper scripts should you use in this scenario?**
    
    - **cfn-init(Correct)**
    - **cfn-get-metadata**
    - **cfn-signal**
    - **cfn-hup**
    
    ### **Explanation**
    
    **AWS CloudFormation** provides the following Python helper scripts that you can use to install software and start services on an Amazon EC2 instance that you create as part of your stack:
    
    [cfn-init](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-init.html): Use to retrieve and interpret resource metadata, install packages, create files, and start services.
    
    [cfn-signal](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-signal.html): Use to signal with a CreationPolicy or WaitCondition, so you can synchronize other resources in the stack when the prerequisite resource or application is ready.
    
    [cfn-get-metadata](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-get-metadata.html): Use to retrieve metadata for a resource or path to a specific key.
    
    [cfn-hup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-hup.html): Use to check for updates to metadata and execute custom hooks when changes are detected.