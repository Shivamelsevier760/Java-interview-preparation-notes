# Neal Davis Test 6

## Wrong

- Q5
    
    **A Developer created an AWS Lambda function and then attempted to add an on failure destination but received the following error:
    `The function's execution role does not have permissions to call SendMessage on arn:aws:sqs:us-east-1:515148212435:FailureDestination`
    How can the Developer resolve this issue MOST securely?**
    
    - **Create a customer managed policy with all read/write permissions to SQS and attach the policy to the function’s execution role(Correct)**
    - **Add the AWSLambdaSQSQueueExecutionRole AWS managed policy to the function’s execution role(Incorrect)**
    - **Add the Lambda function to a group with administrative privileges**
    - **Add a permissions policy to the SQS queue allowing the SendMessage action and specify the AWS account number**
    
    ### **Explanation**
    
    The Lambda function needs the privileges to use the SendMessage API action on the Amazon SQS queue. The permissions should be assigned to the function’s execution role. The `AWSLambdaSQSQueueExecutionRole` AWS managed policy cannot be used as this policy does not provide the `SendMessage` action.
    
- Q13
    
    **An independent software vendor (ISV) uses Amazon S3 and Amazon CloudFront to distribute software updates. They would like to provide their premium customers with access to updates faster. What is the MOST efficient way to distribute these updates only to the premium customers? (Select TWO.)**
    
    - [ ]  **Use an access control list (ACL) on the Amazon S3 bucket to restrict access based on IP address**
    - [x]  **Create a signed cookie and associate it with the Amazon S3 distribution(Incorrect)**
    - [ ]  **Use an IAM policy to restrict access to the content using a condition attribute and specify the IP addresses of the premium customers**
    - [ ]  **Create an origin access identity (OAI) and associate it with the distribution and configure permissions(Correct)**
    - [x]  **Create a signed URL with access to the content and distribute it to the premium customers(Correct)**
    
    ### **Explanation**
    
    To restrict access to content that you serve from Amazon S3 buckets, you create CloudFront signed URLs or signed cookies to limit access to files in your Amazon S3 bucket, and then you create a special CloudFront user called an origin access identity (OAI) and associate it with your distribution. Then you configure permissions so that CloudFront can use the OAI to access and serve files to your users, but users can't use a direct URL to the S3 bucket to access a file there. Taking these steps help you maintain secure access to the files that you serve through CloudFront.
    
- Q33
    
    **A monitoring application that keeps track of a large eCommerce website uses Amazon Kinesis for data ingestion. During periods of peak data rates, the producers are not making best use of the available shards.What step will allow the producers to better utilize the available shards and increase write throughput to the Kinesis data stream?**
    
    - **Install the Kinesis Producer Library (KPL) for ingesting data into the stream(Correct)**
    - **Increase the shard count of the stream using `UpdateShardCount`**
    - **Create an SQS queue and decouple the producers from the Kinesis data stream**
    - **Ingest multiple records into the stream in a single call using `BatchWriteItem`(Incorrect)**
    
    ### **Explanation**
    
    An Amazon Kinesis Data Streams producer is an application that puts user data records into a Kinesis data stream (also called *data ingestion*). The Kinesis Producer Library (KPL) simplifies producer application development, allowing developers to achieve high write throughput to a Kinesis data stream.
    
    The KPL is an easy-to-use, highly configurable library that helps you write to a Kinesis data stream. It acts as an intermediary between your producer application code and the Kinesis Data Streams API actions. The KPL performs the following primary tasks:
    
    - Writes to one or more Kinesis data streams with an automatic and configurable retry mechanism
    - Collects records and uses `PutRecords` to write multiple records to multiple shards per request
    - Aggregates user records to increase payload size and improve throughput
    - Integrates seamlessly with the [Kinesis Client Library](https://docs.aws.amazon.com/kinesis/latest/dev/developing-consumers-with-kcl.html) (KCL) to de-aggregate batched records on the consumer
    - Submits Amazon CloudWatch metrics on your behalf to provide visibility into producer performance
    
    The question states that the producers are not making best use of the available shards. Therefore, we understand that there are adequate shards available but the producers are either not discovering them or are not writing records at sufficient speed to best utilize the shards.
    
    We therefore need to install the Kinesis Producer Library (KPL) for ingesting data into the stream.
    
    **CORRECT:** "Install the Kinesis Producer Library (KPL) for ingesting data into the stream" is the correct answer.
    
    **INCORRECT:** "Create an SQS queue and decouple the producers from the Kinesis data stream " is incorrect. In this case we need to ensure our producers are discovering shards and writing records to best utilize those shards.
    
    **INCORRECT:** "Increase the shard count of the stream using UpdateShardCount" is incorrect. The problem statement is that the producers are not making best use of the available shards. We don’t need to add more shards, we need to make sure the producers are discovering and then fully utilizing the shards that are available.
    
    **INCORRECT:** "Ingest multiple records into the stream in a single call using BatchWriteItem" is incorrect. This API is used with DynamoDB, not Kinesis.
    
- Q39
    
    **A company is reviewing their security practices. According to AWS best practice how should access keys be managed to improve security? (Select TWO.)**
    
    - [ ]  **Embed access keys directly into code**
    - [ ]  **Delete all access keys for the root account IAM user(Correct)**
    - [x]  **Use different access keys for different applications(Correct)**
    - [x]  **Rotate access keys daily(Incorrect)**
    - [ ]  **Use the same access key in all applications for consistency**
    
    ### **Explanation**
    
    When you access AWS programmatically, you use an access key to verify your identity and the identity of your applications. An access key consists of an access key ID (something like AKIAIOSFODNN7EXAMPLE) and a secret access key (something like wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY).
    
    Anyone who has your access key has the same level of access to your AWS resources that you do. Steps to protect access keys include the following:
    
    - Remove (or Don't Generate) Account Access Key – this is especially important for the root account.
    - Use Temporary Security Credentials (IAM Roles) Instead of Long-Term Access Keys.
    - Don't embed access keys directly into code.
    - Use different access keys for different applications.
    - Rotate access keys periodically.
    - Remove unused access keys.
    - Configure multi-factor authentication for your most sensitive operations.
    

## Doubtful

- Q14
    
    **A Developer is creating a social networking app for games that uses a single Amazon DynamoDB table. All users’ saved game data is stored in the single table, but users should not be able to view each other’s data.
    How can the Developer restrict user access so they can only view their own data?**
    
    - **Read records from DynamoDB and discard irrelevant data client-side**
    - **Restrict access to specific items based on certain primary key values(Correct)**
    - **Use separate access keys for each user to call the API and restrict access to specific items based on access key ID**
    - **Use an identity-based policy that restricts read access to the table to specific principals**
    
    ### **Explanation**
    
    In DynamoDB, you have the option to specify conditions when granting permissions using an IAM policy. For example, you can:
    
    - Grant permissions to allow users read-only access to certain items and attributes in a table or a secondary index.
    - Grant permissions to allow users write-only access to certain attributes in a table, based upon the identity of that user.
    
    To implement this kind of fine-grained access control, you write an IAM permissions policy that specifies conditions for accessing security credentials and the associated permissions. You then apply the policy to IAM users, groups, or roles that you create using the IAM console. Your IAM policy can restrict access to individual items in a table, access to the attributes in those items, or both at the same time.
    
    You use the IAM Condition element to implement a fine-grained access control policy. By adding a Condition element to a permissions policy, you can allow or deny access to items and attributes in DynamoDB tables and indexes, based upon your particular business requirements. You can also grant permissions on a table, but restrict access to specific items in that table based on certain primary key values.
    
    **CORRECT:** "Restrict access to specific items based on certain primary key values" is the correct answer.
    
    **INCORRECT:** "Use separate access keys for each user to call the API and restrict access to specific items based on access key ID" is incorrect. You cannot restrict access based on access key ID.
    
    **INCORRECT:** "Use an identity-based policy that restricts read access to the table to specific principals" is incorrect as this would only restrict read access to the entire table, not to specific items in the table.
    
    **INCORRECT:** "Read records from DynamoDB and discard irrelevant data client-side" is incorrect as this is inefficient and insecure as it will use more RCUs and has more potential to leak the information.
    
- Q15 - important
    
    Question 15:
    
    **Correct**
    
    **A Developer has created a task definition that includes the following JSON code:
    
    `1. "placementConstraints": [
    2. {
    3. "expression": "attribute:ecs.instance-type =~ t2.*",
    4. "type": "memberOf"
    5. }
    6. ]`
    What will be the effect for tasks using this task definition?**
    
    - **They will be placed only on container instances of T2 or T3 instance types**
    - **They will be added to distinct instances using the T2 instance type**
    - **They will be placed only on container instances using the T2 instance type(Correct)**
    - **They will be spread across all instances except for T2 instances**
- Q21
    
    **A serverless application composed of multiple Lambda functions has been deployed. A developer is setting up AWS CodeDeploy to manage the deployment of code updates. The developer would like a 10% of the traffic to be shifted to the new version in equal increments, 10 minutes apart.
    Which setting should be chosen for configuring how traffic is shifted?**
    
    - **Canary**
    - **Blue/green**
    - **All-at-once**
    - **Linear(Correct)**
    
    ### **Explanation**
    
    A deployment configuration is a set of rules and success and failure conditions used by CodeDeploy during a deployment. These rules and conditions are different, depending on whether you deploy to an EC2/On-Premises compute platform or an AWS Lambda compute platform.
    
    The following table lists the predefined configurations available for AWS Lambda deployments.
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-23_04-00-04-d3e9f996df007d5519fddba490278419.jpg)
    
    As you can see from the table above, the linear option shifts a specific amount of traffic in equal increments of time. Therefore, the following option should be chosen:
    
    CodeDeployDefault.LambdaLinear10PercentEvery10Minutes
    
    **CORRECT:** "Linear" is the correct answer.
    
    **INCORRECT:** "Canary" is incorrect as it does not shift traffic in equal increments.
    
    **INCORRECT:** "All-at-once" is incorrect as it shifts all traffic at once.
    
    **INCORRECT:** "Blue/green" is incorrect as it is a type of deployment, not a setting for traffic shifting.
    
- Q22 - important
    
    **An application uses Amazon EC2 instances, AWS Lambda functions and an Amazon SQS queue. The Developer must ensure all communications are within an Amazon VPC using private IP addresses. How can this be achieved? (Select TWO.)**
    
    - [x]  **Create a VPC endpoint for Amazon SQS(Correct)**
    - [ ]  **Create a VPN and connect the services to the VPG**
    - [x]  **Add the AWS Lambda function to the VPC(Correct)**
    - [ ]  **Create a VPC endpoint for AWS Lambda**
    - [ ]  **Create the Amazon SQS queue within a VPC**
    
    ### **Explanation**
    
    This solution can be achieved by adding the AWS Lambda function to a VPC through the function configuration, and by creating a VPC endpoint for Amazon SQS. This will result in the services using purely private IP addresses to communicate without traversing the public Internet.
    
    **CORRECT:** "Add the AWS Lambda function to the VPC" is the correct answer.
    
    **CORRECT:** "Create a VPC endpoint for Amazon SQS" is also correct.
    
    **INCORRECT:** "Create the Amazon SQS queue within a VPC" is incorrect as you cannot create a queue within a VPC as Amazon SQS is a public service.
    
    **INCORRECT:** "Create a VPC endpoint for AWS Lambda" is incorrect as you can't create a VPC endpoint for AWS Lambda. You can, however, connect a Lambda function to a VPC.
    
    **INCORRECT:** "Create a VPN and connect the services to the VPG" is incorrect as you cannot create a VPN between each of these services.
    
- Q57
    
    **A Developer is creating an AWS Lambda function to process a stream of data from an Amazon Kinesis Data Stream. When the Lambda function parses the data and encounters a missing field, it exits the function with an error. The function is generating duplicate records from the Kinesis stream. When the Developer looks at the stream output without the Lambda function, there are no duplicate records.
    What is the reason for the duplicates?**
    
    - **The Lambda event source used asynchronous invocation, resulting in duplicate records**
    - **The Lambda function did not handle the error, and the Lambda service attempted to reprocess the data(Correct)**
    - **The Lambda function did not advance the Kinesis stream point to the next record after the error**
    - **The Lambda function is not keeping up with the amount of data coming from the stream**
    
    ### **Explanation**
    
    When you invoke a function, two types of error can occur. Invocation errors occur when the invocation request is rejected before your function receives it. Function errors occur when your function's code or [runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) returns an error.
    
    Depending on the type of error, the type of invocation, and the client or service that invokes the function, the retry behavior and the strategy for managing errors varies. Function errors occur when your function code or the runtime that it uses return an error.
    
    In this case, with an event source mapping from a stream (Kinesis Data Stream), Lambda retries the entire batch of items. Therefore, the best explanation is that the Lambda function did not handle the error, and the Lambda service attempted to reprocess the data.
    
    **INCORRECT:** "The Lambda function did not advance the Kinesis stream point to the next record after the error" is incorrect. Lambda does not advance a stream “point” to the next record. It processed records in batches.