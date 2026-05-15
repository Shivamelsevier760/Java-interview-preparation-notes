# John Bonso Test 2

## Wrong

- Q4
    
    **A developer has instrumented an application using the X-Ray SDK to collect all data about the requests that an application serves. There is a new requirement to develop a custom debug tool which will enable them to view the full traces of their application without using the X-Ray console.
    What should the developer do to accomplish this task?**
    
    - **Use the `GetGroup` API to get the list of trace IDs of the application and then retrieve the list of traces using `BatchGetTraces` API.(Incorrect)**
    - **Use the `BatchGetTraces` API to get the list of trace IDs of the application and then retrieve the list of traces using `GetTraceSummaries` API.**
    - **Use the `GetTraceSummaries` API to get the list of trace IDs of the application and then retrieve the list of traces using `BatchGetTraces` API.(Correct)**
    - **Use the `GetServiceGraph` API to get the list of trace IDs of the application and then retrieve the list of traces using `GetTraceSummaries` API.**
    
    ### **Explanation**
    
    X-Ray compiles and processes segment documents to generate queryable **trace summaries** and **full traces** that you can access by using the [`GetTraceSummaries`](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html) and [`BatchGetTraces`](https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html) APIs, respectively. In addition to the segments and subsegments that you send to X-Ray, the service uses information in subsegments to generate **inferred segments** and adds them to the full trace. Inferred segments represent downstream services and resources in the service map.
    
    ![](https://docs.aws.amazon.com/xray/latest/devguide/images/scorekeep-timeline-POSTmove.png)
    
    In this scenario, the developer should **use the `GetTraceSummaries` API to get the list of trace IDs of the application and then retrieve the list of traces using `BatchGetTraces` API** in order to develop the custom debug tool
    
    The option that says: **Use the `GetGroup` API to get the list of trace IDs of the application and then retrieving the list of traces using `BatchGetTraces` API** is incorrect because the `GetGroup` API just retrieves the group resource details.
    
    The option that says: **Use the `GetServiceGraph` API to get the list of trace IDs of the application and then retrieving the list of traces using `GetTraceSummaries` API** is incorrect because the `GetServiceGraph` API just shows which services process the incoming requests, including the downstream services that they call as a result. In addition, you have to use the `*BatchGetTraces*` API instead of the `*GetTraceSummaries*` API to retrieve the list of traces.
    
- Q6
    
    **A company has a global multi-player game with a multi-master DynamoDB database topology which stores data in multiple AWS regions. You were assigned to develop a real-time data analytics application which will track and store the recent changes on all the tables from various regions. Only the new data of the recently updated item is needed to be tracked by your application.
    Which of the following is the MOST suitable way to configure the data analytics application to detect and retrieve the updated database entries automatically?**
    
    - **Enable DynamoDB Streams and set the value of `StreamViewType` to NEW_AND_OLD_IMAGE. Create a trigger in AWS Lambda to capture stream data and forward it to your application.**
    - **Enable DynamoDB Streams and set the value of `StreamViewType` to NEW_AND_OLD_IMAGE. Use Kinesis Adapter in the application to consume streams from DynamoDB.**
    - **Enable DynamoDB Streams and set the value of `StreamViewType` to NEW_IMAGE. Create a trigger in AWS Lambda to capture stream data and forward it to your application.(Incorrect)**
    - **Enable DynamoDB Streams and set the value of `StreamViewType` to NEW_IMAGE. Use Kinesis Adapter in the application to consume streams from DynamoDB.(Correct)**
    
    ### **Explanation**
    
    DynamoDB Streams provides a time-ordered sequence of item-level changes in any DynamoDB table. The changes are de-duplicated and stored for 24 hours. Applications can access this log and view the data items as they appeared before and after they were modified, in near real time.
    
    The **Kinesis Adapter** is the recommended way to consume streams from DynamoDB for real-time processing. The DynamoDB Streams API is intentionally similar to that of Kinesis Streams, a service for real-time processing of streaming data at a massive scale. You can write applications for Kinesis Streams using the Kinesis Client Library (KCL). The KCL simplifies coding by providing useful abstractions above the low-level Kinesis Streams API. As a DynamoDB Streams user, you can leverage the design patterns found within the KCL to process DynamoDB Streams shards and stream records. To do this, you use the DynamoDB Streams Kinesis Adapter. The Kinesis Adapter implements the Kinesis Streams interface, so that the KCL can be used for consuming and processing records from DynamoDB Streams.
    
    ![](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/streams-kinesis-adapter.png)
    
    When an item in the table is modified, `StreamViewType` determines what information is written to the stream for this table. Valid values for `StreamViewType` are:
    
- Q8
    
    **A serverless application is using API Gateway with a non-proxy Lambda Integration. A developer was tasked to expose a GET method on a new `/getcourses` resource to invoke the Lambda function, which will allow the consumers to fetch a list of online courses in JSON format. The consumers must include a query string parameter named `courseType` in their request to get the data.
    What is the MOST efficient solution that the developer should do to accomplish this requirement?**
    
    - **Configure the integration response of the resource.**
    - **Configure the method response of the resource.**
    - **Configure the method request of the resource.(Correct)**
    - **Configure the integration request of the resource.(Incorrect)**
    
    ### **Explanation**
    
    In Lambda non-proxy (or custom) integration, you can specify how the incoming request data is mapped to the integration request and how the resulting integration response data is mapped to the method response.
    
    ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/apigateway-my-resource-get-method-execution-boxes.png)
    
    ![](https://img-b.udemycdn.com/redactor/raw/2019-06-27_00-25-48-1a9a89f6e15acccad5ad3aac3f0c7fda.png)
    
    In this scenario, you have to enforce the use of a required `courseType` query string parameter in the `/getcourses` resource in API Gateway. In order to do this, you can configure the method request of your resource just as shown in the diagram above.
    
    Hence, the correct answer is to **configure the method request of the resource***.*
    
    **Configuring the integration request of the resource** is incorrect because although configuring the *integration request* may also be valid, the client traffic will hit the *method request* first before it goes to the *integration request* down to the underlying Lambda function. This is why you should configure the *method request first* so it won't be necessary to check the required parameters in the Lambda integration. In addition, the *integration request* does not have the capability to enforce a request to include certain query string parameter nor enable API caching, unlike the *method request.*
    
- Q27 - important
    
    **Due to the popularity of serverless computing, your manager instructed you to share your technical expertise to the whole software development department of your company. You are planning to deploy a simple Node.js 'Hello World' Lambda function to AWS using CloudFormation.
    Which of the following is the EASIEST way of deploying the function to AWS?**
    
    - **Upload the code in S3 then specify the `S3Key` and `S3Bucket` parameters under the `AWS::Lambda::Function` resource in the CloudFormation template.**
    - **Upload the code in S3 as a ZIP file then specify the S3 path in the `ZipFile` parameter of the `AWS::Lambda::Function` resource in the CloudFormation template.**
    - **Include your function source inline in the `ZipFile` parameter of the `AWS::Lambda::Function` resource in the CloudFormation template.(Correct)**
    - **Include your function source inline in the `Code` parameter of the `AWS::Lambda::Function` resource in the CloudFormation template.(Incorrect)**
    
    ### **Explanation**
    
    To create a Lambda function, you first create a Lambda function deployment package, a .zip or .jar file consisting of your code and any dependencies. When creating the zip, include only the code and its dependencies, not the containing folder. You will then need to set the appropriate security permissions for the zip package.
    
    If you are using a CloudFormation template, you can configure the `AWS::Lambda::Function` resource which creates a Lambda function. To create a function, you need a deployment package and an execution role. The deployment package contains your function code. The execution role grants the function permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS X-Ray for request tracing.
    
    ![](https://img-b.udemycdn.com/redactor/raw/2019-06-16_13-40-22-da5b60140125634d546815752f88b63c.png)
    
    Under the `AWS::Lambda::Function` resource, you can use the `Code` property which contains the deployment package for a Lambda function. For all runtimes, you can specify the location of an object in Amazon S3.
    
    For Node.js and Python functions, you can specify the function code inline in the template. Changes to a deployment package in Amazon S3 are not detected automatically during stack updates. To update the function code, change the object key or version in the template.
    
- Q30
    
    **An application in your development account is running in an AWS Elastic Beanstalk environment which has an attached Amazon RDS database. You noticed that if you terminate the environment, it also brings down the database which hinders you from performing seamless updates with blue-green deployments. This also poses a critical security risk if the company decides to deploy the application in production.
    In this scenario, how can you decouple your database instance from your environment without having any data loss?**
    
    - **Use a Canary deployment strategy to decouple the Amazon RDS instance from your Elastic Beanstalk environment. Create an RDS DB snapshot of the database and enable deletion protection. Create a new Elastic Beanstalk environment with the necessary information to connect to the Amazon RDS instance and delete the old environment.**
    - **Use a Canary deployment strategy to decouple the Amazon RDS instance from your Elastic Beanstalk environment. Create an RDS DB snapshot of the database and then create a new Elastic Beanstalk environment with the necessary information to connect to the Amazon RDS instance.**
    - **Use the blue / green deployment strategy to decouple the Amazon RDS instance from your Elastic Beanstalk environment. Create an RDS DB snapshot of the database and enable deletion protection. Create a new Elastic Beanstalk environment with the necessary information to connect to the Amazon RDS instance. Before terminating the old Elastic Beanstalk environment, remove its security group rule first before proceeding.(Correct)**
    - **Use the blue / green deployment strategy to decouple the Amazon RDS instance from your Elastic Beanstalk environment. Create an RDS DB snapshot of the database and enable deletion protection. Create a new Elastic Beanstalk environment with the necessary information to connect to the Amazon RDS instance and delete the old environment.(Incorrect)**
    
    ### **Explanation**
    
    AWS Elastic Beanstalk provides support for running Amazon Relational Database Service (Amazon RDS) instances in your Elastic Beanstalk environment. This works great for development and testing environments. However, it isn't ideal for a production environment because it ties the lifecycle of the database instance to the lifecycle of your application's environment.
    
    If you haven't used a DB instance with your application before, try adding one to a test environment with the Elastic Beanstalk console first. This lets you verify that your application is able to read environment properties, construct a connection string, and connect to a DB instance before you add Amazon Virtual Private Cloud (Amazon VPC) and security group configuration to the mix.
    
    ![](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/aeb-architecture2.png)
    
    To decouple your database instance from your environment, you can run a database instance in Amazon RDS and configure your application to connect to it on launch. This enables you to connect multiple environments to a database, terminate an environment without affecting the database, and perform seamless updates with blue-green deployments.
    
    To allow the Amazon EC2 instances in your environment to connect to an outside database, you can configure the environment's Auto Scaling group with an additional security group. The security group that you attach to your environment can be the same one that is attached to your database instance, or a separate security group from which the database's security group allows ingress.
    
    You can connect your environment to a database by adding a rule to your database's security group that allows ingress from the autogenerated security group that Elastic Beanstalk attaches to your environment's Auto Scaling group. However, doing so creates a dependency between the two security groups. Subsequently, when you attempt to terminate the environment, Elastic Beanstalk will be unable to delete the environment's security group because the database's security group is dependent on it.
    
- Q33 - important
    
    **Your manager assigned you a task of implementing server-side encryption with customer-provided encryption keys (SSE-C) to your S3 bucket, which will allow you to set your own encryption keys. Amazon S3 will manage both the encryption and decryption process using your key when you access your objects, which will remove the burden of maintaining any code to perform data encryption and decryption.
    To properly upload data to this bucket, which of the following headers must be included in your request?**
    
    - **`x-amz-server-side-encryption`, `x-amz-server-side-encryption-customer-key` and `x-amz-server-side-encryption-customer-key-MD5` headers**
    - **`x-amz-server-side-encryption` and `x-amz-server-side-encryption-aws-kms-key-id` headers**
    - **`x-amz-server-side-encryption-customer-key` header only(Incorrect)**
    - **`x-amz-server-side-encryption-customer-algorithm`, `x-amz-server-side-encryption-customer-key` and `x-amz-server-side-encryption-customer-key-MD5` headers(Correct)**
    
    **Explanation**
    
    When using server-side encryption with customer-provided encryption keys (SSE-C), you **must** provide encryption key information using the following request headers:
    
    **`x-amz-server-side-encryption-customer-algorithm`** - This header specifies the encryption algorithm. The header value must be "AES256".
    
    **`x-amz-server-side-encryption-customer-key`** - This header provides the 256-bit, base64-encoded encryption key for Amazon S3 to use to encrypt or decrypt your data.
    
    **`x-amz-server-side-encryption-customer-key-MD5`** - This header provides the base64-encoded 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.
    
- Q37 - important
    
    **To accommodate a new application deployment, you have created a new EBS volume to be attached to your EC2 instance. After attaching the newly created EBS volume to the Linux EC2 instance, which of the following steps are you going to do next in order to use this volume?**
    
    - **Create a file system on this volume.(Correct)**
    - **Mount the volume since it already has a pre-configured file system.**
    - **Assign a file system on this volume using the AWS Console.**
    - **No action needed. AWS automatically configures the EBS volume for use on your instance.(Incorrect)**
    
    ### **Explanation**
    
    New volumes are raw block devices and do not contain any partition or file system. You need to login to the instance and then format the EBS volume with a file system, and then mount the volume for it to be usable.
    
- Q40
    
    **A company is heavily using a range of AWS services to host their enterprise applications. Currently, their deployment process still has a lot of manual steps which is why they plan to automate their software delivery process using continuous integration and delivery (CI/CD) pipelines in AWS. They will use CodePipeline to orchestrate each step of their release process and CodeDeploy for deploying applications to various compute platforms in AWS.
    In this architecture, which of the following are valid considerations when using CodeDeploy? (Select TWO.)**
    
    - [ ]  **You have to install and use the CodeDeploy agent installed on your EC2 instances and ECS cluster.**
    - [ ]  **AWS Lambda compute platform deployments cannot use an in-place deployment type.(Correct)**
    - [ ]  **The CodeDeploy agent communicates using HTTP over port 80.**
    - [x]  **CodeDeploy can deploy applications to both your EC2 instances as well as your on-premises servers.(Correct)**
    - [x]  **CodeDeploy can deploy applications to EC2, AWS Lambda, and Amazon ECS only.(Incorrect)**
- Q42 - important
    
    **In order to quickly troubleshoot their systems, your manager instructed you to record the calls that your application makes to all AWS services and resources. You developed a custom code that will send the segment documents directly to X-Ray by using the `PutTraceSegments` API.
    What should you include in your segment document to meet the above requirement?**
    
    - **subsegments(Correct)**
    - **tracing header(Incorrect)**
    - **annotations**
    - **metadata**
    
    ### **Explanation**
    
    A segment can break down the data about the work done into **subsegments**. Subsegments provide more granular timing information and details about downstream calls that your application made to fulfill the original request. A subsegment can contain additional details about a call to an AWS service, an external HTTP API, or an SQL database. You can even define arbitrary subsegments to instrument specific functions or lines of code in your application.
    
    ![](https://docs.aws.amazon.com/xray/latest/devguide/images/scorekeep-PUTrules-timeline-subsegments.png)
    
    For services that don't send their own segments like Amazon DynamoDB, X-Ray uses subsegments to generate *inferred segments* and downstream nodes on the service map. This lets you see all of your downstream dependencies, even if they don't support tracing, or are external.
    
    Subsegments represent your application's view of a downstream call as a client. If the downstream service is also instrumented, the segment that it sends replaces the inferred segment generated from the upstream client's subsegment. The node on the service graph always uses information from the service's segment, if it's available, while the edge between the two nodes uses the upstream service's subsegment.
    
- Q63 - confusing question
    
    **You are planning to create a DynamoDB table for your employee profile website. This will be used by the Human Resources department to easily view details about each employee.
    When choosing the partition key of the table, which of the following is the BEST attribute to use?**
    
    - **`employee_name` because this will speed up searching of records.**
    - **`position_id` because this will help sort the records per department.**
    - **`department_id` since employees will fall in these departments.(Incorrect)**
    - **`employee_id` because each employee ID is unique.(Correct)**
    
    ### **Explanation**
    
    When you create a table, in addition to the table name, you must specify the primary key of the table. The primary key uniquely identifies each item in the table so that no two items can have the same key.
    
    DynamoDB supports two different kinds of primary keys:
    
    1. Partition key
    
    2. Partition key and sort key
    
    **Partition key** – A simple primary key, composed of one attribute known as the partition key. DynamoDB uses the partition key's value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored. In a table that has only a partition key, no two items can have the same partition key value.
    
    **Partition key and sort key** – Referred to as a composite primary key, this type of key is composed of two attributes. The first attribute is the partition key, and the second attribute is the sort key. DynamoDB uses the partition key value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored. All items with the same partition key are stored together, in sorted order by sort key value.
    
    In a table that has a partition key and a sort key, it's possible for two items to have the same partition key value. However, those two items must have different sort key values. A composite primary key gives you additional flexibility when querying data. For example, if you provide only the value for Artist, DynamoDB retrieves all of the songs by that artist. To retrieve only a subset of songs by a particular artist, you can provide a value for Artist along with a range of values for SongTitle.
    
    Thus, in this scenario, the correct answer is to *use `employee_id` because each employee ID is unique*. Using high-cardinality attributes are recommended when creating primary partition keys. Examples of these unique attributes are email, employee_no, customerid, and so on.
    
    Both `*department_id*` and `*position_id*` are incorrect because these values are not unique per employee.
    
    Using `*employee_name*` is not recommended because in big organizations, somebody may share the same name as someone else.
    
- Q64
    
    **An ECS Cluster has a running X-Ray Daemon that enables developers to easily debug and troubleshoot their application. However, the trace data being sent to AWS X-Ray is still not as detailed as your manager wants it to be. There is a new requirement that requires the application to provide more granular timing information and more details about its downstream calls to various AWS resources.
    What should you do to satisfy this requirement?**
    
    - **Use inferred segment**
    - **Use annotations**
    - **Use metadata(Incorrect)**
    - **Use subsegments(Correct)**

## Doubtful

- Q15
    
    **A developer needs to configure the environment name, solution stack, and environment links of his application environment which will be hosted in Elastic Beanstalk. Which configuration file should the developer add in the source bundle to meet the above requirement?**
    • **`env.yaml`(Correct)**
    • **`cron.yaml`**
    • **`Dockerrun.aws.json`**
    • **`env.config`**
    
- Q17
    
    **Your team is developing a new feature on your application which is already hosted in Elastic Beanstalk. After several weeks, the new version of the application is ready to be deployed and you were instructed to handle the deployment.
    What is the correct way to deploy the new version to Elastic Beanstalk via the CLI?**
    
    - **Package your application as a `zip` file and deploy it using the `eb deploy` command.(Correct)**
    - **Package your application as a `zip` file and deploy it using the `aws elasticbeanstalk update-application` command.**
    - **Package your application as a `tar` file and deploy it using the `aws elasticbeanstalk update-application` command.**
    - **Package your application as a `tar` file and deploy it using the `eb deploy` command.**
- Q20
    
    **You recently deployed an application to a newly created AWS account, which uses two identical Lambda functions to process ad-hoc requests. The first function processes incoming requests efficiently but the second one has a longer processing time even though both of the functions have exactly the same code. Based on your monitoring, the `Throttles` metric of the second function is greater than the first one in Amazon CloudWatch.
    Which of the following are possible solutions that you can implement to fix this issue? (Select TWO.)**
    
    - [x]  **Decrease the concurrency execution limit of the first function.(Correct)**
    - [ ]  **Set the concurrency execution limit of both functions to 500.**
    - [ ]  **Configure the second function to use an unreserved account concurrency.**
    - [ ]  **Set the concurrency execution limit of the second function to 0.**
    - [x]  **Set the concurrency execution limit of both functions to 450.(Correct)**
    
    ### **Explanation**
    
    ![](https://img-b.udemycdn.com/redactor/raw/2019-06-19_05-33-49-25da87db665ac5ffced6882b8070b0d3.png)
    
    If you create a Lambda function to process events from event sources that aren't poll-based (for example, Lambda can process every event from other sources, like Amazon S3 or API Gateway), each published event is a unit of work, in parallel, up to your account limits. Therefore, the number of invocations these event sources make influences the concurrency.
    
    If you set the concurrent execution limit for a function, the value is deducted from the unreserved concurrency pool. For example, if your account's concurrent execution limit is 1000 and you have 10 functions, you can specify a limit on one function at 200 and another function at 100. The remaining 700 will be shared among the other 8 functions.
    
    AWS Lambda will keep the unreserved concurrency pool at a minimum of 100 concurrent executions, so that functions that do not have specific limits set can still process requests. So, in practice, if your total account limit is 1000, you are limited to allocating 900 to individual functions.
    
- Q21
    
    **A developer wants to track the number of visitors on their website, which has a DynamoDB database. This is primarily used to give a rough idea on how many people visit the site whenever they launch a new advertisement, which means it can tolerate a slight overcounting or undercounting of website visitors.
    Which of the following will satisfy the requirement with MINIMAL configuration?**
    
    - **Use `atomic counters` to increment the counter item in the DynamoDB table for every new visitor.(Correct)**
    - **Use `conditional writes` to update the counter item in the DynamoDB table only if the item has a unique primary key and the new value is greater than the current value.**
    - **Use `conditional writes` to update the counter item in the DynamoDB table and set the `ReturnConsumedCapacity` parameter to `TOTAL`.**
    - **Enable DynamoDB Streams to track the number of new visitors.**
    
    ### **Explanation**
    
    You can use the `UpdateItem` operation to implement an *atomic counter* — a numeric attribute that is incremented, unconditionally, without interfering with other write requests. (All write requests are applied in the order in which they were received). With an atomic counter, the updates are not idempotent. In other words, the numeric value will increment each time you call `UpdateItem`.
    
    You might use an atomic counter to keep track of the number of visitors to a website. In this case, your application would increment a numeric value, regardless of its current value. If an `UpdateItem`operation should fail, the application could simply retry the operation. This would risk updating the counter twice, but you could probably tolerate a slight overcounting or undercounting of website visitors.
    
    An atomic counter would not be appropriate where overcounting or undercounting cannot be tolerated (For example, in a banking application). In this case, it is safer to use a conditional update instead of an atomic counter.
    
- Q28
    
    **A Docker application hosted on an ECS cluster has encountered intermittent unavailability issues and timeouts. The lead DevOps engineer instructed you to instrument the application to detect where high latencies are occurring and to determine the specific services and paths impacting application performance.
    Which of the following steps should you take to accomplish this task properly? (Select TWO.)**
    
    - [x]  **Create a Docker image that runs the X-Ray daemon, upload it to a Docker image repository, and then deploy it to your Amazon ECS cluster.(Correct)**
    - [ ]  **Configure the port mappings and network mode settings in the container agent to allow traffic on TCP port 2000.**
    - [x]  **Configure the port mappings and network mode settings in your task definition file to allow traffic on UDP port 2000.(Correct)**
    - [ ]  **Manually install the X-Ray daemon to the instances via a user data script.**
    - [ ]  **Add the `xray-daemon.config` configuration file in your Docker image.**
    
    ### **Explanation**
    
    The AWS X-Ray SDK does not send trace data directly to AWS X-Ray. To avoid calling the service every time your application serves a request, the SDK sends the trace data to a daemon, which collects segments for multiple requests and uploads them in batches. Use a script to run the daemon alongside your application.
    
    To properly instrument your applications in Amazon ECS, you have to create a Docker image that runs the X-Ray daemon, upload it to a Docker image repository, and then deploy it to your Amazon ECS cluster. You can use port mappings and network mode settings in your task definition file to allow your application to communicate with the daemon container.
    
    ![](https://img-b.udemycdn.com/redactor/raw/2019-06-07_00-07-28-efab421cd7dba9b1ebe743e5ec85d4fb.png)
    
    The AWS X-Ray daemon is a software application that listens for traffic on UDP port 2000, gathers raw segment data, and relays it to the AWS X-Ray API. The daemon works in conjunction with the AWS X-Ray SDKs and must be running so that data sent by the SDKs can reach the X-Ray service.
    
- Q46 - important
    
    **A developer is building an application that will be hosted in ECS and must be configured to run tasks and services using the Fargate launch type. The application will have four different tasks, each of which will access different AWS resources than the others.
    Which of the following is the MOST efficient solution that can provide your application in ECS access to the required AWS resources?**
    
    - **Create 4 different IAM Roles with the required permissions and attach them to each of the 4 ECS tasks.(Correct)**
    - **Create 4 different Service-Linked Roles with the required permissions and attach them to each of the 4 ECS tasks.**
    - **Create an IAM Group with all the required permissions and attach them to each of the 4 ECS tasks.**
    - **Create 4 different Container Instance IAM Roles with the required permissions and attach them to each of the 4 ECS tasks.**
    
    ### **Explanation**
    
    The option that says: **Creating 4 different Service-Linked Roles with the required permissions and attaching them to each of the 4 ECS tasks** **is incorrect because a service-linked role is a unique type of IAM role that is linked directly to Amazon ECS itself, not on the ECS task. Service-linked roles are predefined by Amazon ECS and include all the permissions that the service requires to call other AWS services on your behalf.