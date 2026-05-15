# Stephane Maarek Test 6

## Wrong

- Q1 - important
    
    **A video streaming application uses Amazon CloudFront for its data distribution. The development team has decided to use CloudFront with origin failover for high availability.
    Which of the following options are correct while configuring CloudFront with Origin Groups? (Select two)**
    
    - [ ]  **CloudFront fails over to the secondary origin only when the HTTP method of the viewer request is GET, HEAD or OPTIONS(Correct)**
    - [x]  **CloudFront routes all incoming requests to the primary origin, even when a previous request failed over to the secondary origin(Correct)**
    - [ ]  **When there’s a cache hit, CloudFront routes the request to the primary origin in the origin group**
    - [x]  **In the Origin Group of your distribution, all the origins are defined as primary for automatic failover in case an origin fails(Incorrect)**
    - [ ]  **To set up origin failover, you must have a distribution with at least three origins**
    
    ### **Explanation**
    
    Correct options:
    
    **CloudFront routes all incoming requests to the primary origin, even when a previous request failed over to the secondary origin**
    
    CloudFront routes all incoming requests to the primary origin, even when a previous request failed over to the secondary origin. CloudFront only sends requests to the secondary origin after a request to the primary origin fails.
    
    **CloudFront fails over to the secondary origin only when the HTTP method of the viewer request is GET, HEAD or OPTIONS**
    
    CloudFront fails over to the secondary origin only when the HTTP method of the viewer request is GET, HEAD, or OPTIONS. CloudFront does not failover when the viewer sends a different HTTP method (for example POST, PUT, and so on).
    
- Q5 - important
    
    **An investment firm wants to continuously generate time-series analytics of the stocks being purchased by its customers. The firm wants to build a live leaderboard with near-real-time analytics for these in-demand stocks.
    Which of the following represents a fully managed solution with the least cost to address this use-case?**
    
    - **Use Kinesis Data Streams to ingest data and Kinesis Data Analytics to generate leaderboard scores and time-series analytics(Incorrect)**
    - **Use Kinesis Data Streams to ingest data and Amazon Kinesis Client Library to the application logic to generate leaderboard scores and time-series analytics**
    - **Use Kinesis Firehose to ingest data and Kinesis Data Analytics to generate leaderboard scores and time-series analytics(Correct)**
    - **Use Kinesis Firehose to ingest data and Amazon Athena to generate leaderboard scores and time-series analytics**
    
    ### **Explanation**
    
    Although Kinesis Data Streams supports on-demand provisioning of shards, however, the data ingestion cost along with the per hour shards cost would be more than the corresponding cost incurred while using Firehose. The use-case clearly states that the company wants a fully managed solution with the least cost, so Kinesis Firehose is a better solution.
    
- Q41 - important
    
    **The development team at a retail organization wants to allow a Lambda function in its AWS Account A to access a DynamoDB table in another AWS Account B.
    As a Developer Associate, which of the following solutions would you recommend for the given use-case?**
    
    - **Create an IAM role in Account B with access to DynamoDB. Modify the trust policy of the role in Account B to allow the execution role of Lambda to assume this role. Update the Lambda function code to add the AssumeRole API call(Correct)**
    - **Create a clone of the Lambda function in AWS Account B so that it can access the DynamoDB table in the same account**
    - **Create an IAM role in Account B with access to DynamoDB. Modify the trust policy of the execution role in Account A to allow the execution role of Lambda to assume the IAM role in Account B. Update the Lambda function code to add the AssumeRole API call**
    - **Add a resource policy to the DynamoDB table in AWS Account B to give access to the Lambda function in Account A(Incorrect)**
    
    ### **Explanation**
    
    Correct option:
    
    **Create an IAM role in account B with access to DynamoDB. Modify the trust policy of the role in Account B to allow the execution role of Lambda to assume this role. Update the Lambda function code to add the AssumeRole API call**
    
    You can give a Lambda function created in one account ("account A") permissions to assume a role from another account ("account B") to access resources such as DynamoDB or S3 bucket. You need to create an execution role in Account A that gives the Lambda function permission to do its work. Then you need to create a role in account B that the Lambda function in account A assumes to gain access to the cross-account DynamoDB table. Make sure that you modify the trust policy of the role in Account B to allow the execution role of Lambda to assume this role. Finally, update the Lambda function code to add the AssumeRole API call.
    
- Q47
    
    **A developer is configuring the redirect actions for an Application Load Balancer. The developer stumbled upon the following snippet of code.
    Which of the following is an example of a query string condition that the developer can use on AWS CLI?**
    
    - **`[ { "Field": "query-string", "QueryStringConfig": { "Values": [ { "Key": "version", "Value": "v1" }, { "Value": "*example*" } ] } }
    ]`
    (Correct)**
    - **`[ { "Field": "query-string", "StringHeaderConfig": { "Values": ["*.example.com"] } }
    ]`**
    - **`[ { "Type": "redirect", "RedirectConfig": { "Protocol": "HTTPS", "Port": "443", "Host": "#{host}", "Path": "/#{path}", "Query": "#{query}", "StatusCode": "HTTP_301" } }
    ]`
    (Incorrect)**
    - **`[ { "Field": "query-string", "PathPatternConfig": { "Values": ["/img/*"] } }
    ]`**
    
    ### **Explanation**
    
    Correct option:
    
    - *
    
    ```
    [
      {
          "Field": "query-string",
          "QueryStringConfig": {
              "Values": [
                {
                    "Key": "version",
                    "Value": "v1"
                },
                {
                    "Value": "*example*"
                }
              ]
          }
      }
    ]
    
    ```
    
    - *
    
    You can use query string conditions to configure rules that route requests based on key/value pairs or values in the query string. The match evaluation is not case-sensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). You can specify conditions when you create or modify a rule.
    
- Q49 - important
    
    **A development team has noticed that one of the EC2 instances has been wrongly configured with the 'DeleteOnTermination' attribute set to True for its root EBS volume.
    As a developer associate, can you suggest a way to disable this flag while the instance is still running?**
    
    - **Update the attribute using AWS management console. Select the EC2 instance and then uncheck the Delete On Termination check box for the root EBS volume(Incorrect)**
    - **Set the `DisableApiTermination` attribute of the instance using the API**
    - **The attribute cannot be updated when the instance is running. Stop the instance from Amazon EC2 console and then update the flag**
    - **Set the `DeleteOnTermination` attribute to False using the command line(Correct)**
    
    ### **Explanation**
    
    Correct option:
    
    When an instance terminates, the value of the DeleteOnTermination attribute for each attached EBS volume determines whether to preserve or delete the volume. By default, the DeleteOnTermination attribute is set to True for the root volume and is set to False for all other volume types.
    
    **Set the `DeleteOnTermination` attribute to False using the command line** - If the instance is already running, you can set `DeleteOnTermination` to False using the command line.
    
    Incorrect options:
    
    **Update the attribute using AWS management console. Select the EC2 instance and then uncheck the Delete On Termination check box for the root EBS volume** - You can set the `DeleteOnTermination` attribute to False when you launch a new instance. It is not possible to update this attribute of a running instance from the AWS console.
    

## Doubtful

- Q21
    
    **A developer is creating a RESTful API service using an Amazon API Gateway with AWS Lambda integration. The service must support different API versions for testing purposes.
    As a Developer Associate, which of the following would you suggest as the best way to accomplish this?**
    
    - **Use an X-Version header to identify which version is being called and pass that header to the Lambda function**
    - **Deploy the API versions as unique stages with unique endpoints and use stage variables to provide the context to identify the API versions(Correct)**
    - **Use an API Gateway Lambda authorizer to route API clients to the correct API version**
    - **Set up an API Gateway resource policy to identify the API versions and provide context to the Lambda function**
- Q33 - important
    
    **A photo-sharing application manages its EC2 server fleet running behind an Application Load Balancer and the traffic is fronted by a CloudFront distribution. The development team wants to decouple the user authentication process for the application so that the application servers can just focus on the business logic.
    As a Developer Associate, which of the following solutions would you recommend to address this use-case with minimal development effort?**
    
    - **Use Cognito Authentication via Cognito Identity Pools for your CloudFront distribution**
    - **Use Cognito Authentication via Cognito Identity Pools for your Application Load Balancer**
    - **Use Cognito Authentication via Cognito User Pools for your Application Load Balancer(Correct)**
    - **Use Cognito Authentication via Cognito User Pools for your CloudFront distribution**
    
    ### **Explanation**
    
    You cannot directly integrate Cognito User Pools with CloudFront distribution as you have to create a separate Lambda@Edge function to accomplish the authentication via Cognito User Pools. This involves additional development effort, so this option is not the best fit for the given use-case.
    
- Q61 - important
    
    **A development team has been using Amazon S3 service as an object store. With Amazon S3 turning strongly consistent, the team wants to understand the impact of this change on its data storage practices.
    As a developer associate, can you identify the key characteristics of the strongly consistent data model followed by S3? (Select two)**
    
    - [ ]  **A process deletes an existing object and immediately lists keys within its bucket. The object could still be visible for few more minutes till the change propagates**
    - [x]  **If you delete a bucket and immediately list all buckets, the deleted bucket might still appear in the list(Correct)**
    - [ ]  **A process deletes an existing object and immediately tries to read it. Amazon S3 can return data as the object deletion has not yet propagated completely**
    - [ ]  **A process replaces an existing object and immediately tries to read it. Amazon S3 might return the old data**
    - [x]  **A process deletes an existing object and immediately tries to read it. Amazon S3 will not return any data as the object has been deleted(Correct)**
    
    ### **Explanation**
    
    Correct options:
    
    **If you delete a bucket and immediately list all buckets, the deleted bucket might still appear in the list** - Bucket configurations have an eventual consistency model. If you delete a bucket and immediately list all buckets, the deleted bucket might still appear in the list.
    
    **A process deletes an existing object and immediately tries to read it. Amazon S3 will not return any data as the object has been deleted** - Amazon S3 provides strong read-after-write consistency for PUTs and DELETEs of objects in your Amazon S3 bucket in all AWS Regions. This applies to both writes to new objects as well as PUTs that overwrite existing objects and DELETEs.