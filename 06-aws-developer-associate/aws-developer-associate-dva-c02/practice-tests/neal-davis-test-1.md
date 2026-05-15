# Neal Davis Test 1

## Wrong

- Q1 - good
    
    **A company has implemented AWS CodePipeline to automate its release pipelines. The Development team is writing an AWS Lambda function that will send notifications for state changes of each of the actions in the stages.
    Which steps must be taken to associate the Lambda function with the event source?**
    
    - **Create a trigger that invokes the Lambda function from the Lambda console by selecting CodePipeline as the event source**
    - **Create an Amazon CloudWatch alarm that monitors status changes in CodePipeline and triggers the Lambda function(Incorrect)**
    - **Create an event trigger and specify the Lambda function from the CodePipeline console**
    - **Create an Amazon CloudWatch Events rule that uses CodePipeline as an event source(Correct)**
    
    ### **Explanation**
    
    [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchEvents.html) help you to respond to state changes in your AWS resources. When your resources change state, they automatically send events into an event stream. You can create rules that match selected events in the stream and route them to your AWS Lambda function to take action.
    
    AWS CodePipeline can be configured as an event source in CloudWatch Events and can then send notifications using as service such as Amazon SNS.
    
- Q4 - wrong answer I guess
    
    **An ecommerce company manages a storefront that uses an Amazon API Gateway API which exposes an AWS Lambda function. The Lambda functions processes orders and stores the orders in an Amazon RDS for MySQL database. The number of transactions increases sporadically during marketing campaigns, and then goes close to zero during quite times.
    How can a developer increase the elasticity of the system MOST cost-effectively?**
    
    - **Create an Amazon SQS queue. Publish transactions to the queue and set the queue to invoke the Lambda function. Set the reserved concurrency of the Lambda function to be equal to the max number of database connections.(Incorrect)**
    - **Migrate from Amazon RDS to Amazon Aurora MySQL. Use an Aurora Auto Scaling policy to scale read replicas based on average CPU utilization.**
    - **Create an Amazon SNS topic. Publish transactions to the topic configure an SQS queue as a destination. Configure Lambda to process transactions from the queue.**
    - **Migrate from Amazon RDS to Amazon Aurora MySQL. Use an Aurora Auto Scaling policy to scale read replicas based on average connections of Aurora Replicas.(Correct)**
    
    ### **Explanation**
    
    The most efficient solution would be to use Aurora Auto Scaling and configure the scaling events to happen based on target metric. The metric to use is **Average connections of Aurora Replicas** which will create a policy based on the average number of connections to Aurora Replicas.
    
    This will ensure that the Aurora replicas scale based on actual numbers of connections to the replicas which will vary based on how busy the storefront is and how many transactions are being processed.
    
    **CORRECT:** "Migrate from Amazon RDS to Amazon Aurora MySQL. Use an Aurora Auto Scaling policy to scale read replicas based on average connections of Aurora Replicas" is the correct answer (as explained above.)
    
    **INCORRECT:** "Migrate from Amazon RDS to Amazon Aurora MySQL. Use an Aurora Auto Scaling policy to scale read replicas based on average CPU utilization" is incorrect.
    
    The better metric to use for this situation would be the number of connections to Aurora Replicas as that is the metric that has the closest correlation to the number of transactions being executed.
    
    **INCORRECT:** "Create an Amazon SNS topic. Publish transactions to the topic configure an SQS queue as a destination. Configure Lambda to process transactions from the queue" is incorrect.
    
    This is highly inefficient. There is no need for an SNS topic in this situation.
    
    **INCORRECT:** "Create an Amazon SQS queue. Publish transactions to the queue and set the queue to invoke the Lambda function. Set the reserved concurrency of the Lambda function to be equal to the max number of database connections" is incorrect.
    
    This would be less cost effective as you would be paying for the reserved concurrency at all times.
    
- Q14 - good
    
    **A developer is partitioning data using Athena to improve performance when performing queries. What are two things the analyst can do that would counter any benefit of using partitions? (Select TWO.)**
    
    - [x]  **Creating partitions directly from data source.(Incorrect)**
    - [ ]  **Storing the data in S3.**
    - [ ]  **Segmenting data too finely.(Correct)**
    - [ ]  **Using a Hive-style partition format.**
    - [x]  **Skewing data heavily to one partition value.(Correct)**
    
    ### **Explanation**
    
    There is a cost associated with partitioning data. A higher number of partitions can also increase the overhead from retrieving and processing the partition metadata. Multiple smaller files can counter the benefit of using partitioning. If your data is heavily skewed to one partition value, and most queries use that value, then the overhead may wipe out the initial benefit.
    
- Q29 - good
    
    **A Developer is creating a new web application that will be deployed using AWS Elastic Beanstalk from the AWS Management Console. The Developer is about to create a source bundle which will be uploaded using the console.
    Which of the following are valid requirements for creating the source bundle? (Select TWO.)**
    
    - [ ]  **Must not include a parent folder or top-level directory.(Correct)**
    - [x]  **Must consist of one or more ZIP files.(Incorrect)**
    - [x]  **Must not exceed 512 MB.(Correct)**
    - [ ]  **Must include the cron.yaml file.**
    - [ ]  **Must include a parent folder or top-level directory.**
    
    ### **Explanation**
    
    When you use the AWS Elastic Beanstalk console to deploy a new application or an application version, you'll need to upload a source bundle. Your source bundle must meet the following requirements:
    
    •  Consist of a single ZIP file or WAR file (you can include multiple WAR files inside your ZIP file)
    
    •  Not exceed 512 MB
    
    •  Not include a parent folder or top-level directory (subdirectories are fine)
    
    If you want to deploy a worker application that processes periodic background tasks, your application source bundle must also include a cron.yaml file, but in other cases it is not required.
    
- Q34 - good
    
    **A developer is running queries on Hive-compatible partitions in Athena using DDL but is facing time out issues. What is the most effective and efficient way to prevent this from continuing to happen?**
    
    - **Use the MSCK REPAIR TABLE command to update the metadata in the catalog.(Correct)**
    - **Export the data into a JSON document to clean any errors and upload the cleaned data into S3.**
    - **Use the ALTER TABLE ADD PARTITION command to update the column names.(Incorrect)**
    - **Export the data into DynamoDB to perform queries in a more flexible schema.**
    
    ### **Explanation**
    
    The MSCK REPAIR TABLE command scans Amazon S3 for Hive compatible partitions that were added to the file system after the table was created. It compares the partitions in the table metadata and the partitions in S3. If new partitions are present in the S3 location that you specified when you created the table, it adds those partitions to the metadata and to the Athena table. MSK REPAIR TABLE can work better than DDL if have more than a few thousand partitions and DDL is facing timeout issues.
    
- Q48 - good
    
    **A Developer is deploying an AWS Lambda update using AWS CodeDeploy. In the appspec.yaml file, which of the following is a valid structure for the order of hooks that should be specified?**
    
    - **BeforeInstall > AfterInstall > AfterAllowTestTraffic > BeforeAllowTraffic > AfterAllowTraffic**
    - **BeforeBlockTraffic > AfterBlockTraffic > BeforeAllowTraffic > AfterAllowTraffic**
    - **BeforeInstall > AfterInstall > ApplicationStart > ValidateService(Incorrect)**
    - **BeforeAllowTraffic > AfterAllowTraffic(Correct)**
    
    ### **Explanation**
    
    The content in the 'hooks' section of the AppSpec file varies, depending on the compute platform for your deployment. The 'hooks' section for an EC2/On-Premises deployment contains mappings that link deployment lifecycle event hooks to one or more scripts.
    
    The 'hooks' section for a Lambda or an Amazon ECS deployment specifies Lambda validation functions to run during a deployment lifecycle event. If an event hook is not present, no operation is executed for that event. This section is required only if you are running scripts or Lambda validation functions as part of the deployment.
    
    The following code snippet shows a valid example of the structure of hooks for an AWS Lambda deployment:
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-19_12-33-57-404e61aa9de4be6bc1dcd44c189c04c1.jpg)
    
    Therefore, in this scenario a valid structure for the order of hooks that should be specified in the appspec.yml file is: BeforeAllowTraffic > AfterAllowTraffic
    
    **CORRECT:** "BeforeAllowTraffic > AfterAllowTraffic" is the correct answer.
    
    **INCORRECT:** "BeforeInstall > AfterInstall > ApplicationStart > ValidateService" is incorrect as this would be valid for Amazon EC2.
    
    **INCORRECT:** "BeforeInstall > AfterInstall > AfterAllowTestTraffic > BeforeAllowTraffic > AfterAllowTraffic" is incorrect as this would be valid for Amazon ECS.
    
    **INCORRECT:** "BeforeBlockTraffic > AfterBlockTraffic > BeforeAllowTraffic > AfterAllowTraffic" is incorrect as this is a partial listing of hooks for Amazon EC2 but is incomplete.
    
- Q53 - good
    
    **A Developer will be launching several Docker containers on a new Amazon ECS cluster using the EC2 Launch Type. The containers will all run a web service on port 80.
    What is the EASIEST way the Developer can configure the task definition to ensure the web services run correctly and there are no port conflicts on the host instances?**
    
    - **Specify a unique port number for the container port and port 80 for the host port**
    - **Specify port 80 for the container port and port 0 for the host port(Correct)**
    - **Specify port 80 for the container port and a unique port number for the host port(Incorrect)**
    - **Leave both the container port and host port configuration blank**
    
    ### **Explanation**
    
    Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition. The container port is the port number on the container that is bound to the user-specified or automatically assigned host port. The host port is the port number on the container instance to reserve for your container.
    
    ![](https://img-b.udemycdn.com/redactor/raw/2020-04-19_12-14-21-2e05425ee95cbc437d856fb9b53d6aa2.jpg)
    
    As we cannot have multiple services bound to the same host port, we need to ensure that each container port mapping uses a different host port. The easiest way to do this is to set the host port number to 0 and ECS will automatically assign an available port. We also need to assign port 80 to the container port so that the web service is able to run.
    
- Q54 - good
    
    **A developer is using AWS CodeBuild to build an application into a Docker image. The buildspec file is used to run the application build. The developer needs to push the Docker image to an Amazon ECR repository only upon the successful completion of each build.**
    
    - **Add a post_build phase to the buildspec file that uses the commands block to push the Docker image.(Correct)**
    - **Add a post_build phase to the buildspec file that uses the finally block to push the Docker image.**
    - **Add a post_build phase to the buildspec file that uses the artifacts sequence to find the build artifacts and push to Amazon ECR.(Incorrect)**
    - **Add an install phase to the buildspec file that uses the commands block to push the Docker image.**
    
    ### **Explanation**
    
    The post_build phase is an optional sequence. It represents the commands, if any, that CodeBuild runs after the build. For example, you might use Maven to package the build artifacts into a JAR or WAR file, or you might push a Docker image into Amazon ECR.
    
- Q56 - silly
    
    **An application needs to generate SMS text messages and emails for a large number of subscribers. Which AWS service can be used to send these messages to customers?**
    
    - **Amazon SWF**
    - **Amazon SQS**
    - **Amazon SNS(Correct)**
    - **Amazon SES(Incorrect)**
    
    ### **Explanation**
    
    **CORRECT:** "Amazon SNS" is the correct answer.
    
    **INCORRECT:** "Amazon SES" is incorrect as this service only sends email, not SMS text messages.
    
- Q65 - good
    
    **An application on-premises uses Linux servers and a relational database using PostgreSQL. The company will be migrating the application to AWS and require a managed service that will take care of capacity provisioning, load balancing, and auto-scaling.
    Which combination of services should the Developer use? (Select TWO.)**
    
    - [ ]  **AWS Lambda with CloudWatch Events**
    - [ ]  **AWS Elastic Beanstalk(Correct)**
    - [x]  **Amazon EC2 with Auto Scaling(Incorrect)**
    - [ ]  **Amazon EC2 with PostgreSQL**
    - [x]  **Amazon RDS with PostrgreSQL(Correct)**
    
    ### **Explanation**
    
    The company require a managed service therefore the Developer should choose to use Elastic Beanstalk for the compute layer and Amazon RDS with the PostgreSQL engine for the database layer.
    
    AWS Elastic Beanstalk will handle all capacity provisioning, load balancing, and auto-scaling for the web front-end and Amazon RDS provides push-button scaling for the backend.
    
    **CORRECT:** "AWS Elastic Beanstalk" is a correct answer.
    
    **CORRECT:** "Amazon RDS with PostrgreSQL" is also a correct answer.
    
    **INCORRECT:** "Amazon EC2 with Auto Scaling" is incorrect as though these services will be used to provide the automatic scalability required for the solution, they still need to be managed. The questions asks for a managed solution and Elastic Beanstalk will manage this for you. Also, there is no mention of a load balancer so connections cannot be distributed to instances.
    
    **INCORRECT:** "Amazon EC2 with PostgreSQL" is incorrect as the question asks for a managed service and therefore the database should be run on Amazon RDS.
    
    **INCORRECT:** "AWS Lambda with CloudWatch Events" is incorrect as there is no mention of refactoring application code to run on AWS Lambda.
    

## Doubtful

- Q7 - important
    
    **A Developer has created a task definition that includes the following JSON code:
    
    `1. "placementStrategy": [
    2. {
    3. "field": "attribute:ecs.availability-zone",
    4. "type": "spread"
    5. },
    6. {
    7. "field": "instanceId",
    8. "type": "spread"
    9. }
    10. ]`
    What is the effect of this task placement strategy?**
    
    - **It distributes tasks evenly across Availability Zones and then bin packs tasks based on memory within each Availability Zone**
    - **It distributes tasks evenly across Availability Zones and then distributes tasks randomly across instances within each Availability Zone**
    - **It distributes tasks evenly across Availability Zones and then distributes tasks evenly across distinct instances within each Availability Zone**
    - **It distributes tasks evenly across Availability Zones and then distributes tasks evenly across the instances within each Availability Zone(Correct)**
    
    ### **Explanation**
    
    **CORRECT:** "It distributes tasks evenly across Availability Zones and then distributes tasks evenly across the instances within each Availability Zone" is the correct answer.
    
    **INCORRECT:** "It distributes tasks evenly across Availability Zones and then distributes tasks evenly across distinct instances within each Availability Zone" is incorrect as it does not spread tasks across distinct instances (use a task placement constraint).
    
- Q8
    
    **A Development team wants to run their container workloads on Amazon ECS. Each application container needs to share data with another container to collect logs and metrics.
    What should the Development team do to meet these requirements?**
    
    - **Create two pod specifications. Make one to include the application container and the other to include the other container. Link the two pods together**
    - **Create two task definitions. Make one to include the application container and the other to include the other container. Mount a shared volume between the two tasks**
    - **Create a single pod specification. Include both containers in the specification. Mount a persistent volume to both containers**
    - **Create one task definition. Specify both containers in the definition. Mount a shared volume between those two containers(Correct)**
    
    ### **Explanation**
    
    Amazon ECS tasks support Docker volumes. To use data volumes, you must specify the volume and mount point configurations in your task definition. Docker volumes are supported for the EC2 launch type only.
    
    To configure a Docker volume, in the task definition volumes section, define a data volume with name and DockerVolumeConfiguration values. In the containerDefinitions section, define multiple containers with mountPoints values that reference the name of the defined volume and the containerPath value to mount the volume at on the container.
    
    The containers should both be specified in the same task definition. Therefore, the Development team should create one task definition, specify both containers in the definition and then mount a shared volume between those two containers
    
- Q33
    
    **A Developer is setting up a code update to Amazon ECS using AWS CodeDeploy. The Developer needs to complete the code update quickly. Which of the following deployment types should the Developer use?**
    
    - **Linear**
    - **In-place**
    - **Canary**
    - **Blue/green(Correct)**
    
    ### **Explanation**
    
    CodeDeploy provides two deployment type options – in-place and blue/green. Note that AWS Lambda and Amazon ECS deployments cannot use an in-place deployment type.
    
    The Blue/green deployment type on an Amazon ECS compute platform works like this:
    
    Traffic is shifted from the task set with the original version of an application in an Amazon ECS service to a replacement task set in the same service.
    
    You can set the traffic shifting to linear or canary through the deployment configuration.
    
    The protocol and port of a specified load balancer listener is used to reroute production traffic.
    
    During a deployment, a test listener can be used to serve traffic to the replacement task set while validation tests are run.
    
    **CORRECT:** "Blue/green" is the correct answer.
    
    **INCORRECT:** "Canary" is incorrect as this is a traffic shifting option, not a deployment type. Traffic is shifted in two increments.
    
    **INCORRECT:** "Linear" is incorrect as this is a traffic shifting option, not a deployment type. Traffic is shifted in two increments.
    
    **INCORRECT:** "In-place" is incorrect as AWS Lambda and Amazon ECS deployments cannot use an in-place deployment type.
    
- Q38 - good
    
    **A Developer is creating a web application that will be used by employees working from home. The company uses a SAML directory on-premises for storing user information. The Developer must integrate with the SAML directory and authorize each employee to access only their own data when using the application.
    Which approach should the Developer take?**
    
    - **Create the application within an Amazon VPC and use a VPC endpoint with a trust policy to grant access to the employees.**
    - **Use Amazon Cognito user pools, federate with the SAML provider, and use user pool groups with an IAM policy.**
    - **Create a unique IAM role for each employee and have each employee assume the role to access the application so they can access their personal data only.**
    - **Use an Amazon Cognito identity pool, federate with the SAML provider, and use a trust policy with an IAM condition key to limit employee access.(Correct)**
    
    ### **Explanation**
    
    Amazon Cognito leverages IAM roles to generate temporary credentials for your application's users. Access to permissions is controlled by a role's trust relationships.
    
    In this example the Developer must limit access to specific identities in the SAML directory. The Developer can create a trust policy with an IAM condition key that limits access to a specific set of app users by checking the value of cognito-identity.amazonaws.com:sub:
    
    ![](https://img-b.udemycdn.com/redactor/raw/test_question_description/2021-06-09_11-30-30-25305d386d0978ee6835d38458666dfe.jpg)
    
    **CORRECT:** "Use an Amazon Cognito identity pool, federate with the SAML provider, and use a trust policy with an IAM condition key to limit employee access" is the correct answer.
    
    **INCORRECT:** "Use Amazon Cognito user pools, federate with the SAML provider, and use user pool groups with an IAM policy" is incorrect. A user pool can be used to authenticate but the identity pool is used to provide authorized access to AWS services.
    
    **INCORRECT:** "Create the application within an Amazon VPC and use a VPC endpoint with a trust policy to grant access to the employees" is incorrect. You cannot provide access to an on-premises SAML directory using a VPC endpoint.
    
    **INCORRECT:** "Create a unique IAM role for each employee and have each employee assume the role to access the application so they can access their personal data only" is incorrect. This is not an integration into the SAML directory and would be very difficult to manage.
    
- Q41
    
    **A review of Amazon CloudWatch metrics shows that there are a high number of reads taking place on a primary database built on Amazon Aurora with MySQL. What can a developer do to improve the read scaling of the database? (Select TWO.)**
    
    - [x]  **Create Aurora Replicas in same cluster as the primary database instance.(Correct)**
    - [ ]  **Create a duplicate Aurora primary database to process read requests.**
    - [x]  **Create a separate Aurora MySQL cluster and configure binlog replication.(Correct)**
    - [ ]  **Create a duplicate Aurora database cluster to process read requests.**
    - [ ]  **Create Aurora Replicas in a global S3 bucket as the primary read source.**
    
    ### **Explanation**
    
    Aurora Replicas can help improve read scaling because it synchronously updates data with the primary database (within 100 ms). Aurora Replicas are created in the same DB cluster within a Region. With Aurora MySQL you can also enable binlog replication to another Aurora DB cluster which can be in the same or a different Region.
    
- Q42
    
    **A developer is updating an Amazon Aurora MySQL database to allow more clients to connect. What database parameter needs to be updated to support a higher number of client connections?**
    
    - **max_join_size**
    - **max_allowed_packet**
    - **max_user_connections**
    - **max_connections(Correct)**
    
    ### **Explanation**
    
    The maximum number of connections allowed to an Aurora MySQL DB instance is determined by the max_connections parameter in the instance-level parameter group for the DB instance.
    
    You can increase the maximum number of connections to your Aurora MySQL DB instance by scaling the instance up to a DB instance class with more memory, or by setting a larger value for the max_connections parameter in the DB parameter group for your instance, up to 16,000.
    
    **CORRECT:** "max_connections" is the correct answer (as explained above.)
    
    **INCORRECT:** "max_allowed_packet" is incorrect. This parameter sets the maximum size of one packet or any generated or intermediate string.
    
    **INCORRECT:** "max_join_size" is incorrect. This option is used to set a limit on the maximum number of row accesses.
    
    **INCORRECT:** "max_user_connections" is incorrect. This option limits the number of simultaneous connections that the user can make.
    
- Q45
    
    **A company is deploying a microservices application on AWS Fargate using Amazon ECS. The application has environment variables that must be passed to a container for the application to initialize.
    How should the environment variables be passed to the container?**
    
    - **Use standard container definition parameters and define environment variables under the WorkingDirectory parameter within the service definition.**
    - **Use advanced container definition parameters and define environment variables under the environment parameter within the service definition.**
    - **Use advanced container definition parameters and define environment variables under the environment parameter within the task definition.(Correct)**
    - **Use standard container definition parameters and define environment variables under the secrets parameter within the task definition.**
    
    ### **Explanation**
    
    When you register a task definition, you must specify a list of container definitions that are passed to the Docker daemon on a container instance.
    
    The developer should use **advanced container definition** **parameters** and define environment variables to pass to the container.
    
- Q58
    
    **A Development team would use a GitHub repository and would like to migrate their application code to AWS CodeCommit.What needs to be created before they can migrate a cloned repository to CodeCommit over HTTPS?**
    
    - **A set of Git credentials generated with IAM(Correct)**
    - **A GitHub secure authentication token**
    - **An Amazon EC2 IAM role with CodeCommit permissions**
    - **A public and private SSH key file**
    
    ### **Explanation**
    
    AWS CodeCommit is a managed version control service that hosts private Git repositories in the AWS cloud. To use CodeCommit, you configure your Git client to communicate with CodeCommit repositories. As part of this configuration, you provide IAM credentials that CodeCommit can use to authenticate you. IAM supports CodeCommit with three types of credentials:
    
    Git credentials, an IAM -generated user name and password pair you can use to communicate with CodeCommit repositories over HTTPS.
    
    SSH keys, a locally generated public-private key pair that you can associate with your IAM user to communicate with CodeCommit repositories over SSH.
    
    AWS access keys, which you can use with the credential helper included with the AWS CLI to communicate with CodeCommit repositories over HTTPS.