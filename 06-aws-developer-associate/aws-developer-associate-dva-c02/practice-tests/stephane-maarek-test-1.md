# Stephane Maarek Test 1

## Wrong

- Q8
    
    **Amazon Simple Queue Service (SQS) has a set of APIs for various actions supported by the service.
    As a developer associate, which of the following would you identify as correct regarding the `CreateQueue` API? (Select two)**
    
    - [x]  **The dead-letter queue of a FIFO queue must also be a FIFO queue. Whereas, the dead-letter queue of a standard queue can be a standard queue or a FIFO queue(Incorrect)**
    - [ ]  **The visibility timeout value for the queue is in seconds, which defaults to 30 seconds(Correct)**
    - [x]  **You can't change the queue type after you create it(Correct)**
    - [ ]  **The length of time, in seconds, for which the delivery of all messages in the queue is delayed is configured using `MessageRetentionPeriod` attribute**
    - [ ]  **Queue tags are case insensitive. A new tag with a key identical to that of an existing tag overwrites the existing tag**
    
    ### **Explanation**
    
    Correct options:
    
    **You can't change the queue type after you create it** - You can't change the queue type after you create it and you can't convert an existing standard queue into a FIFO queue. You must either create a new FIFO queue for your application or delete your existing standard queue and recreate it as a FIFO queue.
    
    **The visibility timeout value for the queue is in seconds, which defaults to 30 seconds** - The visibility timeout for the queue is in seconds. Valid values are: An integer from 0 to 43,200 (12 hours), the Default value is 30.
    
    Incorrect options:
    
    **The dead-letter queue of a FIFO queue must also be a FIFO queue. Whereas, the dead-letter queue of a standard queue can be a standard queue or a FIFO queue** - The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a standard queue must also be a standard queue.
    
- Q9 - overlooked the detail
    
    **A development team wants to build an application using serverless architecture. The team plans to use AWS Lambda functions extensively to achieve this goal. The developers of the team work on different programming languages like Python, .NET and Javascript. The team wants to model the cloud infrastructure using any of these programming languages.
    Which AWS service/tool should the team use for the given use-case?**
    
    - **AWS Serverless Application Model (SAM)(Incorrect)**
    - **AWS CodeDeploy**
    - **AWS Cloud Development Kit (CDK)(Correct)**
    - **AWS CloudFormation**
- Q16
    
    **You have deployed a Java application to an EC2 instance where it uses the X-Ray SDK. When testing from your personal computer, the application sends data to X-Ray but when the application runs from within EC2, the application fails to send data to X-Ray.
    Which of the following does NOT help with debugging the issue?**
    
    - **CloudTrail(Incorrect)**
    - **EC2 Instance Role**
    - **X-Ray sampling(Correct)**
    - **EC2 X-Ray Daemon**
    
    ### **Explanation**
    
    Correct option:
    
    **X-Ray sampling**
    
    By customizing sampling rules, you can control the amount of data that you record, and modify sampling behavior on the fly without modifying or redeploying your code. Sampling rules tell the X-Ray SDK how many requests to record for a set of criteria. X-Ray SDK applies a sampling algorithm to determine which requests get traced however because our application is failing to send data to X-Ray it does not help in determining the cause of failure.
    
    **CloudTrail** - You can check CloudTrail to see if any API call is being denied on X-Ray.
    
- Q30 - important
    
    **The development team has just configured and attached the IAM policy needed to access AWS Billing and Cost Management for all users under the Finance department. But, the users are unable to see AWS Billing and Cost Management service in the AWS console.
    What could be the reason for this issue?**
    
    - **You need to activate IAM user access to the Billing and Cost Management console for all the users who need access(Correct)**
    - **Only root user has access to AWS Billing and Cost Management console**
    - **The users might have another policy that restricts them from accessing the Billing information(Incorrect)**
    - **IAM user should be created under AWS Billing and Cost Management and not under AWS account to have access to Billing console**
    
    ### **Explanation**
    
    Correct option:
    
    **You need to activate IAM user access to the Billing and Cost Management console for all the users who need access** - By default, IAM users do not have access to the AWS Billing and Cost Management console.
    
- Q35
    
    **As a developer, you are working on creating an application using AWS Cloud Development Kit (CDK).
    Which of the following represents the correct order of steps to be followed for creating an app using AWS CDK?**
    
    - **Create the app from a template provided by AWS CloudFormation -> Add code to the app to create resources within stacks -> Build the app (optional) -> Synthesize one or more stacks in the app -> Deploy stack(s) to your AWS account(Incorrect)**
    - **Create the app from a template provided by AWS CDK -> Add code to the app to create resources within stacks -> Synthesize one or more stacks in the app -> Deploy stack(s) to your AWS account -> Build the app**
    - **Create the app from a template provided by AWS CDK -> Add code to the app to create resources within stacks -> Build the app (optional) -> Synthesize one or more stacks in the app -> Deploy stack(s) to your AWS account(Correct)**
    - **Create the app from a template provided by AWS CloudFormation -> Add code to the app to create resources within stacks -> Synthesize one or more stacks in the app -> Deploy stack(s) to your AWS account -> Build the app**
    
    ### **Explanation**
    
    Correct option:
    
    **Create the app from a template provided by AWS CDK -> Add code to the app to create resources within stacks -> Build the app (optional) -> Synthesize one or more stacks in the app -> Deploy stack(s) to your AWS account**
    
    The standard AWS CDK development workflow is similar to the workflow you're already familiar as a developer. There are a few extra steps:
    
    1. Create the app from a **template provided by AWS CDK** - Each AWS CDK app should be in its own directory, with its own local module dependencies. Create a new directory for your app. Now initialize the app using the `cdk init` command, specifying the desired template ("app") and programming language. The `cdk init` command creates a number of files and folders inside the created home directory to help you organize the source code for your AWS CDK app.
    2. Add code to the app to create resources within stacks - Add custom code as is needed for your application.
    3. Build the app (optional) - In most programming environments, after making changes to your code, you'd build (compile) it. This isn't strictly necessary with the AWS CDK—the Toolkit does it for you so you can't forget. But you can still build manually whenever you want to catch syntax and type errors.
    4. Synthesize one or more stacks in the app to create an AWS CloudFormation template - Synthesize one or more stacks in the app to create an AWS CloudFormation template. The synthesis step catches logical errors in defining your AWS resources. If your app contains more than one stack, you'd need to specify which stack(s) to synthesize.
    5. Deploy one or more stacks to your AWS account - It is optional (though good practice) to synthesize before deploying. The AWS CDK synthesizes your stack before each deployment. If your code has security implications, you'll see a summary of these and need to confirm them before deployment proceeds. `cdk deploy` is used to deploy the stack using CloudFormation templates. This command displays progress information as your stack is deployed. When it's done, the command prompt reappears.
- Q36 - important
    
    **You are creating a Cloud Formation template to deploy your CMS application running on an EC2 instance within your AWS account. Since the application will be deployed across multiple regions, you need to create a map of all the possible values for the base AMI.
    How will you invoke the `!FindInMap` function to fulfill this use case?**
    
    - **`!FindInMap [ MapName, TopLevelKey ]`(Incorrect)**
    - **`!FindInMap [ MapName ]`**
    - **`!FindInMap [ MapName, TopLevelKey, SecondLevelKey ]`(Correct)**
    - **`!FindInMap [ MapName, TopLevelKey, SecondLevelKey, ThirdLevelKey ]`**
    
    ### **Explanation**
    
    Correct option:
    
    **`!FindInMap [ MapName, TopLevelKey, SecondLevelKey ]`** - The intrinsic function Fn::FindInMap returns the value corresponding to keys in a two-level map that is declared in the Mappings section. YAML Syntax for the full function name: Fn::FindInMap: [ MapName, TopLevelKey, SecondLevelKey ]
    
- Q38 - important
    
    **A startup with newly created AWS account is testing different EC2 instances. They have used Burstable performance instance - T2.micro - for 35 seconds and stopped the instance.
    At the end of the month, what is the instance usage duration that the company is charged for?**
    
    - **60 seconds**
    - **30 seconds**
    - **35 seconds(Incorrect)**
    - **0 seconds(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    Burstable performance instances, which are T3, T3a, and T2 instances, are designed to provide a baseline level of CPU performance with the ability to burst to a higher level when required by your workload. Burstable performance instances are the only instance types that use credits for CPU usage.
    
    **0 seconds** - AWS states that, if your AWS account is less than 12 months old, you can use a t2.micro instance for free within certain usage limits.
    
- Q51 - important
    
    **An e-commerce company has developed an API that is hosted on Amazon ECS. Variable traffic spikes on the application are causing order processing to take too long. The application processes orders using Amazon SQS queues. The `ApproximateNumberOfMessagesVisible` metric spikes at very high values throughout the day which triggers the CloudWatch alarm. Other ECS metrics for the API containers are well within limits.
    As a Developer Associate, which of the following will you recommend for improving performance while keeping costs low?**
    
    - **Use ECS service scheduler**
    - **Use backlog per instance metric with target tracking scaling policy(Correct)**
    - **Use Docker swarm**
    - **Use ECS step scaling policy(Incorrect)**
    
    ### **Explanation**
    
    Correct option:
    
    **Use backlog per instance metric with target tracking scaling policy** - If you use a target tracking scaling policy based on a custom Amazon SQS queue metric, dynamic scaling can adjust to the demand curve of your application more effectively.
    
    **Use ECS step scaling policy** - Although Amazon ECS Service Auto Scaling supports using Application Auto Scaling step scaling policies, AWS recommends using target tracking scaling policies instead. For example, if you want to scale your service when CPU utilization falls below or rises above a certain level, create a target tracking scaling policy based on the CPU utilization metric provided by Amazon ECS.
    
    With step scaling policies, you create and manage the CloudWatch alarms that trigger the scaling process. If the target tracking alarms don't work for your use case, you can use step scaling. You can also use target tracking scaling with step scaling for an advanced scaling policy configuration. For example, you can configure a more aggressive response when utilization reaches a certain level.
    
    Step Scaling scales your cluster on various lengths of steps based on different ranges of thresholds. Target tracking on the other hand intelligently picks the smart lengths needed for the given configuration.
    
- Q65
    
    Question 65:
    
    **Incorrect**
    
    **A multi-national company has multiple business units with each unit having its own AWS account. The development team at the company would like to debug and trace data across accounts and visualize it in a centralized account.
    As a Developer Associate, which of the following solutions would you suggest for the given use-case?**
    
    - **CloudWatch Events(Incorrect)**
    - **X-Ray(Correct)**
    - **CloudTrail**
    - **VPC Flow Logs**
    
    ### **Explanation**
    
    Correct option:
    
    **X-Ray**
    
    **You can use X-Ray to collect data across AWS Accounts**. The X-Ray agent can assume a role to publish data into an account different from the one in which it is running. This enables you to publish data from various components of your application into a central account.
    
    **CloudWatch Events**: Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources. These help to trigger notifications based on changes happening in AWS services. You cannot use CloudWatch **Events** to debug and trace data across accounts.
    

## Doubtful

- Q7 - important
    
    **A multi-national company has just moved to AWS Cloud and it has configured forecast-based AWS Budgets alerts for cost management. However, no alerts have been received even though the account and the budgets have been created almost three weeks ago.
    What could be the issue with the AWS Budgets configuration?**
    
    - **AWS requires approximately 5 weeks of usage data to generate budget forecasts(Correct)**
    - **Amazon CloudWatch could be down and hence alerts are not being sent**
    - **Budget forecast has been created from an account that does not have enough privileges**
    - **Account has to be part of AWS Organizations to receive AWS Budgets alerts**
- Q13
    
    **CodeCommit is a managed version control service that hosts private Git repositories in the AWS cloud.
    Which of the following credential types is NOT supported by IAM for CodeCommit?**
    
    - **AWS Access Keys**
    - **IAM username and password(Correct)**
    - **Git credentials**
    - **SSH Keys**
- Q21 - important
    
    **After a test deployment in ElasticBeanstalk environment, a developer noticed that all accumulated Amazon EC2 burst balances were lost.
    Which of the following options can lead to this behavior?**
    
    - **The deployment was either run with immutable updates or in traffic splitting mode(Correct)**
    - **When a canary deployment fails, it resets the EC2 burst balances to zero**
    - **The deployment was run as a Rolling deployment, resulting in the resetting of EC2 burst balances**
    - **The deployment was run as a All-at-once deployment, flushing all the accumulated EC2 burst balances**
- Q24
    
    **An application is hosted by a 3rd party and exposed at yourapp.3rdparty.com. You would like to have your users access your application using www.mydomain.com, which you own and manage under Route 53.
    What Route 53 record should you create?**
    
    - **Create an Alias Record**
    - **Create a CNAME record(Correct)**
    - **Create an A record**
    - **Create a PTR record**
- Q32 - important
    
    **Which of the following security credentials can only be created by the AWS Account root user?**
    
    - **CloudFront Key Pairs(Correct)**
    - **EC2 Instance Key Pairs**
    - **IAM User passwords**
    - **IAM User Access Keys**
    
    ### **Explanation**
    
    Correct option:
    
    For Amazon CloudFront, you use key pairs to create signed URLs for private content, such as when you want to distribute restricted content that someone paid for.
    
    **CloudFront Key Pairs** - IAM users can't create CloudFront key pairs. You must log in using root credentials to create key pairs.
    
    To create signed URLs or signed cookies, you need a signer. A signer is either a trusted key group that you create in CloudFront, or an AWS account that contains a CloudFront key pair. AWS recommends that you use trusted key groups with signed URLs and signed cookies instead of using CloudFront key pairs.
    
- Q34
    
    **When running a Rolling deployment in Elastic Beanstalk environment, only two batches completed the deployment successfully, while rest of the batches failed to deploy the updated version. Following this, the development team terminated the instances from the failed deployment.
    What will be the status of these failed instances post termination?**
    
    - **Elastic Beanstalk will not replace the failed instances**
    - **Elastic Beanstalk will replace the failed instances after the application version to be installed is manually chosen from AWS Console**
    - **Elastic Beanstalk will replace the failed instances with instances running the application version from the oldest successful deployment**
    - **Elastic Beanstalk will replace the failed instances with instances running the application version from the most recent successful deployment(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    **Elastic Beanstalk will replace them with instances running the application version from the most recent successful deployment**
    
    When processing a batch, Elastic Beanstalk detaches all instances in the batch from the load balancer, deploys the new application version, and then reattaches the instances. If you enable connection draining, Elastic Beanstalk drains existing connections from the Amazon EC2 instances in each batch before beginning the deployment.
    
    If a deployment fails after one or more batches completed successfully, the completed batches run the new version of your application while any pending batches continue to run the old version. You can identify the version running on the instances in your environment on the health page in the console. This page displays the deployment ID of the most recent deployment that was executed on each instance in your environment. If you terminate instances from the failed deployment, Elastic Beanstalk replaces them with instances running the application version from the most recent successful deployment.
    
- Q42
    
    **A cybersecurity firm wants to run their applications on single-tenant hardware to meet security guidelines.
    Which of the following is the MOST cost-effective way of isolating their Amazon EC2 instances to a single tenant?**
    
    - **Dedicated Instances(Correct)**
    - **Dedicated Hosts**
    - **Spot Instances**
    - **On-Demand Instances**
    
    ### **Explanation**
    
    Correct option:
    
    **Dedicated Instances** - Dedicated Instances are Amazon EC2 instances that run in a virtual private cloud (VPC) on hardware that's dedicated to a single customer. Dedicated Instances that belong to different AWS accounts are physically isolated at a hardware level, even if those accounts are linked to a single-payer account. However, Dedicated Instances may share hardware with other instances from the same AWS account that are not Dedicated Instances.
    
    **Dedicated Hosts** - An Amazon EC2 Dedicated Host is a physical server with EC2 instance capacity fully dedicated to your use. Dedicated Hosts allow you to use your existing software licenses on EC2 instances. With a Dedicated Host, you have visibility and control over how instances are placed on the server. This option is costlier than the Dedicated Instance and hence is not the right choice for the current requirement.
    
- Q44 - important
    
    **A development team lead is configuring policies for his team at an IT company.
    Which of the following policy types only limit permissions but cannot grant permissions (Select two)?**
    
    - [ ]  **Identity-based policy**
    - [x]  **Permissions boundary(Correct)**
    - [ ]  **Access control list (ACL)**
    - [ ]  **Resource-based policy**
    - [x]  **AWS Organizations Service Control Policy (SCP)(Correct)**
    
    ### **Explanation**
    
    Correct options:
    
    **AWS Organizations Service Control Policy (SCP)** – Use an AWS Organizations Service Control Policy (SCP) to define the maximum permissions for account members of an organization or organizational unit (OU). SCPs limit permissions that identity-based policies or resource-based policies grant to entities (users or roles) within the account, but do not grant permissions.
    
    **Permissions boundary** - Permissions boundary is a managed policy that is used for an IAM entity (user or role). The policy defines the maximum permissions that the identity-based policies can grant to an entity, but does not grant permissions.
    
- Q55
    
    **A development team lead is responsible for managing access for her IAM principals. At the start of the cycle, she has granted excess privileges to users to keep them motivated for trying new things. She now wants to ensure that the team has only the minimum permissions required to finish their work.
    Which of the following will help her identify unused IAM roles and remove them without disrupting any service?**
    
    - **Amazon Inspector**
    - **AWS Trusted Advisor**
    - **Access Advisor feature on IAM console(Correct)**
    - **IAM Access Analyzer**
- Q57
    
    **In addition to regular sign-in credentials, AWS supports Multi-Factor Authentication (MFA) for accounts with privileged access.
    Which of the following MFA mechanisms is NOT for root user authentication?**
    
    - **SMS text message-based MFA(Correct)**
    - **Hardware MFA device**
    - **Virtual MFA devices**
    - **U2F security key**
- Q62
    
    **An organization has offices across multiple locations and the technology team has configured an Application Load Balancer across targets in multiple Availability Zones. The team wants to analyze the incoming requests for latencies and the client's IP address patterns.
    Which feature of the Load Balancer will help collect the required information?**
    
    - **ALB access logs(Correct)**
    - **CloudWatch metrics**
    - **CloudTrail logs**
    - **ALB request tracing**
    
    ### **Explanation**
    
    Correct option:
    
    **ALB access logs** - Elastic Load Balancing provides access logs that capture detailed information about requests sent to your load balancer. Each log contains information such as the time the request was received, the client's IP address, latencies, request paths, and server responses. You can use these access logs to analyze traffic patterns and troubleshoot issues. Access logging is an optional feature of Elastic Load Balancing that is disabled by default.