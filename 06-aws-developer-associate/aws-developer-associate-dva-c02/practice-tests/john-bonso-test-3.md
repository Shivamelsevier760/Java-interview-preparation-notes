# John Bonso Test 3

## Wrong

- Q21
    
    **A company has an AWS account with an ID of 061218980612 and has a centralized Java web application hosted in AWS Elastic Beanstalk that is used by different departments. The developer used the `iam create-account-alias --account-alias finance-dept` AWS CLI command to create a user-friendly identifier for the finance department.
    For faster troubleshooting, the application must also be configured to easily trace all its downstream requests, such as Apache HTTP requests, AWS SDK requests, and SQL queries made using a JDBC driver. The ability to send traces to multiple different tracing backends without having to re-instrument the application code is required as well.
    Which of the following options is the MOST suitable solution that the developer implements?**
    
    - **Use the `https://061218980612.aws.signin.amazon.com/console` sign-in page URL for the AWS account. Set up and configure the Amazon CloudWatch Evidently to trace all the downstream API calls.**
    - **Use the `https://finance-dept.aws.signin.amazon.com/console` sign-in page URL for the AWS account. Set up and configure an IAM Roles Anywhere trust model in Elastic Beanstalk with a proper source identity prefix to trace all the downstream API calls.**
    - **Use the `https://finance-dept.signin.aws.amazon.com/console` sign-in page URL for the AWS account. Install the AWS Distro for OpenTelemetry Collector and set up the AWS Distro for OpenTelemetry to trace all the downstream API calls.(Correct)**
    - **Use the `https://finance-dept.aws.amazon.com/console` sign-in page URL for the AWS account. Install and configure the AWS X-Ray auto-instrumentation Java agent to trace all the downstream API calls.(Incorrect)**
    
    ### **Explanation**
    
    The SDKs included with X-Ray are part of a tightly integrated instrumentation solution offered by AWS. The AWS Distro for OpenTelemetry is part of a broader industry solution in which X-Ray is only one of many tracing solutions. You can implement end-to-end tracing in X-Ray using either approach, but it’s important to understand the differences in order to determine the most useful approach for you.
    
    It is recommended to instrument your application with the AWS Distro for OpenTelemetry if you need the following:
    
    - The ability to send traces to multiple different tracing backends without having to re-instrument your code
    - Support for a large number of library instrumentations for each language, maintained by the OpenTelemetry community
    - Fully managed Lambda layers that package everything you need to collect telemetry data without requiring code changes when using Java, Python, or Node.js
    
    ![](https://media.tutorialsdojo.com/aws-open-telemetry.png)
    
    Conversely, it is recommended to choose an X-Ray SDK for instrumenting your application if you need the following:
    
    - A tightly integrated single-vendor solution
    - Integration with X-Ray centralized sampling rules, including the ability to configure sampling rules from the X-Ray console and automatically use them across multiple hosts, when using Node.js, Python, Ruby, or .NET
    
    An account alias substitutes for an account ID in the web address for your account. You can create and manage an account alias from the AWS Management Console, AWS CLI, or AWS API. Your sign-in page URL has the following format by default:
    
    [`https://Your_AWS_Account_ID.signin.aws.amazon.com/console/`](https://your_aws_account_id.signin.aws.amazon.com/console/)
    
    If you create an AWS account alias for your AWS account ID, your sign-in page URL looks like the following example.
    
    [`https://Your_Alias.signin.aws.amazon.com/console/`](https://your_alias.signin.aws.amazon.com/console/)
    
    The original URL containing your AWS account ID remains active and can be used after you create your AWS account alias. For example, the following `create-account-alias` command creates the alias **tutorialsdojo** for your AWS account:
    
    `aws iam create-account-alias --account-alias tutorialsdojo`
    
    The option that says: **Use the `https://finance-dept.aws.amazon.com/console` sign-in page URL for the AWS account. Install and configure the AWS X-Ray auto-instrumentation Java agent to trace all the downstream API calls** is incorrect. Although it is right that the AWS X-Ray auto-instrumentation agent for Java is capable of providing a tracing solution that instruments your Java web applications with minimal development effort, it still doesn't have the ability to send traces to multiple different tracing backends without having to re-instrument the application. A more suitable option is to set up the AWS Distro for OpenTelemetry.
    
- Q31
    
    **A developer wants to deploy a REST API using the CloudFormation template shown below:
    Which changes should be done so that the newly created API endpoint can be referenced to other stacks?**
    
    ![](https://img-b.udemycdn.com/redactor/raw/quiz_question/2022-02-07_04-01-07-ee9ab0f628a42f8a1777907c3fbe4edd.jpg)
    
    - **Add the `AWS::Include` transform in the original template to directly import the `HelloWorldFunction` resource to other templates.**
    - **Specify `HelloWorldApi`as parameter when using the `Fn::ImportValue` function in other templates.(Incorrect)**
    - **Include the `Export` property in the original template's `Outputs` section. Then use the `Ref` function in other templates to retrieve the exported value.**
    - **Include the `Export` property in the original template's `Outputs` section. Then use the `Fn::ImportValue` function in other templates to retrieve the exported value.(Correct)**
    
    ### **Explanation**
    
    To share information between stacks, export a stack's output values. Other stacks that are in the same AWS account and region can import the exported values. 
    
    In this scenario, we can expose the API endpoint to other stacks by adding the Export property in the Outputs section. In the example below, we use `SimpleAPI` as the name of the value to be exported:
    
    ![](https://media.tutorialsdojo.com/cda-sample-cf-template-2.JPG)
    
    To reference the endpoint's value in other templates, simply use the `Fn::ImportValue` function and specify `SimpleAPI` as its parameter.
    
- Q32
    
    **An application is hosted in an On-Demand Linux EC2 instance which uses an RDS database. There have been a lot of complaints that the application often crashes, but the support team can't pinpoint the problem using CloudWatch. To properly troubleshoot the issue, the team wants to monitor the memory and swap usage of the instance and the number of idle and running processes as well.
    Which of the following is the MOST suitable solution to use in this scenario?**
    
    - **Use AWS Cloud9 to consolidate all metrics in a single dashboard.**
    - **Install the AWS X-Ray daemon on the EC2 instance.**
    - **Use detailed monitoring in CloudWatch.(Incorrect)**
    - **Install the Amazon CloudWatch Logs agent to the EC2 instance.(Correct)**
    
    ### **Explanation**
    
    You can use the CloudWatch agent to collect both system metrics and log files from Amazon EC2 instances and on-premises servers. The agent supports both Windows Server and Linux, and enables you to select the metrics to be collected, including sub-resource metrics such as per-CPU core. Aside from the usual metrics, it also tracks the memory, swap, and disk space utilization metrics of your server.
    
    Hence, the most suitable solution to use in this scenario is to: ****Install the Amazon CloudWatch Logs agent to the EC2 instance**.
    
    The option that says: **Using detailed monitoring in CloudWatch** is incorrect because this will just send metric data of the EC2 instance to CloudWatch in 1-minute periods instead of 5-minute intervals.
    
- Q33
    
    **A company has a static website running in an Auto Scaling group of EC2 instances which they want to convert as a dynamic e-commerce web portal. One of the requirements is to use HTTPS to improve the security of their portal and also improve their search ranking as a reputable and secure site. A developer recently requested an SSL/TLS certificate from a third-party certificate authority (CA) which is ready to be imported to AWS.
    Which of the following services can the developer use to safely import the SSL/TLS certificate? (Select TWO.)**
    
    - [ ]  **IAM certificate store(Correct)**
    - [ ]  **A private S3 bucket with versioning enabled**
    - [x]  **AWS Certificate Manager(Correct)**
    - [x]  **CloudFront(Incorrect)**
    - [ ]  **Amazon Cognito**
    
    ### **Explanation**
    
    To enable HTTPS connections to your website or application in AWS, you need an **SSL/TLS *server certificate***. For certificates in a Region supported by AWS Certificate Manager (ACM), it is recommended that you use ACM to provision, manage, and deploy your server certificates. In unsupported Regions, you must use IAM as a certificate manager.
    
    ACM is the preferred tool to provision, manage, and deploy your server certificates. With ACM you can request a certificate or deploy an existing ACM or external certificate to AWS resources. Certificates provided by ACM are free and automatically renew. In a supported Region, you can use ACM to manage server certificates from the console or programmatically
    
    Use IAM as a certificate manager only when you must support HTTPS connections in a Region that is not supported by ACM. IAM securely encrypts your private keys and stores the encrypted version in IAM SSL certificate storage. IAM supports deploying server certificates in all Regions, but you must obtain your certificate from an external provider for use with AWS. You cannot upload an ACM certificate to IAM. Additionally, you cannot manage your certificates from the IAM Console.
    
    If you got your certificate from a third-party CA, import the certificate into ACM or upload it to the IAM certificate store. Hence, the correct answers are **AWS Certificate Manager (ACM)** and **IAM certificate store.**
    
- Q39
    
    **An EBS-backed EC2 instance has been recently reported to contain a malware that could spread to your other instances. To fix this security vulnerability, you will need to attach its root EBS volume to a new EC2 instance which hosts a security program that can scan viruses, worms, Trojan horses, or spyware.
    What steps would you take to detach the root volume from the compromised EC2 instance?**
    
    - **Detach the volume from the AWS Console. AWS takes care of unmounting the volume for you.**
    - **Stop the instance then detach the volume.(Correct)**
    - **Unmount the volume from the OS and then detach.(Incorrect)**
    - **Unmount the volume, stop the instance, and then detach.**
    
    ### **Explanation**
    
    You can detach an Amazon EBS volume from an instance explicitly or by terminating the instance. However, if the instance is running, you must first unmount the volume from the instance.
    
    If an EBS volume is the root device of an instance, you must **stop the instance before you can detach the volume.**
    
    The options that say **unmount the volume from the OS and then detach** and **unmount the volume, stop the instance, and then detach** are both incorrect because you can’t unmount the root volume on a running instance.
    
- Q40 - important (confused)
    
    **You are using an AWS Lambda function to process records in an Amazon Kinesis Data Streams stream which has 100 active shards. The Lambda function takes an average of 10 seconds to process the data and the stream is receiving 50 new items per second.
    Which of the following statements are TRUE regarding this scenario?**
    
    - **There will be at most 100 Lambda function invocations running concurrently.(Correct)**
    - **The Lambda function will throttle the incoming requests due to the excessive number of Kinesis shards.**
    - **The Lambda function has 500 concurrent executions.(Incorrect)**
    - **The Kinesis shards must be merged to increase the data capacity of the stream as well as the concurrency execution of the Lambda function.**
    
    ### **Explanation**
    
    You can use an **AWS Lambda function** to process records in an Amazon Kinesis data stream. With Kinesis, you can collect data from many sources and process them with multiple consumers. Lambda supports standard data stream iterators and HTTP/2 stream consumers. Lambda reads records from the data stream and invokes your function synchronously with an event that contains stream records. Lambda reads records in batches and invokes your function to process records from the batch.
    
    ![](https://d1.awsstatic.com/Products/product-name/diagrams/product-page-diagram_Amazon-Kinesis-Data-Streams.074de94302fd60948e1ad070e425eeda73d350e7.png)
    
    ***Concurrent executions*** refers to the number of executions of your function code that are happening at any given time. You can estimate the concurrent execution count, but the it will differ depending on whether or not your Lambda function is processing events from a poll-based event source.
    
    For Lambda functions that process Kinesis or DynamoDB streams, the number of shards is the unit of concurrency. If your stream has 100 active shards, there will be at most 100 Lambda function invocations running concurrently. This is because Lambda processes each shard’s events in sequence.
    
    Hence, the correct answer in this scenario is that: **there will be at most 100 Lambda function invocations running concurrently.**
    
    The option that says: **the Lambda function has 500 concurrent executions** is incorrect because the number of concurrent executions for poll-based event sources is different from push-based event sources. This number of concurrent executions would have been correct if the Lambda function is integrated with a push-based even source such as API Gateway or Amazon S3 Events. Remember that the Kinesis and Lambda integration is using a poll-based event source, which means that the number of shards is the unit of concurrency for the function.
    
- Q48 - important
    
    **A developer runs a shell script that uses the AWS CLI to upload a large file to an S3 bucket, which includes an AWS KMS key. An `Access Denied` error always shows up whenever the developer uploads a file with a size of 100 GB or more. However, when he tried to upload a smaller file with the KMS key, the upload succeeds.
    Which of the following are possible reasons why this issue is happening? (Select TWO.)**
    
    - [ ]  **The AWS CLI S3 commands perform a multipart upload when the file is large.(Correct)**
    - [ ]  **The developer does not have the `kms:Decrypt` permission.(Correct)**
    - [x]  **The maximum size that can be encrypted in KMS is only 100 GB.(Incorrect)**
    - [x]  **The developer's IAM permission has an attached inline policy that restricts him from uploading a file to S3 with a size of 100 GB or more.(Incorrect)**
    - [ ]  **The developer does not have the `kms:Encrypt` permission.**
    
    ### **Explanation**
    
    If you are getting an **`Access Denied`** error when trying to upload a large file to your S3 bucket with an upload request that includes an AWS KMS key then you have to confirm that you have the permission to perform `kms:Decrypt` actions on the AWS KMS key that you're using to encrypt the object.
    
    To perform a multipart upload with encryption using a KMS customer master key (CMK), the requester must have permission to the **`kms:Decrypt`** and **`kms:GenerateDataKey*`** actions on the key. These permissions are required because Amazon S3 must decrypt and read data from the encrypted file parts before it completes the multipart upload.
    
    Hence, the correct answers in this scenario are:
    
    - **The AWS CLI S3 commands perform a multipart upload when the file is large.**
    - **The developer does not have the `kms:Decrypt` permission**
    
    The option that says: **the developer does not have the `kms:Encrypt` permission** is incorrect because the operation is successful if the developer uploads a smaller file.
    
    The option that says: **the maximum size that can be encrypted in KMS is only 100 GB** is incorrect because there is no such limitation in KMS.
    
- Q49
    
    **A software engineer is developing a serverless application which will use a DynamoDB database. One of the requirements is that each write request should return the total number of write capacity units consumed, with subtotals for the table and any secondary indexes that were affected by the operation.
    What should be done to accomplish this feature?**
    
    - **Add the `ReturnConsumedCapacity` parameter with a value of `INDEXES` in every write request.(Correct)**
    - **Add the `ReturnValues` parameter with a value of `INDEXES` in every write request.**
    - **Add the `ReturnConsumedCapacity` parameter with a value of `TOTAL` in every write request.(Incorrect)**
    - **Add the `ReturnValues` parameter with a value of `TOTAL` in every write request.**
    
    ### **Explanation**
    
    To return the number of write capacity units consumed by any of these operations, set the `ReturnConsumedCapacity` parameter to one of the following:
    
    **`TOTAL**` — returns the total number of write capacity units consumed.
    
    **`INDEXES**` — returns the total number of write capacity units consumed, with subtotals for the table and any secondary indexes that were affected by the operation.
    
    **`NONE**` — no write capacity details are returned. (This is the default.)
    
- Q50
    
    **A developer is designing an application which will be hosted in ECS and uses an EC2 launch type. You need to group your container instances by certain attributes such as Availability Zone, instance type, or custom metadata. After you have defined a group of container instances, you will need to customize Amazon ECS to place tasks on container instances based on the group you specified.
    Which of the following ECS features provides you with expressions that you can use to group container instances by a specific attribute?**
    
    - **Cluster Query Language(Correct)**
    - **Task Placement Strategies**
    - **Task Placement Constraints(Incorrect)**
    - **Task Groups**
    
- Q56
    
    **Both the read and write operations to your DynamoDB table are throttled, which are causing errors in your application. You checked the CloudWatch metrics but they indicate that the consumed capacity units haven't exceeded the provisioned capacity units. Upon further investigation, you found that the issue is caused by a "hot partition" in your table in which a certain partition is accessed by your downstream applications much more frequently than other partitions.
    What should you do to resolve this issue in your application with MINIMAL cost? (Select TWO.)**
    
    - [ ]  **Increase the amount of read or write capacity for your table.**
    - [ ]  **Refactor your application to distribute your read and write operations as evenly as possible across your table.(Correct)**
    - [ ]  **Use DynamoDB Accelerator (DAX).**
    - [x]  **Implement read sharding to distribute workloads evenly.(Incorrect)**
    - [x]  **Implement error retries and exponential backoff.(Correct)**
    
    ### **Explanation**
    
    Partitions are usually throttled when they are accessed by your downstream applications much more frequently than other partitions (that is, a "hot" partition), or when workloads rely on short periods of time with high usage (a "burst" of read or write activity). To avoid hot partitions and throttling, you must optimize your table and partition structure.
    
    DynamoDB adaptive capacity automatically boosts throughput capacity to high-traffic partitions. However, each partition is still subject to the hard limit. This means that adaptive capacity can't solve larger issues with your table or partition design. To avoid hot partitions and throttling, optimize your table and partition structure.
    
- Q59
    
    **A medical technology company has a system hosted in AWS that manages their patients' high-resolution imaging records such as MRI, PET Positron Emission Tomography, CAT scan, and many others. For their archiving process, the records that are one year older are encrypted before they are archived to AWS Glacier. A doctor has a non-urgent request for a patient’s medical record from 2 years ago, which should be made available within 5 hours.
    Which of the following is the MOST cost-effective retrieval option to use in this scenario?**
    
    - **Ranged Archive Retrievals**
    - **Bulk Retrieval**
    - **Expedited Retrieval(Incorrect)**
    - **Standard Retrieval(Correct)**
    
    ### **Explanation**
    
    There are three options for retrieving data with varying access times and cost:
    
    - **Expedited retrievals** allow you to quickly access your data when occasional urgent requests for a subset of archives are required. Expedited retrievals are typically made available within 1–5 minutes.
    - **Standard retrievals** allow you to access any of your archives within several hours. Standard retrievals typically complete within 3–5 hours. This is the default option.
    - **Bulk retrievals** are Glacier’s lowest-cost retrieval option, which you can use to retrieve large amounts, even petabytes, of data inexpensively in a day. Bulk retrievals typically complete within 5–12 hours.

## Doubtful

- Q4
    
    **You were recently hired as a developer for a leading insurance firm in Asia which has a hybrid cloud architecture with AWS. The project that was assigned to you involves setting up a static website using Amazon S3 with a CORS configuration as shown below:
    
    `1. <?xml version="1.0" encoding="UTF-8"?>
    2. <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    3.  <CORSRule>
    4.   <AllowedOrigin>https://tutorialsdojo.com</AllowedOrigin>
    5.   <AllowedMethod>GET</AllowedMethod>
    6.   <AllowedMethod>PUT</AllowedMethod>
    7.   <AllowedMethod>POST</AllowedMethod>
    8.   <AllowedMethod>DELETE</AllowedMethod>
    9.   <AllowedHeader>*</AllowedHeader>
    10.   <ExposeHeader>ETag</ExposeHeader>
    11.   <ExposeHeader>x-amz-meta-custom-header</ExposeHeader>
    12.   <MaxAgeSeconds>3600</MaxAgeSeconds>
    13.  </CORSRule>
    14. </CORSConfiguration>`
    
    Which of the following statements are TRUE with regards to this S3 configuration? (Select TWO.)**
    
    - [x]  **This will cause the browser to cache the response of the preflight OPTIONS request for 1 hour.(Correct)**
    - [x]  **It allows a user to view, add, remove or update objects inside the S3 bucket from the domain tutorialsdojo.com.(Correct)**
    - [ ]  **All HTTP Methods are allowed.**
    - [ ]  **This configuration authorizes the user to perform actions on the S3 bucket.**
    - [ ]  **The request will fail if the `x-amz-meta-custom-header` header is not included.**
- Q11
    
    **A developer is designing a multitiered system which utilizes various AWS resources. The application will be hosted in Elastic Beanstalk, which uses an RDS database and an S3 bucket that is configured to use Server-Side Encryption with Customer-Provided Encryption Keys (SSE-C). In this configuration, Amazon S3 does not store the encryption key you provide but instead, stores a randomly salted hash-based message authentication code (HMAC) value of the encryption key in order to validate future requests.
    Which of the following is a valid consideration that the developer should keep in mind when implementing this architecture?**
    
    - **The salted HMAC value can be used to decrypt the contents of the encrypted object.**
    - **If you lose the encryption key, you lose the object.(Correct)**
    - **If you lose the encryption key, the salted HMAC value can be used to decrypt the object.**
    - **The salted HMAC value can be used to derive the value of the encryption key.**
    
    ### **Explanation**
    
    Server-side encryption is about protecting data at rest. Using server-side encryption with customer-provided encryption keys (SSE-C) allows you to set your own encryption keys. With the encryption key you provide as part of your request, Amazon S3 manages both the encryption, as it writes to disks, and decryption, when you access your objects. 
    
    When you upload an object, Amazon S3 uses the encryption key you provide to apply AES-256 encryption to your data and removes the encryption key from memory. It is important to note that Amazon S3 does not store the encryption key you provide. Instead, it is stored in a randomly salted HMAC value of the encryption key in order to validate future requests. The salted HMAC value cannot be used to derive the value of the encryption key or to decrypt the contents of the encrypted object. That means, **if you lose the encryption key, you lose the object.**
    
- Q12
    
    **A developer has recently released a new Lambda function which calculates accruals, interests, and other financial data. This function must have a streamlined integration setup with API Gateway. The requirement is to pass the incoming request from the client as the input to the backend Lambda function, via HTTPS, in the following format: 
    
    `1. {
    2.     "resource": "Resource path",
    3.     "path": "Path parameter",
    4.     "httpMethod": "Incoming request's method name"
    5.     "headers": {String containing incoming request headers}
    6.     "multiValueHeaders": {List of strings containing incoming request headers}
    7.     "queryStringParameters": {query string parameters }
    8.     "multiValueQueryStringParameters": {List of query string parameters}
    9.     "pathParameters":  {path parameters}
    10.     "stageVariables": {Applicable stage variables}
    11.     "requestContext": {Request context, including authorizer-returned key-value pairs}
    12.     "body": "A JSON string of the request payload."
    13.     "isBase64Encoded": "A boolean flag to indicate if the applicable request payload is Base64-encode"
    14. }`
    
    Which of the following options is the MOST appropriate method to use to meet this requirement?**
    
    - **Lambda proxy integration(Correct)**
    - **HTTP Proxy integration**
    - **HTTP custom integration**
    - **Lambda custom integration**
- Q37
    
    **The current application deployment process of a company is tedious and is prone to errors. They asked a developer to set up CodeDeploy as their deployment service, which can automate their application deployments on their hybrid cloud architecture.
    Which of the following deployment types does CodeDeploy support? (Select TWO.)**
    
    - [ ]  **Blue/green deployments to on-premises servers.**
    - [x]  **In-place deployments to on-premises servers(Correct)**
    - [x]  **Blue/green deployments to ECS.(Correct)**
    - [ ]  **Rolling deployments to ECS.**
    - [ ]  **In-place deployments to AWS Lambda.**
- Q41 - important
    
    **A developer will be building a game data feed application which will continuously collect data about player-game interactions and feed the data into your gaming platform. The application uses the Kinesis Client Library to process the data stream from the Amazon Kinesis Data Streams and stores the data to Amazon DynamoDB. It is required that the system should have enough shards and EC2 instances in order to handle failover and adequately process the amount of data coming in and out of the stream.
    Which of the following ratio of the number of Kinesis shards to EC2 worker instances should the developer implement to achieve the above requirement in the most cost-effective and highly available way?**
    
    - **6 shards : 1 instance**
    - **4 shards : 8 instances**
    - **4 shards : 2 instances(Correct)**
    - **1 shard : 6 instances**
    
    ### **Explanation**
    
    A stream is composed of one or more shards, each of which provides a fixed unit of capacity. The total capacity of the stream is the sum of the capacities of its shards. The Kinesis Client Library (KCL) ensures that for every shard there is a record processor running and processing that shard. It also tracks the shards in the stream using an Amazon DynamoDB table.
    
    ![](https://docs.aws.amazon.com/streams/latest/dev/images/enhanced_fan-out.png)
    
    Typically, when you use the KCL, you should ensure that the number of instances does not exceed the number of shards (except for failure standby purposes). Each shard is processed by exactly one KCL worker and has exactly one corresponding record processor, so you never need multiple instances to process one shard. However, one worker can process any number of shards, so it's fine if the number of shards exceeds the number of instances.
    
    Since the question requires the system to smoothly process streaming data, a fair number of shards and instances are required. By launching 4 shards, the stream will have more capacity for reading and writing data. By launching 2 instances, each instance will focus on processing two shards. It also provides high availability in the event that one instance goes down. Therefore, the ratio of ***4 shards : 2 instances*** is the correct answer.
    
    The ***1 shard : 6 instances*** ratio is incorrect because having just one shard for the stream will be insufficient and in the event that your incoming data rate increases, this single shard will not be able to handle the load.
    
    The ***6 shards : 1 instance*** ratio is incorrect because having just one instance to process multiple shards will be insufficient since the processing capacity of your system will be severely limited. You have to allocate more instances in proportion to the number of open shards in your data stream. Moreover, a single instance is not a highly available option since the application doesn't have a backup instance to process the shards in the event of an outage.
    
    The ***4 shards : 8 instances*** ratio is incorrect because launching more instances than the number of open shards will not improve the processing of the stream as it is only useful for failure standby purposes. Take note that each shard is processed by exactly one KCL worker and has exactly one corresponding record processor, so you never need multiple instances to process one shard. In addition, this option is not the most cost-effective choice as well.
    
- Q52 - important
    
    **You are developing a new batch job for the enterprise application suite in your company, which is hosted in an Auto Scaling group of EC2 instances behind an ELB. The application is using an S3 bucket configured with Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS). The batch job must upload files to the bucket using the default AWS KMS key to protect the data at rest.
    What should you do to satisfy this requirement with the LEAST amount of configuration?**
    
    - **Include the `x-amz-server-side-encryption` header with a value of `aws:kms` as well as the `x-amz-server-side-encryption-aws-kms-key-id` header containing the ID of the default AWS KMS key in your upload request.**
    - **Include the `x-amz-server-side-encryption-customer-algorithm`, `x-amz-server-side-encryption-customer-key`, and `x-amz-server-side-encryption-customer-key-MD5` headers with appropriate values in the upload request.**
    - **Include the `x-amz-server-side-encryption` header with a value of `AES256` in your upload request.**
    - **Include the `x-amz-server-side-encryption` header with a value of `aws:kms` in your upload request.(Correct)**
    
    ### **Explanation**
    
    To upload an object to the S3 bucket which uses SSE-KMS, you have to send a request with an `x-amz-server-side-encryption` header with the value of `aws:kms`. There's also an optional `x-amz-server-side-encryption-aws-kms-key-id` header which specifies the ID of the AWS KMS master encryption key that was used for the object. The Amazon S3 API also supports encryption context, with the `x-amz-server-side-encryption-context` header.
    
    When you upload an object, you can specify the KMS key using the `x-amz-server-side-encryption-aws-kms-key-id` header. If the header is not present in the request, Amazon S3 assumes the default KMS key.
    
- Q54 - important
    
    **A clickstream application uses Amazon Kinesis Data Stream for real-time processing. `PutRecord` API calls are being used by the producer to send data to the stream. However, there are cases where the producer intermittently restarted while doing the processing, which resulted in sending the same data twice to the stream. This inadvertently causes duplication of entries in the data stream, which affects the processing of the consumers.
    Which of the following should you implement to resolve this issue?**
    
    - **Split shards of the data stream.**
    - **Merge shards of the data stream.**
    - **Embed a primary key within the record.(Correct)**
    - **Add more shards.**