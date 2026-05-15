# Course Complementary test

## Wrong

- Q3
    
    **A Developer at a company is working on a CloudFormation template to set up resources. Resources will be defined using code and provisioned based on certain conditions.
    Which section of a CloudFormation template does not allow for conditions?**
    
    - **Outputs**
    - **Conditions(Incorrect)**
    - **Resources**
    - **Parameters(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    **Parameters**
    
    Conditions cannot be used within the Parameters section. After you define all your conditions, you can associate them with resources and resource properties only in the Resources and Outputs sections of a template.
    
    Incorrect options:
    
    **Resources** - Resources section describes the resources that you want to provision in your AWS CloudFormation stacks. You can associate conditions with the resources that you want to conditionally create.
    
    **Conditions** - You actually define conditions in this section of the CloudFormation template
    
    **Outputs** - The optional Outputs section declares output values that you can import into other stacks (to create cross-stack references), return in response (to describe stack calls), or view on the AWS CloudFormation console. For example, you can output the S3 bucket name for a stack to make the bucket easier to find. You can associate conditions with the outputs that you want to conditionally create.
    
- Q47 - out of context
    
    **A large firm stores its static data assets on Amazon S3 buckets. Each service line of the firm has its own AWS account. For a business use case, the Finance department needs to give access to their S3 bucket's data to the Human Resources department.
    Which of the below options is NOT feasible for cross-account access of S3 bucket objects?**
    
    - **Use Resource-based Access Control List (ACL) and IAM policies for programmatic-only access to S3 bucket objects(Incorrect)**
    - **Use IAM roles and resource-based policies delegate access across accounts within different partitions via programmatic access only(Correct)**
    - **Use Cross-account IAM roles for programmatic and console access to S3 bucket objects**
    - **Use Resource-based policies and AWS Identity and Access Management (IAM) policies for programmatic-only access to S3 bucket objects**
    
    ### **Explanation**
    
    Correct option:
    
    **Use IAM roles and resource-based policies delegate access across accounts within different partitions via programmatic access only** - This statement is incorrect and hence the right choice for this question. IAM roles and resource-based policies delegate access across accounts only within a single partition. For example, assume that you have an account in US West (N. California) in the standard `aws` partition. You also have an account in China (Beijing) in the `aws-cn` partition. You can't use an Amazon S3 resource-based policy in your account in China (Beijing) to allow access for users in your standard AWS account.
    
    Incorrect options:
    
    **Use Resource-based policies and AWS Identity and Access Management (IAM) policies for programmatic-only access to S3 bucket objects** - Use bucket policies to manage cross-account control and audit the S3 object's permissions. If you apply a bucket policy at the bucket level, you can define who can access (Principal element), which objects they can access (Resource element), and how they can access (Action element). Applying a bucket policy at the bucket level allows you to define granular access to different objects inside the bucket by using multiple policies to control access. You can also review the bucket policy to see who can access objects in an S3 bucket.
    
    **Use Resource-based Access Control List (ACL) and IAM policies for programmatic-only access to S3 bucket objects** - Use object ACLs to manage permissions only for specific scenarios and only if ACLs meet your needs better than IAM and S3 bucket policies. Amazon S3 ACLs allow users to define only the following permissions sets: READ, WRITE, READ_ACP, WRITE_ACP, and FULL_CONTROL. You can use only an AWS account or one of the predefined Amazon S3 groups as a grantee for the Amazon S3 ACL.
    
    **Use Cross-account IAM roles for programmatic and console access to S3 bucket objects** - Not all AWS services support resource-based policies. This means that you can use cross-account IAM roles to centralize permission management when providing cross-account access to multiple services. Using cross-account IAM roles simplifies provisioning cross-account access to S3 objects that are stored in multiple S3 buckets, removing the need to manage multiple policies for S3 buckets. This method allows cross-account access to objects that are owned or uploaded by another AWS account or AWS services. If you don't use cross-account IAM roles, the object ACL must be modified.
    
- Q48
    
    **A junior developer working on ECS instances terminated a container instance in Amazon Elastic Container Service (Amazon ECS) as per instructions from the team lead. But the container instance continues to appear as a resource in the ECS cluster.
    As a Developer Associate, which of the following solutions would you recommend to fix this behavior?**
    
    - **The container instance has been terminated with AWS CLI, whereas, for ECS instances, Amazon ECS CLI should be used to avoid any synchronization issues(Incorrect)**
    - **You terminated the container instance while it was in STOPPED state, that lead to this synchronization issues(Correct)**
    - **You terminated the container instance while it was in RUNNING state, that lead to this synchronization issues**
    - **A custom software on the container instance could have failed and resulted in the container hanging in an unhealthy state till restarted again**
    
    ### **Explanation**
    
    Correct option:
    
    **You terminated the container instance while it was in STOPPED state, that lead to this synchronization issues** - If you terminate a container instance while it is in the STOPPED state, that container instance isn't automatically removed from the cluster. You will need to deregister your container instance in the STOPPED state by using the Amazon ECS console or AWS Command Line Interface. Once deregistered, the container instance will no longer appear as a resource in your Amazon ECS cluster.
    
- Q53
    
    **Your company has been hired to build a resilient mobile voting app for an upcoming music award show that expects to have 5 to 20 million viewers. The mobile voting app will be marketed heavily months in advance so you are expected to handle millions of messages in the system. You are configuring Amazon Simple Queue Service (SQS) queues for your architecture that should receive messages from 20 KB to 200 KB.
    Is it possible to send these messages to SQS?**
    
    - **No, the max message size is 64KB**
    - **Yes, the max message size is 512KB**
    - **No, the max message size is 128KB(Incorrect)**
    - **Yes, the max message size is 256KB(Correct)**
    
- Q54 - good question
    
    **You are working for a technology startup building web and mobile applications. You would like to pull Docker images from the ECR repository called `demo` so you can start running local tests against the latest application version.
    Which of the following commands must you run to pull existing Docker images from ECR? (Select two)**
    
    - [ ]  **`docker build -t 1234567890.dkr.ecr.eu-west-1.amazonaws.com/demo:latest`**
    - [x]  **`docker login -u $AWS_ACCESS_KEY_ID -p $AWS_SECRET_ACCESS_KEY`(Incorrect)**
    - [ ]  **`aws docker push 1234567890.dkr.ecr.eu-west-1.amazonaws.com/demo:latest`**
    - [ ]  **`$(aws ecr get-login --no-include-email)`(Correct)**
    - [x]  **`docker pull 1234567890.dkr.ecr.eu-west-1.amazonaws.com/demo:latest`(Correct)**
    
    ### **Explanation**
    
    Correct options:
    
    **`$(aws ecr get-login --no-include-email)`**
    
    **`docker pull 1234567890.dkr.ecr.eu-west-1.amazonaws.com/demo:latest`**
    
    The get-login command retrieves a token that is valid for a specified registry for 12 hours, and then it prints a docker login command with that authorization token. You can execute the printed command to log in to your registry with Docker, or just run it automatically using the $() command wrapper. After you have logged in to an Amazon ECR registry with this command, you can use the Docker CLI to push and pull images from that registry until the token expires. The docker pull command is used to pull an image from the ECR registry.
    
- Q55 - good question
    
    **Your company leverages Amazon CloudFront to provide content via the internet to customers with low latency. Aside from latency, security is another concern and you are looking for help in enforcing end-to-end connections using HTTPS so that content is protected.
    Which of the following options is available for HTTPS in AWS CloudFront?**
    
    - **Between clients and CloudFront only(Incorrect)**
    - **Neither between clients and CloudFront nor between CloudFront and backend**
    - **Between CloudFront and backend only**
    - **Between clients and CloudFront as well as between CloudFront and backend(Correct)**
    
- Q56 - good question
    
    **A multi-national company maintains separate AWS accounts for different verticals in their organization. The project manager of a team wants to migrate the Elastic Beanstalk environment from Team A's AWS account into Team B's AWS account. As a Developer, you have been roped in to help him in this process.
    Which of the following will you suggest?**
    
    - **It is not possible to migrate Elastic Beanstalk environment from one AWS account to the other**
    - **Create an export configuration from the Elastic Beanstalk console from Team A's account. This configuration has to be shared with the IAM Role of Team B's account. The import option of Team B's account will show the saved configuration, that can be used to create a new Beanstalk application(Incorrect)**
    - **Create a saved configuration in Team A's account and configure it to Export. Now, log into Team B's account and choose the Import option. Here, you need to specify the name of the saved configuration and allow the system to create the new application. This takes a little time based on the Regions the two accounts belong to**
    - **Create a saved configuration in Team A's account and download it to your local machine. Make the account-specific parameter changes and upload to the S3 bucket in Team B's account. From Elastic Beanstalk console, create an application from 'Saved Configurations'(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    **Create a saved configuration in Team A's account and download it to your local machine. Make the account-specific parameter changes and upload to the S3 bucket in Team B's account. From Elastic Beanstalk console, create an application from 'Saved Configurations** - You must use saved configurations to migrate an Elastic Beanstalk environment between AWS accounts. You can save your environment's configuration as an object in Amazon Simple Storage Service (Amazon S3) that can be applied to other environments during environment creation, or applied to a running environment. Saved configurations are YAML formatted templates that define an environment's platform version, tier, configuration option settings, and tags.
    
    Download the saved configuration to your local machine. Change your account-specific parameters in the downloaded configuration file, and then save the changes. For example, change the key pair name, subnet ID, or application name (such as application-b-name). Upload the saved configuration from your local machine to an S3 bucket in Team B's account. From this account, create a new Beanstalk application by choosing 'Saved Configurations' from the navigation panel.
    
    Incorrect options:
    
    **Create a saved configuration in Team A's account and configure it to Export. Now, log into Team B's account and choose the Import option. Here, you need to specify the name of the saved configuration and allow the system to create the new application. This takes a little time based on the Regions the two accounts belong to** - There is no direct Export and Import option for migrating Elastic Beanstalk configurations.
    

## Doubtful

- Q26
    
    **You are working for a shipping company that is automating the creation of ECS clusters with an Auto Scaling Group using an AWS CloudFormation template that accepts cluster name as its parameters. Initially, you launch the template with input value 'MainCluster', which deployed five instances across two availability zones. The second time, you launch the template with an input value 'SecondCluster'. However, the instances created in the second run were also launched in 'MainCluster' even after specifying a different cluster name.
    What is the root cause of this issue?**
    
    - **The ECS agent Docker image must be re-built to connect to the other clusters**
    - **The cluster name Parameter has not been updated in the file /etc/ecs/ecs.config during bootstrap(Correct)**
    - **The security groups on the EC2 instance are pointing to the wrong ECS cluster**
    - **The EC2 instance is missing IAM permissions to join the other clusters**
    
    ### **Explanation**
    
    Correct option:
    
    **The cluster name Parameter has not been updated in the file /etc/ecs/ecs.config during bootstrap** - In the ecs.config file you have to configure the parameter ECS_CLUSTER='your_cluster_name' to register the container instance with a cluster named 'your_cluster_name'.
    
    Sample config for ECS Container Agent:
    
    ![](https://media.datacumulus.com/aws-dva-pt/assets/pt3-q35-i1.jpg)
    
- Q30
    
    **You were assigned to a project that requires the use of the AWS CLI to build a project with AWS CodeBuild. Your project's root directory includes the buildspec.yml file to run build commands and would like your build artifacts to be automatically encrypted at the end.
    How should you configure CodeBuild to accomplish this?**
    
    - **Specify a KMS key to use(Correct)**
    - **Use In Flight encryption (SSL)**
    - **Use the AWS Encryption SDK**
    - **Use an AWS Lambda Hook**
    
- Q44
    
    **A client has hired you as an AWS Certified Developer Associate for a consulting project. The client wants to weigh their options of choosing between an Amazon SQS standard queue and Amazon Simple Workflow Service (SWF).
    Which of the following statements are correct regarding the two services? (Select two)**
    
    - [ ]  **SQS has task-oriented APIs and SWF has message-oriented APIs**
    - [x]  **SWF ensures the task is assigned only once while SQS may deliver the message multiple times(Correct)**
    - [x]  **SWF has task-oriented APIs and SQS has message-oriented APIs(Correct)**
    - [ ]  **SQS ensures the task is assigned only once while SWF may deliver the message multiple times**
    - [ ]  **SWF offers synchronous programming option whereas SQS offers an asynchronous facility**
- Q65
    
    **Your team-mate has configured an Amazon S3 event notification for an S3 bucket that holds sensitive audit data of a firm. As the Team Lead, you are receiving the SNS notifications for every event in this bucket. After validating the event data, you realized that few events are missing.
    What could be the reason for this behavior and how to avoid this in the future?**
    
    - **Your notification action is writing to the same bucket that triggers the notification**
    - **If two writes are made to a single non-versioned object at the same time, it is possible that only a single event notification will be sent(Correct)**
    - **Someone could have created a new notification configuration and that has overridden your existing configuration**
    - **Versioning is enabled on the S3 bucket and event notifications are getting fired for only one version**
    
    ### **Explanation**
    
    Correct option:
    
    **If two writes are made to a single non-versioned object at the same time, it is possible that only a single event notification will be sent** - Amazon S3 event notifications are designed to be delivered at least once. Typically, event notifications are delivered in seconds but can sometimes take a minute or longer.
    
    If two writes are made to a single non-versioned object at the same time, it is possible that only a single event notification will be sent. If you want to ensure that an event notification is sent for every successful write, you can enable versioning on your bucket. With versioning, every successful write will create a new version of your object and will also send event notification.