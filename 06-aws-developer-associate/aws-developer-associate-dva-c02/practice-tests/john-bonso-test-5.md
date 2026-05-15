# John Bonso Test 5

## Wrong

- Q2
    
    **A startup is integrating an event-driven alerting tool with a third-party platform. The platform requires a publicly accessible HTTPS endpoint to receive webhook requests, which will be processed by a Lambda function.
    Given that the platform signs each request with a secret key and includes it in the headers, the developer must ensure that the Lambda function executes the domain logic only when a webhook request comes from a valid user.
    Which action would satisfy the requirement with the least amount of development effort?**
    
    - **Configure API Gateway to connect with the Lambda function using a Lambda proxy integration. Create a Lambda function authorizer to validate incoming requests based on a signature provided in the HTTP headers.**
    - **Create a Lambda function URL. Attach a resource-based policy to the function allowing anyone to invoke it only if the `"lambda:CodeSigningConfigArn": "arn:aws:lambda:<AWS_REGION>:<ACCOUNT_NUMBER>:code-signing-config:csc-<SIGNING_SECRET>"` condition is present.(Incorrect)**
    - **Create a Lambda function URL. Attach a resource-based policy to the function allowing anyone to invoke it only if the `"lambda:FunctionUrlAuthType": "NONE"` condition is present. Write a custom authorization logic based on a signature provided in the HTTP headers.(Correct)**
    - **Create a Lambda function URL. Attach a resource-based policy to the function allowing anyone to invoke it only if the `"lambda:FunctionUrlAuthType": "AWS_IAM"` condition is present.**
    
    ### **Explanation**
    
    If you need a simple way to configure an HTTPS endpoint in front of your Lambda function without having to learn and configure additional services besides Lambda, you can use Lambda function URLs. This can be useful in cases where you need to implement a simple webhook handler or form validator that runs within an individual Lambda function and does not require additional functionality beyond processing incoming requests.
    
    By using Lambda function URLs, you can directly invoke your Lambda function using a simple HTTPS request without needing to set up and configure additional services like API Gateway. This approach can be a simple and efficient way to handle incoming requests and integrate with other services or third-party platforms that require a publicly accessible HTTPS endpoint.
    
    There are two types of authorization available for Lambda function URLs:
    
    **AWS_IAM** - the function URL can only be invoked by an IAM user or role with the necessary permissions. This can be useful in cases where you need to restrict access to the Lambda function to a specific set of users or roles within your organization.
    
    **NONE** - anyone can invoke the Lambda function using the URL. This approach can be useful in cases where you want to make the Lambda function publicly accessible and do not require any additional authentication or authorization beyond the URL. However, you may still need to validate the incoming requests in the Lambda function to ensure that the request comes from a trusted source.
    
    By setting the "lambda:FunctionUrlAuthType" condition to "NONE," the function will be publicly accessible without requiring any additional authentication. However, you still need to write custom authorization logic to verify the signature provided in the HTTP headers and ensure that the request is coming from a valid user.
    
- Q4 - important
    
    **A development team has migrated an existing Git repository to a CodeCommit repository. One of the developers was given an HTTPS clone URL of their new repository. The developer must be able to clone the repository using his access key credentials.
    What must the developer do before he can proceed?**
    
    - **Generate an RSA key pair to use with AWS CodeCommit using AWS KMS.**
    - **Import an SSL/TLS certificate into the AWS Certificate Manager.**
    - **Configure the Git credential helper with the AWS credential profile.(Correct)**
    - **Generate an HTTPS Git credential for AWS CodeCommit. Configure the Git credential helper with the AWS credential profile.(Incorrect)**
    
    ### **Explanation**
    
    You can authenticate with CodeCommit (HTTPS) in two ways:
    
    1. Set-up a Git credential helper using your access key credentials specified in your AWS credential profile.
    
    2. Generate HTTPS Git credentials for AWS CodeCommit. Specify the credentials in the Git Credential Manager.
    
    The AWS CLI includes a Git credential helper that you can use with CodeCommit. **The Git credential helper requires an AWS *credential profile*, which stores a copy of an IAM user's access key ID and secret access key** (along with a default AWS Region name and default output format). The Git credential helper uses this information to automatically authenticate with CodeCommit so you don't need to enter this information every time you use Git to interact with CodeCommit.
    
    The option that says: **Generate an HTTPS Git credential for AWS CodeCommit. Configure the Git credential helper with the AWS credential profile** is incorrect. Although this solution works, you still don't have to create HTTPS GIT credentials since you're already using the access key credentials to authenticate with CodeCommit.
    
- Q10 - important
    
    **A developer is building an application that uses Amazon CloudFront to distribute thousands of images stored in an S3 bucket. The developer needs a fast and cost-efficient solution that will allow him to update the images immediately without waiting for the object’s expiration date.
    Which solution meets the requirements?**
    
    - **Update the images by invalidating them from the edge caches.(Incorrect)**
    - **Update the images by using versioned file names.(Correct)**
    - **Disable the CloudFront distribution and re-enable it to update the images in all edge locations.**
    - **Upload the new images in the S3 bucket and wait for the objects in the edge locations to expire to reflect the changes.**
    
    ### **Explanation**
    
    When you update existing files in a CloudFront distribution, AWS recommends that you include some sort of version identifier either in your file names or in your directory names to give yourself better control over your content. This identifier might be a date-time stamp, a sequential number, or some other method of distinguishing two versions of the same object.
    
    ![](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2020/06/07/S3-Blog-3-1024x576.jpg)
    
    For example, instead of naming a graphic file image.jpg, you might call it image_1.jpg. When you want to start serving a new version of the file, you'd name the new file image_2.jpg, and you'd update the links in your web application or website to point to image_2.jpg. Alternatively, you might put all graphics in an images_v1 directory and, when you want to start serving new versions of one or more graphics, you'd create a new images_v2 directory, and you'd update your links to point to that directory. With versioning, you don't have to wait for an object to expire before CloudFront begins to serve a new version of it, and you don't have to pay for object invalidation.
    
    The option that says: **Update the images by invalidating them from the edge caches** is incorrect. While this will update the images, it is not a cost-efficient solution as you have to pay for the additional invalidation requests.
    
- Q12
    
    **An application uses the `PutObject` operation in parallel to upload hundreds of thousands of objects per second to an S3 bucket. To meet security compliance, the developer uses the server-side encryption in AWS KMS (SSE-KMS) to encrypt objects as they get stored in the S3 bucket. There is a noticeable performance degradation after making the change.
    Which of the following is the most likely cause of the problem?**
    
    - **The KMS is not using an alias to easily identify the CMK required for the server-side encryption with AWS KMS (SSE-KMS.)**
    - **The Amazon S3 throttles the `PutObject` operation for objects encrypted with SSE-KMS.**
    - **The API request rate has exceeded the quota for AWS KMS API operations.(Correct)**
    - **The CMK is using an AES 256 algorithm, which makes the encryption process slower. AES 128 should be used instead.(Incorrect)**
    
    ### **Explanation**
    
    **AWS KMS** establishes quotas for the number of API operations requested in each second.
    
    You can make API requests directly or by using an integrated AWS service that makes API requests to AWS KMS on your behalf. The quota applies to both kinds of requests.
    
    For example, you might store data in Amazon S3 using server-side encryption with AWS KMS (SSE-KMS). Each time you upload or download an S3 object that's encrypted with SSE-KMS, Amazon S3 makes a `GenerateDataKey` (for uploads) or `Decrypt` (for downloads) request to AWS KMS on your behalf. These requests count toward your quota, so AWS KMS throttles the requests if you exceed a combined total of 5,500 (or 10,000 or 30,000 depending upon your AWS Region) uploads or downloads per second of S3 objects encrypted with SSE-KMS.
    
- Q13 - important
    
    **A Lamba function has multiple sub-functions that are chained together to process large data synchronously. When invoked, the function tends to exceed its maximum timeout limit. This has prompted the developer to break the Lambda function into manageable coordinated states using Step Functions, enabling each sub-function to run in separate processes.
    Which of the following type of states should the developer use to run processes?**
    
    - **Pass State**
    - **Parallel State(Incorrect)**
    - **Wait State**
    - **Task State(Correct)**
    
    ### **Explanation**
    
    **AWS Step Functions** is a serverless function orchestrator that makes it easy to sequence AWS Lambda functions and multiple AWS services into business-critical applications. Through its visual interface, you can create and run a series of checkpointed and event-driven workflows that maintain the application state. The output of one step acts as an input to the next. Each step in your application executes in order, as defined by your business logic.
    
    Step Functions can help solve the problem of timeout errors of Lambda functions. Imagine a Lambda function that has four utility functions that are run sequentially. Each of those functions takes 5 minutes to finish which translates to a total execution time of 20 minutes. This is a problem since Lambda can only run for a maximum of 15 minutes. To solve this, we can refactor the functions inside the Lambda function into individual Step Functions states. This way, each function is contained in a separate Lambda function, which has its own execution timeout.
    
    ![](https://media.tutorialsdojo.com/public/refactor-lambdafunctions-to-stepfunction-states.jpg)
    
    Individual states can make decisions based on their input, perform actions, and pass output to other states. In AWS Step Functions, you define your workflows in the Amazon States Language. The Step Functions console provides a graphical representation of that state machine to help visualize your application logic.
    
    States are elements in your state machine. A state is referred to by its *name*, which can be any string, but must be unique within the scope of the entire state machine.
    
    States can perform a variety of functions in your state machine:
    
    **Task State** - Do some work in your state machine
    
    **Choice State** - Make a choice between branches of execution
    
    **Fail or Succeed State** - Stop execution with failure or success
    
    **Pass State** - Simply pass its input to its output or inject some fixed data, without performing work.
    
    **Wait State** - Provide a delay for a certain amount of time or until a specified time/date.
    
    **Parallel State** - Begin parallel branches of execution.
    
    **Map State** - Dynamically iterate steps.
    
    Out of all the types of State, only the Task State and the Parallel State can be used to run processes in the state machine. In the given scenario, the application logic inside the Lambda function process data **synchronously**. In this case, **Task State** should be used.
    
    **Parallel State** is incorrect. Although it can be used to run processes in a state machine, this type of state should only be used when you want to run processes **asynchronously**. Parallel state executes each branch concurrently and independently. In the given scenario, the Lambda function processes data synchronously. This means that each output of a function is piped as an input to the next function. The Task State is much more applicable in this scenario.
    
- Q18 - important
    
    **A developer is debugging an issue in an AWS Lambda-based application. To save time searching through logs, the developer wants the function to return the corresponding log location of an invocation request.
    Which approach should the developer take with the least amount of effort?**
    
    - **Extract the log stream name from the `Event` object of the handler function.**
    - **Extract the invocation request id from the `Context` object of the handler function. Then, call the `FilterLogEvents` API and pass the request id to filter results.**
    - **Extract the log stream name from the `Context` object of the handler function.(Correct)**
    - **Extract the invocation request id from the `Event` object of the handler. Call the `FilterLogEvents` API and use the request id to filter results.(Incorrect)**
- Q20
    
    **A developer uses AWS Serverless Application Model (SAM) in a local machine to create a serverless Python application. After defining the required dependencies in the `requirements.txt` file, the developer is now ready to test and deploy.
    What are the steps to successfully deploy the application?**
    
    - **Build the SAM template in the local machine. Run the `sam deploy` command to package and deploy the SAM template from AWS CodeCommit.**
    - **Build the SAM template in the local machine and call the `sam deploy` command to package and deploy the SAM template from an S3 bucket.(Correct)**
    - **Run the `sam init` command. Build the SAM template in the local machine and call the `sam deploy` command to package and deploy the SAM template from an S3 bucket.(Incorrect)**
    - **Upload and build the SAM template in an EC2 instance. Run the `sam deploy` command to package and deploy the SAM template.**
    
    ### **Explanation**
    
    Here are the SAM CLI commands needed to deploy serverless applications:
    
    **`sam init`** - Initializes a serverless application with an AWS SAM template. The template provides a folder structure for your Lambda functions and is connected to an event source such as APIs, S3 buckets, or DynamoDB tables. This application includes everything you need to get started and to eventually extend it into a production-scale application.
    
    **`sam build` -** The `sam build` command builds any dependencies that your application has, and copies your application source code to folders under `.aws-sam/build` to be zipped and uploaded to Lambda.
    
    **`sam deploy`** - performs the functionality of `sam package`. You can use the `sam deploy` command to directly package and deploy your application.
    
    Since the application's runtime and dependencies are already defined, the next step is to call the `sam build` command to install and build the dependencies of the application. After running a series of local tests, you can now package and deploy the SAM template into an S3 bucket via the sam deploy command.
    
- Q23
    
    **A development team needs to deploy an application revision into three environments: Test, Staging, and Production. The application should be deployed into the Test environment first, then Staging, and then Production.
    Which approach will conveniently allow the team to deploy the application into different environments?**
    
    - **Create multiple deployment groups for each environment using AWS CodeDeploy.(Correct)**
    - **Create multiple data pipeline provisions for each environment to deploy the application using the AWS Data Pipeline.(Incorrect)**
    - **Create, configure, and deploy multiple application projects for each environment using CodeBuild.**
    - **Create a repository for each environment in AWS CodeCommit to deploy the application.**
    
    ### **Explanation**
    
    In an EC2/On-Premises deployment, a deployment group is a set of individual instances targeted for deployment. A deployment group contains individually tagged instances, Amazon EC2 instances in Amazon EC2 Auto Scaling groups, or both.
    
    ![](https://media.tutorialsdojo.com/codedeploy-deployment-groups.PNG)
    
    You can associate more than one deployment group with an application in CodeDeploy. This makes it possible to deploy an application revision to different sets of instances at different times. For example, you might use one deployment group to deploy an application revision to a set of instances tagged Test where you ensure the code's quality. Next, you deploy the same application revision to a deployment group with instances tagged Staging for additional verification. Finally, when you are ready to release the latest application to customers, you deploy to a deployment group that includes instances tagged Production.
    
- Q26
    
    **A developer is building an AWS Lambda-based Java application that optimizes pictures uploaded to an S3 bucket. Upon running several tests, the Lambda function shows a cold start of about 5 seconds.
    Which of the following could the developer do to reduce the cold start time? (Select TWO.)**
    
    - [ ]  **Increase the memory allocation setting for the Lambda function.(Correct)**
    - [x]  **Reduce the deployment package’s size by including only the needed modules from the AWS SDK for Java.(Correct)**
    - [ ]  **Run the Lambda function in a VPC to gain access to Amazon’s high-end infrastructure.**
    - [x]  **Increase the timeout setting for the Lambda function.(Incorrect)**
    - [ ]  **Add the Spring Framework to the project and enable dependency injection.**
    
    ### **Explanation**
    
    A cold start happens when a system needs to create a new resource in response to an event/request. Cold starts are not unique to Lambda. There are also cold starts in container orchestration, high-performance computing, or any places where IT resources need to be spun up.
    
    ![](https://media.tutorialsdojo.com/function-lifecycle.PNG)
    
    In AWS Lambda, whenever you execute a helper function/pre-handler code where you need to do things like pulling data from an S3 bucket, connecting to a database, pulling configuration information and dependencies, or anything of the sorts, it gets executed on the INIT code where the partial cold start occurs.
    
    It's important to note that basically everything that you're doing outside of the handler function will block its execution. When it comes to thinking about pre handler code dependencies that you want to use, remember that less is more. The more targeted you are at the resource that you include, the better the overall performance your function will have during its execution.
    
    You also have the option to tweak the power of the resources that run your function by increasing the memory allocated to your function to optimize its overall performance.
    
- Q47 - confusing wording
    
    **A Development team is building a fault-tolerant solution for a web application hosted on Amazon EC2. The session data is stored globally but it is cached in the instance’s memory for better performance. The solution aims to ensure that no user requests are lost during a session in case an EC2 instance is terminated or has failed a health check.
    Which solution best fits the requirement with the least effort?**
    
    - **Use an Elastic Load Balancer and configure sticky sessions.(Correct)**
    - **Use the DynamoDB Session Handler to save session data.**
    - **Use an Elastic Load Balancer and configure connection draining.(Incorrect)**
    - **Create an SQS queue to store session data.**
    
    ### **Explanation**
    
    When a particular request reaches a given EC2 instance, the instance must retrieve information about the user from state data that must be stored globally. There’s no opportunity for the instance to cache any data since the odds of receiving several requests from the same user/browser decreases as more instances are added to the load balancer.
    
    With the sticky session feature, it is possible to instruct the load balancer to route repeated requests to the same EC2 instance whenever possible.
    
    ![](http://d1nqddva888cns.cloudfront.net/elb_sticky.png)
    
    In this case, the instances can cache user data locally for better performance. A series of requests from the user will be routed to the same EC2 instance if possible. If an instance fails or becomes unhealthy, the load balancer stops routing requests to that instance and chooses a new healthy instance based on the existing load balancing algorithm. The load balancer treats the session as now "stuck" to the new healthy instance, and continues routing requests to that instance even if the failed instance comes back.
    
- Q48 - important
    
    **A San Francisco-based tech startup is building a cross-platform mobile app that can notify the user of upcoming astronomical events. Your mobile app authenticates with the Identity Provider (IdP) using the provider's SDK and Amazon Cognito. Once the end-user is authenticated with the IdP, the OAuth or OpenID Connect token returned from the IdP is passed by your app to Amazon Cognito.
    Which of the following is returned for the user to provide a set of temporary, limited-privilege AWS credentials?**
    
    - **Cognito SDK**
    - **Cognito API**
    - **Cognito ID(Correct)**
    - **Cognito Key Pair(Incorrect)**
    
    ### **Explanation**
    
    You can use Amazon Cognito to deliver temporary, limited-privilege credentials to your application so that your users can access AWS resources. Amazon Cognito identity pools support both authenticated and unauthenticated identities. You can retrieve a unique Amazon Cognito identifier (identity ID) for your end-user immediately if you're allowing unauthenticated users or after you've set the login tokens in the credentials provider if you're authenticating users.
    
- Q51
    
    **A Ruby developer is looking to offload some of the processing on his application to the AWS cloud without managing any servers. The submodules must be written in Ruby, which mainly invokes API calls to an external web service. The response from the API call is parsed and stored in a MongoDB database.
    What should he do to develop the Lambda function in his preferred programming language?**
    
    - **Create a Lambda function on Ruby with a custom runtime and use the AWS SDK for Ruby.**
    - **Create a Lambda function with a custom runtime to use Ruby. Then include the runtime in the function's deployment package. Migrate it to a layer that you manage independently from the function.(Incorrect)**
    - **Create a Lambda function with a supported runtime version for Ruby.(Correct)**
    - **Create a Lambda function using the AWS SDK for Ruby.**
    
    ### **Explanation**
    
    AWS Lambda **natively supports Java, Go, PowerShell, Node.js, C#, Python, and Ruby.**
    
- Q54 - information
    
    **A developer is building a ReactJS application that will be hosted on Amazon S3. Amazon Cognito handles the registration and signing of users using the AWS Software Development Kit (SDK) for JavaScript. The JSON Web Token (JWT) received upon authentication will be stored on the browser's local storage. After signing in, the application will use the JWT as an authorizer to access an API Gateway endpoint.
    What are the steps needed to implement the scenario above? (Select THREE.)**
    
    - [x]  **Set the name of the header that will be used from the request to the Cognito Identity Pool as a token source for authorization.(Incorrect)**
    - [x]  **On the API Gateway Console, create an authorizer using the Cognito User Pool ID.(Correct)**
    - [ ]  **Set the name of the header that will be used from the request to the Cognito User Pool as a token source for authorization.(Correct)**
    - [ ]  **Choose and set the authentication provider for your website.**
    - [ ]  **Create an Amazon Cognito Identity Pool.**
    - [x]  **Create an Amazon Cognito User Pool.(Correct)**
    
    ### **Explanation**
    
    As an alternative to using IAM roles and policies or **Lambda Authorizers** (formerly known as custom authorizers), you can use an **Amazon Cognito User Pool** to control who can access your API in Amazon API Gateway.
    
    To use an Amazon Cognito user pool with your API, you must first create an authorizer of the `COGNITO_USER_POOLS` type and then configure an API method to use that authorizer. After the API is deployed, the client must first sign the user into the user pool, obtain an identity or access token for the user, and then call the API method with one of the tokens, which are typically set to the request's Authorization header. The API call succeeds only if the required token is supplied and the supplied token is valid, otherwise, the client isn't authorized to make the call because the client did not have credentials that could be authorized.
    
    The option that says: **Set the name of the header that will be used from the request to the Cognito Identity Pool as a token source for authorization** is incorrect because Cognito Identity Pool cannot be used as an authorizer for API Gateway. You should use the Cognito User Pool.
    
- Q57 - silly
    
    **Private documents have to be securely stored in an S3 Standard-IA bucket. These documents must be encrypted at rest, and the encryption keys should be rotated every 365 days.
    Which encryption method is the easiest to implement?**
    
    - **Use OpenSSL to generate an encryption key and import it into AWS KMS with automatic annual key rotation enabled.**
    - **Use a customer managed KMS key and enable automatic annual key rotation.(Correct)**
    - **Generate a symmetric key using an external library and use that to encrypt the data before sending it to the S3 bucket. Write a script that will automate the key rotation.**
    - **Use the AWS owned key for S3 to encrypt data.(Incorrect)**
    
    ### **Explanation**
    
    The option that says: **Use the AWS Owned Key for S3 to encrypt data** is incorrect. AWS Owned keys are KMS keys that an AWS service owns and manages for use in multiple AWS accounts. You cannot control nor modify the key rotation for AWS Owned keys.
    

## Doubtful

- Q5
    
    **A startup plans to use Amazon Cognito User Pools to easily manage their users' sign-up and sign-in workflows to an application. To save time from designing the User Interface (UI) for the login page, the development team has decided to use Cognito's built-in UI. However, the product manager finds the UI bland and instructed the developer to include the product logo on the web page.
    How should the developer meet the above requirements?**
    
    - **Upload the logo to the Amazon Cognito app settings and use that logo on the custom login page.(Correct)**
    - **Create a login page with the product logo and upload it to an S3 bucket. Point the S3 endpoint in the Cognito app settings.**
    - **Upload the logo to an S3 bucket and point the S3 endpoint on the custom login page.**
    - **Create a login page with the product logo and upload it to Amazon Cognito.**
- Q30
    
    **A developer plans to use AWS Elastic Beanstalk to deploy a microservice application. The application will be implemented in a multi-container Docker environment.
    How should the developer configure the container definitions in the environment?**
    
    - **Configure the container definitions in the `Dockerrun.aws.json.config` and put it inside the .ebextensions folder.**
    - **Use the `eb config` command to configure the container definitions.**
    - **Configure the container definitions in the Amazon ECS Console when building the Docker environment.**
    - **Configure the container definitions in the `Dockerrun.aws.json` file.(Correct)**
- Q37 - important
    
    **An AWS Site-to-Site VPN connection that uses Border Gateway Protocol (BGP) is used to establish a connection between an on-premises server and multiple EC2 instances in a VPC. A Developer cannot connect to an instance in subnet A but can access an instance in subnet B.
    Which action should the developer do as the first step in troubleshooting?**
    
    - **Check the BGP Logs if the traffic is reaching subnet A.**
    - **Check the AWS CloudTrail Logs if the traffic is reaching subnet A.**
    - **Check the VPN Logs if the traffic is reaching subnet A.**
    - **Check the VPC Flow Logs if the traffic is reaching subnet A.(Correct)**
    
    ### **Explanation**
    
    **VPC Flow Logs** is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon CloudWatch Logs or Amazon S3. After you've created a flow log, you can retrieve and view its data in the chosen destination.
    
    ![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2019/09/13/2019-08-13_10-41-04.png)
    
    Flow Logs for Amazon Virtual Private Cloud enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow Logs data can be published to Amazon CloudWatch Logs or Amazon Simple Storage Service (S3).
    
    Hence, the correct answer is: **Check the VPC Flow Logs if the traffic is reaching subnet A.**
    
    The option that says: **Check the BGP Logs if the traffic is reaching subnet A** is incorrect because you can only collect BGP logs on the customer gateway device outside the AWS network. In the scenario, there's no connection problem between the on-premises network and the AWS network since the developer is able to access a subnet inside the VPC.
    
    The option that says: **Check the AWS CloudTrail Logs if the traffic is reaching subnet A** is incorrect as this is only used to gain insight into the API activities in an AWS account.
    
    The option that says: **Check the VPN Logs if the traffic is reaching subnet A** is incorrect because you can't directly view VPN logs. You have to use AWS CloudWatch to monitor the VPN tunnel by collecting and processing raw data from the VPN service into readable, near real-time metrics. Additionally, it is more logical to view the VPC Flow Logs since the problem lies at the subnet level which is within the VPC.
    
- Q53 - important
    
    **An application has a feature that displays GIFs based on keyword inputs. The code streams random GIF links from an external API to your local machine. When run, the application's process takes longer than expected. You are suspecting that the new function `sendRequest()` you added is the culprit.
    Which of the following actions should you do to determine the latency of the function?**
    
    - **Use CloudTrail to record and store event logs for actions made by your function.**
    - **Using AWS X-Ray, disable sampling to efficiently trace all requests for calls.**
    - **Using CloudWatch, troubleshoot the issue by checking the logs.**
    - **Using AWS X-Ray, define an arbitrary subsegment inside the code to instrument the function.(Correct)**
    
    ### **Explanation**
    
    AWS X-ray analyzes and debugs production, distributed applications, such as those built using a microservices architecture. With, X-Ray, you can identify performance bottlenecks, edge case errors, and other hard to detect issues.
    
    A segment can break down the data about the work done into **subsegments**. Subsegments provide more granular timing information and details about downstream calls that your application made to fulfill the original request. A subsegment can contain additional details about a call to an AWS service, an external HTTP API, or an SQL database. **You can define arbitrary subsegments to instrument specific functions or lines of code in your application**.
    
    Subsegments extend a trace's segment with details about work done in order to serve a request. Each time you make a call with an instrumented client, the X-Ray SDK records the information generated in a subsegment. You can create additional subsegments to group other subsegments, to measure the performance of a section of code, or to record annotations and metadata.
    
    ![](https://media-tutorials-dojo.s3-ap-southeast-2.amazonaws.com/pic.PNG)
    
- Q58
    
    **A developer is writing a web application that will allow users to save and retrieve images in an Amazon S3 bucket. The users are required to register and log in to access the application.
    Which combination of AWS Services should the Developer utilize for implementing the user authentication module of the application?**
    
    - **Amazon Cognito Identity Pools and User Pools.(Correct)**
    - **Amazon User Pools and AWS Security Token Service (STS)**
    - **Amazon Cognito User Pools and AWS Key Management Service (KMS)**
    - **Amazon Cognito Identity Pools and IAM Role.**
    
    ### **Explanation**
    
    **Amazon User Pools and AWS Security Token Service (STS)** are incorrect. While it is true that you need AWS STS to allow users to access Amazon S3, it is already abstracted by the Amazon Cognito Identity Pools. That being said, you have to configure an Identity Pool to accept users federated with your Cognito User Pool.