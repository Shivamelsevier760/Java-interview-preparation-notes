# Neal Davis Test 5

## Wrong

- Q7
    
    **A Developer needs to restrict all users and roles from using a list of API actions within a member account in AWS Organizations. The Developer needs to deny access to a few specific API actions.
    What is the MOST efficient way to do this?**
    
    - **Create an IAM policy that denies the API actions for all users and roles(Incorrect)**
    - **Create an IAM policy that allows only the unrestricted API actions**
    - **Create an allow list and specify the API actions to deny**
    - **Create a deny list and specify the API actions to deny(Correct)**
    
    ### **Explanation**
    
    Service control policies (SCPs) are one type of policy that you can use to manage your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization, allowing you to ensure your accounts stay within your organization’s access control guidelines.
    
    You can configure the SCPs in your organization to work as either of the following:
    
    - A [deny list](https://docs.aws.amazon.com/organizations/latest/userguide/SCP_strategies.html#orgs_policies_denylist) – actions are allowed by default, and you specify what services and actions are prohibited
    - An [allow list](https://docs.aws.amazon.com/organizations/latest/userguide/SCP_strategies.html#orgs_policies_allowlist) – actions are prohibited by default, and you specify what services and actions are allowed
- Q11
    
    C**ontainers will be deployed across some newly deployed ECS containers instances using the same instance type. High availability is provided within the microservices architecture. Which task placement strategy requires the LEAST configuration for this scenario?**
    
    - **spread(Incorrect)**
    - **binpack**
    - **Fargate**
    - **random(Correct)**
    
    ### **Explanation**
    
    **INCORRECT:** "spread" is incorrect. As high availability is taken care of within the containers there is no need to use a spread strategy to ensure HA.
    
- Q20
    
    **A Developer is deploying an Amazon ECS update using AWS CodeDeploy. In the appspec.yaml file, which of the following is a valid structure for the order of hooks that should be specified?**
    
    - **BeforeAllowTraffic > AfterAllowTraffic(Incorrect)**
    - **BeforeInstall > AfterInstall > ApplicationStart > ValidateService**
    - **BeforeInstall > AfterInstall > AfterAllowTestTraffic > BeforeAllowTraffic > AfterAllowTraffic(Correct)**
    - **BeforeBlockTraffic > AfterBlockTraffic > BeforeAllowTraffic > AfterAllowTraffic**
    
    ### **Explanation**
    
    The content in the 'hooks' section of the AppSpec file varies, depending on the compute platform for your deployment. The 'hooks' section for an EC2/On-Premises deployment contains mappings that link deployment lifecycle event hooks to one or more scripts.
    
    The 'hooks' section for a Lambda or an Amazon ECS deployment specifies Lambda validation functions to run during a deployment lifecycle event. If an event hook is not present, no operation is executed for that event. This section is required only if you are running scripts or Lambda validation functions as part of the deployment.
    
    The following code snippet shows a valid example of the structure of hooks for an Amazon ECS deployment:
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-23_02-44-56-2017625f2c25c61736eb3231c9b6895f.jpg)
    
    Therefore, in this scenario a valid structure for the order of hooks that should be specified in the appspec.yml file is: BeforeInstall > AfterInstall > AfterAllowTestTraffic > BeforeAllowTraffic > AfterAllowTraffic
    
- Q59
    
    **A Developer is writing an AWS Lambda function that processes records from an Amazon Kinesis Data Stream. The Developer must write the function so that it sends a notice to Administrators if it fails to process a batch of records.
    How should the Developer write the function?**
    
    - **Configure an Amazon SNS topic as an on-failure destination(Correct)**
    - **Use Amazon CloudWatch Events to send the processed data**
    - **Push the failed records to an Amazon SQS queue(Incorrect)**
    - **Separate the Lambda handler from the core logic**
    
    ### **Explanation**
    
    With Destinations, you can route asynchronous function results as an execution record to a destination resource without writing additional code. An execution record contains details about the request and response in JSON format including version, timestamp, request context, request payload, response context, and response payload.
    
    For each execution status such as *Success* or *Failure* you can choose one of four destinations: another Lambda function, SNS, SQS, or EventBridge.
    
- Q63
    
    **A developer has created a YAML template file that includes the following header: '`AWS::Serverless-2016-10-31`'. Which commands should the developer use to deploy the application?**
    
    - **`aws cloudformation create-stack-set`**
    - **`sam package` and `sam deploy`(Correct)**
    - **`aws cloudformation package` and `aws cloudformation create-stack`(Incorrect)**
    - **`sam package` and `sam build`**
    
    ### **Explanation**
    
    The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. With just a few lines per resource, you can define the application you want and model it using YAML.
    
    The “Transform” header indicates that the developer is creating a SAM template as it has the value: Transform: '`AWS::Serverless-2016-10-31`'
    
- Q65
    
    **A Developer has noticed some suspicious activity in her AWS account and is concerned that the access keys associated with her IAM user account may have been compromised. What is the first thing the Developer do in should do in this situation?**
    
    - **Delete her IAM user account(Incorrect)**
    - **Change her IAM User account password**
    - **Delete the compromised access keys(Correct)**
    - **Report the incident to AWS Support**
    
    ### **Explanation**
    
    In this case the Developer’s access keys may have been compromised so the first step would be to invalidate the access keys by deleting them.
    
    The next step would then be to determine if any temporary security credentials have been issued an invalidating those too to prevent any further misuse.
    
    The user account and user account password have not been compromised so they do not need to be deleted / changed as a first step. However, changing the account password would typically be recommended as a best practice in this situation.
    

## Doubtful

- Q46
    
    **Every time an Amazon EC2 instance is launched, certain metadata about the instance should be recorded in an Amazon DynamoDB table. The data is gathered and written to the table by an AWS Lambda function.
    What is the MOST efficient method of invoking the Lambda function?**
    
    - **Create a CloudTrail trail alarm that triggers the Lambda function based on the `RunInstances` API action**
    - **Create a CloudWatch alarm that triggers the Lambda function based on log streams indicating an EC2 state change in CloudWatch logs**
    - **Configure detailed monitoring on Amazon EC2 and create an alarm that triggers the Lambda function in initialization**
    - **Create a CloudWatch Event with an event pattern looking for EC2 state changes and a target set to use the Lambda function(Correct)**
    
    ### **Explanation**
    
    Amazon CloudWatch Events **delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources**. Using simple rules that you can quickly set up, you can match events and route them to one or more target functions or streams. CloudWatch Events becomes aware of operational changes as they occur. CloudWatch Events responds to these operational changes and takes corrective action as necessary, by sending messages to respond to the environment, activating functions, making changes, and capturing state information.
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-23_03-05-05-4d71f304fa9f2b4d827c5a87a7108193.jpg)
    
    In this scenario the only workable solution is to create a CloudWatch Event with an event pattern looking for EC2 state changes and a target set to use the Lambda function.
    
- Q48
    
    **An application is running on a fleet of EC2 instances running behind an Elastic Load Balancer (ELB). The EC2 instances session data in a shared Amazon S3 bucket. Security policy mandates that data must be encrypted in transit.
    How can the Developer ensure that all data that is sent to the S3 bucket is encrypted in transit?**
    
    - **Create an S3 bucket policy that denies any S3 Put request that does not include the x-amz-server-side-encryption**
    - **Configure HTTP to HTTPS redirection on the Elastic Load Balancer**
    - **Create an S3 bucket policy that denies traffic where SecureTransport is false(Correct)**
    - **Create an S3 bucket policy that denies traffic where SecureTransport is true**
    
    ### **Explanation**
    
    At the Amazon S3 bucket level, you can configure permissions through a bucket policy. For example, you can limit access to the objects in a bucket by IP address range or specific IP addresses. Alternatively, you can make the objects accessible only through HTTPS.
    
    The following bucket policy allows access to Amazon S3 objects only through HTTPS (the policy was generated with the AWS Policy Generator).
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-23_02-15-33-c945d6087ebcc622bf8f8ec6d087332b.jpg)
    
    Here the bucket policy explicitly denies ("Effect": "Deny") all read access ("Action": "s3:GetObject") from anybody who browses ("Principal": "*") to Amazon S3 objects within an Amazon S3 bucket if they are not accessed through HTTPS ("aws:SecureTransport": "false").
    
- Q50
    
    **An application uses multiple Lambda functions to write data to an Amazon RDS database. The Lambda functions must share the same connection string. What is the BEST solution to ensure security and operational efficiency?**
    
    - **Embed the connection string within the Lambda function code**
    - **Use a CloudHSM encrypted environment variable that is shared between the functions**
    - **Create a secure string parameter using AWS systems manager parameter store(Correct)**
    - **Use KMS encrypted environment variables within each Lambda function**
    
    ### **Explanation**
    
    AWS Systems Manager Parameter Store provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, and license codes as parameter values.
    
    You can store values as plaintext (unencrypted data) or ciphertext (encrypted data). You can then reference values by using the unique name that you specified when you created the parameter.
    
    A secure string parameter is any sensitive data that needs to be stored and referenced in a secure manner. If you have data that you don't want users to alter or reference in plaintext, such as passwords or license keys, create those parameters using the SecureString datatype.
    
    If you choose the SecureString datatype when you create a parameter, then Parameter Store uses an AWS Key Management Service (KMS) customer master key (CMK) to encrypt the parameter value.
    
    This is the most secure and operationally efficient way to meet this requirement. The connection string will be encrypted and only needs to be managed in one place where it can be shared by the multiple Lambda functions.
    
- Q56
    
    **An application is being instrumented to send trace data using AWS X-Ray. A Developer needs to upload segment documents using JSON-formatted strings to X-Ray using the API. Which API action should the developer use?**
    
    - **The `PutTelemetryRecords` API action**
    - **The `PutTraceSegments` API action(Correct)**
    - **The `GetTraceSummaries` API action**
    - **The `UpdateGroup` API action**
    
    ### **Explanation**
    
    You can upload segment documents with the [`PutTraceSegments`](https://docs.aws.amazon.com/xray/latest/api/API_PutTraceSegments.html) API. The API has a single parameter, `TraceSegmentDocuments`, that takes a list of JSON segment documents.
    
    **INCORRECT:** "The `PutTelemetryRecords` API action" is incorrect as this is used by the AWS X-Ray daemon to upload telemetry.