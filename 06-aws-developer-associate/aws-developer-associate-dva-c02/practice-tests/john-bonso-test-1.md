# John Bonso Test 1

## Wrong

- Q14 - good
    
    **An application hosted in an Auto Scaling group of On-Demand EC2 instances is used to process data polled from an SQS queue and the generated output is stored in an S3 bucket. To improve security, you were tasked to ensure that all objects in the S3 bucket are encrypted at rest using server-side encryption with AWS KMS–Managed Keys (SSE-KMS).
    Which of the following is required to properly implement this requirement?**
    
    - **Add a bucket policy which denies any `s3:PutObject` action unless the request includes the `x-amz-server-side-encryption-aws-kms-key-id` header.(Incorrect)**
    - **Add a bucket policy which denies any `s3:PostObject` action unless the request includes the `x-amz-server-side-encryption` header.**
    - **Add a bucket policy which denies any `s3:PostObject` action unless the request includes the `x-amz-server-side-encryption-aws-kms-key-id` header.**
    - **Add a bucket policy which denies any `s3:PutObject` action unless the request includes the `x-amz-server-side-encryption` header.(Correct)**
    
    ### **Explanation**
    
    **Server-side encryption** is about protecting data at rest. AWS Key Management Service (**AWS KMS**) is a service that combines secure, highly available hardware and software to provide a key management system scaled for the cloud. AWS KMS uses customer master keys (CMKs) to encrypt your Amazon S3 objects. You use AWS KMS via the AWS Management Console or AWS KMS APIs to centrally create encryption keys, define the policies that control how keys can be used, and audit key usage to prove they are being used correctly. You can use these keys to protect your data in Amazon S3 buckets.
    
    The first time you add an SSE-KMS–encrypted object to a bucket in a region, a default CMK is created for you automatically. This key is used for SSE-KMS encryption unless you select a CMK that you created separately using AWS Key Management Service. Creating your own CMK gives you more flexibility, including the ability to create, rotate, disable, and define access controls, and to audit the encryption keys used to protect your data.
    
    ![](https://media.tutorialsdojo.com/amazon-s3-sse-kms-encryption.PNG)
    
    Amazon S3 supports bucket policies that you can use if you require server-side encryption for all objects that are stored in your bucket. For example, you can set a bucket policy that denies permission to upload an object (`s3:PutObject`) to everyone if the request does not include the `x-amz-server-side-encryption` header requesting server-side encryption with SSE-KMS.
    
    When you upload an object, you can specify the KMS key using the `x-amz-server-side-encryption-aws-kms-key-id` header which you can use to require a specific KMS key for object encryption. If the header is not present in the request, Amazon S3 assumes the default KMS key. Regardless, the KMS key ID that Amazon S3 uses for object encryption must match the KMS key ID in the policy, otherwise Amazon S3 denies the request.
    
    Therefore, the correct answer is: **Add a bucket policy which denies any `s3:PutObject` action unless the request includes the `x-amz-server-side-encryption` header.**
    
    The option that says: **Adding a bucket policy which denies any `s3:PutObject` action unless the request includes the `x-amz-server-side-encryption-aws-kms-key-id` header** is incorrect because you have to use the `x-amz-server-side-encryption` header instead.
    
- Q22 - important
    
    **An internal web application is hosted in a custom VPC with multiple private subnets only. Every EC2 instance that will be provisioned on this VPC will require access to an S3 bucket to pull configuration files as well as to push application logs.
    Which of the following options is the most suitable solution to use in this scenario?**
    
    - **Create a VPC endpoint for S3.(Correct)**
    - **Store the IAM user and password in the application code to access the S3 bucket.**
    - **Use the AWS SDK for your application and issue the `aws configure` CLI command to store your access keys, which will be referred to by the SDK.**
    - **Create an IAM Role and attach it to each EC2 instance.(Incorrect)**
    
    ### **Explanation**
    
    In this scenario, the key point that you have to understand is that **S3 is not part of your VPC.**
    
    The option that says: **Create an IAM Role and attach it to each EC2 instance** is incorrect. Although this is the recommended way to grant access to S3, there would still be **no**
     connectivity between your instance and S3. Your VPC should have an Internet Gateway, a NAT Instance/Gateway, or a VPC endpoint in order to establish a connection between these two services.
    
- Q25 - good
    
    **A reporting application is hosted in Elastic Beanstalk and uses DynamoDB as its database. If a user requests data, the application scans the entire table and returns the requested data. In the coming weeks, it is expected that the table will grow due to the surge of new users and requested reports.
    Which of the following should be done as a preparation to improve the application's performance with minimal cost? (Select TWO.)**
    
    - [ ]  **Increase page size**
    - [x]  **Use Query operations instead(Correct)**
    - [ ]  **Increase the Write Compute Unit (WCU) of the table**
    - [ ]  **Reduce page size(Correct)**
    - [x]  **Use DynamoDB Accelerator (DAX)(Incorrect)**
    
    ### **Explanation**
    
    In general, `Scan` operations are less efficient than other operations in DynamoDB. A `Scan` operation always scans the entire table or secondary index. It then filters out values to provide the result you want, essentially adding the extra step of removing data from the result set.
    
    If possible, you should avoid using a `Scan` operation on a large table or index with a filter that removes many results. Also, as a table or index grows, the `Scan` operation slows. The `Scan` operation examines every item for the requested values and can use up the provisioned throughput for a large table or index in a single operation. For faster response times, design your tables and indexes so that your applications can use `Query` instead of `Scan`. For tables, you can also consider using the `GetItem` and `BatchGetItem` APIs.
    
    Alternatively, you can refactor your application to use `Scan` operations in a way that minimizes the impact on your request rate. Instead of using a large `Scan` operation, you can use the following techniques to minimize the impact of a scan on a table's provisioned throughput.
    
    **Reduce page size** - Because a Scan operation reads an entire page (by default, 1 MB), you can reduce the impact of the scan operation by setting a smaller page size. The `Scan` operation provides a *Limit* parameter that you can use to set the page size for your request. Each `Query` or `Scan` request that has a smaller page size uses fewer read operations and creates a "pause" between each request.
    
    **Using DynamoDB Accelerator (DAX)** 
    is incorrect. Although this will improve the scalability and read performance of the application, it adds a significant cost in maintaining your application. Using Query operations and reducing the page size of your query are the more cost-effective solutions in this scenario.
    
- Q34
    
    **A website hosted in AWS has a custom CloudWatch metric to track all HTTP server errors in the site every minute, which occurs intermittently. An existing CloudWatch Alarm has already been configured for this metric but you would like to re-configure this to properly monitor the application. The alarm should only be triggered when all three data points in the most recent three consecutive periods are above the threshold.
    Which of the following options is the MOST appropriate way to monitor the website based on the given threshold?**
    
    - **Use high-resolution metrics.**
    - **Set both the `Period` and `Datapoints to Alarm` to 3.(Incorrect)**
    - **Use metric math in CloudWatch to properly compute the threshold.**
    - **Set both the `Evaluation Period` and `Datapoints to Alarm` to 3.(Correct)**
    
    ### **Explanation**
    
    When you create an alarm, you specify three settings to enable CloudWatch to evaluate when to change the alarm state:
    
    - **Period** is the length of time to evaluate the metric or expression to create each individual data point for an alarm. It is expressed in seconds. If you choose one minute as the period, there is one datapoint every minute.
    - **Evaluation Period** is the number of the most recent periods, or data points, to evaluate when determining alarm state.
    - **Datapoints to Alarm** is the number of data points within the evaluation period that must be breaching to cause the alarm to go to the `ALARM` state. The breaching data points do not have to be consecutive, they just must all be within the last number of data points equal to **Evaluation Period**.
    
    In the following figure, the alarm threshold is set to three units. The alarm is configured to go to the `ALARM` state and both **Evaluation Period** and **Datapoints to Alarm** are 3. That is, when all three datapoints in the most recent three consecutive periods are above the threshold, the alarm goes to the `ALARM` state. In the figure, this happens in the third through fifth time periods. At period six, the value dips below the threshold, so one of the periods being evaluated is not breaching, and the alarm state changes to `OK`. During the ninth time period, the threshold is breached again, but for only one period. Consequently, the alarm state remains `OK`.
    
- Q49
    
    **You have created a Node.js Lambda function that updates a DynamoDB table and sends an email notification via Amazon SNS. However, upon testing, the function is not working as expected. Which of the following is the BEST way to troubleshoot this issue?**
    
    - **Use AWS X-Ray(Correct)**
    - **Use Amazon CloudWatch(Incorrect)**
    - **Use AWS CloudTrail**
    - **Use Amazon Inspector**
    
    ### **Explanation**
    
    AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. With X-Ray, you can understand how your application and its underlying services are performing to identify and troubleshoot the root cause of performance issues and errors. X-Ray provides an end-to-end view of requests as they travel through your application, and shows a map of your application’s underlying components.
    
    *Amazon CloudWatch* is incorrect because although you can troubleshoot the issue by checking the logs, it is still better to use AWS X-Ray as it enables you to analyze and debug your serverless application more effectively.
    
- Q56
    
    **A recently deployed Lambda function has an intermittent issue in processing customer data. You enabled the active tracing option in order to detect, analyze, and optimize performance issues of your function using the X-Ray service.
    Which of the following environment variables are used by AWS Lambda to facilitate communication with X-Ray? (Select TWO.)**
    
    - [x]  **`AWS_XRAY_DEBUG_MODE`(Incorrect)**
    - [x]  **`_X_AMZN_TRACE_ID`(Correct)**
    - [ ]  **`AUTO_INSTRUMENT`**
    - [ ]  **`AWS_XRAY_CONTEXT_MISSING`(Correct)**
    - [ ]  **`AWS_XRAY_TRACING_NAME`**
    
    ### **Explanation**
    
    AWS X-Ray is an AWS service that allows you to detect, analyze, and optimize performance issues with your AWS Lambda applications. X-Ray collects metadata from the Lambda service and any upstream or downstream services that make up your application. X-Ray uses this metadata to generate a detailed service graph that illustrates performance bottlenecks, latency spikes, and other issues that impact the performance of your Lambda application.
    
    ![](https://docs.aws.amazon.com/xray/latest/devguide/images/scorekeep-servicemap-lambda-node.png)
    
    AWS Lambda uses environment variables to facilitate communication with the X-Ray daemon and configure the X-Ray SDK.
    
    **_X_AMZN_TRACE_ID:** Contains the tracing header, which includes the sampling decision, trace ID, and parent segment ID. If Lambda receives a tracing header when your function is invoked, that header will be used to populate the _X_AMZN_TRACE_ID environment variable. If a tracing header was not received, Lambda will generate one for you.
    
    **AWS_XRAY_CONTEXT_MISSING:** The X-Ray SDK uses this variable to determine its behavior in the event that your function tries to record X-Ray data, but a tracing header is not available. Lambda sets this value to `LOG_ERROR` by default.
    
    **AWS_XRAY_DAEMON_ADDRESS:** This environment variable exposes the X-Ray daemon's address in the following format: `*IP_ADDRESS*`**:**`*PORT*`. You can use the X-Ray daemon's address to send trace data to the X-Ray daemon directly without using the X-Ray SDK.
    
- Q63 - important
    
    **A developer is refactoring a Lambda function that currently processes data using a public GraphQL API. There’s a new requirement to store query results in a database hosted in a VPC. The function has been configured with additional VPC-specific information, and the database connection has been successfully established. However, the engineer has discovered that the function can no longer connect to the internet after testing.
    Which of the following should the developer do to fix this issue? (Select TWO.)**
    
    - [x]  **Add a NAT gateway to your VPC.(Correct)**
    - [x]  **Set up elastic network interfaces (ENIs) to enable your Lambda function to connect securely to other resources within your private VPC.(Incorrect)**
    - [ ]  **Ensure that the associated security group of the Lambda function allows outbound connections.(Correct)**
    - [ ]  **Submit a limit increase request to AWS to raise the concurrent executions limit of your Lambda function.**
    - [ ]  **Configure your function to forward payloads that were not processed to a dead-letter queue (DLQ) using Amazon SQS.**
    
    ### **Explanation**
    
    If your Lambda function needs Internet access, just as described in this scenario, do not attach it to a public subnet or to a private subnet without Internet access. Instead, attach it only to private subnets with Internet access through a NAT instance or **add a NAT gateway to your VPC**. You should also **ensure that the associated security group of the Lambda function allows outbound connections.**
    
    **Setting up elastic network interfaces (ENIs) to enable your Lambda function to connect securely to other resources within your private VPC** is incorrect because this is already done automatically by AWS Lambda. It uses the VPC information you provide to automatically set up ENIs that allow your Lambda function to access VPC resources. You don't need to do this step in order for your Lambda function to be integrated with your VPC.
    

## Doubtful

- Q1
    
    **An application, which already uses X-Ray, generates thousands of trace data every hour. The developer wants to use a filter expression that will limit the results based on custom attributes or keys that he specifies.
    How should the developer refactor the application in order to filter the results in the X-Ray console?**
    
    - **Add the custom attributes as annotations in your segment document.(Correct)**
    - **Include the custom attributes as new segment fields in the segment document.**
    - **Add the custom attributes as metadata in your segment document.**
    - **Create a new sampling rule based on the custom attributes.**
    
    ### **Explanation**
    
    **Annotations** are simple key-value pairs that are indexed for use with [filter expressions](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-filters.html). Use annotations to record data that you want to use to group traces in the console, or when calling the [`GetTraceSummaries`](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html) API. X-Ray indexes up to 50 annotations per trace.
    
    **Metadata** are key-value pairs with values of any type, including objects and lists, but that are not indexed. Use metadata to record data you want to store in the trace but don't need to use for searching traces. You can view annotations and metadata in the segment or subsegment details in the X-Ray console.
    
- Q26
    
    **An application performs various workflows and processes long-running tasks that take a long time to complete. The users are complaining that the application is unresponsive since the workflow substantially increased the time it takes to complete a user request.
    Which of the following is the BEST way to improve the performance of the application?**
    
    - **Use a multicontainer docker environment in Elastic Beanstalk to process the long-running tasks asynchronously.**
    - **Use an Amazon ECS Cluster with a Fargate launch type to process the tasks asynchronously.**
    - **Spawn a worker process locally in the EC2 instances and process the tasks asynchronously.**
    - **Use an Elastic Beanstalk worker environment to process the tasks asynchronously.(Correct)**
- Q29
    
    **A new IT policy requires you to trace all calls that your Node.js application sends to external HTTP web APIs as well as SQL database queries. You have to instrument your application, which is hosted in Elastic Beanstalk, in order to properly trace the calls via the X-Ray console.
    What should you do to comply with the given requirement?**
    
    - **Use a user data script to run the daemon automatically.**
    - **Create a Docker image that runs the X-Ray daemon.**
    - **Enable the X-Ray daemon by including the `xray-daemon.config` configuration file in the `.ebextensions` directory of your source code.(Correct)**
    - **Enable active tracing in the Elastic Beanstalk by including the `healthcheckurl.config` configuration file in the `.ebextensions` directory of your source code.**
    
    ### **Explanation**
    
    You can use the **AWS Elastic Beanstalk** console or a configuration file to run the AWS X-Ray daemon on the instances in your environment. X-Ray is an AWS service that gathers data about the requests that your application serves, and uses it to construct a service map that you can use to identify issues with your application and opportunities for optimization.
    
    ![](https://img-b.udemycdn.com/redactor/raw/2019-06-06_12-50-29-f6e9a9e669fdcc779a8695f4866cdb99.png)
    
    To relay trace data from your application to AWS X-Ray, you can run the X-Ray daemon on your Elastic Beanstalk environment's Amazon EC2 instances. Elastic Beanstalk platforms provide a configuration option that you can set to run the daemon automatically. You can enable the daemon in a configuration file in your source code or by choosing an option in the Elastic Beanstalk console. When you enable the configuration option, the daemon is installed on the instance and runs as a service.
    
    Hence, the correct answer is to: **enable the X-Ray daemon by including the `xray-daemon.config` configuration file in the `.ebextensions` directory of your source code**.
    
    **Using a user data script to run the daemon automatically** is incorrect because this is only applicable if you want to enable X-Ray to your EC2 instances.
    
    **Creating a Docker image that runs the X-Ray daemon** is incorrect because this is what you need to do if you want to enable X-Ray on ECS Cluster and not on Elastic Beanstalk.
    
- Q33
    
    **Your customers require access to the REST APIs of your web application which is hosted on EC2 instances behind a load balancer in your VPC. To accommodate this request, your web services should be integrated with API Gateway that has a custom data mapping. You need to specify how the incoming request data is mapped to the integration request and how the resulting integration response data is mapped to the method response.
    Which of the following integration types is the MOST suitable one to use in API Gateway to meet this requirement?**
    
    - **`HTTP`(Correct)**
    - **`AWS`**
    - **`AWS_PROXY`**
    - **`HTTP_PROXY`**
    
    ### **Explanation**
    
    You can integrate an API method in your API Gateway with a custom HTTP endpoint of your application in two ways:
    
    - HTTP proxy integration
    
    - HTTP custom integration
    
    In your API Gateway console, you can define the type of HTTP integration of your resource by toggling the "**Configure as proxy resource**" checkbox.
    
    ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/api-gateway-create-api-step-by-step-create-resource-2.png)
    
    With proxy integration, the setup is simple. You only need to set the HTTP method and the HTTP endpoint URI, according to the backend requirements, if you are not concerned with content encoding or caching.
    
    With custom integration, setup is more involved. In addition to the proxy integration setup steps, you need to specify how the incoming request data is mapped to the integration request and how the resulting integration response data is mapped to the method response. API Gateway supports the following endpoint ports: 80, 443 and 1024-65535.
    
- Q51
    
    **You developed a shell script which uses AWS CLI to create a new Lambda function. However, you received an `InvalidParameterValueException` after running the script.
    What is the MOST likely cause of this issue?**
    
    - **You have exceeded your maximum total code size per account.**
    - **The resource already exists.**
    - **The AWS Lambda service encountered an internal error.**
    - **You provided an IAM role in the `CreateFunction` API which AWS Lambda is unable to assume.(Correct)**
    
    ### **Explanation**
    
    To create a Lambda function, you need a deployment package and an execution role. The deployment package contains your function code. The execution role grants the function permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS X-Ray for request tracing. You can use the CreateFunction API via the AWS CLI or the AWS SDK of your choice.
    
    The `InvalidParameterValueException` will be returned if one of the parameters in the request is invalid. For example, if *you provided an IAM role in the `CreateFunction` API which AWS Lambda is unable to assume*. Hence, this option is the most likely cause of the issue in this scenario.
    
- Q54
    
    **There have been reports that your application, which has a MySQL RDS database, becomes unresponsive from time to time. You were instructed to collect all SQL statements that took longer to execute for troubleshooting.
    What should you do to properly troubleshoot this issue with the LEAST amount of effort?**
    
    - **Instrument your application using the X-Ray SDK.**
    - **Enable active tracing using AWS X-Ray.**
    - **Use Amazon Inspector to get all the slow queries.**
    - **Enable slow query log in RDS.(Correct)**
- Q57
    
    **A web application is running in an ECS Cluster and updates data in DynamoDB several times a day. The clients retrieve data directly from the DynamoDB through APIs exposed by Amazon API Gateway. Although API caching is enabled, there are specific clients that want to retrieve the latest data from DynamoDB for every API request sent.
    What should be done to only allow authorized clients to invalidate an API Gateway cache entry when submitting API requests? (Select TWO.)**
    
    - [x]  **Tick the `Require Authorization` checkbox in the Cache Settings of your API via the console.(Correct)**
    - [ ]  **Modify the cache settings to retrieve the latest data from DynamoDB if the request header's authorization signature matches your API's trusted clients list.**
    - [ ]  **Provide your clients an authorization token from STS to query data directly from DynamoDB.**
    - [x]  **The client must send a request which contains the `Cache-Control: max-age=0` header.(Correct)**
    - [ ]  **The client must send a request which contains the `Cache-Control: max-age=1` header.**
    
    ### **Explanation**
    
    A client of your API can invalidate an existing cache entry and reload it from the integration endpoint for individual requests. The client must send a request that contains the `Cache-Control: max-age=0` header. The client receives the response directly from the integration endpoint instead of the cache, provided that the client is authorized to do so. This replaces the existing cache entry with the new response, which is fetched from the integration endpoint.
    
    ![](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/apig-cache-invalidation.png)
    
    Ticking the `Require authorization` checkbox ensures that not every client can invalidate the API cache. If most or all of the clients invalidate the API cache, this could significantly increase the latency of your API.
    
- Q60
    
    **A developer is building a new Docker application using ECS. She needs to allow containers to access ports on the host container instance to send or receive traffic using port mapping.
    Which component of ECS should the developer configure to properly implement this task?**
    
    - **Container instance**
    - **Service scheduler**
    - **Task definition(Correct)**
    - **Container Agent**