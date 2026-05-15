# Neal Davis Test 3

## Wrong

- Q10
    
    **An application has been instrumented to use the AWS X-Ray SDK to collect data about the requests the application serves. The Developer has set the user field on segments to a string that identifies the `user` who sent the request.
    How can the Developer search for segments associated with specific users?**
    
    - **Use a filter expression to search for the `user` field in the segment metadata**
    - **By using the `GetTraceSummaries` API with a filter expression(Correct)**
    - **By using the `GetTraceGraph` API with a filter expression**
    - **Use a filter expression to search for the `user` field in the segment annotations(Incorrect)**
    
    ### **Explanation**
    
    A subset of segment fields are indexed by X-Ray for use with filter expressions. For example, if you set the user field on a segment to a unique identifier, you can search for segments associated with specific users in the X-Ray console or by using the `GetTraceSummaries` API.
    
    **CORRECT:** "By using the `GetTraceSummaries` API with a filter expression" is the correct answer.
    
    **INCORRECT:** "By using the `GetTraceGraph` API with a filter expression" is incorrect as this API action retrieves a service graph for one or more specific trace IDs.
    
    **INCORRECT:** "Use a filter expression to search for the `user` field in the segment metadata" is incorrect as the `user` field is not part of the segment metadata and metadata is not is not indexed for search.
    
    **INCORRECT:** "Use a filter expression to search for the `user` field in the segment annotations" is incorrect as the `user` field is not part of the segment annotations.
    
- Q35
    
    **An application that processes financial transactions receives thousands of transactions each second. The transactions require end-to-end encryption, and the application implements this by using the AWS KMS GenerateDataKey operation. During operation the application receives the following error message:
    *“You have exceeded the rate at which you may call KMS. Reduce the frequency of your calls.*
    *(Service: AWSKMS; Status Code: 400; Error Code: ThrottlingException; Request ID: <ID>”*
    Which actions are best practices to resolve this error? (Select TWO.)**
    
    - [x]  **Create a local cache using the AWS Encryption SDK and the LocalCryptoMaterialsCache feature.(Correct)**
    - [ ]  **Create a case in the AWS Support Center to increase the quota for the account.(Correct)**
    - [x]  **Call the AWS KMS Encrypt operation directly to allow AWS KMS to encrypt the data.(Incorrect)**
    - [ ]  **Create an AWS KMS custom key store and generate data keys through AWS CloudHSM.**
    - [ ]  **Use Amazon SQS to queue the requests and configure AWS KMS to poll the queue.**
    
    ### **Explanation**
    
    To ensure that AWS KMS can provide fast and reliable responses to API requests from all customers, it throttles API requests that exceed certain boundaries. *Throttling* occurs when AWS KMS rejects an otherwise valid request and returns a ThrottlingException error.
    
    *Data key caching* stores data keys and related cryptographic material in a cache. When you encrypt or decrypt data, the AWS Encryption SDK looks for a matching data key in the cache. If it finds a match, it uses the cached data key rather than generating a new one. Data key caching can improve performance, reduce cost, and help you stay within service limits as your application scales.
    
    Your application can benefit from data key caching if:
    
    - It can reuse data keys.
    - It generates numerous data keys.
    - Your cryptographic operations are unacceptably slow, expensive, limited, or resource-intensive.
    
    To create an instance of the local cache, use the LocalCryptoMaterialsCache constructor in Java and Python, the getLocalCryptographicMaterialsCache function in JavaScript, or the aws_cryptosdk_materials_cache_local_new constructor in C.
    
    Additionally, the developer can request an increase in the quota for AWS KMS which will provide the ability to submit more API calls the AWS KMS.
    
- Q44
    
    **A company is planning to use AWS CodeDeploy to deploy a new AWS Lambda function
    What are the MINIMUM properties required in the 'resources' section of the AppSpec file for CodeDeploy to deploy the function successfully?**
    
    - **name, alias, currentversion, and targetversion(Correct)**
    - **TaskDefinition, LoadBalancerInfo, and ContainerPort**
    - **TaskDefinition, PlatformVersion, and ContainerName**
    - **name, alias, PlatformVersion, and type(Incorrect)**
    
    ### **Explanation**
    
    The content in the 'resources' section of the AppSpec file varies, depending on the compute platform of your deployment. The 'resources' section for an AWS Lambda deployment contains the name, alias, current version, and target version of a Lambda function.
    
    Here is an example of a 'resources' section with the minimum required properties:
    
    ![](https://img-b.udemycdn.com/redactor/raw/test_question_description/2022-04-30_07-11-12-a81cd00fae3f3338c68bdeaa23ac61f5.jpg)
    
- Q45
    
    **An application uses an Auto Scaling group of Amazon EC2 instances, an Application Load Balancer (ALB), and an Amazon Simple Queue Service (SQS) queue. An Amazon CloudFront distribution caches content for global users. A Developer needs to add in-transit encryption to the data by configuring end-to-end SSL between the CloudFront Origin and the end users.
    How can the Developer meet this requirement? (Select TWO.)**
    
    - [ ]  **Add a certificate to the Auto Scaling Group**
    - [ ]  **Create an Origin Access Identity (OAI)**
    - [ ]  **Configure the Viewer Protocol Policy(Correct)**
    - [x]  **Create an encrypted distribution(Incorrect)**
    - [x]  **Configure the Origin Protocol Policy(Correct)**
    
    ### **Explanation**
    
    To enable SSL between the origin and the distribution the Developer can configure the Origin Protocol Policy. Depending on the domain name used (CloudFront default or custom), the steps are different. To enable SSL between the end-user and CloudFront the Viewer Protocol Policy should be configured.
    
- Q59
    
    **A company needs to provide additional security for their APIs deployed on Amazon API Gateway. They would like to be able to authenticate their customers with a token. What is the SAFEST way to do this?**
    
    - **Create an API Gateway Lambda authorizer(Correct)**
    - **Use AWS Single Sign-on to authenticate the customers**
    - **Setup usage plans and distribute API keys to the customers(Incorrect)**
    - **Create an Amazon Cognito identity pool**
    
    ### **Explanation**
    
    A *Lambda authorizer* (formerly known as a *custom authorizer*) is an API Gateway feature that uses a Lambda function to control access to your API.
    
    A Lambda authorizer is useful if you want to implement a custom authorization scheme that uses a bearer token authentication strategy such as OAuth or SAML, or that uses request parameters to determine the caller's identity.
    
    There are two types of Lambda authorizers:
    
    A *token-based* Lambda authorizer (also called a TOKEN authorizer) receives the caller's identity in a bearer token, such as a JSON Web Token (JWT) or an OAuth token.
    
    A *request parameter-based* Lambda authorizer (also called a REQUEST authorizer) receives the caller's identity in a combination of headers, query string parameters, stageVariables, and $context variables.
    
    For this scenario, a Lambda authorizer is the most secure method available. It can also be used with usage plans and AWS recommend that you don’t rely only on API keys, so a Lambda authorizer is a better solution.
    
    **CORRECT:** "Create an API Gateway Lambda authorizer" is the correct answer.
    
    **INCORRECT:** "Setup usage plans and distribute API keys to the customers" is incorrect as this is not the most secure (safest) option. AWS recommend that you don't rely on API keys as your only means of authentication and authorization for your APIs.
    
- Q65
    
    **A Developer is creating an AWS Lambda function that will process data from an Amazon Kinesis data stream. The function is expected to be invoked 50 times per second and take 100 seconds to complete each request.
    What MUST the Developer do to ensure the functions runs without errors?**
    
    - **Contact AWS and request to increase the limit for concurrent executions(Correct)**
    - **Increase the concurrency limit for the function**
    - **No action is required as AWS Lambda can easily accommodate this requirement(Incorrect)**
    - **Implement exponential backoff in the function code**
    
    To calculate the concurrency requirements for this scenario, simply multiply the invocation requests per second (50) with the average execution time in seconds (100). This calculation is 50 x 100 = 5,000.
    
    Therefore, 5,000 concurrent executions is over the default limit and the Developer will need to request in the AWS Support Center console.
    

## Doubtful

- Q6
    
    **A developer is creating a microservices application that includes and AWS Lambda function. The function generates a unique file for each execution and must commit the file to an AWS CodeCommit repository.
    How should the developer accomplish this?**
    
    - **Send a message to an Amazon SQS queue with the file attached. Configure an AWS Step Function as a destination for messages in the queue. Configure the Step Function to add the new file to the repository and commit the change.**
    - **After the new file is created in Lambda, use CURL to invoke the CodeCommit API. Send the file to the repository and automatically commit the change.**
    - **Use an AWS SDK to instantiate a CodeCommit client. Invoke the PutFile method to add the file to the repository and execute a commit with CreateCommit.(Correct)**
    - **Upload the new file to an Amazon S3 bucket. Create an AWS Step Function to accept S3 events. Use AWS Lambda functions in the Step Function, to add the file to the repository and commit the change.**
    
    ### **Explanation**
    
    The developer can instantiate a CodeCommit client using the AWS SDK. This provides the ability to programmatically work with the AWS CodeCommit repository. The PutFile method is used to add or modify a single file in a specified repository and branch. The CreateCommit method creates a commit for changes to a repository.
    
    **INCORRECT:** "After the new file is created in Lambda, use CURL to invoke the CodeCommit API. Send the file to the repository and automatically commit the change" is incorrect.
    
    CURL cannot be used to work with the CodeCommit API. The developer must use the AWS SDK.
    
    **INCORRECT:** "Upload the new file to an Amazon S3 bucket. Create an AWS Step Function to accept S3 events. Use AWS Lambda functions in the Step Function, to add the file to the repository and commit the change" is incorrect.
    
    Step Functions is not a supported destination for Amazon S3 event notifications. Supported destinations are SNS topics, SQS queues, Lambda functions, and EventBridge event buses.
    
- Q18
    
    **The development team is working on an API that will be served from Amazon API Gateway. The API will serve three environments PROD, DEV, and TEST and requires a cache size of 250GB. What is the MOST cost-efficient deployment strategy?**
    
    - **Create a single API Gateway with three stages and enable the cache for the DEV and TEST environments only when required(Correct)**
    - **Create three API Gateways, one for each environment and enable the cache for the DEV and TEST environments only when required**
    - **Create a single API Gateway with three stages and enable the cache for all environments**
    - **Create a single API Gateway with three deployments and configure a global cache of 250GB**
    
    ### **Explanation**
    
    You can enable API caching in Amazon API Gateway to cache your endpoint's responses. With caching, you can reduce the number of calls made to your endpoint and also improve the latency of requests to your API.
    
    Caching is enabled for a stage. When you enable caching for a stage, API Gateway caches responses from your endpoint for a specified time-to-live (TTL) period, in seconds. API Gateway then responds to the request by looking up the endpoint response from the cache instead of making a request to your endpoint.
    
    The default TTL value for API caching is 300 seconds. The maximum TTL value is 3600 seconds. TTL=0 means caching is disabled.
    
    In this scenario we are asked to choose the most cost-efficient solution. Therefore, the best answer is to use a single API Gateway with three stages and, as caching is enabled per stage, we can choose to save cost by only enabling the cache on DEV and TEST when we need to perform tests relating to that functionality.
    
    **CORRECT:** "Create a single API Gateway with three stages and enable the cache for the DEV and TEST environments only when required" is the correct answer.
    
    **INCORRECT:** "Create three API Gateways, one for each environment and enable the cache for the DEV and TEST environments only when required" is incorrect. It is unnecessary to create separate API Gateways. This will increase complexity. Instead we can choose to use stages for the different environments.
    
    **INCORRECT:** "Create a single API Gateway with three stages and enable the cache for all environments" is incorrect as this would not be the most cost-efficient option.
    
    **INCORRECT:** "Create a single API Gateway with three deployments and configure a global cache of 250GB" is incorrect. When you deploy you API, you do so to a stage. Caching is enabled at the stage level, not globally.
    
- Q34
    
    **A Developer needs to create an instance profile for an Amazon EC2 instance using the AWS CLI. How can this be achieved? (Select THREE.)**
    
    - [x]  **Run the `aws iam add-role-to-instance-profile` command(Correct)**
    - [ ]  **Run the `CreateInstanceProfile` API**
    - [ ]  **Run the `AssignInstanceProfile` API**
    - [x]  **Run the `aws iam create-instance-profile` command(Correct)**
    - [x]  **Run the `aws ec2 associate-instance-profile` command(Correct)**
    - [ ]  **Run the `AddRoleToInstanceProfile` API**
    
    ### **Explanation**
    
    To add a role to an Amazon EC2 instance using the AWS CLI you must first create an instance profile. Then you need to add the role to the instance profile and finally assign the instance profile to the Amazon EC2 instance.
    
    The following example commands would achieve this outcome:
    
    `1. aws iam create-instance-profile --instance-profile-name EXAMPLEPROFILENAME
    2. aws iam add-role-to-instance-profile --instance-profile-name EXAMPLEPROFILENAME --role-name EXAMPLEROLENAME
    3. aws ec2 associate-iam-instance-profile --iam-instance-profile Name=EXAMPLEPROFILENAME --instance-id i-012345678910abcde`