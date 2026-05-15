# Architecture Diagrams

- 3-tier Web Application
    
    The application and data tier utilize different private subnets while the ELB is put in a public subnet.
    
    ![Untitled](architecture-diagrams/untitled.png)
    
- Serverless image processing using ECS Fargate
    
    Instead of using Lambda functions, we can run an ECS task on an EB event.
    
    ![Untitled](architecture-diagrams/untitled-1.png)
    
- Run scheduled jobs on ECS
    
    ![Untitled](architecture-diagrams/untitled-2.png)
    
- Asynchronous Job processing using SQS and ECS
    
    The ECS service will auto-scale on the queue length.
    
    ![Untitled](architecture-diagrams/untitled-3.png)
    
- Tech Stack for CICD
    
    ![Untitled](architecture-diagrams/untitled-4.png)
    
- Indexing S3 Objects Metadata
    
    Store objects’ metadata in S3 to query later.
    
    ![Untitled](architecture-diagrams/untitled-5.png)
    
- API Gateway as a single interface to all the resources
    
    ![Untitled](architecture-diagrams/untitled-6.png)
    
- Authentication at ALB using an OIDC compliant IDP
    
    ![Untitled](architecture-diagrams/untitled-7.png)