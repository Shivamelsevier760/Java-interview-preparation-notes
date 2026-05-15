# Neal Davis Test 2

## Wrong

- Q5
    
    **A developer needs use the attribute of an Amazon S3 object that uniquely identifies the object in a bucket. Which of the following represents an Object Key?**
    
    - **Development/Projects.xls(Correct)**
    - **Project=Blue**
    - **arn:aws:s3:::dctlabs**
    - **s3://dctlabs/Development/Projects.xls(Incorrect)**
- Q8
    
    **A Developer is developing a web application and will maintain separate sets of resources for the alpha, beta, and release stages. Each version runs on Amazon EC2 and uses an Elastic Load Balancer.
    How can the Developer create a single page to view and manage all of the resources?**
    
    - **Create a resource group(Correct)**
    - **Create a single AWS CodeDeploy deployment**
    - **Deploy all resources using a single Amazon CloudFormation stack**
    - **Create an AWS Elastic Beanstalk environment for each stage(Incorrect)**
    
    ### **Explanation**
    
    In AWS, a *resource* is an entity that you can work with. Examples include an Amazon EC2 instance, an AWS CloudFormation stack, or an Amazon S3 bucket. If you work with multiple resources, you might find it useful to manage them as a group rather than move from one AWS service to another for each task.
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-20_15-05-01-8d8d858713fe382fe148dd7d39441d93.jpg)
    
    By default, the AWS Management Console is organized by AWS service. But with Resource Groups, you can create a custom console that organizes and consolidates information based on criteria specified in tags, or the resources in an AWS CloudFormation stack. The following list describes some of the cases in which resource grouping can help organize your resources.
    
    An application that has different phases, such as development, staging, and production.
    
    Projects managed by multiple departments or individuals.
    
    A set of AWS resources that you use together for a common project or that you want to manage or monitor as a group.
    
    A set of resources related to applications that run on a specific platform, such as Android or iOS.
    
- Q18
    
    **A Developer is creating a DynamoDB table for storing transaction logs. The table has 10 write capacity units (WCUs). The Developer needs to configure the read capacity units (RCUs) for the table in order to MAXIMIZE the number of requests allowed per second. Which of the following configurations should the Developer use?**
    
    - **Strongly consistent reads of 5 RCUs reading items that are 4 KB in size(Incorrect)**
    - **Eventually consistent reads of 15 RCUs reading items that are 1 KB in size(Correct)**
    - **Strongly consistent reads of 15 RCUs reading items that are 1KB in size**
    - **Eventually consistent reads of 5 RCUs reading items that are 4 KB in size**
    
    ### **Explanation**
    
    The following bullets provide the read throughput for each configuration:
    
    · Eventually consistent, 15 RCUs, 1 KB item = 30 items read per second.
    
    · Strongly consistent, 15 RCUs, 1 KB item = 15 items read per second.
    
    · Eventually consistent, 5 RCUs, 4 KB item = 10 items read per second.
    
    · Strongly consistent, 5 RCUs, 4 KB item = 5 items read per second.
    
    Therefore, the Developer should choose the option to enable eventually consistent reads of 15 RCUs reading items that are 1 KB in size as this will result in the highest number of items read per second.
    
- Q22
    
    **A developer is configuring health checks using Amazon Route 53 and needs to set values to determine the health of critical endpoints. What is the parameter that Amazon Route 53 reviews before deciding if an endpoint is unhealthy?**
    
    - **latency.**
    - **failure threshold.(Correct)**
    - **network response.(Incorrect)**
    - **fault tolerance.**
    
    ### **Explanation**
    
    The failure threshold is specified by the AWS customer. A failure is when the endpoint does not respond to a request.
    
- Q28
    
    **A start-up organization imported their X.509 certificate from another issuer into AWS Certificate Manager (ACM) approximately 11 months ago. What needs to be done to ensure that visitors will continue to have secure access to the website? (Select TWO.)**
    
    - [ ]  **A new certificate will need to be requested from ACM.(Correct)**
    - [x]  **A new certificate will need to be imported into ACM.(Correct)**
    - [x]  **A new certificate will automatically be created prior to the certificate expiring at 12 months.(Incorrect)**
    - [ ]  **A new certificate will be automatically imported into ACM.**
    - [ ]  **A new certificate will automatically be created prior to the certificate expiring at 13 months.**
    
    ### **Explanation**
    
    AWS ACM issued certificates are valid for 13 months. They are also renewed automatically. Imported certificates are not automatically renewed and would need to be imported once created from the third party.
    
    **CORRECT:** "A new certificate will need to be requested from ACM" is the correct answer (as explained above.)
    
    **CORRECT:** "A new certificate will need to be imported into ACM” is also a correct answer (as explained above.)
    
    **INCORRECT:** "A new certificate will automatically be created prior to the certificate expiring at 12 months" is incorrect. Imported certificates are not automatically renewed by AWS ACM.
    
    **INCORRECT:** "A new certificate will automatically be created prior to the certificate expiring at 13 months" is incorrect. Imported certificates are not automatically renewed by AWS ACM.
    
    **INCORRECT:** "A new certificate will be automatically imported into ACM" is incorrect. A new certificate issued by a third-party can be imported but it is not automatically done.
    
- Q32
    
    **A company is developing a new online game that will run on top of Amazon ECS. Four distinct Amazon ECS services will be part of the architecture, each requiring specific permissions to various AWS services. The company wants to optimize the use of the underlying Amazon EC2 instances by bin packing the containers based on memory reservation.
    Which configuration would allow the Development team to meet these requirements MOST securely**
    
    - **Create a new Identity and Access Management (IAM) instance profile containing the required permissions for the various ECS services, then associate that instance role with the underlying EC2 instances**
    - **Create four distinct IAM roles, each containing the required permissions for the associated ECS services, then configure each ECS task definition to reference the associated IAM role(Correct)**
    - **Create four distinct IAM roles, each containing the required permissions for the associated ECS services, then, create an IAM group and configure the ECS cluster to reference that group**
    - **Create four distinct IAM roles, each containing the required permissions for the associated ECS services, then configure each ECS service to reference the associated IAM role(Incorrect)**
    
    ### **Explanation**
    
    With IAM roles for Amazon ECS tasks, you can specify an IAM role that can be used by the containers in a task. Applications must sign their AWS API requests with AWS credentials, and this feature provides a strategy for managing credentials for your applications to use, similar to the way that Amazon EC2 instance profiles provide credentials to EC2 instances.
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-21_06-21-36-8e63335980c5cab31bb81697b00df2f2.png)
    
    Instead of creating and distributing your AWS credentials to the containers or using the EC2 instance’s role, you can associate an IAM role with an ECS task definition or RunTask API operation. The applications in the task’s containers can then use the AWS SDK or CLI to make API requests to authorized AWS services.
    
    In this case each service requires access to different AWS services so following the principal of least privilege it is best to assign as a separate role to each task definition.
    
    **CORRECT:** "Create four distinct IAM roles, each containing the required permissions for the associated ECS services, then configure each ECS task definition to reference the associated IAM role" is the correct answer.
    
    **INCORRECT:** "Create four distinct IAM roles, each containing the required permissions for the associated ECS services, then configure each ECS service to reference the associated IAM role" is incorrect as the reference should be made within the task definition.
    
- Q36
    
    **An application running on Amazon EC2 generates a large number of small files (1KB each) containing personally identifiable information that must be converted to ciphertext. The data will be stored on a proprietary network-attached file system. What is the SAFEST way to encrypt the data using AWS KMS?**
    
    - **Create a data encryption key from a customer master key and encrypt the data with the customer master key**
    - **Encrypt the data directly with an AWS managed customer master key(Incorrect)**
    - **Create a data encryption key from a customer master key and encrypt the data with the data encryption key**
    - **Encrypt the data directly with a customer managed customer master key(Correct)**
    
    ### **Explanation**
    
    With AWS KMS you can encrypt files directly with a customer master key (CMK). A CMK can encrypt up to 4KB (4096 bytes) of data in a single encrypt, decrypt, or reencrypt operation. As CMKs cannot be exported from KMS this is a very safe way to encrypt small amounts of data.
    
    *Customer managed CMKs* are CMKs in your AWS account that you create, own, and manage. You have full control over these CMKs, including establishing and maintaining their [key policies, IAM policies, and grants](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html), [enabling and disabling](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) them, [rotating their cryptographic material](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), [adding tags](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html), [creating aliases](https://docs.aws.amazon.com/kms/latest/developerguide/programming-aliases.html) that refer to the CMK, and [scheduling the CMKs for deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html).
    
    *AWS managed CMKs* are CMKs in your account that are created, managed, and used on your behalf by an AWS service that is integrated with AWS KMS. Some AWS services support only an AWS managed CMK. In this example the Amazon EC2 instance is saving files on a proprietary network-attached file system and this will not have support for AWS managed CMKs.
    
    **INCORRECT:** "Encrypt the data directly with an AWS managed customer master key" is incorrect as the network-attached file system is proprietary and therefore will not be supported by AWS managed CMKs.
    
- Q39
    
    **A Developer needs to manage AWS services from a local development server using the AWS CLI. How can the Developer ensure that the CLI uses their IAM permissions?**
    
    - **Create an IAM Role with the required permissions and attach it to the local server’s instance profile**
    - **Run the aws configure command and provide the Developer’s IAM access key ID and secret access key(Correct)**
    - **Save the Developer’s IAM login credentials as environment variables and reference them when executing AWS CLI commands(Incorrect)**
    - **Put the Developer’s IAM user account in an IAM group that has the necessary permissions**
    
    ### **Explanation**
    
    **INCORRECT:** "Save the Developer’s IAM login credentials as environment variables and reference them when executing AWS CLI commands" is incorrect as the IAM login credentials cannot be used with the AWS CLI. You need to use an access key ID and secret access key with the AWS CLI and these are configured for use by running aws configure.
    
- Q41
    
    **A serverless application uses an IAM role to authenticate and authorize access to an Amazon DynamoDB table. A Developer is troubleshooting access issues affecting the application. The Developer has access to the IAM role that the application is using.
    Which of the following commands will help the Developer to test the role permissions using the AWS CLI?**
    
    - **aws iam get-role-policy(Incorrect)**
    - **aws sts get-session-token**
    - **aws dynamodb describe-endpoints**
    - **aws sts assume-role(Correct)**
    
    ### **Explanation**
    
    The AWS CLI “aws sts assume role” command will enable the Developer to assume the role and gain temporary security credentials. The Developer can then use those security credentials to troubleshoot access issues that are affecting the application.
    
- Q49
    
    **A company is creating an application that must support Security Assertion Markup Language (SAML) and authentication with social identity providers. The application must also be authorized to access data in Amazon S3 buckets and Amazon DynamoDB tables.
    Which AWS service or feature will meet these requirements with the LEAST amount of additional coding?**
    
    - **AWS AppSync GraphQL API.**
    - **Amazon Cognito identity pools.(Correct)**
    - **Amazon Cognito user pools.(Incorrect)**
    - **Amazon API Gateway REST API.**
    
    ### **Explanation**
    
    Amazon Cognito identity pools (federated identities) enable you to create unique identities for your users and federate them with identity providers. With an identity pool, you can obtain temporary, limited-privilege AWS credentials to access other AWS services.
    
    Amazon Cognito identity pools support the following identity providers:
    
    - Public providers: Amazon, Facebook, Google, Apple
    - Amazon Cognito user pools
    - Open ID Connect providers (identity pools)
    - SAML identity providers (identity pools)
    - Developer authenticated identities (identity pools)
    
    Identity pools are well suited to use cases where you need to authenticate users through one of the above IdPs and then authorize access to AWS services such as Amazon S3 and DynamoDB.
    
    **CORRECT:** "Amazon Cognito identity pools" is the correct answer (as explained above.)
    
    **INCORRECT:** "Amazon Cognito user pools" is incorrect.
    
    You can use a user pool for authentication but you would then need to use the identity pool for authorization to AWS services. Therefore, this option would require more additional coding.
    
- Q55
    
    **A Developer is deploying an application using Docker containers running on the Amazon Elastic Container Service (ECS). The Developer is testing application latency and wants to capture trace information between the microservices.
    Which solution will meet these requirements?**
    
    - **Install the AWS X-Ray daemon on each of the Amazon ECS instances.**
    - **Install the Amazon CloudWatch agent on the container image. Use the CloudWatch SDK to publish custom metrics from each of the microservices.**
    - **Create a Docker image that runs the X-Ray daemon, upload it to a Docker image repository, and then deploy it to the Amazon ECS cluster.(Correct)**
    - **Install the AWS X-Ray daemon locally on an Amazon EC2 instance and instrument the Amazon ECS microservices using the X-Ray SDK.(Incorrect)**
    
    ### **Explanation**
    
    In Amazon ECS, create a Docker image that runs the X-Ray daemon, upload it to a Docker image repository, and then deploy it to your Amazon ECS cluster. You can use port mappings and network mode settings in your task definition file to allow your application to communicate with the daemon container.
    
- Q59
    
    **A Developer needs to be notified by email for all new object creation events in a specific Amazon S3 bucket. Amazon SNS will be used for sending the messages. How can the Developer enable these notifications?**
    • **Create an event notification for all `s3:ObjectCreated:Put` API calls(Incorrect)**
    • **Create an event notification for all `s3:ObjectRestore:Post` API calls**
    • **Create an event notification for all `s3:ObjectCreated:*` API calls(Correct)**
    • **Create an event notification for all `s3:ObjectRemoved:Delete` API calls**
    
- Q60
    
    **A developer received the following error message during an AWS CloudFormation deployment:
    DELETE_FAILED (The following resource(s) failed to delete: (sg-11223344).)
    Which action should the developer take to resolve this error?**
    
    - **Manually delete the security group. Then execute a change set to force deletion of the CloudFormation stack.(Incorrect)**
    - **Modify the CloudFormation template to retain the security group resource. Then manually delete the resource after deployment.(Correct)**
    - **Update the logical ID of the security group resource with the security groups ARN. Then delete the stack.**
    - **Add a DependsOn attribute to the sg-11223344 resource in the CloudFormation template. Then delete the stack.**
    
    ### **Explanation**
    
    The stack may be stuck in the DELETE_FAILED state because the dependent object (security group), can't be deleted. This can be for many reasons, for example, the security group could have an ENI attached that’s not part of the CloudFormation stack.
    
    To delete the stack you must choose to delete the stack in the console and then select to retain the resource(s) that failed to delete. This can also be achieved from the AWS CLI:
    
    ![](https://img-b.udemycdn.com/redactor/raw/test_question_description/2022-04-30_04-35-14-3cedd43a9f1f0a220452f4b399842a88.jpg)
    
    **CORRECT:** "Modify the CloudFormation template to retain the security group resource. Then manually delete the resource after deployment" is the correct answer (as explained above.)
    
    **INCORRECT:** "Add a DependsOn attribute to the sg-11223344 resource in the CloudFormation template. Then delete the stack" is incorrect.
    
    This creates a dependency for stack creation. It does not assist with resolving the issue that is preventing the stack from deleting successfully.
    
    **INCORRECT:** "Manually delete the security group. Then execute a change set to force deletion of the CloudFormation stack" is incorrect.
    
    You can manually delete the security group. However, you would not then use a change set to continue with the deletion. You would instead simply choose to delete the stack from the console or the CLI.
    
- Q62
    
    **A company has deployed a REST API using Amazon API Gateway with a Lambda authorizer. The company needs to log who has accessed the API and how the caller accessed the API. They also require logs that include errors and execution traces for the Lambda authorizer.
    Which combination of actions should the Developer take to meet these requirements? (Select TWO.)**
    
    - [ ]  **Enable API Gateway execution logging.(Correct)**
    - [ ]  **Create an API Gateway usage plan.**
    - [x]  **Enable API Gateway access logs.(Correct)**
    - [ ]  **Enable detailed logging in Amazon CloudWatch.**
    - [x]  **Enable server access logging.(Incorrect)**
    
    ### **Explanation**
    
    There are two types of API logging in CloudWatch: execution logging and access logging. In execution logging, API Gateway manages the CloudWatch Logs. The process includes creating log groups and log streams, and reporting to the log streams any caller's requests and responses.
    
    The logged data includes errors or execution traces (such as request or response parameter values or payloads), data used by Lambda authorizers, whether API keys are required, whether usage plans are enabled, and so on.
    
    In access logging, you, as an API Developer, want to log who has accessed your API and how the caller accessed the API. You can create your own log group or choose an existing log group that could be managed by API Gateway.
    
    **CORRECT:** "Enable API Gateway execution logging" is a correct answer.
    
    **CORRECT:** "Enable API Gateway access logs" is also a correct answer.
    
- Q64
    
    **A start-up organization is launching a new website. Which statement correctly describes how to set up the domain, routing, and health checks in AWS?**
    
    - **Use Route 53 to register a domain name and perform routing to the domain and Shield to perform health checks on resources.**
    - **Use Route 53 to register a domain name, route the internet traffic to domain, and specify the values to perform health checks on resources.(Correct)**
    - **Use Route 53 to specify the IP address to perform health checks, register a domain name, and route the internet traffic to domain.(Incorrect)**
    - **Use Route 53 to register a domain name and AWS Certificate Manager to perform routing to the domain and Shield to perform health checks on resources.**
    
    ### **Explanation**
    
    Route 53 can be used as a DNS to register a domain name, route the internet traffic, and perform health checks on resources. If being used for all three tasks, the order of register domain, route the traffic, and perform health checks must be sequential.
    

## Doubtful

- Q15
    
    **A Developer is building a WebSocket API using Amazon API Gateway. The payload sent to this API is JSON that includes an action key which can have multiple values. The Developer must integrate with different routes based on the value of the action key of the incoming JSON payload.
    How can the Developer accomplish this task with the LEAST amount of configuration?**
    
    - **Create a separate stage for each possible value of the action key.**
    - **Set the value of the route selection expression to $default.**
    - **Create a mapping template to map the action key to an integration request.**
    - **Set the value of the route selection expression to $request.body.action.(Correct)**
    
    ### **Explanation**
    
    In your WebSocket API, incoming JSON messages are directed to backend integrations based on routes that you configure. (Non-JSON messages are directed to a $default route that you configure.)
    
    A *route* includes a *route key*, which is the value that is expected once a *route selection expression* is evaluated. The routeSelectionExpression is an attribute defined at the API level. It specifies a JSON property that is expected to be present in the message payload.
    
    For example, if your JSON messages contain an action property and you want to perform different actions based on this property, your route selection expression might be ${request.body.action}. Your routing table would specify which action to perform by matching the value of the action property against the custom route key values that you have defined in the table.
    
- Q51
    
    **Twelve months ago, an organization requested a public certificate for their domain via AWS Certificate Manager (ACM). It was validated using DNS validation. What will ACM do prior to expiration? (Select TWO.)**
    • [ ] **If the certificate was issued by a third party, AWS ACM will send a request to the third party to verify the domain owner.**
    • [ ] **If the certificate is being used by an AWS service and ACM-provided CNAME records are accessible via the public DNS, ACM will consider the domain name validated and send Health events or EventBridge events to notify the owner to renew the certificate.**
    • [ ] **If the certificate was validated through DNS validation with a valid CNAME record provided by ACM and is currently being used by an AWS service, it will use SNS to send notifications of pending expiration.**
    • [x] **If the domain is not validated, it will send Health events or EventBridge events to notify the domain owner prior to expiration.(Correct)**
    • [x] **If the certificate is being used by an AWS service and ACM-provided CNAME records are accessible via the public DNS, ACM will consider the domain name validated and auto renew the certificate.(Correct)**
    
    ### **Explanation**
    
    An AWS ACM certificate that was validated using DNS validation will automatically renew if the certificate is still being using by an AWS service 60 days prior to its expiration and has an ACM-provided CNAME that is accessible via public DNS. If the certificate is not being used or if the CNAME is not correct, ACM will not automatically validate the DNS and will send notifications starting at 45 days prior to the expiration date.
    
- Q57
    
    **A company maintains a REST API service using Amazon API Gateway with native API key validation. The company recently launched a new registration page, which allows users to sign up for the service. The registration page creates a new API key using CreateApiKey and sends the new key to the user. When the user attempts to call the API using this key, the user receives a 403 Forbidden error. Existing users are unaffected and can still call the API.
    What code updates will grant these new users’ access to the API?**
    
    - **The `createUsagePlanKey` method must be called to associate the newly created API key with the correct usage plan(Correct)**
    - **The `importApiKeys` method must be called to import all newly created API keys into the current stage of the API**
    - **The `createDeployment` method must be called so the API can be redeployed to include the newly created API key**
    - **The `updateAuthorizer` method must be called to update the API’s authorizer to include the newly created API key**
    
    ### **Explanation**
    
    A *usage plan* specifies who can access one or more deployed API stages and methods—and also how much and how fast they can access them. The plan uses API keys to identify API clients and meters access to the associated API stages for each key. It also lets you configure throttling limits and quota limits that are enforced on individual client API keys.
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-21_06-18-45-d98c869175c80055460abda8f9de14ff.png)
    
    *API keys* are alphanumeric string values that you distribute to application developer customers to grant access to your API. You can use API keys together with [usage plans](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) or [Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) to control access to your APIs. API Gateway can generate API keys on your behalf, or you can import them from a [CSV file](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-key-file-format.html). You can generate an API key in API Gateway, or import it into API Gateway from an external source.
    
    To associate the newly created key with a usage plan the CreatUsagePlanKey API can be called. This creates a usage plan key for adding an existing API key to a usage plan.