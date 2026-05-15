# Need to print this cloud practitioner notes

### What is Cloud Computing?

- On-demand delivery of compute, database storage, applications, other IT resources through cloud platform via Internet
- Pay-as-you-go pricing

### 6 Advantages of Cloud Computing

1. Trade capital expense for variable expense
    - Only pay for what you use
2. Benefit from massive economies of scale
    - You won’t have same purchasing power as Amazon
    - They get cheaper prices to purchase servers, hardware
3. Stop guessing about capacity
    - You’ll buy too much or too little. Too much = wasted money, too little
4. Increase speed and agility
    - Websites/apps can scale infinitely with demand
5. Stop spending money running/maintaining data centers
    - Focus on what you’re good at, not managing infrastructures
6. Go global in minutes
    - Deploy apps in minutes
    - Provide lower latency and better experience at minimal cost

### 3 Types of Cloud Computing

1. Infrastructure as a Service (IAAS)
    - You manage the server (physical or virtual) as well as the operating system
    - Data center provider has no access to your server
2. Platform as a Service (PAAS)
    - Someone else manages the underlying hardware and operating systems, you just focus on your applications
    - You upload your code and it just executes
    - Think of GoDaddy
3. Software as a Service (SAAS)
    - Think of Gmail
    - All you do is interact with the application, manage the software and how you want to use it
    - Someone else takes care of the infrastructure and everything related to it

### 3 Types of Cloud Computing Deployments

1. Public Cloud – AWS, Azure, Google Cloud Platform
2. Hybrid – Mix of public and private
    - May want to keep some sensitive data on-premise
3. Private Cloud (or on-premise) – You manage it in your data center. Openstack or Vmware

# Around the World with AWS

### Region

- Geographic area consisting of 2 or more availability zones

### Availability Zone

- A data center

### Edge Location

- CDN Endpoints for CloudFront
- Many more edge locations than regions

# Let’s Log Into AWS

### Support Plans

1. Basic
2. Developer
    - Experimenting with AWS
    - $29/month
    - One person can ask technical questions through support center, 12-24 hour support rate
3. Business
    - 24/7 support by phone
    - Full access to AWS Trusted Advisor
    - $100/mo
4. Enterprise
    - $15,000/month
    - Everything in business + technical account manager
    - 15 min response time for critical support cases

### Create Billing Alarm

- Click Name at top-right, click My Billing Dashboard
- Enable Billing Alert
- Add the threshold in Cloudwatch and add e-mail address

# Identify Access Management

### Tick off five marks on Security Status:

1. Delete root access keys
    - We can skip this as a new user
2. Enable MFA (multi-factor authentication)
    - Set up MFA with Google Authenticator
3. Create individual IAM users
    - Access types:
        - **Programmatic access:** Access via command line
        - **AWS Management Console access:** Login to AWS console and make changes
        - **AWS SDK access:**
4. Create IAM groups
    - Once you decide access, you need to add to a Group
    - Choose a policy access type (or multiple types) and add the group name
5. IAM password policy
    - A password policy is a set of rules that define the type of password an IAM user can set
    - Change upper/lowercase required, number required, min password length, etc.

### Policies

- How to define permissions to users, groups, roles
- You can click on a policy to get details about what it gives people access to
- Detailed JSON allows you to define a **statement** comprised of an effect (Allow, Disallow), Action (what will happen), and Resource (to what resource)

### Exam Tips

### 3 ways to access AWS platform:

1. Via AWS Console
2. Programatically using command line
3. Using Software Development Kit (SDK)

### Root account

- Full admin access
- Should never give away
- Instead, create a user for each individual in your organization and secure root account with MFA

### Groups

- Place to store your users
- Users will inherit all permissions that group has
- To set permissions for a group, need to set policies for that group using JSON

# S3 (Simple Storage Service)

### Overview

- Provides developers and IT teams with secure, durable, highly-scalable object storage
- Safe place to store your files
- Object-based storage (pictures, Word files, videos), not operating system or database
- Files can be anywhere from 0 bytes to 5 TB in size
- Unlimited storage, but you pay by the gig
- Files are stored in **buckets**
- Bucket is a folder in the cloud
- Buckets are universal namespace. Must be unique globally.
- URL looks like [**https://s3-eu-west-1.amazonaws.com/acloudguru**](https://s3-eu-west-1.amazonaws.com/acloudguru)
    - Region + Region # + amazonaws.com + bucket name
- You will receive HTTP 200 code if file upload is successful

### Data Consistency Model

- Read after Write consistency for PUTS of new objects
    - If you read a file as soon as you upload it, you’ll be able to read the file
- Eventual consistency for overwrite PUTS and DELETES (can take some time to propogate)
    - If you update a file and overwrite the old version, you may get the old file or the new file. It will eventually show up.
    - You may be updating to one availability zone, may take time to propagate to other availability zones

### S3 Key-Value Store

- S3 is object based, objects consist of:
    1. Key (name of object, e.g. *hello.txt*
    2. Data in file (sequence of bytes)
    3. Version ID (important for versioning)
    4. Metadata (data about data, e.g. tags)
    5. Subresources:
        1. Access Control List
        2. Torrents

### Other Points

- Built for 99.99% availability
- Amazon guarantees 99.99999999999% (11 x 9s) durability
    - If you upload x amount of files, 99.99999999999% of those files will actually be uploaded (you won’t lose any files)
- Tiered storage availability
- Lifecycle management
    - If a file is over 30 days old, move it from one storage tier to another and eventually archive to Glacier
- Versioning
    - Multiple versions of a file
- Encryption
- Secure data with Access Control Lists and Bucket Policies
    - Bucket policies: Policy is for a specific bucket
    - ACL: Individual file level, control who can access a specific file

### S3 Storage Tiers/Classes

1. S3 Standard
    - 99.99% availability
    - 99.99999999999% durability
    - Stored redundantly across multiple devices (multiple disks) and multiple facilities (multiple availability zones)
    - Designed to sustain loss of 2 facilities concurrently
2. S3 – IA (Infrequently Accessed)
    - Data accessed less frequently but requires rapid access when needed
    - Lower fee than Standard but charged a retrieval fee
3. S3 One Zone – IA
    - Same as S3 – IA but do not require multiple availability zone data resilience
    - Only stored in one availability zone
4. Glacier
    - Used for archival only
    - Cheapest
    - Expedited, standard, or bulk
        - Expedited: Restored within few mins, high fee
        - Standard: 3-5 hours for restore
        - Bulk: 5-12 hours
- No retrieval fee for Standard, only for the other three

### S3 – Charges

### Charged for:

- Storage
- Requests
- Storage management pricing
    - Tags that define who owns an object
- Data transfer pricing
    - Transferring from one region to another
- Transfer acceleration
    - Fast and easy secure transfers across long distances

### S3 Transfer Acceleration

- Users upload to an edge location instead of directly to S3 bucket
- Once it goes to an edge location, it automatically gets distributed to the S3 bucket
- File goes across Amazon’s backbone to transfer much faster

**Read the S3 FAQ before taking the exam!**

# Creating an S3 Bucket

- Buckets must have unique names
- **Note:** Interface for S3 is Global (similar to IAM), but buckets created can be deployed in any region
- Bucket names must be DNS compliant (3-63 characters, no invalid characters)
- By default, buckets are **private** (recommended)
- You can change storage class and encryption on the fly by using the More menu

### Setting public access

- Trying to open a file through a URL won’t work by default because public read access is not enabled. Need to enable when uploading.
- Click box next to file > More > Make public
- Another way: Click into file > Permissions tab > Everyone (under public access) > Read Object

### Transfer acceleration

1. Click Properties in bucket
2. Advanced Settings > Transfer acceleration > Enable
- S3 has a feature to allow you to test your transfer speeds to different regions around the world

### Cross Region Replication

- Management > Replication
- Allows you to replicate bucket in one region to bucket in another region in the world
- Useful for disaster recovery
- Any object upload to first bucket is automatically replicated to second bucket

# S3 for Web Pages

- S3 can host **static** web pages (not dynamic like WordPress or PHP)
- It will scale automatically, will scale with demand. Useful for large number of requests.
- You can use bucket policies to make an entire bucket public (used for static websites)

# CloudFront

- Amazon’s CDN network
- Used to deliver entire website, including dynamic, static, streaming, and interactive content using edge locations
- Requests for content automatically routed to nearest ege location so content is delivered with best performance possible

### CDN

- Content-delivery network
- System of services around the world that deliver web pages or web page content to a user based on user geographic location, origin of the webpage, and content delivery server
- Works with origin types listed below
- Also works with non-AWS origins

### Edge Location

- Location where content will be cached
- Similar to AWS Region/AZ
- As close to user as possible

### Origin

- Origin of files that CDN will distribute
- S3 bucket, EC2 instance, Elastic Load Balancer, or Route53

### Distribution

- Name given to the CDN which consists of a collection of edge locations
- First time a user goes to a website, it’ll check a local edge location to see if website asset is there
- If not, it will download the asset from the origin and cache it to the edge location
- Next time someone tries to access, they will get the cached version from a local edge location
- Reduces stress on web servers and increases speed to download large files

### Distribution Types

1. Web distribution – Used for websites
2. RTMP – Used for media streaming

### Setting up CloudFront

1. Choose Web distrbution
2. Origin Domain Name: Choose an S3 bucket
3. Origin Path: You can choose subdirectories for your origin
- Once it’s deployed, you will see a domain name. Use that and the name of a file in your bucket to access.

### Exam Tips

- Content comes from Origin
- Cached at a local Edge Location
- Takes awhile for the first person to access, much quicker every time after that because it’s cached geographically close to you

# EC2 (Elastic Cloud Compute)

### Setup

- **VPC:** Virtual data center in the cloud
    - Deploy all EC2 instances into a VPC
- **AMI:** Using Amazon Linux AMI because it includes stuff to connect to AWS
- **Instance:** Choosing t2.micro because it’s usually used to test in dev
- **Instance Details:**
    - **Network:** Keep default VPC
    - **Subnet:** Choose which availability zone you want to be put into
    - **Auto-assign Public IP:** Allows you to assign a public IP so you can SSH into instance
    - **Shutdown behavior:** Choose what happens if your EC2 instance turns out (stop or have Amazon terminate for you)
    - **Enable termination protection:** Prevents people from accidentally shutting down your instance
- **Storage:**
    - 8GB is default
    - **Volume Type:** General purpose is most common, Provisioned IOPS lets you choose a very fast disk (database server), Magnetic is a very slow disk (file server)
- **Tags:** Allow us to add tags like Department and Employee ID to help with cost tracking later on
- **Security Group:** Virtual firewall in the cloud
    - Open ports like 22 for SSH or 3389 for RDP (Windows) or 80 for HTTP

### Connect to the EC2 server

- Open Terminal
- `chmod 400 MyVirginiaKP.pem` – Protects file from accidental overwriting
- `ssh ec2-user@54.242.147.206 i MyVirginiaKP.pem` to connect
- `sudo su` for root
- `yum update` to update security patches

### Exam Tips

- EC2 is compute-based, it’s not serverless. It is a server!
- Use private key to connect to EC2
- Security groups are virtual firewalls in the cloud. Need to open ports in order to use them (22 for SSH, 80 for HTTP, 443 for HTTPS, 3389 for RDP)
- Always design for failure, have one EC2 instance in each availability zone

# AWS Command Line

- Use `aws configure` on command line to set up login details
    - Enter Access Key and Secret Access Key
    - Region name: us-east-1
    - No output format
- `aws s3 ls` to view s3 buckets
- `aws s3 mb s3://myacloudgurubucket2018` to make a bucket
- `aws s3 cp hello.txt s3://myacloudgurubucket2018sheil` to upload EC2 file to S3 bucket

### Tips

- Interact with AWS in 3 ways:
    1. Using the console
    2. Using the command line interface (CLI)
    3. Using the software development kits

# Using Roles

- Prevent account from getting hacked
- `cd /~.aws` and `rm -rf credentials` to remove credentials file
- Roles are a secure way to grant permission to entities that you trust
- AWS Console > IAM > Roles
- Create new EC2 role, choose S3 Admin access, and name the role
- In EC2, find the instance, choose Actions > Instance Settings > Attach/Replace IAM Role
- No Role to My Admin S3 Access (the role I created in previous step)
- This process allows me to access S3 via CLI without having to store credentials on the EC2 instance itself

### Tips

- Roles are much more secure than using access key IDs and secret access keys
- Much easier to manage
- Can apply roles to EC2 instances at any time (not just when it boots up)
- Changes take place immediately
- Roles are universal, no need to specify region. Similar to users

# Build a Website

- Connect to EC2 with CLI
- Web servers need either Apache (Linux) or IIS (Windows)
- `yum install httpd -yes` to install
- `service httpd start` to start server
- Anything you put into `/var/www/html` will be on the website
- `aws s3 cp s3://myacloudgurubucket2018sheil /var/www/html --recursive` to copy files from S3 to web server on EC2

# Databases

### Relational Database Service (RDS)

Types:

1. SQL Server
2. Oracle
3. MySQL Server
4. PostgreSQL
5. Aurora (Amazon’s own database)
6. MariaDB

Two key features:

1. Multi availability zones for disaster recovery
2. Read replicas for performance improvement
- **Multi AZ:** Exact copy of your database in case the primary goes down
    - Disaster recovery
- **Read replica:** Spread read access across five databases, only one is for writing
    - Scaling out / performance

### Nonrelational Databases

1. Collection (table)
2. Documents (row)
3. Key-value pairs (fields)
- Allows you to add in extra fields all the time
- **Amazon DynamoDB** is Amazon’s nonrelational/NoSQL database
    - Fast, flexible
    - Scales with your application

### Aurora

- Relational, Amazon’s own
- 6 copies of itself
- 5 times better performance than MySQL, 1/10 price point
- Choose Aurora if you have an RDS
- Choose DynamoDB if you have nonrelational

### Data Warehousing

- Used for business intelligence
- Used to pull in large and complex datasets
- Used by management to do queries (current performance targets, etc)
- **Redshift** is Amazon’s data warehouse in the cloud for business intelligence
    - Start with a few hundred GB of data, scale to petabyte or more

# Autoscaling

- Review: EC2 connects to one database that is duplicated to a second database (redundancy).
- No redundancy on the EC2 itself. Autoscaling group will fix this.
- You can set up how many instances you want with Autoscaling. When one fails, it will automatically create a new one
- You can set a startup script to run when each new instance starts

# Route 53

- Amazon’s DNS service
- Domain registration

# Elastic Beanstalk

- Allows you to deploy everything (provisions everything like EC2 and RDS and everything else) all at one button
- Creates load balancers, auto-scaling groups, security groups, etc.
- Provisioning EC2 instances, installs PHP

# CloudFormation

- Way of scripting out infrastructure
- Turning infrastructure into code
- Codify creating EC2 instances, security groups, etc
- JSON that describes your cloud environment – this is a template
- Elastic Beanstack and CloudFormation are free, but you pay for the resources that are provisioned as a result of using EB and CF

# Architecting for the Cloud – Best Practices

### Why Cloud Computing?

- IT assets becoming programmable resources
- Global availability and unlimited capacity
- High-level managed services, incl call center functionality, text to voice, machine learning, etc
- Security built in (AWS manages security)

### Design Principles – Scalability

1. Scale Up – Start with a small virtual machine and increase size
2. Scale Out – Start with an elastic load balancer, add more virtual machines as your project gets bigger
    1. Stateless Applications – Lambda (no state is stored)
    2. Stateless Components – Instead of storing state on server, it stores state on cookies on user’s browser
    3. Stateful Components – Can store some stuff with databases that can scale with you (add replicas or increase size)
    4. Distributed Processing – Break your data into pieces and have EC2 instances work on them separately in parallel (Elastic MapReduce)

### Design Priciples – Disposable Resources

- Treat your services like cattle, not pets
- If a server dies, just replace with another one
    1. Bootstrapping – Scripts allow you to set up an instance automatically, setup Apache
    2. Golden images – Take an Amazon Machine Image (AMI) and use it for autoscaling
    3. Hybrid of the two

### Design Principles – Infrastructure as Code

- Cloudformation
- Allows you to deploy infrastructure to many clients very easily without manually setting anything up

### Design Principles – Automation

- Use alarms, events to automate creation/maintenance of infrastructure
- Loose coupling: Make sure failure in one component doesn’t affect other pieces of infrastructure
    - Well defined interfaces: Use RESTful API
    - Service discovery: Don’t use fixed IP addresses. Instead use DNS names/endpoints.
    - Asyncronous integration: Messages (actions) remain in queue so if one EC2 goes down, the actions are stored in queues for the next EC2 to pick up
    - Graceful failure: If something breaks, nicely tell the user and report to developers

### Design Principles – Serverless not services

- Managed Services (other compnanies like Paypal)
- Serverless Architectures (Lambda, DynamoDB, etc)

### Design Principles – Databases

- Relational: Aurora
    - High scalability
    - High availability (6 copies of data at any given time)
    - Data needs joins or complex transactions
- Nonrelational: DynamoDB
    - High scalability
    - High availability
    - Data does not need joins or complex transactions
- Data Warehouse: Red Shift
    - Meant for data for business analysis
    - Red Shift is highly scalability and available
    - Red Shift not meant for online transaction processing (not production database)

### Design Principles – Search

- Cloud Search or Elastic Search
- Cloud search: less control, easier
- Elastic search: more control
- Both are very scalability

### Design Principles – Misc

- Remove single points of failure, everything should have redundancy
- Detect failure with monitoring (Health checks)
- Durable data storage
    - Don’t store all on an EC2 instances
    - Store instead in S3 or Dynamo
- Automate multi-center resilience (multiple Availability Zones)
- Introduce fault isolation and horizontal scaling

### Design Principles – Financial

- Optimize for cost
    - Elasticity: More servers when busy, less when not busy with auto saling
    - Purchasing options:
        - Reserviced Capacity
        - Spot Instances

### Design Principles – Caching

- Application Caching
- Edge Caching

### Design Principles – Security

- Offload security to AWS
- Reduce privileged access
- Treat security as code

### Tips

- Understand the basic services:
    - Databases – RDS, DynamoDB, Red Shift
    - Compute – EC2 vs Lambda
    - Storage – S3 (great for static hosting)

# Summary of Cloud Concepts and Tech Summary

### General

1. 6 Advantages of Cloud
2. 3 Types of Cloud Computing
    1. Infrastructure as a Service (IAAS) – Lightsail
    2. Platform as a Service (PAAS)
    3. Software as a Service (SAAS)
3. 3 Types of Cloud Computing Deployment
    1. Public Cloud (AWS, Azure, Google Cloud)
    2. Hybrid (mix)
    3. Private Cloud (managed locally)
4. Difference between:
    1. Regions – London, Frankfurt, N. Virginia
    2. Availability Zones – Collections of data centers, geographically distributed
    3. Edge Locations – Caching
5. Access AWS Console by:
    1. Via AWS console
    2. Programatically using command line
    3. SDKs
6. Root account has full admin, never give out. Create user for each individuals and secure with multi-factor auth.
7. Groups are places to store users
8. Set permissions in group with policies with JSON

### S3

1. S3 bucket is a place to store objects
2. S3 unique namespace
3. Object based only, 200 status code when complete
4. Storage places:
    1. S3 – Current data
    2. Glacier – Archival (2-5 hour retrieval)
5. Restrict access with bucket policy
6. Restrict access to indiv objects with access control lists
7. S3 transfer acceleration – Upload to edge locations. Edge locations then send to central place.
8. Cross-region replication – Replicate to other buckets
9. S3 hosts static websites
10. Scales automatically to meet demand (movie preview)

### Cloudfront

1. Edge Location: Location where content is cached
2. Origin: Origin of files that CDN will distribute (S3, EC2, Elastic Load Balancer, Route53)
3. Distribution: Name given to CDN, consists of edge locations
    1. Web – Websites
    2. RTP – Media streaming
4. Can write to edge locations (S3 transfer acceleration)

### EC2

- NOT SERVERLESS, compute-based
- Private key to connect
- Security Groups: Virtual firewalls in the cloud, open ports to use
- Design for failure, have one EC2 instance in each Avail Zone
- Pricing models
- Types of EC2 depending on the purpose of EC2
- EBS: Elastic block storage where you install operating system and file
- 4 kinds of EBS:
    - General Purpose SSD
    - Provisioned IOPS SSD
    - Throughput Optimized HDD
    - Cold HDD
- Roles much more security and easier to managethan using access and secret access keys
- Roles are universal, no need to specify users

### RDS

1. Multi Avail Zone: Disaster Recovery
2. Read replicas: Scaling out or performance
3. DynamoDB for nonrelational, Aurora for relational, Red Shift for data warehousing

# Billing

- Philosophy on pricing: Pay for what you use, start or stop using product at any time. No long-term contracts required.
- Free Tier to help new AWS users get started

### Pricing policies

- *Pay as you go: **EC2 used to be pay by hour, pay by second as it’s used
- **Pay less when you reserve:** If you reserve time ahead of time, you get a discount
- *Pay even less by unit when using more: **If you use more, you pay less per GB
- **Pay even less as AWS grows**
- Custom pricing for enterprise

### What’s free?

1. Amazon VPC
2. Elastic Beanstalk (services it provisions are not free)
3. CloudFormation (services it provisions not free)
4. Identity Access Management (IAM)
5. Auto Scaling (EC2 instances it uses are not free)
6. Opsworks
7. Consolidated Billing (add all AWS accounts into one bill)

### 3 Fundamental Charges

1. Compute
2. Storage
3. Data Out to Internet (Data In is free)

### What determines price?

1. Clock hours of server time (time server is running)
2. Machine configuration (more resources consumed = more paid)
3. Machine purchase type (some instance types cost more)
4. Number of instances
5. Load balancing
6. Detailed monitoring (monitor EC2 by minute instead of 5-min intervals)
7. Auto scaling (EC2 instances cost money)
8. Elastic IP Addresses
9. Operating systems (Windows) and software packages
- Elastic Compute Cloud can reserve instances ahead of time, even cheaper if you pay upfront

### S3 – What determines price?

1. Storage class (Standard or IA)
2. Storage amount
3. Number of requests
4. Data transfer (data transfer out)

### RDS – What determines price?

1. Number of hours RDS is running
2. Database characteristics (licensed?)
3. Database purchase type (huge, nano?)
4. Number of instances
5. Provisioned storage (how big?)
6. Requests made to database
7. Deployment type (multi A-Z, read replicas)
8. Data transfer out

### Cloudfront – What determines price?

1. Traffic distribution
2. Requests
3. Data transfers out

# Billing: Support Plans

1. Basic
    1. Free, no tech acct mgt, no open cases
2. Developer
    1. $29/mo, business hr access via email, no TAM, 1 person can open unlim cases
    2. General guidance: < 24 business hours
    3. System impaired: < 12 business hours
3. Business
    1. $100/mo, 24×7 email, chat, and phone support, no TAM, unlimited cases for support
    2. General guidance: < 24 business hours
    3. System impaired: < 12 hours
    4. Prod system impaired: < 4 business hours
    5. Prod system down: < 1 hour
4. Enterprise
    1. $15,000/mo, 24×7 email chat and phone, TAM, unlimited cases for support
    2. General guidance: < 24 business hours
    3. System impaired: < 12 hours
    4. Prod system impaired: < 4 business hours
    5. Prod system down: < 1 hour
    6. Business critical down: < 15 mins
- Pricing can be higher if you use AWS a lot

# Billing: Resource Groups

- Tags are key-value pairs attached to resources
- Tags can be inherited (created by one service, moves to another service)
- **Resource groups:** Make it easy to group resources based on tags assigned to them
- Resource groups contain info like:
    - Region
    - Name
    - Healthchecks
    - EC2 – Public/Private IP Addresses
    - ELB – Port Configs
    - RDS – Database Engine
- You can search for resources by a specific tag (used by a particular department, user ID, etc)
- Tag Editor allows you to find resources not tagged and add tags

# Billing: Consolidated Billing

- **AWS Organization:** Enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage
- **Consolidated billing:** One monthly bill (paying account) for all linked accounts in organization
- 20 linked accounts for consolidating billing
- Easy to track charges and allocate costs
- Volume pricing
- You can also reserve EC2 instances and if one group isn’t using them, you can carry them over to another group to save money
- Best practices:
    - Always enable multi factor auth
    - Strong and complex factor
    - Restrict root access
- Billing alerts

### Exam Tips

- Consolidated billing allows you to get volume discounts for all your accounts
- Unsused reserved instances for EC2 are applied across group
- CloudTrail is on per-account and per-region basis , can be aggregated into single bucket in paying account

# AWS Quick Starts

- Allow you to enable a particular type of technology very quickly
- Templates to get you started with a server that runs a particular technology
- Uses CloudFormation based on a template URL

# AWS Cost Calculators

### Simple Monthly Calculator

- Allows you to quickly add the resources you’re going to use and the types of resources and it’ll tell you the cost of each and total monthly bill
- Not comparing what you have on premise and in cloud

### Total Cost of Ownership Calculator

- Compares against your current costs for total cost of ownership
- Takes into account:
    - Server costs (hardware & software)
    - Storage costs (hardware & storage admin)
    - Networking costs (network hardware & network admin)
    - IT labor costs

# Billing & Pricing Summary

- Remember the free services!
- AWS Support Plans and features of each
- What are tags?
- What are resource groups? Group resources based on tags
- What is the benefit of consolidated billing?
- What’s the benefit of AWS Quick Starts?
- Two different AWS calculators

# AWS Compliance

### Certifications / Attestations

AWS certified with:

1. ISO 27001
2. PCI DSS Level 1
3. SOC 1
4. SOC 2
5. SOC 3

### Laws, Regulations, Privacy

1. HIPAA compliant – Meets standards to store health information

### Alignments / Frameworks

1. G-Cloud (UK) – Frameworks for government customers to meet these requirements in UK

# Shared Responsibility Model

- AWS manages security of cloud, security in cloud itself is responsibilty of customer. Customers are responsibility for security of how AWS is set up. AWS is responsible for the infrastructure
- Do you have the ability to stop something from happening? If you dont have the ability to stop it, it’s Amazon’s responsibility
- You have control over encryption, customer data

# AWS Web Application Firewall and AWS Shield

### AWS WAF

- Application firewall that helps protect your web apps from common web exploits that could affect availability, compromise security, or consume excessive resources
- AWF can read data hacker is sending and can intervene on your behalf
- Prevents common attacks
- Goes down to Layer 7

### AWS Shield

- Managed DDOS service
- Provides safeguards for web apps running on AWS Two tiers:
1. Standard – Free, avail automatically
2. Advanced – Advanced protection for $3000/mo

# AWS Inspector vs AWS Trusted Advisor

### AWS Inspector

- Automated security assessment service
- Automatically asses apps for vulnerabilities or deviations from best practices
- Assessment done, provides detailed list of security findings prioritized by leve of severity

### AWS Trusted Advisor

- Optimizes AWS environment to reduce cost, increase performance and improve security
1. Cost Optimization (do you have an EC2 with nothing happening on it or an empty DB?)
2. Performance
3. Security
4. Fault Tolerance (are you using multiple avail zones?)
- Two options:
1. Core checks and recommendations 2 Full trusted advisor – business/enterprise only

# Security Summary

- Name some of the compliance that AWS meets (above)
- Define what shared responsibility means
- AWS WAF reads data and blocks traffic if it will cause problems
- AWS shield blocks DDOS attacks. Two tiers: Standard and Advanced
- Inspector looks for vulnerabilies on your EC2 instances.
- Advisor gives suggestions for improvement, advanced one requires business subscription

My notes while giving the practice mock tests

1. An Amazon Machine Image (AMI) is a template that contains a software configuration (for example, an operating system, an application server, and applications). This pre-configured template save time and avoid errors when configuring settings to create new instances. You specify an AMI when you launch an instance, and you can launch as many instances from the AMI as you need. You can also launch instances from as many different AMIs as you need.
2.  IAM refers to the AWS Identity and Access Management.
3. An EBS snapshot is a point-in-time copy of your Amazon EBS volume.
4. An internet gateway is a VPC component that allows communication between instances in your VPC and the internet.
5. you‘ll need to build the relational schema that best fits your use case and are responsible for any performance tuning to optimize your database for your application’s workflow.
- Installing the database software is AWS’ responsibility.
- Performing backups is AWS’ responsibility.
- Patching the database software is AWS’ responsibility.

1. The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.  

          

- AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS.
- AWS OpsWorks can be used to automate one service which is EC2. AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet.
- AWS Console lets you access and manage Amazon Web Services through a web-based user interface.

1. When comparing AWS with on-premises TCO, customers should consider all costs of owning and operating a data center. Examples of these costs include facilities, physical servers, storage devices, networking equipment, cooling and power consumption, data center space, and Labor IT cost.

1. Dedicated Hosts provide additional control over your instances and visibility into Host level resources and tooling that allows you to manage software that consumes licenses on a per-core or per-socket basis, such as Windows Server and SQL Server. This is why most BYOL scenarios are supported through the use of Dedicated Hosts,
- Dedicated Hosts is recommended for most BYOL scenarios for the reasons we mentioned above.
- On-demand Instances“ and “Reserved Instances“ are incorrect. On-demand instances and Reserved instances don’t support the Bring Your Own License (BYOL) model.

1. Amazon Inspector is an automated security assessment service that helps you test the network accessibility of your Amazon EC2 instances and the security state of your applications running on the instances. Amazon Inspector allows you to create assessment templates to automate security vulnerability assessments throughout your development and deployment pipelines or for static production systems.

  

- Security groups can be used to check the network accessibility of your Amazon EC2 instances -at the instance level- but this is not done automatically.
- Amazon Kinesis allows you to collect, process, and analyze video and data streams in real time.
- AWS Network Access Control Lists can be used to check the network accessibility of your Amazon EC2 instances -at the subnet level- but this is not done automatically.

1. Amazon EC2 Auto Scaling is a fully managed service designed to launch or terminate Amazon EC2 instances automatically to help ensure you have the correct number of Amazon EC2 instances available to handle the load for your application. Amazon EC2 Auto Scaling helps you maintain application availability and fault tolerance through fleet management for EC2 instances, which detects and replaces unhealthy instances, and by scaling your Amazon EC2 capacity automatically according to conditions you define. You can use Amazon EC2 Auto Scaling to automatically increase the number of Amazon EC2 instances during demand spikes to maintain performance and decrease capacity during lulls to reduce costs.

          

- Elastic Load Balancing provides an effective way to increase the availability and fault tolerance of a system. First ELB tries to discover the availability of your EC2 instances, it periodically sends pings, attempts connections, or sends requests to test the EC2 instances. These tests are called health checks. The load balancer routes user requests only to the healthy instances. When the load balancer determines that an instance is unhealthy, it stops routing requests to that instance. The load balancer resumes routing requests to the instance when it has been restored to a healthy state.
- AWS CloudFormation automates and simplifies the task of creating groups of related resources that power your applications. AWS CloudFormation allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts.
- Network ACLs is used to control traffic at the subnet level.
- AWS Direct Connect allows you to establish a dedicated network connection from your on-premises to AWS.

1. S3 Glacier Flexible Retrieval (Formerly S3 Glacier) delivers the most flexible retrieval options that balance cost with access times ranging from minutes to hours and with free bulk retrievals. Amazon S3 Glacier Flexible Retrieval provides three retrieval options to fit your use case. Expedited retrievals typically return data in 1-5 minutes, and are best used for Active Archive use cases
- Active databases require consistent and low-latency storage performance. For example, DB instances for Amazon RDS for MySQL, MariaDB, PostgreSQL, Oracle, and Microsoft SQL Server use Amazon Elastic Block Store (Amazon EBS) volumes for database and log storage. S3 Glacier Flexible Retrieval is generally used for data archiving and backup, not for live databases.
- A cache is a high-speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster than is possible by accessing the data’s primary storage location. Caching allows you to efficiently reuse previously retrieved or computed data. The data in a cache is generally stored in fast access hardware such as RAM (Random-access memory) and may also be used in correlation with a software component. A cache‘s primary purpose is to increase data retrieval performance by reducing the need to access the underlying slower storage layer.
- Dynamic websites usually require immediate retrieval, which is not available in S3 Glacier Flexible Retrieval.

1. Access keys consist of two parts: an access key ID and a secret access key. You must provide your AWS access keys to make programmatic requests to AWS or to use the AWS Command Line Interface or AWS Tools for PowerShell. Like a user name and password, you must use both the access key ID and secret access key together to authenticate your requests.

      

- MFA is an additional security layer that can be used to secure your AWS console. MFA can also be used to control access to AWS service APIs.
- The AWS key pair is used to securely connect to your Amazon EC2 instances.

1. AWS is continuously innovating the design and systems of its data centers to protect them from man-made and natural risks. For example, at the first layer of security, AWS provides a number of security features depending on the location, such as security guards, fencing, security feeds, intrusion detection technology, and other security measures.
- According to the Shared Responsibility model, patching of the underlying hardware is the AWS’ responsibility. AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
- The configuration and security of the VPC are customer’s responsibilities.
- The customer is responsible for encrypting their data on EBS either on the client side or on the server side.
- The customer is responsible for managing the IAM permissions.

1. EC2 instance pricing varies depending on many variables:

– The buying option (On-demand, Savings Plans, Reserved, Spot, Dedicated)

– Selected instance type

– Selected Region

– Number of instances

– Load balancing

– Allocated Elastic IP Addresses

- Load balancing: The number of hours the Elastic Load Balancer runs and the amount of data it processes contribute to the EC2 monthly cost.
- Instance type: Amazon EC2 provides a wide selection of instance types optimized to fit different use cases. Instance types comprise varying combinations of CPU, memory, storage, and networking capacity.
- Prices of the Amazon EC2 instances may vary depending on the Region where the instances are provisioned. Amazon EC2 instances provisioned in different Availability Zones within the same Region have the same price.
- There is no charge for private IPs.
- The number of allocated Elastic IPs is the factor that may affect Amazon EC2 charges. To ensure efficient use of Elastic IP addresses, AWS imposes a small hourly charge if an Elastic IP address is not associated with a running instance, or if it is associated with a stopped instance. While the instance is running, you are not charged for one Elastic IP address associated with the instance, but additional Elastic IPs are not free.
- A bucket is an Amazon S3 resource, not an Amazon EC2 resource.
- To upload your data (photos, videos, documents, etc.) to Amazon S3, you must first create an S3 bucket (which is like a file folder) in one of the AWS Regions. You can then upload any number of objects to the bucket. The customer is charged based on the total size of the objects (in GB) stored in their S3 bucket, not for the bucket itself.

1. Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions. Elastic Load Balancing supports four types of load balancers (Application Load Balancer, Network Load Balancer, Gateway Load Balancer, and Classic Load Balancer). You can select the appropriate load balancer based on your application needs.

1- If you need to load balance HTTP\HTTPS requests, AWS recommends using the AWS Application Load Balancer.

2- For network/transport protocols (layer4 – TCP, UDP) load balancing and for extreme performance/low latency applications, AWS recommends using the AWS Network Load Balancer.

3- To manage and distribute traffic across multiple third-party virtual appliances, AWS recommends using the AWS Gateway Load Balancer.

4- If you have an existing application built within the EC2-Classic network, you should use the AWS Classic Load Balancer.

Application Load Balancer is best suited for load balancing of HTTP and HTTPS traffic. In our case, the application receives HTTP traffic. Hence, the Application Load

- The traffic comes to the instances through HTTP. Network Load Balancer is best suited for load balancing of TCP and UDP traffic.
- AWS Gateway Load Balancer is used to manage and distribute traffic across multiple third-party virtual appliances.
- Gateway Load Balancer helps you easily deploy, scale, and manage third-party virtual appliances such as firewalls, Anti-malware, deep packet inspection systems, and intrusion detection and prevention systems.

1. AWS is responsible for physical controls and environmental controls. Customers inherit these controls from AWS.

As mentioned in the AWS Shared Responsibility Model page, Inherited Controls are controls which a customer fully inherits from AWS such as physical controls and environmental controls.

As a customer deploying an application on AWS infrastructure, you inherit security controls pertaining to the AWS physical, environmental and media protection, and no longer need to provide a detailed description of how you comply with these control families.

- Patch Management belongs to the shared controls. AWS is responsible for patching the underlying hosts and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
- Database controls belongs to the shared controls. AWS maintains the configuration of its infrastructure devices that run the database, but customers are responsible for configuring their own databases, and applications.
- Awareness & Training belongs to the shared controls. AWS trains AWS employees, but customers must train their own employees.

1. Change management is defined as “the Process responsible for controlling the Lifecycle of all Changes. The primary objective of Change Management is to enable beneficial changes to be made, with minimum disruption to IT Services.
- AWS Config and AWS CloudTrail are change management tools that help AWS customers audit and monitor all resource and configuration changes in their AWS environment
- Customers can use AWS Config to answer “What did my AWS resource look like?” at a point in time. Customers can use AWS CloudTrail to answer “Who made an API call to modify this resource?” For example, a customer can use the AWS Management Console for AWS Config to detect that the security group “Production-DB” was incorrectly configured in the past. Using the integrated AWS CloudTrail information, they can pinpoint which user misconfigured the “Production-DB” security group. In brief, AWS Config provides information about the changes made to a resource, and AWS CloudTrail provides information about who made those changes. These capabilities enable customers to discover any misconfigurations, fix them, and protect their workloads from failures.
- AWS Transit Gateway is a network transit hub that customers can use to interconnect their virtual private clouds (VPCs) and their on-premises networks.
- AWS X-Ray is a debugging service that helps developers understand how their application and its underlying services are performing to identify and troubleshoot the root cause of performance issues and errors.
- Amazon Comprehend is a Natural Language Processing (NLP) service that uses machine learning to find meaning and insights in text. Customers can use Amazon Comprehend to identify the language of the text, extract key phrases, places, people, brands, or events, understand sentiment about products or services, and identify the main topics from a library of documents.

1. Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. It allows you to run complex analytic queries against petabytes of structured data. You can start with just a few hundred gigabytes of data and scale to a petabyte or more. Amazon Redshift manages the work needed to set up, operate, and scale a data warehouse, from provisioning the infrastructure capacity to automating ongoing administrative tasks such as backups, and patching.
- Amazon Kinesis is used to collect, process, and analyze video and data streams in real time.
- Amazon Relational Database Service (Amazon RDS) is a managed service that makes it easy to set up, operate, and scale a relational database in the AWS Cloud. Amazon RDS provides you with six relational database engines to choose from, including Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, and Microsoft SQL Server.
- Amazon DynamoDB is a NoSQL database service.

1. In cloud computing, hybrid cloud refers to the use of both on-premises resources in addition to public cloud resources. A hybrid cloud enables an organization to migrate applications and data to the cloud, extend their datacenter capacity, utilize new cloud-native capabilities, move applications closer to customers, and create a backup and disaster recovery solution with cost-effective high availability. By working closely with enterprises, AWS has developed the industry’s broadest set of hybrid capabilities across storage, networking, security, application deployment, and management tools to make it easy for you to integrate the cloud as a seamless and secure extension of your existing investments.
- AWS Virtual Private Network solutions establish secure connections between your on-premises networks, remote offices, client devices, and the AWS global network. AWS VPN is comprised of two services: AWS Site-to-Site VPN and AWS Client VPN. AWS Site-to-Site VPN enables you to securely connect your on-premises network or branch office site to AWS. AWS Client VPN enables you to securely connect users (from any location) to AWS or on-premises networks. VPN Connections can be configured in minutes and are a good solution if you have an immediate need, have low to modest bandwidth requirements, and can tolerate the inherent variability in Internet-based connectivity.
- AWS Direct Connect does not involve the Internet; instead, it uses dedicated, private network connections between your on-premises network or branch office site and Amazon VPC. AWS Direct Connect is a network service that provides an alternative to using the Internet to connect customer‘s on-premise sites to AWS. Using AWS Direct Connect, data that would have previously been transported over the Internet can now be delivered through a private network connection between AWS and your datacenter or corporate network. Companies of all sizes use AWS Direct Connect to establish private connectivity between AWS and datacenters, offices, or colocation environments. Compared to AWS VPN (Internet-based connection), AWS Direct Connect can reduce network costs, increase bandwidth throughput, and provide a more consistent network experience.
- AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. It includes a code editor, debugger, and terminal. Cloud9 comes prepackaged with essential tools for popular programming languages, including JavaScript, Python, PHP, and more, so you don’t need to install files or configure your development machine to start new projects.
- AWS Artifact provides on-demand access to AWS’ compliance reports.
- AWS CloudTrail is a web service that tracks and records all user interactions with AWS services.

1. Savings Plans are a flexible pricing model that offers low prices on EC2, Lambda, and Fargate usage, in exchange for a commitment to a consistent amount of usage (measured in $/hour) for a 1 or 3 year term. When you sign up for Savings Plans, you will be charged the discounted Savings Plans price for your usage up to your commitment. For example, if you commit to $10 of compute usage an hour, you will get the Savings Plans prices on that usage up to $10 and any usage beyond the commitment will be charged On Demand rates.

Additional information:

What is the difference between Amazon EC2 Savings Plans and Amazon EC2 Reserved instances?

Reserved Instances are a billing discount applied to the use of On-Demand Compute Instances in your account. These On-Demand Instances must match certain attributes, such as instance type and Region to benefit from the billing discount.

For example, let say you have a t2.medium instance running as an On-Demand Instance and you purchase a Reserved Instance that matches the configuration of this particular t2.medium instance. At the time of purchase, the billing mode for the existing instance changes to the Reserved Instance discounted rate. The existing t2.medium instance doesn‘t need replacing or migrating to get the discount.

After the reservation expires, the instance is charged as an On-Demand Instance. You can repurchase the Reserved Instance to continue the discounted rate on your instance. Reserved Instances act as an automatic discount on new or existing On-Demand Instances in your account.

Savings Plans also offer significant savings on your Amazon EC2 costs compared to On-Demand Instance pricing. With Savings Plans, you make a commitment to a consistent usage amount, measured in USD per hour. This provides you with the flexibility to use the instance configurations that best meet your needs, instead of making a commitment to a specific instance configuration (as is the case with reserved instances). For example, with Compute Savings Plans, if you commit to $10 of compute usage an hour, you can use as many instances as you need (of any type) and you will get the Savings Plans prices on that usage up to $10 and any usage beyond the commitment will be charged On Demand rates.

- Savings Plans are not available for AWS Batch.AWS Batch is a compute service that allows you to run hundreds of thousands of batch computing jobs on AWS. AWS Batch dynamically provisions the optimal quantity and type of compute resources (e.g., CPU or memory optimized instances) based on the volume and specific resource requirements of the batch jobs submitted.
- Savings Plans are not available for AWS Outposts.

AWS Outposts is an AWS service that delivers the same AWS infrastructure, native AWS services, APIs, and tools to virtually any customer on-premises facility. With AWS Outposts, customers can run AWS services locally on their Outpost, including EC2, EBS, ECS, EKS, and RDS, and also have full access to services available in the Region.

Customers can use AWS Outposts to securely store and process data that needs to remain on-premises or in countries where there is no AWS region. AWS Outposts is ideal for applications that have low latency or local data processing requirements, such as financial services, healthcare, etc.

- savings Plans are not available for Amazon Lightsail.

Amazon Lightsail provides a low-cost Virtual Private Server (VPS) in the cloud.

1. Since the data is structured, then it is best to use a relational database service such as Amazon RDS.
- ElastiCache is an in-memory data store and cache service.
- DynamoDB is a NoSQL database service. NoSQL is designed for unstructured data.
- Amazon Simple Notification Service (SNS) is not a database service. Amazon SNS is a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications.

1. With AWS, you can deploy your application in multiple regions around the world. The user will be redirected to the Region that provides the lowest possible latency and the highest performance. You can also use the CloudFront service that uses edge locations (which are located in most of the major cities across the world) to deliver content with low latency and high performance to your global users.
- High Availability can be achieved by deploying your application in multiple Availability Zones within a single Region. If one Availability Zone goes down, the others can handle user requests. This may not reduce latency to your international users. In other words, the application will be available for them all the time, but with high latency.
- Elasticity refers to the ability of a system to scale the underlying resources up when demand increases (to maintain performance), or scale down when demand decreases (to reduce costs). This option does not indicate whether your resources will be deployed in a single Region or multiple Regions.
- Durability refers to the ability of a system to assure data is stored and data remains consistent in the system as long as it is not changed by legitimate access. This means that data should not become corrupted or disappear due to a system malfunction. Durability is used to measure the likelihood of data loss. For example, assume you have confidential data stored in your Laptop. If you make a copy of it and store it in a secure place, you have just improved the durability of that data. It is much less likely that all copies will be simultaneously destroyed.

Data durability can be achieved by replicating data across multiple Availability Zones within a single Region. For example, the S3 Standard Tier is designed for 99.999999999% durability. This means that if you store 100 billion objects in S3, you will lose one object at most.

1. AWS consolidated billing enables an organization to consolidate payments for multiple AWS accounts within a single organization by making a single paying account. For billing purposes, AWS treats all the accounts on the consolidated bill as one account. Some services, such as Amazon EC2 and Amazon S3 have volume pricing tiers across certain usage dimensions that give the user lower prices when they use the service more. For example if you use 50 TB in each account you would normally be charged $23 *50*3 (because they are 3 different accounts), But with consolidated billing you would be charged $23*50+$22*50*2 (because they are treated as one account) which means that you would save $100.

HOW IT WORKS

After you create an organization and verify that you own the email address associated with the master (management) account, you can invite existing AWS accounts to join your organization. When you invite an account, the AWS Organizations service sends an invitation to the account owner, who decides whether to accept or decline the invitation. If they accept, their account becomes a member of that organization.

At the moment an account accepts the invitation to join an organization, the master account of the organization becomes liable for all charges accrued by the new member account. The payment method attached to the member account is no longer used. Instead, the payment method attached to the master account of the organization pays for all charges accrued by the member account

1. Access keys consist of an access key ID and secret access key, which are used to sign programmatic requests to AWS using the CLI or the SDK.
2. “Amazon S3 can run any type of application or backend system“ is not a benefit of S3 and thus is a correct answer. Amazon S3 is a storage service not a compute service.

“Amazon S3 can be scaled manually to store and retrieve any amount of data from anywhere“ is not a benefit of S3 and thus is a correct answer. Amazon S3 scales automatically to store and retrieve any amount of data from anywhere.

Companies today need the ability to simply and securely collect, store, and analyze their data at a massive scale. Amazon S3 is object storage built to store and retrieve any amount of data from anywhere – web sites and mobile apps, corporate applications, and data from IoT sensors or devices.  It’s a simple storage service that offers highly available, and infinitely scalable data storage infrastructure at very low costs. It is designed to deliver 99.999999999% durability, and stores data for millions of applications used by market leaders in every industry. S3 provides comprehensive security and compliance capabilities that meet even the most stringent regulatory requirements. It gives customers flexibility in the way they manage data for cost optimization, access control, and compliance. S3 provides query-in-place functionality, allowing you to run powerful analytics directly on your data at rest in S3. And Amazon S3 is the most supported cloud storage service available, with integration from the largest community of third-party solutions, systems integrator partners, and other AWS services.

Amazon S3 stores any number of objects, but each object does have a size limitation. Individual Amazon S3 objects can range in size from a minimum of 0 bytes to a maximum of 5 terabytes.

1. Amazon Relational Database Service (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient, resizable capacity while automating time-consuming administration tasks such as hardware provisioning, operating system maintenance, database setup, patching and backups. It frees you to focus on your applications so you can give them the fast performance, high availability, security and compatibility they need.

Amazon RDS can be used to host Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle, and Microsoft SQL Server databases.

- Amazon Redshift is not a MySQL database service. Amazon Redshift is a fully managed data warehouse service that makes it simple and cost-effective to analyze all your data using standard SQL and your existing Business Intelligence (BI) tools.
- Amazon DynamoDB is not a MySQL database service. Amazon DynamoDB is a fully managed NoSQL database service.
- Amazon CloudWatch is not a database service. Amazon CloudWatch is a monitoring service that gives you complete visibility of your cloud resources and applications

1. Amazon DynamoDB is a NoSQL database service. NoSQL databases are used for non-structured data that are typically stored in JSON-like, key-value documents.
- Amazon Redshift is a data warehouse service that only supports relational data, NOT key-value data.Amazon Redshift is a fast, fully managed data warehouse service that is specifically designed for online analytic processing (OLAP) and business intelligence (BI) applications, which require complex queries against large datasets.
- Amazon Aurora is a MySQL and PostgreSQL-compatible relational database NOT a key-value database.
- Amazon RDS is a relational database NOT a key-value database.

1. AWS Infrastructure Event Management is a short-term engagement with AWS Support, included in the Enterprise-level Support product offering, and available for additional purchase for Business-level Support subscribers. AWS Infrastructure Event Management partners with your technical and project resources to gain a deep understanding of your use case and provide architectural and scaling guidance for an event. Common use-case examples for AWS Event Management include advertising launches, new product launches, and infrastructure migrations to AWS.
- The AWS Health Dashboard (previously AWS Personal Health Dashboard) is the single place to learn about the availability and operations of AWS services. You can view the overall status of all AWS services, and you can sign in to access a personalized view of the health of the specific services that are powering your workloads and applications. AWS Health Dashboard proactively notifies you when AWS experiences any events that may affect you, helping provide quick visibility and guidance to minimize the impact of events in progress, and plan for any scheduled changes, such as AWS hardware maintenance.
- AWS Knowledge Center is not part of the Enterprise support plan. AWS Knowledge Center is available for everyone free of charge. The AWS Knowledge Center helps answer the questions most frequently asked by AWS customers. The AWS Knowledge Center does not provide guidance on a case-by-case basis.
- AWS Support Concierge Service assists customers with account and billing inquiries.

1. The AWS Management Console allows you to access and manage Amazon Web Services through a simple and intuitive web-based user interface. You can also use the AWS Console mobile app to quickly view resources on the go.
- The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.
- The AWS SDK (Software Development Kit) allows you to interact with AWS services using your preferred programming language.
- AWS API refers to the AWS application programming interface

1. For billing purposes, the consolidated billing feature of AWS Organizations treats all the accounts in the organization as one account. This means that all accounts in the organization can receive the hourly cost benefit of Reserved Instances that are purchased by any other account. For example, Suppose that Fiona and John each have an account in an organization. Fiona has five Reserved Instances of the same type, and John has none. During one particular hour, Fiona uses three instances and John uses six, for a total of nine instances on the organization‘s consolidated bill. AWS bills five instances as Reserved Instances, and the remaining four instances as On-demand instances
- There is no difference in performance between On-demand and Reserved instances of the same type.
- The Reserved Instance discounts can be shared with all accounts in the organization.
- With Consolidated Billing, you can combine the usage across all accounts in the organization to share the Reserved Instance discounts, volume pricing discounts, and Savings Plans. This can result in a lower charge for your project, department, or company than with individual standalone accounts.

1. Amazon ElastiCache is a web service that makes it easy to deploy, operate, and scale an in-memory data store or cache in the cloud. The service improves the performance of web applications by allowing you to retrieve information from fast, managed, in-memory data stores, instead of relying entirely on slower disk-based databases.

The primary purpose of an in-memory data store is to provide ultrafast (submillisecond latency) and inexpensive access to copies of data. Querying a database is always slower and more expensive than locating a copy of that data in a cache. Some database queries are especially expensive to perform. An example is queries that involve joins across multiple tables or queries with intensive calculations. By caching (storing) such query results, you pay the price of the query only once. Then you can quickly retrieve the data multiple times without having to re-execute the query.

- AWS Storage Gateway is not a caching service, it is a hybrid storage service that enables your on-premises applications to seamlessly use AWS cloud storage.
- An Amazon EBS volume is a durable, block-level storage device that you can attach to a single EC2 instance. You can use EBS volumes as primary storage for data that requires frequent updates, such as the system drive for an instance or storage for a database application. You can also use them for throughput-intensive applications that perform continuous disk scans.
- AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. Chef and Puppet are automation platforms that allow you to use code to automate the configurations of your servers. OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments.

1. Amazon CloudWatch is a service that monitors AWS cloud resources and the applications you run on AWS. You can use Amazon CloudWatch to collect and track metrics, collect and monitor log files, set alarms, and automatically react to changes in your AWS resources. Amazon CloudWatch can monitor AWS resources such as Amazon EC2 instances, Amazon DynamoDB tables, and Amazon RDS DB instances, as well as custom metrics generated by your applications and services, and any log files your applications generate. You can use CloudWatch to detect anomalous behavior in your environments, take automated actions, troubleshoot issues, and discover insights to keep your applications running smoothly.
- AWS Config is a fully managed service that provides you with an AWS resource inventory, configuration history, and configuration change notifications to enable security and governance. With AWS Config you can discover existing AWS resources, export a complete inventory of your AWS resources with all configuration details, and determine how a resource was configured at any point in time. These capabilities enable compliance auditing, security analysis, and resource change tracking.
- AWS CloudTrail is an AWS service that can be used to monitor all user interactions with the AWS environment.
- AWS Lambda is a serverless compute service.

1. AWS Auto Scaling is the feature that automates the process of adding/removing server capacity (based on demand). Autoscaling allows you to reduce your costs by automatically turning off resources that aren’t in use. On the other hand, Autoscaling ensures that your application runs effectively by provisioning more server capacity if required.
- AWS Budgets gives you the ability to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.
- AWS Elastic Load Balancer (ELB) is a service that distributes the incoming application traffic to multiple targets that you define.
- AWS Cost Explorer provides an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time.

1. AWS Database Migration Service (DMS) helps you migrate databases to AWS easily and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. 
- AWS Database Migration Service can also be used for continuous data replication with high availability.
- AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet.
- AWS Application Migration Service is a highly automated lift-and-shift (rehost) solution that simplifies the process of migrating applications from physical, virtual, and cloud-based infrastructure, ensuring that they are fully operational in any AWS Region without compatibility issues.
- AWS Application Discovery Service helps enterprise customers plan migration projects by gathering information about their on-premises data centers.

1. As application complexity increases, a desirable attribute of an IT system is that it can be broken into smaller, loosely coupled components. This means that IT systems should be designed in a way that reduces interdependencies—a change or a failure in one component should not cascade to other components. On the other hand if the components of an application are tightly coupled and one component fails, the entire application will also fail. Therefore when designing your application, you should always decouple its components.
- Decoupling allows you to deal with your application as multiple independent components (microservices) not as a single, cohesive unit.
- There is no relation between decoupling an application and tracking API calls. API calls are tracked by AWS CloudTrail.
- Decoupling is the exact opposite of having a monolithic application. A monolithic application is designed to be self-contained; components of the program are interconnected and interdependent rather than loosely coupled as is the case with Microservices applications (or loosely-coupled applications).

1. The AWS Health Dashboard (previously AWS Personal Health Dashboard) is the single place to learn about the availability and operations of AWS services. You can view the overall status of all AWS services, and you can sign in to access a personalized view of the health of the specific services that are powering your workloads and applications. AWS Health Dashboard proactively notifies you when AWS experiences any events that may affect you, helping provide quick visibility and guidance to minimize the impact of events in progress, and plan for any scheduled changes, such as AWS hardware maintenance.

The benefits of the AWS Health Dashboard include:

- *A personalized View of Service Health: AWS Health Dashboard gives you a personalized view of the status of the AWS services that power your applications, enabling you to quickly see when AWS is experiencing issues that may impact you. For example, in the event of a lost EBS volume associated with one of your EC2 instances, you would gain quick visibility into the status of the specific service you are using, helping save precious time troubleshooting to determine root cause.
- *Proactive Notifications: The dashboard also provides forward looking notifications, and you can set up alerts across multiple channels, including email and mobile notifications, so you receive timely and relevant information to help plan for scheduled changes that may affect you. In the event of AWS hardware maintenance activities that may impact one of your EC2 instances, for example, you would receive an alert with information to help you plan for, and proactively address any issues associated with the upcoming change.

1. Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available. SQS lets you decouple application components so that they run independently, increasing the overall fault tolerance of the system. Multiple copies of every message are stored redundantly across multiple availability zones so that they are available whenever needed.
- Amazon SES (Amazon Simple Email Service) is a flexible, affordable, and highly-scalable email messaging platform for businesses and developers.
- Amazon Connect is a cloud-based contact center service that makes it easy for businesses to deliver customer service at low cost.
- AWS Direct Connect is a cloud service solution that is used to establish a dedicated network connection between your premises and AWS.

1. Creating snapshots of EBS Volumes can help ensure that you have a backup of your EBS volumes just in case any issues arise. You can use Amazon Data Lifecycle Manager (Amazon DLM) to automate the creation, retention, and deletion of EBS snapshots.

Automating snapshot management with Amazon DLM helps you to:

– Protect valuable data by enforcing a regular backup schedule.

– Retain backups as required by auditors or internal compliance.

– Reduce storage costs by deleting outdated backups.

– Create disaster recovery backup policies that back up data to isolated accounts.

Amazon EBS encryption offers a straight-forward encryption solution for your EBS resources that doesn‘t require you to build, maintain, and secure your own key management infrastructure. Encryption operations occur on the servers that host EC2 instances, ensuring the security of both data-at-rest and data-in-transit between an instance and its attached EBS storage.

- It is the responsibility of AWS to control and restrict access to its data centers.
- To make a backup of your EBS volumes you should use the Snapshot feature. Snapshots can provide a Copy-on-Write Consistency (reflect the exact image of the volume at the point-in-time of the snapshot).
- It is the responsibility of AWS to regularly update firmware on hardware devices.
- EBS Snapshots are incremental backups, which means that only the blocks on the device that have changed after your last snapshot are saved. This minimizes the time required to create the snapshot and saves on storage costs by not duplicating data.

1. Customers should be aware that their responsibilities may vary depending on the AWS services chosen.  For example, when using Amazon EC2, you are responsible for applying operating system and application security patches regularly. However, such patches are applied automatically when using Amazon RDS.
- A computer on which AWS runs one or more virtual machines is called a host machine, and each virtual machine is called a guest machine. AWS drives the concept of virtualization by allowing the physical host machine to operate multiple virtual machines as guests (for multiple customers) to help maximize the effective use of computing resources such as memory, network bandwidth and CPU cycles.

Patching the guest operating system is the responsibility of AWS for the managed services only (such as Amazon RDS). The customer is responsible for patching the guest OS for other services (such as Amazon EC2).

1. AWS Organizations helps customers centrally govern their environments as they grow and scale their workloads on AWS. Whether customers are a growing startup or a large enterprise, Organizations helps them to centrally manage billing; control access, compliance, and security; and share resources across their AWS accounts.

AWS Organizations has five main benefits:

1) Centrally manage access polices across multiple AWS accounts.

2) Automate AWS account creation and management.

3) Control access to AWS services.

4) Consolidate billing across multiple AWS accounts.

5) Configure AWS services across multiple accounts.

- AWS Trusted Advisor is an online tool that provides customers with real time guidance to help them provision their resources following AWS best practices.
- IAM user groups are not used to manage multiple AWS accounts. An IAM user group is a collection of IAM users – within the same AWS account – that are managed as a unit. IAM user groups let customers specify permissions for multiple users, which can make it easier to manage the permissions for those users. For example, customers could have a user group called Admins and give that user group the types of permissions that administrators typically need.
- AWS Config is a fully managed service that provides customers with an AWS resource inventory, configuration history, and configuration change notifications to enable security and governance.

1. Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud. Amazon Aurora combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases. It delivers up to five times the throughput of standard MySQL and up to three times the throughput of standard PostgreSQL. Amazon Aurora is designed to be compatible with MySQL and with PostgreSQL, so that existing applications and tools can run without requiring modification. It is available through Amazon Relational Database Service (RDS), freeing you from time-consuming administrative tasks such as provisioning, patching, backup, recovery, failure detection, and repair.
- You can Install MySQL on an EC2 instance, but in this scenario, you would have to manage the database and the backup processes yourself; it would not be automatic.
- Amazon DynamoDB does not support MySQL. Amazon DynamoDB is a NoSQL database service.
- Amazon Neptune is a graph database service, not a MySQL database service. Amazon Neptune is used to build and run applications that work with highly connected datasets, such as social networking, recommendation engines, and knowledge graphs.

1. Amazon Route 53 is a global service that provides highly available and scalable Domain Name System (DNS) services, domain name registration, and health-checking web services. It is designed to give developers and businesses an extremely reliable and cost effective way to route end users to Internet applications by translating names like [example.com](http://example.com/) into the numeric IP addresses, such as 192.0.2.1, that computers use to connect to each other.
- EMR is used to process vast amounts of data easily and securely. Use cases include: big data,log analysis, web indexing, data transformations (ETL), machine learning, financial analysis, scientific simulation, and bioinformatics.
- AWS Config is a fully managed service that provides you with an AWS resource inventory, configuration history, and configuration change notifications to enable security and governance.
- Amazon CloudFront gives businesses and web application developers an easy and cost effective way to distribute content globally with low latency and high data transfer speeds.

1. Included as part of the Enterprise Support plan, the Support Concierge Team are AWS billing and account experts that specialize in working with enterprise accounts. The Concierge team will quickly and efficiently assist you with your billing and account inquiries, and work with you to help implement billing and account best practices so that you can focus on running your business.

Support Concierge service includes:

- * 24 x7 access to AWS billing and account inquires.
- * Guidance and best practices for billing allocation, reporting, consolidation of accounts, and root-level account security.
- * Access to Enterprise account specialists for payment inquiries, training on specific cost reporting, assistance with service limits, and facilitating bulk purchases.
- AWS Customer Service can help AWS customers with their billing and account inquiries, and it is included in all AWS support plans (Basic, Developer, Business, and Enterprise). However, due to the fact that AWS Customer Service is not dedicated to specific types of inquiries, it is not as quick or as efficient as the AWS Support Concierge. AWS Support Concierge is available only for AWS Enterprise support subscribers and is dedicated only to help AWS customers with their billing and account inquiries.
- AWS Operations Support is an Enterprise support program that provides operations assessments and analysis to identify gaps across the operations lifecycle, as well as recommendations based on best practices.
- The AWS Health Dashboard (previously AWS Personal Health Dashboard) is the single place to learn about the availability and operations of AWS services. You can view the overall status of all AWS services, and you can sign in to access a personalized view of the health of the specific services that are powering your workloads and applications.

1. AWS Snowball is a petabyte-scale data transport solution that uses secure appliances to transfer large amounts of data into and out of the AWS cloud. Using Snowball addresses common challenges with large-scale data transfers, including high network costs, long transfer times, and security concerns. AWS Customers use Snowball to migrate analytics data, genomics data, video libraries, image repositories, and backups. Transferring data with Snowball is simple, fast, secure, and can cost as little as one-fifth the cost of using high-speed internet.

Additionally, With AWS Snowball, you can access the compute power of the AWS Cloud locally and cost-effectively in places where connecting to the internet might not be an option. AWS Snowball is a perfect choice if you need to run computing in rugged, austere, mobile, or disconnected (or intermittently connected) environments.

With AWS Snowball, you have the choice of two devices, Snowball Edge Compute Optimized with more computing capabilities, suited for higher performance workloads, or Snowball Edge Storage Optimized with more storage, which is suited for large-scale data migrations and capacity-oriented workloads.

Snowball Edge Storage Optimized is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. It is also a good fit for running general purpose analysis such as IoT data aggregation and transformation.

Snowball Edge Compute Optimized is the optimal choice if you need powerful compute and high-speed storage for data processing. Examples include high-resolution video processing, advanced IoT data analytics, and real-time optimization of machine learning models.

- A catalog of third-party software solutions that customers need to build solutions and run their businesses“ is incorrect. AWS Marketplace is the service that provides this catalog. AWS Marketplace is a digital catalog with thousands of software listings from independent software vendors that make it easy to find, test, buy, and deploy software that runs on AWS. AWS Marketplace includes software listings from categories such as security, networking, storage, machine learning, business intelligence, database, and DevOps.

1. There are three Cloud Computing Models:

1) Infrastructure as a Service (IaaS) – Infrastructure as a Service (IaaS) contains the basic building blocks for cloud IT and typically provide access to networking features, computers (virtual or on dedicated hardware), and data storage space. IaaS provides you with the highest level of flexibility and management control over your IT resources and is most similar to existing IT resources that many IT departments and developers are familiar with today.

2) Platform as a Service (PaaS) – Platform as a Service (PaaS) removes the need for your organization to manage the underlying infrastructure (usually hardware and operating systems) and allows you to focus on the deployment and management of your applications. This helps you be more efficient as you don’t need to worry about resource procurement, capacity planning, software maintenance, patching, or any of the other undifferentiated heavy lifting involved in running your application.

3) Software as a Service (SaaS) – Software as a Service (SaaS) provides you with a completed product that is run and managed by the service provider. In most cases, people referring to Software as a Service are referring to end-user applications. With a SaaS offering you do not have to think about how the service is maintained or how the underlying infrastructure is managed; you only need to think about how you will use that particular piece of software. A common example of a SaaS application is web-based email which you can use to send and receive email without having to manage feature additions to the email product or maintain the servers and operating systems that the email program is running on.

Networking services are provided as part of the IaaS mode

1. Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment.

The use cases of Amazon CloudFront include:

1- Accelerate static website content delivery.

CloudFront can speed up the delivery of your static content (for example, images, style sheets, JavaScript, and so on) to viewers across the globe. By using CloudFront, you can take advantage of the AWS backbone network and CloudFront edge servers to give your viewers a fast, safe, and reliable experience when they visit your website.

2- Live & on-demand video streaming.

The Amazon CloudFront CDN offers multiple options for streaming your media – both pre-recorded files and live events – at sustained, high throughput required for 4K delivery to global viewers.

3- Security.

CloudFront integrates seamlessly with AWS Shield for Layer 3/4 DDoS mitigation and AWS WAF for Layer 7 protection.

4- Customizable content delivery with Lambda@Edge.

Lambda@Edge is a feature of Amazon CloudFront that lets you run code closer to users of your application, which improves performance and reduces latency.

- AWS CloudFormation allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts.
- Amazon Kinesis Video Streams enables you to securely stream video from connected devices (IoT devices) to AWS for analytics, machine learning (ML), playback, and other processing. Kinesis Video Streams automatically provisions and elastically scales all the infrastructure needed to ingest streaming video data from millions of devices. It durably stores, encrypts, and indexes video data in your streams, and allows you to access your data through easy-to-use APIs.
- Amazon Simple Notification Service (SNS) is a fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications. Using Amazon SNS topics, your publisher systems can fan out messages to a large number of subscriber endpoints for parallel processing, including AWS Lambda functions, and HTTP/S webhooks. Additionally, SNS can be used to fan out notifications to end users using mobile push, SMS, and email.

1. Amazon DynamoDB is a fast and flexible NoSQL database service for all applications that need consistent, single-digit millisecond latency at any scale. It is a fully managed cloud database and supports both document and key-value store models. Its flexible data model, reliable performance, and automatic scaling of throughput capacity, makes it a great fit for mobile, web, gaming, ad tech, IoT, and many other applications.
- Amazon Elastic Block Store (Amazon EBS) is a storage service, NOT a database service.
- Amazon Aurora doesn’t support NoSQL databases. Amazon Aurora is a MySQL and PostgreSQL-compatible relational database.
- Amazon Redshift doesn’t support non-relational data. Amazon Redshift is a fully managed data warehouse service that allows you to run complex analytic queries against petabytes of structured data using standard SQL and your existing Business Intelligence (BI) tools.

1. For Enterprise-level customers, a TAM (Technical Account Manager) provides technical expertise for the full range of AWS services and obtains a detailed understanding of your use case and technology architecture. TAMs work with AWS Solution Architects to help you launch new projects and give best practices recommendations throughout the implementation life cycle. Your TAM is the primary point of contact for ongoing support needs, and you have a direct telephone line to your TAM.
- AWS Infrastructure Event Management (IEM) is a structured program available to Enterprise Support customers (and Business Support customers for an additional fee) that helps you plan for large-scale events such as product or application launches, infrastructure migrations, and marketing events. With Infrastructure Event Management, you get strategic planning assistance before your event, as well as real-time support during these moments that matter most for your business. AWS Infrastructure Event Management is not for day-to-day support needs.
- An AWS Identity and Access Management (IAM) user is an entity that you create in AWS to represent the person or service that uses it to directly interact with AWS. A primary use for IAM users is to grant individuals access to the AWS Management Console for interactive tasks and / or to make programmatic requests to AWS services using the API or CLI.
- AWS Consulting Partners are not part of AWS support. AWS Consulting Partners are professional services firms that help customers design, architect, build, migrate, and manage their workloads and applications on AWS. Consulting Partners include System Integrators, Strategic Consultancies, Agencies, Managed Service Providers, and Value-Added Resellers.

1. The customer is responsible for securing their network by configuring Security Groups, Network Access control Lists (Network ACLs), and Routing Tables. The customer is also responsible for setting a password policy on their AWS account that specifies the complexity and mandatory rotation periods for their IAM users‘ passwords.
- Disk disposal ( Storage Device Decommissioning): When a storage device has reached the end of its useful life, AWS procedures include a decommissioning process that is designed to prevent customer data from being exposed to unauthorized individuals. All decommissioned magnetic storage devices are degaussed and physically destroyed in accordance with industry-standard practices.
- AWS is responsible for controlling physical access to the data centers.
- Patching the underlying infrastructure is the responsibility of AWS. The customer is responsible for patching the Operating System of their EC2 instances and any software installed on these instances.

1. Spot instances provide a discount (up to 90%) off the On-Demand price. The Spot price is determined by long-term trends in supply and demand for EC2 spare capacity. If the Spot price exceeds the maximum price you specify for a given instance or if capacity is no longer available, your instance will automatically be interrupted.

Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if you don‘t mind if your applications get interrupted. For example, Spot Instances are well-suited for data analysis, batch jobs, background processing, and optional tasks.

- Reserved instances are recommended for Customers who can commit to using EC2 over a 1 or 3-year term to reduce their total computing costs. Even if the project will last for more than a year, the cost-benefit for acquiring Reserved Instances is not as great as the cost-benefit from using Spot Instances. The Spot option provides the largest discount (up to 90%).
- On-demand instances are significantly less cost-effective than spot instances.
- Dedicated instances are used when you need your instances to be physically isolated at the host hardware level from instances that belong to other AWS accounts. Dedicated instances are significantly more expensive than Spot Instances

1. Horizontal Scaling:

Scaling horizontally takes place through an increase in the number of resources (e.g., adding more hard drives to a storage array or adding more servers to support an application). This is a great way to build Internet-scale applications that leverage the elasticity of cloud computing.

Vertical Scaling:

Scaling vertically takes place through an increase in the specifications of an individual resource (e.g., upgrading a server with a larger hard drive, adding more memory, or provisioning a faster CPU). On Amazon EC2, this can easily be achieved by stopping an instance and resizing it to an instance type that has more RAM, CPU, I/O,or networking capabilities. This way of scaling can eventually hit a limit and it is not always a cost efficient or highly available approach. However, it is very easy to implement and can be sufficient for many use cases especially as a short term solution.

Additional information:

Vertical-scaling is often limited to the capacity constraints of a single machine, scaling beyond that capacity often involves downtime and comes with an upper limit. With horizontal-scaling it is often easier to scale dynamically by adding more machines in parallel. Hence, in most cases, horizontal-scaling is recommended over vertical-scaling.

1. An IAM user group is a collection of IAM users that are managed as a unit. User groups let you specify permissions for multiple users, which can make it easier to manage the permissions for those users. For example, you could have a user group called Admins and give that user group the types of permissions that administrators typically need. Any user in that user group automatically has the permissions that are assigned to the user group. If a new user joins your organization and needs administrator privileges, you can assign the appropriate permissions by adding the user to that user group. Similarly, if a person changes jobs in your organization, instead of editing that user‘s permissions, you can remove him or her from the old user groups and add him or her to the appropriate new user groups.
- An IAM role is an IAM identity that you can create in your account that has specific permissions. IAM roles allow you to delegate access (for a limited time) to users or services that normally don‘t have access to your organization‘s AWS resources. IAM users or AWS services can assume a role to obtain temporary security credentials that can be used to interact with specific AWS resources.

You can use roles to delegate access to users, applications, or services that don‘t normally have access to your AWS resources. For example, you might want to grant users in your AWS account access to resources they don‘t usually have, or grant users in one AWS account access to resources in another account. Or you might want to allow a mobile app to use AWS resources, but not want to embed AWS keys within the app. Sometimes you want to give AWS access to users who already have identities defined outside of AWS, such as in your corporate directory. Or, you might want to grant access to your account to third parties so that they can perform an audit on your resources. For these scenarios, you can delegate access to AWS resources using an IAM role.

- AWS Organizations can be used to group AWS accounts, not IAM users (the employees). AWS Organization helps you to centrally manage billing; control access, compliance, and security; and share resources across multiple AWS accounts.

1. AWS Cost Explorer is a free tool that you can use to view your costs and usage. You can view data up to the last 12 months, forecast how much you are likely to spend for the next 12 months, and get recommendations for what Reserved Instances to purchase. You can use AWS Cost Explorer to see patterns in how much you spend on AWS resources over time, identify areas that need further inquiry, and see trends that you can use to understand your costs. You can also specify time ranges for the data, and view time data by day or by month.
- AWS Cost Explorer is a free tool that you can use to view your costs and usage. You can view data up to the last 12 months, forecast how much you are likely to spend for the next 12 months, and get recommendations for what Reserved Instances to purchase. You can use AWS Cost Explorer to see patterns in how much you spend on AWS resources over time, identify areas that need further inquiry, and see trends that you can use to understand your costs. You can also specify time ranges for the data, and view time data by day or by month.
- The AWS support team will direct you to use AWS Cost Explorer.
- You can use the Amazon Virtual Private Cloud console to launch AWS resources, such as Amazon EC2 instances. You can use it to specify an IP address range for the VPC, add subnets, associate security groups, and configure route tables.

1. The S3 Intelligent-Tiering storage class is designed to optimize costs by automatically moving data to the most cost-effective access tier, without performance impact or operational overhead. It works by storing objects in two access tiers: one tier that is optimized for frequent access and another lower-cost tier that is optimized for infrequent access. For a small monthly monitoring and automation fee per object, Amazon S3 monitors access patterns of the objects in S3 Intelligent-Tiering, and moves the ones that have not been accessed for 30 consecutive days to the infrequent access tier. If an object in the infrequent access tier is accessed, it is automatically moved back to the frequent access tier. There are no retrieval fees when using the S3 Intelligent-Tiering storage class, and no additional tiering fees when objects are moved between access tiers. It is the ideal storage class for long-lived data with access patterns that are unknown or unpredictable.
- S3 Standard offers high durability, availability, and performance object storage for frequently accessed data.
- Amazon S3 Standard-Infrequent Access (S3 Standard-IA) is for data that is accessed less frequently, but requires rapid access when needed.
- Amazon S3 Glacier Flexible Retrieval (Formerly S3 Glacier) is a low-cost storage class for archive data that is accessed 1 – 2 times per year.

1. AWS CloudFormation allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts. You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and AWS CloudFormation takes care of provisioning and configuring those resources for you. You don‘t need to individually create and configure AWS resources and figure out what‘s dependent on what; AWS CloudFormation handles all that for you.
- Amazon SES refers to the Amazon Simple Email service.
- AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources.
- Amazon EMR is used to run and scale Apache Spark, Hadoop, Presto, and other Big Data Frameworks.

1. The AWS Abuse team can assist you when AWS resources are being used to engage in the following types of abusive behavior:

I. Spam: You are receiving unwanted emails from an AWS-owned IP address, or AWS resources are being used to spam websites or forums.

II. Port scanning: Your logs show that one or more AWS-owned IP addresses are sending packets to multiple ports on your server, and you believe this is an attempt to discover unsecured ports.

III. Denial of service attacks (DOS): Your logs show that one or more AWS-owned IP addresses are being used to flood ports on your resources with packets, and you believe this is an attempt to overwhelm or crash your server or software running on your server.

IV. Intrusion attempts: Your logs show that one or more AWS-owned IP addresses are being used to attempt to log in to your resources.

V. Hosting objectionable or copyrighted content: You have evidence that AWS resources are being used to host or distribute illegal content or distribute copyrighted content without the consent of the copyright holder.

VI. Distributing malware: You have evidence that AWS resources are being used to distribute software that was knowingly created to compromise or cause harm to computers or machines on which it is installed.

Note: Anyone can report abuse of AWS resources, not just AWS customers

- The AWS Security team is responsible for the security of services offered by AWS.
- The AWS Concierge team can assist you with the issues that are related to your billing and account management.
- The AWS Customer Service team is at the forefront of this transformational technology assisting a global list of customers that are taking advantage of a growing set of services and features to run their mission-critical applications. The team helps AWS customers understand what Cloud Computing is all about, and whether it can be useful for their business needs.

1. The principle of least privilege is one of the most important security practices and it means granting users the required permissions to perform the tasks entrusted to them and nothing more. The security administrator determines what tasks users need to perform and then attaches the policies that allow them to perform only those tasks. You should start with a minimum set of permissions and grant additional permissions when necessary. Doing so is more secure than starting with permissions that are too lenient and then trying to tighten them down.

1. To deliver content to global end users with lower latency, Amazon CloudFront uses a global network of Edge Locations and Regional Edge Caches in multiple cities around the world. Amazon CloudFront uses this network to cache copies of your content close to your end-users. Amazon CloudFront ensures that end-user requests are served by the closest edge location. As a result, end-user requests travel a short distance, improving performance for your end-users, while reducing the load on the origin servers.
- AWS Global Accelerator is incorrect. AWS Global Accelerator and CloudFront are two separate services that use the AWS global network and its edge locations around the world. CloudFront improves performance for both cacheable (e.g., images and videos) and dynamic content (e.g. dynamic site delivery). Global Accelerator is a good fit for specific use cases, such as gaming, IoT or Voice over IP.
- Amazon CloudFront only uses Edge Locations or Regional Edge Caches.

1. All of the physical security are taken care of for you. Amazon data centers are surrounded by three physical layers of security. “Nothing can go in or out without setting off an alarm”. It’s important to keep bad guys out, but equally important to keep the data in which is why Amazon monitors incoming gear, tracking every disk that enters the facility. And “if it breaks we don’t return the disk for warranty. The only way a disk leaves our data center is when it’s confetti.”

Most (not all) data and network security are taken care of for you. When we talk about the data/network security, AWS has a “shared responsibility model” where AWS and the customer share the responsibility of securing them. For example, the customer is responsible for creating rules to secure their network traffic using the security groups and is also responsible for protecting data with encryption.

“Increasing speed and agility“ is also a correct answer because in a cloud computing environment, new IT resources are only a click away, which means it requires less time to make those resources available to developers – from weeks to just minutes. This results in a dramatic increase in agility for the organization, since the cost and time it takes to experiment and develop is significantly lower.

- The Physical infrastructure is a responsibility of AWS, not the customer
- AWS customers are responsible for building and operating their applications.
- As mentioned above, security is a shared responsibility between AWS and the customer. For example, the customer has to manage who can access and use AWS resources using the IAM service.

1. AWS Artifact is a self-service audit artifact retrieval portal that provides customers with on-demand access to AWS’ compliance documentation and AWS agreements. You can use AWS Artifact Agreements to review, accept, and track the status of AWS agreements such as the Business Associate Addendum (BAA).

Additional information:

You can also use AWS Artifact Reports to download AWS security and compliance documents, such as AWS ISO certifications, Payment Card Industry (PCI), and System and Organization Control (SOC) reports.

- AWS Organizations provides central governance and management across multiple AWS accounts.
- AWS Systems Manager gives you visibility and control of your infrastructure on AWS. Systems Manager provides a unified user
- AWS Certificate Manager is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources

1. AWS Partner Solutions (formerly AWS Quick Starts) outline the architectures for popular enterprise solutions on AWS and provide AWS CloudFormation templates to automate their deployment. Each Partner Solution launches, configures, and runs the AWS compute, network, storage, and other services required to deploy a specific workload on AWS, using AWS best practices for security and availability.

AWS Partner Solutions are automated reference deployments built by AWS solutions architects and partners to help you deploy popular technologies on AWS, based on AWS best practices. These accelerators reduce hundreds of manual installation and configuration procedures into just a few steps, so you can build your production environment quickly and start using it immediately.

- AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. Chef and Puppet are automation platforms that allow you to use code to automate the configurations of your servers.
- Amazon CloudWatch is mainly used to monitor the utilization of your AWS resources.
- Amazon Aurora is a database service.