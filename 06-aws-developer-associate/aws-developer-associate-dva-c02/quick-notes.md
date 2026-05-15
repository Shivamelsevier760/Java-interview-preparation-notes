# Quick Notes

---

### Route 53

- EC2 cannot be a pointed to by an Alias record
- Primary record must have health check for failover routing policy
- **Failure Threshold** is the parameter used by Route 53 health checks to determine if an endpoint is healthy. A failure occurs if an endpoint does not respond to a request.
- Route 53 can be used as a DNS to register a domain name, route the internet traffic, and perform health checks on resources. If being used for all three tasks, the order of setup must be sequential as above.

### ELB

- ELB has access logs
- ALB, NLB and CloudFront support SNI
- Session affinity is only supported by CLB and ALB (layer 7)

### API Gateway

- For `HTTP_PROXY` integration type, option to add HTTP headers in the request (eg. API key)
- Mapping template uses **Velocity Template Language (VTL)**
- Private endpoints can only be accessed within your VPC using an **Interface VPC endpoint** (ENI)
- **TTL: 0 s - 1 h (default 300 sec)**
- Two types of logs:
    - **Execution Logs**: log requests, responses, etc.
    - **Access Logs**: who accessed the API and how
- When the integration type is proxy-based, the responses are proxied to the client without modification by API gateway. So, CORS needs to be handled by the backend itself.
- `MaxAgeSeconds` specifies the TTL used by browser to cache pre-flight response
- **Associate** API stages and **API keys with the usage plan** using `CreateUsagePlanKey` API

### ECS

- It doesn't automatically handle resource provisioning, balancing load, auto-scaling, monitoring, and placing your containers across your cluster. Use **Elastic Beanstalk** for that.
- **ECS Cluster Capacity Provider** - automatically scales out EC2 instances when the service is missing capacity.
- Use **advanced container definition parameters** to define environment variables for a task.
- **Cluster Query Language** can be used to write expressions to group container instances

### ASG

- Predictive scaling using ML

### CloudFormation

- Parameters can be modified without having to re-upload the template
- Supported parameter types:
    
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
    
- Exported output name must be unique within the region.
- **Conditions cannot be used within the Parameters section**
- Conditions can reference other conditions for nesting
- Enable SNS integration when creating a stack to **send stack events to an SNS topic**
- **Stack Policy defines the update actions that are allowed or denied on specific resources during stack update**
- By default, all update actions are allowed to all the resources during a stack update. When you create a **stack policy**, all update operations on all the stack resources are denied. You need to explicitly allow update operations on the resources.
- If the stack is stuck in a `DELETE_FAILED` state because some resource failed to be deleted, modify the template to retain the resource and manually delete it after the deployment.

### Elastic Beanstalk

- Lifecycle policy to phase out old versions based on:
    - **Days** (delete versions older than x days)
    - **Count** (keep latest x versions)
- Option to retain the old version’s source bundle in S3
- Config files should be present in `.ebextensions/` directory in the root of the source code
- Config files should have `.config` extension and should be in YAML or JSON format
- Through EB Extensions, we have the ability to add resources (RDS, ElastiCache, etc.) through CloudFormation, which cannot be done from the EB console.
- **If some change cannot be done in an environment** (eg. changing the load balancer type), **we need to migrate our environment.**
- Running containerized applications
    - Single container (without ECS)
        - `Dockerfile` - EB will build and run the Docker container (doesn’t require a pre-built docker image in a container repository)
        - `Dockerrun.aws.json` (v1) - describes where the prebuilt Docker image is along with how to run it (ports, volumes, etc.)
    - Multi container (uses ECS)
        - `Dockerrun.aws.json` (v2) - The Docker images must be pre-built and stored in a container repository.
- TLS certificate can be configured in the `.ebextensions/securelistener-alb.config` file
- Health Checks should not be redirected from HTTP to HTTPS
- If your app’s language is incompatible with Beanstalk and does not use Docker, create a custom platform using `Platform.yaml` file.
- Blue-Green deployment is not directly available in Beanstalk
- To deploy a new application version through the console, you'll need to upload a source bundle that meets the following requirements:
    - Consist of a **single** ZIP file or WAR file
    - Not exceed 512 MB
    - Not include a parent folder or top-level directory (subdirectories are fine)
- To deploy a worker application that processes periodic background tasks, the application bundle must include a `cron.yaml` file.
- EB can configure EC2, CloudWatch and ALB. **It cannot configure Lambda or CloudFront.**
- Environment variables can be defined in `env.yaml` present in the root of the source bundle.
- To deploy a new version of the application, package your application as a `zip` or `war` file and deploy it using `eb deploy` command.
- To migrate an EB environment between accounts, create a saved configuration in the first account and download it to your local machine. Make the account-specific parameter changes and upload to the S3 bucket in second account. From Elastic Beanstalk console, create an application from **Saved Configurations**.

### SAM

- Deploy locally for development using **SAM CLI** and **AWS Toolkits**
- SAM uses CodeDeploy under the hood to update Lambda functions every time we update the code and deploy (traffic shifting using aliases).

### CDK

- Supports JavaScript/TypeScript, Python, Java and .NET
- The code is compiled to a CloudFormation template using **CDK CLI**
- **AWS Construct Library** - a collection of Constructs included in AWS CDK which contains Constructs for every AWS resource
- **Construct Hub** - repository of constructs created by AWS, 3rd parties, and open-source CDK community
- Before using CDK to deploy an app in any AWS environment, we need to deploy a CloudFormation stack called **CDK Toolkit** in that environment (combination of account & region), using the command ****`cdk bootstrap aws://<aws_account>/<aws_region>`.
- Use **CDK Assertions Module** along with testing frameworks like Jest or PyTest for testing the resources created by CDK.
    - **Fine-grained Assertions** (common) - test specific aspects of the CloudFormation template
    - **Snapshot Tests** - test the synthesized CloudFormation template against a previously stored baseline template

### CUP

- To host the hosted UI on a custom domain, we must create an ACM certificate in `us-east-1`
- **Adaptive authentication** - sign-in attempts may be blocked or require MFA if they seem suspicious
- For integration with ALB, must use an HTTPS listener

### CIP

- Use CUP or any OIDC compliant IDP for authentication
- IAM roles must have a **trust policy** of CIP
- IAM policies for each role can be customized for each user using **policy variables**.

### Cognito Misc

- Cognito lets you save end user data in datasets containing key-value pairs. This data is associated with an Amazon Cognito identity, so that it can be accessed across logins and devices. To sync this data between the Amazon Cognito service and an end user’s devices, invoke the `synchronize` method. Each dataset can have a maximum size of 1 MB. You can associate up to 20 datasets with an identity.
- Cognito supports **developer authenticated identities** to obtain unique identifiers for application users.
- When a user signs in to an application using their username and password, Cognito generates a unique **Cognito ID** for that user. This ID is used to track the user's session and to provide secure access to AWS resources.

### IAM

- Global Service (IAM entities like roles can be used in any region without recreation)
- **IAM Query API** can be used to make direct calls to the IAM web service (using access key ID and secret access key for authentication)
- By default, IAM users do not have access to the AWS Billing and Cost Management console.
- The following policy types only limit permissions (cannot grant permissions)
    - Service Control Policy (SCP)
    - Permission Boundary
- SMS-based MFA is available only for IAM users, not for the root user.
- IAM Groups cannot be identified as principal in an IAM policy. They cannot assume a role.
- Customer managed policy is versioned whereas inline policy is not
- A **service-linked role** is a pre-defined IAM role that is linked directly to an AWS service, not a resource. It includes all the permissions that the service requires to call other AWS services on your behalf.
- If access keys are compromised, invalidate the access keys by deleting them.
- Best practices
    - Delete (don’t generate) access keys for the root user
    - Use Temporary Security Credentials (IAM Roles) instead of long-term access keys
    - The root account should only be accessible by one admin user with MFA
- Permission boundaries can only be applied to users and roles (not groups)
- To pass a Role to an AWS service, to assume, requires `iam:PassRole` permission for the user. The user should also have `iam:GetRole` permission to view the role being passed.
- Roles can only be passed to those services that are allowed to assume that role (specified in the role’s **Trust Policy**)
- IAM roles and resource-based policies delegate access across accounts only within a single partition.

### AD

- AWS managed AD supports **directory-aware workloads on AWS** whereas AD connector does not.

### KMS

- **Does not support versioning of keys** (cannot get back the old key)
- For customer managed keys, deletion has a waiting period (**pending deletion state**) between **7 - 30 days** (default 30 days). The key can be recovered during the pending deletion state.
- Asymmetric keys
    - Can be generated in KMS
    - No need to call the KMS API to encrypt data (data can be encrypted by the client)
    - Not eligible for automatic rotation (use manual rotation)
- Cannot access KMS keys without a key policy attached to them
- Default key policy - full access to the key for any user or role in the account
- Custom key policy can only be applied to customer-owned keys
- **Encryption SDK** implements envelope encryption with **data key caching** (leverages `LocalCryptoMaterialsCache` feature)
- Some supported key operations:
    - **Temporarily disable keys** so they cannot be used by anyone
    - **Re-enable disabled keys**
    - **Schedule deletion of keys**

### Parameter Store

- Parameters are versioned

### Secrets Manager

- **Mandatory encryption** using KMS
- **Ability to force rotation of secrets every n days** (not available in Parameter Store)
- **Automated secret rotation using Lambda** (needs IAM permission)
- **Secrets are retained after deletion for 7 - 30** (default) days (waiting period)
- Mostly used for DB authentication

### Nitro Enclaves

- **Fully isolated VMs** for **processing highly sensitive data** such as PII, healthcare data, etc.
- **No interactive access** (eg. SSH) or external networking (reduces attack surface)
- **Cryptographic Attestation**: only authorized code can be run in the Enclave

### ACM

- TLS certificates can be loaded on ELB, API Gateway and CloudFront distributions.
- **ACM issued certificates are valid for 13 months.** They are also renewed automatically.
- **Imported certificates are not automatically renewed** and would need to be imported after getting renewed from the 3rd party.
- For regions where ACM is not supported, **IAM Certificate Store** can be used to import SSL certificates issued by a 3rd party.
- An ACM certificate that was validated using DNS validation will automatically renew if the certificate is still being using by an AWS service 60 days prior to its expiration and has an ACM-provided CNAME that is accessible via public DNS. If the certificate is not being used or if the CNAME is not correct, ACM will not automatically validate the DNS and will send notifications starting at 45 days prior to the expiration date.

### Private CA

- Used to create Private CA (root or subordinate)
- Integrates with ELB, API Gateway, CloudFront and **EKS** to load private certificates

### Organization

- SCP - Whitelist or blacklist IAM actions at the OU or Account level
- SCP does not apply to the master account or service-linked roles

### SQS

- Max message size: 256 KB
- Default message retention: 4 days (max: 14 days)
- Batching is configured using `MaxNumberOfMessages` parameter in the `ReceiveMessage` API
- Queue type cannot be changed once created
- For FIFO queues, max number of consumers = number of unique group IDs
- Default message visibility timeout = 30 s
- Max long polling duration = 20 s (uses `WaitTimeSeconds` parameter)
- DLQ must be of the same type as the original queue

### SNS

- In-flight encryption by default using HTTPS API
- At-rest encryption using KMS keys (optional)
- KDF can be subscribed to a standard SNS topic to send data into S3 or Redshift

### EventBridge

- EventBridge delivers a near real-time stream of system events that describe changes in AWS resources.
- Event buses support cross-account access using Event Bus Policy
- Can archive events (all or based on a filter) sent to an event bus to replay later
- Event schema can be versioned
- The target for an event rule in an account can be an event bus in another account.

### KDS

- Data Retention: 1 day (default) to 365 days
- Once data is inserted in KDS, it can’t be modified or deleted (immutability)
- Ability to re-process (**replay**) data
- Capacity modes
    - **Provisioned**
        - Publishing: 1MB/sec per shard or 1000 records/sec per shard
        - Consuming:
            - **Shared**: 2MB/sec per shard
            - **Enhanced Fanout**: 2MB/sec per shard per consumer
    - **On-demand** - auto scaling with default capacity provisioned - **4 MB/sec or 4000 records/sec**
- **KDS is present outside the VPC.** VPC endpoints can be used to access Kinesis from within the VPC.
- **Batching** in `PutRecord` API **reduces cost and increases throughput** (automatically done by KPL)
- **Use KPL to achieve high write throughput in KDS**
- Embed a primary key within the record to handle duplicate records on the consumer side
- In shared consumer model, **consumers poll data from KDS** using `GetRecords` API call (**pull-based**)
- In enhanced fanout consumer model, **consumers subscribe to a shard** using `SubscribeToShard` API. KDS pushes data to consumers (**push-based**)
- Maximum number of KCL instances = number of shards
- KCL checkpoints the read progress into DynamoDB

### KDF

- **Writes data in batches efficiently (near real time)**
- AWS destinations: S3, Redshift (copy through S3), **OpenSearch**
- Greater the buffer size, higher the write efficiency, longer it will take to fill the buffer
- **Custom data transformation using Lambda functions** (not supported in KDS)
- **No replay capability** (does not store data like KDS)

### KDA

- Perform real-time analytics on streaming data
- SQL
    - ingests data from **KDS** or **KDF**
    - **serverless** querying using SQL
- Flink
    - ingests data from **KDS** or **MSK**
    - advanced querying using Flink

### AppSync

- Building **GraphQL** APIs
- **Offline data synchronization** in mobile devices
- Retrieve data in real-time with WebSocket or MQTT on WebSocket
- To get HTTPS on AppSync with a custom domain, use CloudFront in front of AppSync

### MSK

- Used to stream data (alternative to KDS)
- **MSK Serverless**: auto-scaling MSK cluster without provisioning or managing capacity
- No in-flight encryption

### Instance Store

- Millions of IOPS
- Loses data even when the instance is hibernated
- Can be configured only during instance launch

### EBS

- Bound to an AZ
- `DeleteOnTermination` attribute can be updated for the root EBS volume for a running instance only from the CLI. It can be done from the console only if the instance is stopped.
- **New EBS volumes are raw block storage and do not contain any partition or file system**. You need to login to the instance and **format the EBS volume with a file system** for it to be usable.
- Boot volumes must be SSD type
- General purpose SSD
    - 3 IOPS per GB
    - max 16,000 IOPS (at 5,334 GB)
- Provisioned IOPS SSD
    - 50 IOPS per GB
    - max 32,000 IOPS for normal EC2 instances and 64,000 IOPS for nitro EC2 instances
    - supports EBS multi-attach (not supported by other types)
    - io2 block express - 1000 IOPS per GB, max 256,000 IOPS
- Throughput Optimized HDD (st1) - max 500 IOPS
- Cold HDD (sc1) - max 250 IOPS
- **Data Lifecycle Manager (DLM)** can be used to automate the creation, retention, and deletion of snapshots of EBS volumes
- **Snapshots are incremental** but only the most recent snapshot is required to restore the volume

### EFS

- Serverless
- Can be mounted to multiple EC2 instances **across AZs**
- Compatible with **Linux** based AMIs (**POSIX** file system)
- Lifecycle management feature to move files to **EFS-IA** after N days

### RDS

- **Automated daily backup**
    - Backup retention: 7 days (max 35 days)
    - **Transaction logs** are backed-up every **5 minutes** for **Point In Time Recovery (PITR)**
    - **Automated backups happen in the same region** (can happen in multiple AZs in a multi-AZ deployment)
- Manually triggered **DB Snapshots**
    - Backup retention: unlimited
    - **Snapshots can be saved across regions**
- Read replicas can be within AZ, cross AZ or cross region
- RDS proxy
    - **No code changes required** (just update the connection URL)
    - **Allows to enforce IAM DB Auth** (credentials can be stored in Secrets Manager)
    - **RDS Proxy can only be accessed from within the VPC**
- To enable encryption in transit, download the **AWS-provided root certificates** and use them when connecting to DB
- IAM DB Auth (only for MySQL and PostgreSQL) - token based access (token valid for 15 mins)
- Secrets - credentials based access
- Monitoring
    - CW metrics - CPU utilization, connections, etc.
    - Enhanced monitoring - OS processes, child processes, etc.
- **Slow Query Logs** - logs queries that took longer to execute (can be enabled)
- RDS supports using **Transparent Data Encryption (TDE)** to encrypt stored data on your DB instances running **Microsoft SQL Server**. TDE automatically encrypts data before it is written to storage, and automatically decrypts data when the data is read from storage.

### Aurora

- **Supports only MySQL & PostgreSQL**
- **Backtrack**: restore data at any point of time without taking backups
- **Writer Endpoint** (Cluster Endpoint) points to the master
- **Automated failover**
    - A read replica is promoted as the new master in less than 30 seconds. Aurora flips the **CNAME** record for your DB Instance to point at the healthy replica
    - In case **no replica** is available, Aurora will attempt to **create a new DB Instance** in the **same AZ** as the original instance.
- Maintains 6 copies of data across 3 AZ
- Aurora multi-master - Immediate failover for writes (high availability in terms of write). If disabled and the master node fails, need to promote a Read Replica as the new master (will take some time).
- Aurora Replicas are created in the same DB cluster within a Region. With **Aurora MySQL** you can also enable **binlog replication** to another Aurora DB cluster which can be in the **same or different region**.
- Important parameters:
    - `max_connections` - max number of simultaneous connections Aurora allows
    - `max_user_connections` - max number of simultaneous connections Aurora allows for a single user

### DynamoDB

- **Maximum item size: 400 KB**
- If the partition (hash) key is not highly diverse (only few unique values), add a suffix to the partition key to make the partition key diverse.
- Set `ConsistentRead: True` in API calls (`GetItem`, `BatchGetltem`, `Query`, `Scan`) to perform a strongly consistent read
- Provisioned capacity mode has **optional throughput auto-scaling** (automatically scales RCU and WCU) based on target utilization
- Provisioned throughput can be exceeded temporarily using **Burst Capacity**
- Backup types:
    - **On-demand**
    - **Point-in-time recovery (PITR)** - automatic continuous backups
- **Backups are written to S3** under the hood but we cannot access these backup buckets
- `Query` can be made on the table, LSI or GSI whereas `Scan` is done on the table.
- `FilterExpression` - client-side filtering on non-key attributes after a query
- `Query` and `Scan` return up to 1 MB of data (use pagination for more)
- Conditional write is supported by `PutItem`, `UpdateItem`, `DeleteItem` and `BatchWriteItem` APIs
- Queries on LSI support both eventual consistency and strong consistency whereas for GSI only eventual consistency is supported.
- If the writes are throttled on the GSI, the main table will be throttled for writes as well. So, provision WCUs equal or more than the main table for GSI.
- Max 10 nodes in DAX cluster
- Data retention in DynamoDB stream = 1 day
- **KCL** (using **Kinesis Adapter**) is the **recommended way to consume DynamoDB streams** for real-time processing because it provides useful abstractions.
- No need to provision shards for DynamoDB streams
- DynamoDB stream can be used to recover items deleted through TTL
- **Fine-grained (low level) access control** using **federated login** and:
    - `LeadingKeys` - limit access to rows
    - `Attributes` - limit access to columns
- Use `UpdateItem` operation to implement an ***atomic counter,*** a numeric attribute that is incremented, unconditionally.
- **Global Tables** - multi-region, multi-active, replicated tables (need to enable DynamoDB streams)
- **DynamoDB Local** - deploy DynamoDB locally for development or testing
- **AWS Database Migration Service (DMS)** can be used to migrate data to DynamoDB
- **Partitioning data too finely is bad** (can increase the overhead of retrieving and processing the partition metadata)
- Reduce page size to reduce consumed RCU
- To perform scan operations for analytics purposes, the best way is to create a **shadow table** (copy of the original table) and perform scans on it. This way scan operations don’t impact the RCU of the main table.
- To return the number of WCUs consumed by any write operation, set the `ReturnConsumedCapacity` parameter to one of the following:
    - `TOTAL` - total number of WCU consumed
    - `INDEXES` - total number of WCU consumed, with subtotals for the table and any secondary indexes that were affected by the operation
    - `NONE` - returns nothing (default)
- To perform an upsert operation, we only need permission for `GetItem` and `UpdateItem` (also has the permission to put an item if it doesn’t exist).

### S3

- Max object size = 5 TB
- S3 objects are strongly consistent but the bucket configuration is eventually consistent
- Envelope encryption is used in SSE-KMS. The user uploading the file must have `kms:GenerateDataKey` permission.
- Enforce HTTPS connection by creating an S3 bucket policy that denies incoming request where `SecureTransport` is `false`
- Pre-signed URL (Query String Authentication)
- Bucket versioning must be enabled for MFA delete
- S3 access logs (sent to another bucket) do not support **Data Events** & **Log File Validation** (use CloudTrail for that)
- CloudTrail Logging
    - Bucket level API access logs enabled by default
    - Object level API access logs not enabled by default
    - Bucket owner needs to be the object owner to get object access logs
- Replication
    - Versioning must be enabled for source and destination buckets
    - Lifecycle actions are not replicated
    - Can be configured at the S3 bucket level, prefix level, or object level using S3 object tags
- Storage Classes
    - Standard
    - IA
        - Standard IA
        - One-zone IA
    - Glacier (need to restore objects)
        - Instant Retrieval ~ ms
        - Flexible Retrieval
            - Expedited Retrieval → 1 - 5 mins (provision capacity option)
            - Standard Retrieval → 3 - 5 h
            - Bulk Retrieval → 5 - 12 h
        - Deep Archive
            - Standard Retrieval → 12 h
            - Bulk Retrieval → 48 h
    - Intelligent Tiering - no retrieval fee
- Lifecycle Rules can be created for the bucket or prefix (ex `s3://mybucket/mp3/*`) or object tags (ex Department: Finance)
- S3 Analytics provides analytics to determine when to transition data into different storage classes (does not work for `ONEZONE_IA` & `GLACIER`)
- **Multi-part upload**
    - recommended for files > 100 MB
    - must use for files > 5 GB
- **Transfer acceleration** - recommended for objects > 1 GB (both upload and download)
- For the same combination of prefix and event type, we can only have one event rule.
- Targets for S3 notification events cannot be SQS FIFO queues
- **Access Point** allows having a simple bucket policy and moving the complexity of defining access at the access point level using **Access Point Policies**.
- Each Access Point has a unique DNS name (public or private) through which it can be accessed.
- **S3 Object Lambda** allows us to modify the object dynamically, using a Lambda function, when it is fetched.
- **Cannot search on metadata or tags directly in S3** (need to build a search index in an external DB)
- With versioning, every successful write will create a new version of your object and will also send event notification.
- To ensure SSE-KMS on the bucket, add a bucket policy which denies any `s3:PutObject` action unless the request includes the `x-amz-server-side-encryption` header.
- `x-amz-server-side-encryption-aws-kms-key-id` header is used to enforce SSE-KMS using a specific KMS key.
- **S3 Object Ownership** setting can be used to make the bucket owner default owner of uploaded objects in the bucket.
- To perform a multipart upload with encryption using a KMS customer master key (CMK), the requester must have permission to the **`kms:Decrypt`**  and **`kms:GenerateDataKey*`** actions on the key. These permissions are required because Amazon S3 must decrypt and read data from the encrypted file parts before it completes the multipart upload.

### CloudFront

- TTL (0 sec - 1 year)
- **Edge Locations are present outside the VPC** so the origin's SG must be configured to allow inbound requests from the list of public IPs of all the edge locations.
- Supports HTTP/RTMP protocol (**does not support UDP protocol**)
- To block a specific IP at the CloudFront level, deploy a WAF on CloudFront
- Origin Groups
    - Automated failover from **primary** to **secondary** origin (can be in **different regions**)
    - CloudFront fails over to the secondary origin only when the HTTP method of the viewer request is `GET`, `HEAD`, or `OPTIONS`.
    - CloudFront routes all incoming requests to the primary origin, even when a previous request failed over to the secondary origin. It only sends requests to the secondary origin after a request to the primary origin fails.
- Signed URL/Cookies
    - **Trusted Key Group** signer is the recommended way of configuring CloudFront to use signed URLs or cookies. It is not recommended to create a CloudFront key-pair in an AWS account and access it at the root level.
    - The signer uses its private key to sign the URL or cookies, and CloudFront uses the public key to verify the signature.
    - Can apply filtering rules (cannot for S3 pre-signed URL)
- **Default Cache Key**: hostname + resource portion of the URL
- The fewer items in the cache key, the better the caching performance.
- All HTTP headers, cookies, and query strings included in the Cache Key are automatically included in origin requests
- **Cache behavior** - configure cache differently based on the path pattern in the request
- If the content is updated at the origin, we can invalidate the cache at all the edge locations using `CreateInvalidation` API.
- Can invalidate the entire cache, a single file or all the files at a given path.
- **Cache invalidation is not cost-effective** (need to pay extra for invalidation requests)
- For a cost effective solution, version your objects using the path or filename and update the application to pull the new version.
- Send CloudFront logs in real-time to KDS
- **Origin Protocol Policy**: used to enable SSL between the distribution and the origin
- **Viewer Protocol Policy**: used to enable SSL between the client (user) and the distribution
- TLS termination takes place at the distribution level. If the distribution - origin connection needs to be encrypted, another TLS connection is established.
- You cannot directly integrate Cognito User Pools with CloudFront distribution as you have to create a separate Lambda@Edge function to accomplish the authentication via Cognito User Pools.

### ElastiCache

- Need to provision EC2 instances (nodes for the cluster)
- Use **Redis Auth** to authenticate to ElastiCache for Redis
- **Automated failover over multi-AZ** - if the primary node fails, one of the read-replicas will take over as the new master
- 1 primary node and up to 5 read-replicas (asynchronous replication)
- Cluster Mode Enabled
    - You cannot manually promote any of the replica nodes to primary.
    - You can only change the structure of a cluster, the node type, and the number of nodes by restoring from a backup.
- In write through caching strategy, the cache and the DB cannot be updated at the same time via a single atomic operation as these are two separate systems. The cache must be updated or invalidated after writing to the DB.

### Athena

- Use compressed or columnar data for cost-savings (due to less scan)
- Use fewer large files (> 128 MB) instead of many small files for faster processing
- **Federated Query** - run SQL queries on data stored in any data source using **Data Source Connector** running on Lambda
- The `MSCK REPAIR TABLE` command scans Amazon S3 for Hive compatible partitions that were added to the file system after the table was created. It compares the partitions in the table metadata and the partitions in S3. If new partitions are present in S3, it adds those partitions to the metadata and to the Athena table. It can work better than DDL commands if have more than a few thousand partitions and DDL is facing **timeout issues.**

### OpenSearch

- Used in combination with a database to perform **enhanced search operations on the database** (can search on any field, even supports **partial matches)**
- Need to provision a cluster of instances (supports multi-AZ)
- **Does not support SQL** (has its own query language)
- CW logs can be written to OpenSearch using KDF for advanced search capability

### CLI & SDK

- The CLI or SDK looks for the credentials in the following order:
    - CLI or SDK options
    - Environment Variables
    - `~/.aws/credentials` file
    - `~/.aws/config` file
    - ECS Container Credentials or EC2 Instance Profile Credentials
- The CLI or SDK automatically signs the request made by you to the AWS HTTP APIs so that AWS can verify whether or not the request came from you.
- **The request is signed using your AWS credentials** using AWS proprietary **SigV4 signing algorithm**.
- Custom **HTTP requests** made to the AWS API must be signed by the user.

### Extras

- AWS requires approximately 5 weeks of usage data to generate budget forecasts.
- **Never store AWS credentials in your code.** If your code is running inside AWS, use IAM roles to access AWS services. If your code is running outside AWS, use environment variables or named AWS profiles.
- By default, the AWS Management Console is organized by AWS service. But with **Resource Groups**, you can create a custom console that organizes and consolidates information based on criteria specified in tags, or the resources in an AWS CloudFormation stack.

### CloudWatch

- Custom Metrics
    - Standard: 1 min
    - High Resolution: 1 sec
    - Alarm period: 10 sec
- EC2 Monitoring
    - CW Agent must be running
    - Standard: 5 min
    - Detailed Monitoring: 1 min (can be enabled using `aws ec2 monitor-instances` command)
- An alarm monitors a single CW metric
- Alarm Configuration:
    - **Period**: length of time (seconds) to evaluate the metric to create a data point for the alarm (**min 10 sec** for high resolution custom metric)
    - **Evaluation Period**: number of the most recent periods (data points) to consider when determining the alarm state
    - **Datapoints to Alarm**: number of data points within the evaluation period that must be breached to cause the alarm to go into `ALARM` state
- **Composite Alarms** are used to reduce alarm noise
- Log Encryption must be done using CloudWatch Logs API (cannot be done through the console)

### CloudTrail

- **Global Service** (a single trail can be applied to multiple regions)
- **Event retention: 90 days**
- Export CloudTrail logs into
    - CloudWatch Logs
    - S3 (encrypted by default using **SSE-S3**)
- CloudTrail logs up to the last 90 days can be analyzed in CloudTrail Console. Older logs should be present in S3 and can be analyzed using **Athena**.
- Modifications to log files can be detected by enabling **Log File Validation** on the logging bucket
- A single KMS key can be used to encrypt log files for trails applied to all regions
- Organization trail
    - Trail that logs events across all the accounts in an organization
    - Must be created in the master account
    - Member accounts will be able to see the organization trail, but cannot modify or delete it.
    - By default, member accounts will not have access to the log files for the organization trail in the S3 bucket.

### X-Ray

- **Preferred over CloudWatch to debug serverless or distributed applications**
- X-Ray daemon can **send traces across accounts** **by assuming an IAM Role** (allows to have a central account for application tracing)
- X-Ray SDK sends traces to X-Ray daemon through **UDP** on **port 2000**
- **Annotations**: indexed key-value pairs attached to traces for search capability and filtering traces using **filter expressions**
- Sampling rules can be modified in the X-Ray console without changing the application code or restarting the application. The sampling rules are automatically applied to the X-Ray daemons.
- By **default**, the X-Ray SDK records the **first request each second** (**reservoir**), and **five percent of any additional requests** (**rate**).
- With Elastic Beanstalk
    - Enable X-Ray daemon by including the `xray-daemon.config` configuration file in the `.ebextensions` directory of your source code.
    - X-Ray daemon must be manually setup in Multi-Container Docker
- With ECS, X-Ray daemon must be running as a container
    - EC2 - one X-Ray daemon container per EC2 instance or sidecar
    - Fargate - one X-Ray daemon container per task (sidecar)
    - Create a Docker image that runs the X-Ray daemon, upload it to a Docker image repository, and then deploy it to the Amazon ECS cluster.
- Trace segments can be uploaded using `PutTraceSegments` API
- X-Ray daemon uses `PutTelemetryRecords` API to send telemetry data
- Lambda functions use environment variables to facilitate communication with X-Ray
    - `AWS_XRAY_DAEMON_ADDRESS`
    - `_X_AMZN_TRACE_ID`
    - `AWS_XRAY_CONTEXT_MISSING`
- Use the `GetTraceSummaries` API to get the list of trace IDs and then retrieve the list of traces using `BatchGetTraces` API
- Prefer **AWS Distro for OpenTelemetry** over X-Ray if you want to send traces to multiple different tracing backends without having to re-instrument your code.
- We can define arbitrary subsegments to instrument specific functions or lines of code in an application.
    
    ![](https://media-tutorials-dojo.s3-ap-southeast-2.amazonaws.com/pic.PNG)
    
- A subset of segment fields are indexed by X-Ray for use with filter expressions. Example, if you set the `user` field on a segment to a unique identifier, you can search for segments associated with specific users in the X-Ray console or by using the `GetTraceSummaries` API.

### CodeCommit

- **Repos are encrypted by default** (at rest using KMS keys and in flight using HTTPS or SSH)
- Enable **repository level notifications** on an **SNS topic**
- IAM supports CodeCommit with three types of credentials:
    - **Git credentials**: an IAM-generated username and password pair you can use to communicate with CodeCommit repositories over **HTTPS**
    - **SSH keys**: a locally generated public-private key pair that you can associate with your IAM user to communicate with CodeCommit repositories over **SSH**
    - **AWS access keys**: which you can use with the **Git Credential Helper** included with the AWS CLI to communicate with CodeCommit repositories over **HTTPS**
- **cURL cannot be used to work with the CodeCommit API** (must use AWS SDK)
- Recommended to generate Git credentials in the IAM console to access repos in CodeCommit

### CodeBuild

- **CodeBuild can be run locally** (requires Docker) using **CodeBuild Agent** for troubleshooting purposes.
- **By default, CodeBuild containers are launched outside the VPC.** It cannot access resources within the VPC. When creating a CodeBuild project, we can specify the VPC where it should be launched. This way, the CodeBuild project can access resources within the VPC.
- Can’t access the CodeBuild containers
- **CodeBuild scales automatically** to meet peak build requests.

### CodeDeploy

- **Compute Platform** - what platform the application will be deployed to
    - EC2 or On-Premises (**CodeDeploy Agent** must be installed)
    - AWS Lambda
    - Amazon ECS
- **Deployment Group** - group of tagged EC2 instances (allows to deploy gradually, ex: first deploy to `dev`, then `test` and then `prod`)
- **Service Role** - IAM Role for CodeDeploy to perform operations on EC2 instances, ASGs, ELBs for deployment
- Hooks
    - Lambda: BeforeAllowTraffic > AfterAllowTraffic
    - EC2: BeforeInstall → AfterInstall → ApplicationStart → ValidateService
    - ECS: BeforeInstall → AfterInstall → AfterAllowTestTraffic → BeforeAllowTraffic → AfterAllowTraffic
- The content in the `resources` section varies, depending on the compute platform of your deployment. For Lambda functions, it has `name`, `alias`, `currentversion` and `targetversion`.
- Deployment Type
    - In place (EC2, on-premise)
    - Blue/Green (EC2, Lambda, ECS)
- Once deployment fails, EC2 instances stay in failed state
- New deployments will first be deployed to failed instances
- If a rollback happens, CodeDeploy redeploys the last known good revision with a new deployment ID (does not restore to a previous version).
- `InvalidSignatureException` - the date or time in CodeDeploy (AWS) does not match that in the EC2 instance where the application is to be deployed

### CodePipeline

- **Each stage in the pipeline creates an artifact which is stored in S3** (**Artifact Store**). The next stage uses this artifact as input.
- **Within a stage, we have action groups where actions can run sequentially or in parallel.**
- **Events are generated in EventBridge (CW Events) for changes in the state of a pipeline**.
- CodePipeline can be triggered by an EB event generated by CodeCommit
- For a version control application outside of AWS (eg. GitHub), need to use **CodeStar Source Connection** to trigger the CodePipeline on event from GitHub.
- For manual approval, the owner must be AWS and the user must have `codepipeline:GetPipeline*` permission to view the pipeline and `codepipeline:PutApprovalResult` permission to approve the pipeline.
- CloudFormation can be integrated with CodePipeline to create a test stack and delete it after the tests have been run.

### CodeArtifact

- **Artifacts (dependencies) live inside the VPC**
- A repository can have **max 10 upstream repositories**
- Domain - single shared storage for all the repositories across multiple accounts
- **Domain Resource-based Policy**: domain administrator can apply policy across the domain such as:
    - Restricting which accounts have access to repositories in the domain
    - Who can configure connections to public repositories to use as sources of packages

### CodeStar

- **Create CICD-ready projects** for **EC2, Lambda and Elastic Beanstalk**
- One dashboard to view all the components

### CodeGuru

- **CodeGuru Profiler** works by running **CodeGuru Agent** alongside the application