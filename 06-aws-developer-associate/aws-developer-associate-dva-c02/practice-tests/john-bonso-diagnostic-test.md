# John Bonso Diagnostic Test

## Wrong

- Q2
    
    **A code that runs on a Lambda function performs a `GetItem` call from a DynamoDB table. The function runs three times every week. You noticed that the application kept receiving a `ProvisionedThroughputExceededException` error for 10 seconds most of the time.
    How should you handle this error?**
    
    - **Create a Local Secondary Index (LSI) to the existing DynamoDB table to increase the provisioned throughput.**
    - **Enable DynamoDB Accelerator (DAX) to reduce response times from milliseconds to microseconds.(Incorrect)**
    - **Refactor the code in the Lambda function to optimize its performance.**
    - **Reduce the frequency of requests using error retries and exponential backoff.(Correct)**
    
    ### **Explanation**
    
    **ProvisionedThroughputExceededException** means that your request rate is too high. The AWS SDKs for DynamoDB automatically retries requests that receive this exception. Your request is eventually successful unless your retry queue is too large to finish. To handle this error, you can reduce the frequency of requests using error retries and exponential backoff.
    
    Hence, the correct answer is: **Reduce the frequency of requests using error retries and exponential backoff.**
    
    The option that says: **Enable DynamoDB Accelerator (DAX) to reduce response times from milliseconds to microseconds** is incorrect because DAX is used to provide a fully managed, in-memory caching solution. This option is not the right way to handle errors due to high request rates.
    
- Q6
    
    **A full-stack developer has developed an application written in Node.js to host an upcoming mobile game tournament. The developer has decided to deploy the application using AWS Elastic Beanstalk because of its ease-of-use. Upon experimenting, he learned that he could configure the webserver environment with several resources.
    Which of the following services can the developer configure with Elastic Beanstalk? (Select THREE.)**
    
    - [x]  **Amazon EC2 Instance(Correct)**
    - [ ]  **Amazon CloudWatch(Correct)**
    - [x]  **AWS Lambda(Incorrect)**
    - [x]  **Application Load Balancer(Correct)**
    - [ ]  **Amazon Athena**
    - [ ]  **Amazon CloudFront**
    
    ### **Explanation**
    
    **AWS Elastic Beanstalk** is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.
    
    You can upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring. At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources.
    
    With ElasticBeanstalk, you can:
    
    - Select the operating system that matches your application requirements (e.g., Amazon Linux or Windows Server 2016)
    - Choose from several Amazon EC2 instances, including On-Demand, Reserved Instances, and Spot Instances.
    - Choose from several available database and storage options.
    - Enable login access to Amazon EC2 instances for immediate and direct troubleshooting
    - Quickly improve application reliability by running in more than one Availability Zone.
    - Enhance application security by enabling HTTPS protocol on the load balancer
    - Access built-in Amazon CloudWatch monitoring and getting notifications on application health and other important events
    - Adjust application server settings (e.g., JVM settings) and pass environment variables
    - Run other application components, such as a memory caching service, side-by-side in Amazon EC2.
    - Access log files without logging in to the application servers
    
    Hence, the correct answers are: **Amazon EC2 Instance, Amazon CloudWatch,** and **Application Load Balancer.**
    
    You cannot configure **Amazon Athena, AWS Lambda**, and **Amazon CloudFront** on ElasticBeanstalk.