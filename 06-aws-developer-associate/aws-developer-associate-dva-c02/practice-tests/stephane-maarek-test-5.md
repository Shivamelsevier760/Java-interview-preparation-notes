# Stephane Maarek Test 5

## Wrong

- Q17 - important
    
    **An IT company leverages CodePipeline to automate its release pipelines. The development team wants to write a Lambda function that will send notifications for state changes within the pipeline.
    As a Developer Associate, which steps would you suggest to associate the Lambda function with the event source?**
    
    - **Set up an Amazon CloudWatch alarm that monitors status changes in Code Pipeline and triggers the Lambda function(Incorrect)**
    - **Set up an Amazon CloudWatch Events rule that uses CodePipeline as an event source with the target as the Lambda function(Correct)**
    - **Use the Lambda console to configure a trigger that invokes the Lambda function with CodePipeline as the event source**
    - **Use the CodePipeline console to set up a trigger for the Lambda function**
    
    ### **Explanation**
    
    Correct option:
    
    Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources. Using simple rules that you can quickly set up, you can match events and route them to one or more target functions or streams.
    
- Q24 - tricky
    
    **You are running a public DNS service on an EC2 instance where the DNS name is pointing to the IP address of the instance. You wish to upgrade your DNS service but would like to do it without any downtime.
    Which of the following options will help you accomplish this?**
    
    - **Use Route 53(Incorrect)**
    - **Create a Load Balancer and an auto scaling group**
    - **Elastic IP(Correct)**
    - **Provide a static private IP**
    
    ### **Explanation**
    
    Correct option:
    
    Route 53 is a DNS managed by AWS, but nothing prevents you from running your own DNS (it's just a software) on an EC2 instance. The trick of this question is that it's about EC2, running some software that needs a fixed IP, and not about Route 53 at all.
    
    **Elastic IP**
    
    DNS services are identified by a public IP, so you need to use Elastic IP.
    
- Q26 - important
    
    **You are responsible for an application that runs on multiple Amazon EC2 instances. In front of the instances is an Internet-facing load balancer that takes requests from clients over the internet and distributes them to the EC2 instances. A health check is configured to ping the index.html page found in the root directory for the health status. When accessing the website via the internet visitors of the website receive timeout errors.
    What should be checked first to resolve the issue?**
    
    - **IAM Roles**
    - **Security Groups(Correct)**
    - **The ALB is warming up(Incorrect)**
    - **The application is down**
    
    ### **Explanation**
    
    Correct option:
    
    **Security Groups**
    
    A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance.
    
    Check the security group rules of your EC2 instance. You need a security group rule that allows inbound traffic from your public IPv4 address on the proper port.
    
    Incorrect options:
    
    **The application is down** - Although you can set a health check for application ping or HTTP, timeouts are usually caused by blocked firewall access.
    
- Q58 - important
    
    **The development team at an e-commerce company is preparing for the upcoming Thanksgiving sale. The product manager wants the development team to implement appropriate caching strategy on Amazon ElastiCache to withstand traffic spikes on the website during the sale. A key requirement is to facilitate consistent updates to the product prices and product description, so that the cache never goes out of sync with the backend.
    As a Developer Associate, which of the following solutions would you recommend for the given use-case?**
    
    - **Use a caching strategy to write to the cache directly and sync the backend at a later time**
    - **Use a caching strategy to write to the backend first and wait for the cache to expire via TTL**
    - **Use a caching strategy to write to the backend first and then invalidate the cache(Correct)**
    - **Use a caching strategy to update the cache and the backend at the same time(Incorrect)**
    
    ### **Explanation**
    
    **Use a caching strategy to write to the backend first and then invalidate the cache**
    
    This option is similar to the write-through strategy wherein the application writes to the backend first and then invalidate the cache. As the cache gets invalidated, the caching engine would then fetch the latest value from the backend, thereby making sure that the product prices and product description stay consistent with the backend.
    
    Incorrect options:
    
    **Use a caching strategy to update the cache and the backend at the same time** - The cache and the backend cannot be updated at the same time via a single atomic operation as these are two separate systems. Therefore this option is incorrect.
    
- Q62 - tricky
    
    **An EC2 instance has an IAM instance role attached to it, providing it read and write access to the S3 bucket 'my_bucket'. You have tested the IAM instance role and both reads and writes are working. You then remove the IAM role from the EC2 instance and test both read and write again. Writes stopped working but reads are still working.
    What is the likely cause of this behavior?**
    
    - **The S3 bucket policy authorizes reads(Correct)**
    - **When a read is done on a bucket, there's a grace period of 5 minutes to do the same read again**
    - **Removing an instance role from an EC2 instance can take a few minutes before being active**
    - **The EC2 instance is using cached temporary IAM credentials(Incorrect)**

## Doubtful

- Q35
    
    **An e-commerce company has multiple EC2 instances operating in a private subnet which is part of a custom VPC. These instances are running an image processing application that needs to access images stored on S3. Once each image is processed, the status of the corresponding record needs to be marked as completed in a DynamoDB table.
    How would you go about providing private access to these AWS resources which are not part of this custom VPC?**
    
    - **Create a separate gateway endpoint for S3 and DynamoDB each. Add two new target entries for these two gateway endpoints in the route table of the custom VPC(Correct)**
    - **Create a gateway endpoint for S3 and add it as a target in the route table of the custom VPC. Create an interface endpoint for DynamoDB and then connect to the DynamoDB service using the private IP address**
    - **Create a gateway endpoint for DynamoDB and add it as a target in the route table of the custom VPC. Create an API endpoint for S3 and then connect to the S3 service using the private IP address**
    - **Create a separate interface endpoint for S3 and DynamoDB each. Then connect to these services using the private IP address**
- Q61 - important
    
    **Your company likes to operate multiple AWS accounts so that teams have their environments. Services deployed across these accounts interact with one another, and now there's a requirement to implement X-Ray traces across all your applications deployed on EC2 instances and AWS accounts.
    As such, you would like to have a unified account to view all the traces. What should you in your X-Ray daemon set up to make this work? (Select two)**
    
    - [x]  **Configure the X-Ray daemon to use an IAM instance role(Correct)**
    - [x]  **Create a role in the target unified account and allow roles in each sub-account to assume the role.(Correct)**
    - [ ]  **Create a user in the target unified account and generate access and secret keys**
    - [ ]  **Configure the X-Ray daemon to use access and secret keys**
    - [ ]  **Enable Cross Account collection in the X-Ray console**
    
    ### **Explanation**
    
    **The X-Ray agent can assume a role to publish data into an account different from the one in which it is running.** This enables you to publish data from various components of your application into a central account.