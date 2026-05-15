# Neal Davis Test 4

## Wrong

- Q2
    
    **A company is developing a game for the Android and iOS platforms. The mobile game will securely store user game history and other data locally on the device. The company would like users to be able to use multiple mobile devices and synchronize data between devices.
    Which service can be used to synchronize the data across mobile devices without the need to create a backend application?**
    
    - **Amazon DynamoDB(Incorrect)**
    - **AWS Lambda**
    - **Amazon API Gateway**
    - **Amazon Cognito(Correct)**
    
    ### **Explanation**
    
    Amazon Cognito lets you save end user data in datasets containing key-value pairs. This data is associated with an Amazon Cognito identity, so that it can be accessed across logins and devices. To sync this data between the Amazon Cognito service and an end user’s devices, invoke the synchronize method. Each dataset can have a maximum size of 1 MB. You can associate up to 20 datasets with an identity.
    
    The Amazon Cognito Sync client creates a local cache for the identity data. Your app talks to this local cache when it reads and writes keys. This guarantees that all of your changes made on the device are immediately available on the device, even when you are offline. When the synchronize method is called, changes from the service are pulled to the device, and any local changes are pushed to the service. At this point the changes are available to other devices to synchronize.
    
- Q27
    
    **An AWS Lambda function requires several environment variables with secret values. The secret values should be obscured in the Lambda console and API output even for users who have permission to use the key.
    What is the best way to achieve this outcome and MINIMIZE complexity and latency?**
    
    - **Encrypt the secret values with a customer-managed CMK(Incorrect)**
    - **Use an external encryption infrastructure to encrypt the values and add them as environment variables**
    - **Store the encrypted values in an encrypted Amazon S3 bucket and reference them from within the code**
    - **Encrypt the secret values client-side using encryption helpers(Correct)**
    
    ### **Explanation**
    
    You can use environment variables to store secrets securely for use with Lambda functions. Lambda always encrypts environment variables at rest.
    
    Additionally, you can use the following features to customize how environment variables are encrypted.
    
    - **Key configuration** – On a per-function basis, you can configure Lambda to use an encryption key that you create and manage in AWS Key Management Service. These are referred to as *customer managed* customer master keys (CMKs) or customer managed keys. If you don't configure a customer managed key, Lambda uses an AWS managed CMK named aws/lambda, which Lambda creates in your account.
    - **Encryption helpers** – The Lambda console lets you encrypt environment variable values client side, before sending them to Lambda. This enhances security further by preventing secrets from being displayed unencrypted in the Lambda console, or in function configuration that's returned by the Lambda API. The console also provides sample code that you can adapt to decrypt the values in your function handler.
    
    The configuration for using encryption helps to encrypt data client-side looks like this:
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-25_00-50-15-1e05fef0cb751da67a515a336b9ce91c.jpg)
    
    This is the best way to achieve this outcome and minimizes complexity as the encryption infrastructure will still use AWS KMS and be able to decrypt the values during function execution.
    
    **CORRECT:** "Encrypt the secret values client-side using encryption helpers" is the correct answer.
    
    **INCORRECT:** "Encrypt the secret values with a customer-managed CMK" is incorrect as this alone will not achieve the desired outcome as the environment variables should be encrypted client-side with the encryption helper to ensure users cannot see the secret values.
    
- Q34
    
    **A mobile application has hundreds of users. Each user may use multiple devices to access the application. The Developer wants to assign unique identifiers to these users regardless of the device they use.
    Which of the following methods should be used to obtain unique identifiers?**
    
    - **Assign IAM users and roles to the users. Use the unique IAM resource ID as the unique identifier**
    - **Implement developer-authenticated identities by using Amazon Cognito, and get credentials for these identities(Correct)**
    - **Create a user table in Amazon DynamoDB as key-value pairs of users and their devices. Use these keys as unique identifiers**
    - **Use IAM-generated access key IDs for the users as the unique identifier, but do not store secret keys(Incorrect)**
    
    ### **Explanation**
    
    Amazon Cognito supports developer authenticated identities, in addition to web identity federation. With developer authenticated identities, you can register and authenticate users via your own existing authentication process, while still using Amazon Cognito to synchronize user data and access AWS resources.
    
    Using developer authenticated identities involves interaction between the end user device, your backend for authentication, and Amazon Cognito.
    
    Therefore, the Developer can implement developer-authenticated identities by using Amazon Cognito, and get credentials for these identities.
    
    **CORRECT:** "Implement developer-authenticated identities by using Amazon Cognito, and get credentials for these identities" is the correct answer.
    
    **INCORRECT:** "Create a user table in Amazon DynamoDB as key-value pairs of users and their devices. Use these keys as unique identifiers" is incorrect as this solution would require additional application logic and would be more complex.
    
    **INCORRECT:** "Use IAM-generated access key IDs for the users as the unique identifier, but do not store secret keys" is incorrect as it is not a good practice to provide end users of mobile applications with IAM user accounts and access keys. Cognito is a better solution for this use case.
    
- Q37
    
    **A Developer manages a monitoring service for a fleet of IoT sensors in a major city. The monitoring application uses an Amazon Kinesis Data Stream with a group of EC2 instances processing the data. Amazon CloudWatch custom metrics show that the instances a reaching maximum processing capacity and there are insufficient shards in the Data Stream to handle the rate of data flow.
    What course of action should the Developer take to resolve the performance issues?**
    
    - **Increase the number of EC2 instances to match the number of shards(Incorrect)**
    - **Increase the EC2 instance size**
    - **Increase the number of open shards**
    - **Increase the EC2 instance size and add shards to the stream(Correct)**
    
    ### **Explanation**
    
    **INCORRECT:** "Increase the number of EC2 instances to match the number of shards" is incorrect as you can have an individual instance running multiple KCL workers.
    
- Q38 - must read
    
    **An organization has a new AWS account and is setting up IAM users and policies. According to AWS best practices, which of the following strategies should be followed? (Select TWO.)**
    
    - [x]  **Create standalone policies instead of using inline policies(Correct)**
    - [ ]  **Use user accounts to delegate permissions**
    - [ ]  **Create user accounts that can be shared for efficiency**
    - [ ]  **Use groups to assign permissions to users(Correct)**
    - [x]  **Always use customer managed policies instead of AWS managed policies(Incorrect)**
    
    ### **Explanation**
    
    AWS provide a number of best practices for AWS IAM that help you to secure your resources. The key best practices referenced in this scenario are as follows:
    
    - Use groups to assign permissions to users – this is correct as you should create permissions policies and assign them to groups. Users can be added to the groups to get the permissions they need to perform their jobs.
    - Create standalone policies instead of using inline policies ([Use Customer Managed Policies Instead of Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#best-practice-managed-vs-inline) in the AWS best practices) – this refers to creating your own policies that are standalone policies which can be reused multiple times (assigned to multiple entities such as groups, and users). This is better than using inline policies which are directly attached to a single entity.
    
    **CORRECT:** "Use groups to assign permissions to users" is the correct answer.
    
    **CORRECT:** "Create standalone policies instead of using inline policies" is the correct answer.
    
    **INCORRECT:** "Use user accounts to delegate permissions" is incorrect as you should use roles to delegate permissions.
    
    **INCORRECT:** "Create user accounts that can be shared for efficiency" is incorrect as you should not share user accounts. Always create individual user accounts.
    
    **INCORRECT:** "Always use customer managed policies instead of AWS managed policies" is incorrect as this is not a best practice. AWS recommend getting started by using AWS managed policies ([Get Started Using Permissions with AWS Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)).
    

## Doubtful

- Q29
    
    **A team of Developers require access to an AWS account that is a member account in AWS Organizations. The administrator of the master account needs to restrict the AWS services, resources, and API actions that can be accessed by the users in the account.
    What should the administrator create?**
    
    - **A Consolidated Billing account**
    - **A Service Control Policy (SCP)(Correct)**
    - **A Tag Policy**
    - **An Organizational Unit**
    
    ### **Explanation**
    
    As an administrator of the master account of an organization, you can use service control policies (SCPs) to specify the maximum permissions for member accounts in the organization.
    
- Q32
    
    **A developer is building a multi-tier web application that accesses an Amazon RDS MySQL database. The application must use a credentials to connect and these need to be stored securely. The application will take care of secret rotation.
    Which AWS service represents the LOWEST cost solution for storing credentials?**
    
    - **AWS Systems Manager Parameter Store(Correct)**
    - **AWS Key Management Service (KMS)**
    - **AWS Secrets Manager**
    - **AWS IAM with the Security Token Service (STS)**
    
    ### **Explanation**
    
    AWS Systems Manager Parameter Store provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, and license codes as parameter values. It is highly scalable, available, and durable.
    
    You can store values as plaintext (unencrypted data) or ciphertext (encrypted data). You can then reference values by using the unique name that you specified when you created the parameter.
    
    There are no additional charges for using SSM Parameter Store. However, there are limit of 10,000 parameters per account
    
    **CORRECT:** "AWS Systems Manager Parameter Store" is the correct answer.
    
    **INCORRECT:** "AWS IAM with the Security Token Service (STS)" is incorrect as the application is using credentials to connect, it is not using IAM.
    
    **INCORRECT:** "AWS Secrets Manager" is incorrect as it is not the lowest cost solution as it is a chargeable service. Secrets Manager performs native key rotation; however, this isn’t required in this scenario as the application is handling credential rotation.
    
- Q48
    
    **A serverless application is used to process customer information and outputs a JSON file to an Amazon S3 bucket. AWS Lambda is used for processing the data. The data is sensitive and should be encrypted.
    How can a Developer modify the Lambda function to ensure the data is encrypted before it is uploaded to the S3 bucket?**
    
    - **Use the S3 managed key and call the `GenerateDataKey` API to encrypt the file**
    - **Enable server-side encryption on the S3 bucket and create a policy to enforce encryption**
    - **Use the default KMS key for S3 and encrypt the file using the Lambda code**
    - **Use the `GenerateDataKey` API, then use the data key to encrypt the file using the Lambda code(Correct)**
    
    ### **Explanation**
    
    The `GenerateDataKey` API is used with the AWS KMS services and generates a unique symmetric data key. This operation returns a plaintext copy of the data key and a copy that is encrypted under a customer master key (CMK) that you specify. You can use the plaintext key to encrypt your data outside of AWS KMS and store the encrypted data key with the encrypted data.
    
    For this scenario we can use `GenerateDataKey` to obtain an encryption key from KMS that we can then use within the function code to encrypt the file. This ensures that the file is encrypted BEFORE it is uploaded to Amazon S3.
    
    **CORRECT:** "Use the `GenerateDataKey` API, then use the data key to encrypt the file using the Lambda code" is the correct answer.
    
    **INCORRECT:** "Enable server-side encryption on the S3 bucket and create a policy to enforce encryption" is incorrect. This would not encrypt data before it is uploaded as S3 would only encrypt the data as it is written to storage.
    
    **INCORRECT:** "Use the S3 managed key and call the `GenerateDataKey` API to encrypt the file" is incorrect as you do not use an encryption key to call KMS. You call KMS with the `GenerateDataKey` API to obtain an encryption key. Also, the S3 managed key can only be used within the S3 service.
    
    **INCORRECT:** "Use the default KMS key for S3 and encrypt the file using the Lambda code" is incorrect. You cannot use the default KMS key for S3 within the Lambda code as it can only be used within the S3 service.
    
- Q49
    
    **A mobile application is being developed that will use AWS Lambda, Amazon API Gateway and Amazon DynamoDB. A developer would like to securely authenticate the users of the mobile application and then grant them access to the API.
    What is the BEST way to achieve this?**
    
    - **Create a Lambda authorizer in API Gateway**
    - **Create a `COGNITO_USER_POOLS` authorizer in API Gateway(Correct)**
    - **Create an IAM authorizer in API Gateway**
    - **Create a `COGNITO_IDENTITY_POOLS` authorizer in API Gateway**
    
    ### **Explanation**
    
    **Explanation:**
    
    A user pool is a user directory in Amazon Cognito. With a user pool, your users can sign into your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers. Whether your users sign in directly or through a third party, all members of the user pool have a directory profile that you can access through a Software Development Kit (SDK).
    
    As an alternative to using IAM roles and policies or Lambda authorizers (formerly known as custom authorizers), you can use an Amazon Cognito user pool to control who can access your API in Amazon API Gateway.
    
    To use an Amazon Cognito user pool with your API, you must first create an authorizer of the COGNITO_USER_POOLS type and then configure an API method to use that authorizer. After the API is deployed, the client must first sign the user in to the user pool, obtain an identity or access token for the user, and then call the API method with one of the tokens, which are typically set to the request's Authorization header. The API call succeeds only if the required token is supplied and the supplied token is valid, otherwise, the client isn't authorized to make the call because the client did not have credentials that could be authorized.
    
- Q50
    
    **A Developer is creating a service on Amazon ECS and needs to ensure that each task is placed on a different container instance.
    How can this be achieved?**
    
    - **Use a task placement strategy**
    - **Use a task placement constraint(Correct)**
    - **Create a cluster with multiple container instances**
    - **Create a service on Fargate**
    
    ### **Explanation**
    
    A *task placement constraint* is a rule that is considered during task placement. Task placement constraints can be specified when either running a task or creating a new service.
    
    Amazon ECS supports the following types of task placement constraints:
    
    `distinctInstance`
    
    Place each task on a different container instance. This task placement constraint can be specified when either running a task or creating a new service.
    
    `memberOf`
    
    Place tasks on container instances that satisfy an expression. For more information about the expression syntax for constraints, see [Cluster Query Language](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html).
    
    The `memberOf` task placement constraint can be specified with the following actions:
    
    Running a task
    
    Creating a new service
    
    Creating a new task definition
    
    Creating a new revision of an existing task definition
    
    The following code can be used in a task definition to specify a task placement constraint that ensures that each task will run on a distinct instance:
    
    `1. "placementConstraints": [
    2. {
    3. "type": "distinctInstance"
    4. }
    5. ]`
    
    **CORRECT:** "Use a task placement constraint" is the correct answer.
    
    **INCORRECT:** "Use a task placement strategy" is incorrect as this is used to select instances for task placement using the binpack, random and spread algorithms.
    
- Q62
    
    **A web application is using Amazon Kinesis Data Streams for ingesting IoT data that is then stored before processing for up to 24 hours.How can the Developer implement encryption at rest for data stored in Amazon Kinesis Data Streams?**
    
    - **Use the Amazon Kinesis Consumer Library (KCL) to encrypt the data**
    - **Enable server-side encryption on Kinesis Data Streams with an AWS KMS CMK(Correct)**
    - **Add a certificate and enable SSL/TLS connections to Kinesis Data Streams**
    - **Encrypt the data once it is at rest with an AWS Lambda function**
    
    ### **Explanation**
    
    Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.
    
    Server-side encryption is a feature in Amazon Kinesis Data Streams that automatically encrypts data before it's at rest by using an AWS KMS customer master key (CMK) you specify. Data is encrypted before it's written to the Kinesis stream storage layer and decrypted after it’s retrieved from storage. As a result, your data is encrypted at rest within the Kinesis Data Streams service. This allows you to meet strict regulatory requirements and enhance the security of your data.
    
    With server-side encryption, your Kinesis stream producers and consumers don't need to manage master keys or cryptographic operations. Your data is automatically encrypted as it enters and leaves the Kinesis Data Streams service, so your data at rest is encrypted. AWS KMS provides all the master keys that are used by the server-side encryption feature. AWS KMS makes it easy to use a CMK for Kinesis that is managed by AWS, a user-specified AWS KMS CMK, or a master key imported into the AWS KMS service.
    
    Therefore, in this scenario the Developer can enable server-side encryption on Kinesis Data Streams with an AWS KMS CMK
    
    **CORRECT:** "Enable server-side encryption on Kinesis Data Streams with an AWS KMS CMK" is the correct answer.
    
    **INCORRECT:** "Add a certificate and enable SSL/TLS connections to Kinesis Data Streams" is incorrect as SSL/TLS is already used with Kinesis (you don’t need to add a certificate) and this only provides encryption in-transit, not encryption at rest.
    
    **INCORRECT:** "Use the Amazon Kinesis Consumer Library (KCL) to encrypt the data" is incorrect. The KCL provides design patterns and code for Amazon Kinesis Data Streams consumer applications. The KCL is not used for adding encryption to the data in a stream.
    
    **INCORRECT:** "Encrypt the data once it is at rest with an AWS Lambda function" is incorrect as this is unnecessary when Kinesis natively supports server-side encryption.