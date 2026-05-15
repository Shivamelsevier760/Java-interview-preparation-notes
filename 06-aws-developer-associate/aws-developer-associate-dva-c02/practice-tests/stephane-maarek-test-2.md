# Stephane Maarek Test 2

## Wrong

- Q3
    
    **The development team at an e-commerce company completed the last deployment for their application at a reduced capacity because of the deployment policy. The application took a performance hit because of the traffic spike due to an on-going sale.
    Which of the following represents the BEST deployment option for the upcoming application version such that it maintains at least the FULL capacity of the application and MINIMAL impact of failed deployment?**
    
    - **Deploy the new application version using 'All at once' deployment policy**
    - **Deploy the new application version using 'Immutable' deployment policy(Correct)**
    - **Deploy the new application version using 'Rolling with additional batch' deployment policy(Incorrect)**
    - **Deploy the new application version using 'Rolling' deployment policy**
- Q16 - important
    
    **A development team is working on an AWS Lambda function that accesses DynamoDB. The Lambda function must do an upsert, that is, it must retrieve an item and update some of its attributes or create the item if it does not exist.
    Which of the following represents the solution with MINIMUM IAM permissions that can be used for the Lambda function to achieve this functionality?**
    
    - **dynamodb:AddItem, dynamodb:GetItem**
    - **dynamodb:GetRecords, dynamodb:PutItem, dynamodb:UpdateTable**
    - **dynamodb:UpdateItem, dynamodb:GetItem, dynamodb:PutItem(Incorrect)**
    - **dynamodb:UpdateItem, dynamodb:GetItem(Correct)**
    
    ### **Explanation**
    
    `UpdateItem` action of DynamoDB APIs, edits an existing item's attributes or adds a new item to the table if it does not already exist. You can put, delete, or add attribute values. You can also perform a conditional update on an existing item (insert a new attribute name-value pair if it doesn't exist, or replace an existing name-value pair if it has certain expected attribute values).
    
    There is no need to inlcude the `dynamodb:PutItem` action for the given use-case.
    
- Q23 - info
    
    **A Developer is configuring Amazon EC2 Auto Scaling group to scale dynamically.
    Which metric below is NOT part of Target Tracking Scaling Policy?**
    
    - **ALBRequestCountPerTarget**
    - **ApproximateNumberOfMessagesVisible(Correct)**
    - **ASGAverageNetworkOut(Incorrect)**
    - **ASGAverageCPUUtilization**
    
    ### **Explanation**
    
    Correct option:
    
    **ApproximateNumberOfMessagesVisible** - This is a CloudWatch Amazon SQS queue metric. The number of messages in a queue might not change proportionally to the size of the Auto Scaling group that processes messages from the queue. Hence, this metric does not work for target tracking.
    
- Q39 - info
    
    **A development team has configured their Amazon EC2 instances for Auto Scaling. A Developer during routine checks has realized that only basic monitoring is active, as opposed to detailed monitoring.
    Which of the following represents the best root-cause behind the issue?**
    
    - **AWS CLI was used to create the launch configuration**
    - **The default configuration for Auto Scaling was not set(Incorrect)**
    - **SDK was used to create the launch configuration**
    - **AWS Management Console might have been used to create the launch configuration(Correct)**
- Q43 - info
    
    **A developer wants to package the code and dependencies for the application-specific Lambda functions as container images to be hosted on Amazon Elastic Container Registry (ECR).
    Which of the following options are correct for the given requirement? (Select two)**
    
    - [ ]  **Lambda supports both Windows and Linux-based container images**
    - [ ]  **You can deploy Lambda function as a container image, with a maximum size of 15 GB**
    - [x]  **To deploy a container image to Lambda, the container image must implement the Lambda Runtime API(Correct)**
    - [ ]  **You must create the Lambda function from the same account as the container registry in Amazon ECR(Correct)**
    - [x]  **You can test the containers locally using the Lambda Runtime API(Incorrect)**
    
    ### **Explanation**
    
    Correct options:
    
    **To deploy a container image to Lambda, the container image must implement the Lambda Runtime API** - To deploy a container image to Lambda, the container image must implement the Lambda Runtime API. The AWS open-source runtime interface clients implement the API. You can add a runtime interface client to your preferred base image to make it compatible with Lambda.
    
    **You must create the Lambda function from the same account as the container registry in Amazon ECR** - You can package your Lambda function code and dependencies as a container image, using tools such as the Docker CLI. You can then upload the image to your container registry hosted on Amazon Elastic Container Registry (Amazon ECR). **Note that you must create the Lambda function from the same account as the container registry in Amazon ECR.**
    
    **You can test the containers locally using the Lambda Runtime API** - You can test the containers locally using the **Lambda Runtime Interface Emulator.**
    
- Q48 - important
    
    **Your team lead has asked you to learn AWS CloudFormation to create a collection of related AWS resources and provision them in an orderly fashion. You decide to provide AWS-specific parameter types to catch invalid values.
    When specifying parameters which of the following is not a valid Parameter type?**
    
    - **CommaDelimitedList**
    - **AWS::EC2::KeyPair::KeyName(Incorrect)**
    - **DependentParameter(Correct)**
    - **String**
    
    ### **Explanation**
    
    CloudFormation currently supports the following parameter types:
    
    ```
    String – A literal string
    Number – An integer or float
    List<Number> – An array of integers or floats
    CommaDelimitedList – An array of literal strings that are separated by commas
    AWS::EC2::KeyPair::KeyName – An Amazon EC2 key pair name
    AWS::EC2::SecurityGroup::Id – A security group ID
    AWS::EC2::Subnet::Id – A subnet ID
    AWS::EC2::VPC::Id – A VPC ID
    List<AWS::EC2::VPC::Id> – An array of VPC IDs
    List<AWS::EC2::SecurityGroup::Id> – An array of security group IDs
    List<AWS::EC2::Subnet::Id> – An array of subnet IDs
    
    ```
    
    **DependentParameter**
    
    In CloudFormation, parameters are all independent and cannot depend on each other. Therefore, this is an invalid parameter type.
    
- Q51 - important
    
    **The development team at a HealthCare company has deployed EC2 instances in AWS Account A. These instances need to access patient data with Personally Identifiable Information (PII) on multiple S3 buckets in another AWS Account B.
    As a Developer Associate, which of the following solutions would you recommend for the given use-case?**
    
    - **Create an IAM role with S3 access in Account B and set Account A as a trusted entity. Create another role (instance profile) in Account A and attach it to the EC2 instances in Account A and add an inline policy to this role to assume the role from Account B(Correct)**
    - **Copy the underlying AMI for the EC2 instances from Account A into Account B. Launch EC2 instances in Account B using this AMI and then access the PII data on Amazon S3 in Account B**
    - **Add a bucket policy to all the Amazon S3 buckets in Account B to allow access from EC2 instances in Account A(Incorrect)**
    - **Create an IAM role (instance profile) in Account A and set Account B as a trusted entity. Attach this role to the EC2 instances in Account A and add an inline policy to this role to access S3 data from Account B**
    
    ### **Explanation**
    
    Correct option:
    
    **Create an IAM role with S3 access in Account B and set Account A as a trusted entity. Create another role (instance profile) in Account A and attach it to the EC2 instances in Account A and add an inline policy to this role to assume the role from Account B**
    
    You can give EC2 instances in one account ("account A") permissions to assume a role from another account ("account B") to access resources such as S3 buckets. You need to create an IAM role in Account B and set Account A as a trusted entity. Then attach a policy to this IAM role such that it delegates access to Amazon S3 like so -
    
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    "arn:aws:s3:::awsexamplebucket1",
                    "arn:aws:s3:::awsexamplebucket1/*",
                    "arn:aws:s3:::awsexamplebucket2",
                    "arn:aws:s3:::awsexamplebucket2/*"
                ]
            }
        ]
    }
    
    ```
    
    Then you can create another role (instance profile) in Account A and attach it to the EC2 instances in Account A and add an inline policy to this role to assume the role from Account B like so -
    
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "sts:AssumeRole",
                "Resource": "arn:aws:iam::AccountB_ID:role/ROLENAME"
            }
        ]
    }
    
    ```
    
    Incorrect options:
    
    **Add a bucket policy to all the Amazon S3 buckets in Account B to allow access from EC2 instances in Account A** - Just adding a bucket policy in Account B is not enough, as you also need to create an IAM policy in Account A to access S3 objects in Account B.
    
- Q55 - important
    
    **A media publishing company is using Amazon EC2 instances for running their business-critical applications. Their IT team is looking at reserving capacity apart from savings plans for the critical instances.
    As a Developer Associate, which of the following reserved instance types you would select to provide capacity reservations?**
    
    - **Regional Reserved Instances(Incorrect)**
    - **Both Regional Reserved Instances and Zonal Reserved Instances**
    - **Zonal Reserved Instances(Correct)**
    - **Neither Regional Reserved Instances nor Zonal Reserved Instances**
    
    ### **Explanation**
    
    Correct option:
    
    When you purchase a Reserved Instance for a specific Availability Zone, it's referred to as a Zonal Reserved Instance. Zonal Reserved Instances provide capacity reservations as well as discounts.
    
    **Zonal Reserved Instances** - A zonal Reserved Instance provides a capacity reservation in the specified Availability Zone. Capacity Reservations enable you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. This gives you the ability to create and manage Capacity Reservations independently from the billing discounts offered by Savings Plans or regional Reserved Instances.
    
    Regional and Zonal Reserved Instances:
    
    ![](https://assets-pt.media.datacumulus.com/aws-dva-pt/assets/pt2-q31-i1.jpg)
    
    Incorrect options:
    
    **Regional Reserved Instances** - When you purchase a Reserved Instance for a Region, it's referred to as a regional Reserved Instance. A regional Reserved Instance does not provide a capacity reservation.
    
- Q57 - important
    
    **A developer is defining the signers that can create signed URLs for their Amazon CloudFront distributions.
    Which of the following statements should the developer consider while defining the signers? (Select two)**
    
    - [ ]  **Both the signers (trusted key groups and CloudFront key pairs) can be managed using the CloudFront APIs**
    - [x]  **When you use the root user to manage CloudFront key pairs, you can only have up to two active CloudFront key pairs per AWS account(Correct)**
    - [ ]  **You can also use AWS Identity and Access Management (IAM) permissions policies to restrict what the root user can do with CloudFront key pairs**
    - [ ]  **When you create a signer, the public key is with CloudFront and private key is used to sign a portion of URL(Correct)**
    - [x]  **CloudFront key pairs can be created with any account that has administrative permissions and full access to CloudFront resources(Incorrect)**
    
    ### **Explanation**
    
    Correct options:
    
    **When you create a signer, the public key is with CloudFront and private key is used to sign a portion of URL** - Each signer that you use to create CloudFront signed URLs or signed cookies must have a public–private key pair. The signer uses its private key to sign the URL or cookies, and CloudFront uses the public key to verify the signature.
    
    When you create signed URLs or signed cookies, you use the private key from the signer’s key pair to sign a portion of the URL or the cookie. When someone requests a restricted file, CloudFront compares the signature in the URL or cookie with the unsigned URL or cookie, to verify that it hasn’t been tampered with. CloudFront also verifies that the URL or cookie is valid, meaning, for example, that the expiration date and time haven’t passed.
    
    **When you use the root user to manage CloudFront key pairs, you can only have up to two active CloudFront key pairs per AWS account** - When you use the root user to manage CloudFront key pairs, you can only have up to two active CloudFront key pairs per AWS account.
    
    Whereas, with CloudFront key groups, you can associate a higher number of public keys with your CloudFront distribution, giving you more flexibility in how you use and manage the public keys. By default, you can associate up to four key groups with a single distribution, and you can have up to five public keys in a key group.
    
    Incorrect options:
    
    **CloudFront key pairs can be created with any account that has administrative permissions and full access to CloudFront resources** - CloudFront key pairs can only be created using the root user account and hence is not a best practice to create CloudFront key pairs as signers.
    
- Q58 - important
    
    **A new recruit is trying to configure what an Amazon EC2 should do when it interrupts a Spot Instance.
    Which of the below CANNOT be configured as an interruption behavior?**
    
    - **Terminate the Spot Instance**
    - **Reboot the Spot Instance(Correct)**
    - **Hibernate the Spot Instance(Incorrect)**
    - **Stop the Spot Instance**
    
    ### **Explanation**
    
    Correct option:
    
    A Spot Instance is an unused EC2 instance that is available for less than the On-Demand price. Your Spot Instance runs whenever capacity is available and the maximum price per hour for your request exceeds the Spot price. Any instance present with unused capacity will be allocated.
    
    You can specify that Amazon EC2 should do one of the following when it interrupts a Spot Instance:
    
    Stop the Spot Instance
    
    Hibernate the Spot Instance
    
    Terminate the Spot Instance
    
- Q64 - important
    
    **A company runs its flagship application on a fleet of Amazon EC2 instances. After misplacing a couple of private keys from the SSH key pairs, they have decided to re-use their SSH key pairs for the different instances across AWS Regions.
    As a Developer Associate, which of the following would you recommend to address this use-case?**
    
    - **It is not possible to reuse SSH key pairs across AWS Regions**
    - **Encrypt the private SSH key and store it in the S3 bucket to be accessed from any AWS Region(Incorrect)**
    - **Store the public and private SSH key pair in AWS Trusted Advisor and access it across AWS Regions**
    - **Generate a public SSH key from a private SSH key. Then, import the key into each of your AWS Regions(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    **Generate a public SSH key from a private SSH key. Then, import the key into each of your AWS Regions**
    
    Here is the correct way of reusing SSH keys in your AWS Regions:
    
    1. Generate a public SSH key (.pub) file from the private SSH key (.pem) file.
    2. Set the AWS Region you wish to import to.
    3. Import the public SSH key into the new Region.
    
    Incorrect options:
    
    **Encrypt the private SSH key and store it in the S3 bucket to be accessed from any AWS Region** - Storing private key to Amazon S3 is possible. But, this will not make the key accessible for all AWS Regions, as is the need in the current use case.
    

## Doubtful

- Q21 - good question
    
    **While troubleshooting, a developer realized that the Amazon EC2 instance is unable to connect to the Internet using the Internet Gateway.
    Which conditions should be met for Internet connectivity to be established? (Select two)**
    
    - [ ]  **The instance's subnet is associated with multiple route tables with conflicting configurations**
    - [x]  **The route table in the instance’s subnet should have a route to an Internet Gateway(Correct)**
    - [ ]  **The subnet has been configured to be Public and has no access to the internet**
    - [x]  **The network ACLs associated with the subnet must have rules to allow inbound and outbound traffic(Correct)**
    - [ ]  **The instance's subnet is not associated with any route table**
    
    ### **Explanation**
    
    Correct options:
    
    **The network ACLs associated with the subnet must have rules to allow inbound and outbound traffic** - The network access control lists (ACLs) that are associated with the subnet must have rules to allow inbound and outbound traffic on port 80 (for HTTP traffic) and port 443 (for HTTPs traffic). This is a necessary condition for Internet Gateway connectivity
    
    **The route table in the instance’s subnet should have a route to an Internet Gateway** - A route table contains a set of rules, called routes, that are used to determine where network traffic from your subnet or gateway is directed. The route table in the instance’s subnet should have a route defined to the Internet Gateway.
    
    Incorrect options:
    
    **The instance's subnet is not associated with any route table** - This is an incorrect statement. A subnet is implicitly associated with the main route table if it is not explicitly associated with a particular route table. So, a subnet is always associated with some route table.
    
    **The instance's subnet is associated with multiple route tables with conflicting configurations** - This is an incorrect statement. A subnet can only be associated with one route table at a time.
    
    **The subnet has been configured to be Public and has no access to internet** - This is an incorrect statement. Public subnets have access to the internet via Internet Gateway.
    
- Q30 - important
    
    **A diagnostic lab stores its data on DynamoDB. The lab wants to backup a particular DynamoDB table data on Amazon S3, so it can download the S3 backup locally for some operational use.
    Which of the following options is NOT feasible?**
    
    - **Use AWS Glue to copy your table to Amazon S3 and download locally**
    - **Use AWS Data Pipeline to export your table to an S3 bucket in the account of your choice and download locally**
    - **Use Hive with Amazon EMR to export your data to an S3 bucket and download locally**
    - **Use the DynamoDB on-demand backup capability to write to Amazon S3 and download locally(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    **Use the DynamoDB on-demand backup capability to write to Amazon S3 and download locally** - This option is not feasible for the given use-case. DynamoDB has two built-in backup methods (On-demand, Point-in-time recovery) that write to Amazon S3, **but you will not have access to the S3 buckets that are used for these backups.**
    
- Q36
    
    **As a Team Lead, you are expected to generate a report of the code builds for every week to report internally and to the client. This report consists of the number of code builds performed for a week, the percentage success and failure, and overall time spent on these builds by the team members. You also need to retrieve the CodeBuild logs for failed builds and analyze them in Athena.
    Which of the following options will help achieve this?**
    
    - **Use CloudWatch Events**
    - **Use AWS CloudTrail and deliver logs to S3**
    - **Enable S3 and CloudWatch Logs integration(Correct)**
    - **Use AWS Lambda integration**
- Q47
    
    **Signing AWS API requests helps AWS identify an authentic user from a potential threat.
    As a developer associate, which of the following would you identify as the use-case where you need to sign the API requests?**
    
    - **When you send HTTP requests to an AWS service(Correct)**
    - **When you use the AWS Command Line Interface (AWS CLI) to run commands on an AWS resource**
    - **When you use one of the AWS SDKs to make requests to AWS resources/services**
    - **When you send anonymous requests to Amazon Simple Storage Service (Amazon S3)**
- Q63 - important
    
    **You have created a continuous delivery service model with automated steps using AWS CodePipeline. Your pipeline uses your code, maintained in a CodeCommit repository, AWS CodeBuild, and AWS Elastic Beanstalk to automatically deploy your code every time there is a code change. However, the deployment to Elastic Beanstalk is taking a very long time due to resolving dependencies on all of your 100 target EC2 instances.
    Which of the following actions should you take to improve performance with limited code changes?**
    
    - **Bundle the dependencies in the source code during the build stage of CodeBuild(Correct)**
    - **Bundle the dependencies in the source code in CodeCommit**
    - **Create a custom platform for Elastic Beanstalk**
    - **Store the dependencies in S3, to be used while deploying to Beanstalk**
    
    ### **Explanation**
    
    Correct option:
    
    **Bundle the dependencies in the source code during the build stage of CodeBuild**
    
    AWS CodeBuild is a fully managed build service. There are no servers to provision and scale, or software to install, configure, and operate.
    
    A typical application build process includes phases like preparing the environment, updating the configuration, downloading dependencies, running unit tests, and finally, packaging the built artifact.
    
    Downloading dependencies is a critical phase in the build process. These dependent files can range in size from a few KBs to multiple MBs. Because most of the dependent files do not change frequently between builds, you can noticeably reduce your build time by caching dependencies.
    
    This will allow the code bundle to be deployed to Elastic Beanstalk to have both the dependencies and the code, hence **speeding up the deployment time to Elastic Beanstalk**