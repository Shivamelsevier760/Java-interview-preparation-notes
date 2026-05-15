# Cloud Development Kit (CDK)

---

## Intro

- **IaC to define infrastructure using programming languages** (instead of declarative config files as in the case of CloudFormation and SAM)
- A step above CloudFormation (static type checks during programming which is not available in YAML config files)
- Supports JavaScript/TypeScript, Python, Java and .NET
- Deploy infrastructure and application code together
- The code is compiled to a CloudFormation template using **CDK CLI**
- Great for Lambda functions and Docker containers
- Contains high-level components called **constructs**

## Construct

- Component that encapsulates everything CDK needs to create the final CloudFormation stack
- Can represent a single AWS resource (e.g. S3 bucket) or multiple related resources (e.g. worker queue with compute)
- **AWS Construct Library** - a collection of Constructs included in AWS CDK which contains Constructs for every AWS resource
- **Construct Hub** - repository of constructs created by AWS, 3rd parties, and open-source CDK community

### Layers of Construct

- **Layer 1 (L1)**
    
    ![Untitled](Cloud%20Development%20Kit%20(CDK)/Untitled.png)
    
    - AWS resources exactly as available in CloudFormation (low level)
    - Construct names start with `Cfn` (CFN resources)
    - Must explicitly configure all resource properties
- **Layer 2 (L2)**
    
    ![Untitled](Cloud%20Development%20Kit%20(CDK)/Untitled%201.png)
    
    - AWS resources with **intent-based API** (higher level)
    - Convenient defaults (don’t need to know all the details about the resources)
    - **Resource methods** to work easily with resources (eg. `bucket.urlForObject()`)
- **Layer 3 (L3)**
    
    ![Untitled](Cloud%20Development%20Kit%20(CDK)/Untitled%202.png)
    
    - Collection of multiple related AWS resources forming a pattern (high level)
    - Don’t have to setup the infrastructure from scratch as in CloudFormation
    - Available for common architectures:
        - `aws-apigateway.LambdaRestApi` - represents an API gateway backed by a Lambda function
        - `aws-ecs-patterns.ApplicationLoadBalancerFargateService` - represents an architecture that includes a Fargate cluster with ALB

## Bootstrapping

- **Provisioning resources for CDK before deploying CDK apps in an AWS environment** (combination of account & region)
- Before using CDK to deploy an app in any AWS environment, we need to deploy a CloudFormation stack called **CDK Toolkit** in that environment, using the command ****`cdk bootstrap aws://<aws_account>/<aws_region>`.
- If CDKToolkit is not deployed, we’ll get an error: “***Policy contains a statement with one or more invalid principal***”.
- The CDKToolkit stack contains:
    - S3 Bucket - to store files
    - IAM Roles - to grant permissions to perform deployments

## Commands

![Untitled](Cloud%20Development%20Kit%20(CDK)/Untitled%203.png)

## Testing

- Use **CDK Assertions Module** along with testing frameworks like Jest or PyTest for testing the resources created by CDK.
- Two types:
    - **Fine-grained Assertions** (common) - test specific aspects of the CloudFormation template
    - **Snapshot Tests** - test the synthesized CloudFormation template against a previously stored baseline template
        - To import a CloudFormation template:
            - `Template.fromStack()` - for stack built in CDK
            - `Template.fromString()` - for stack build outside CDK
    
    ![Untitled](Cloud%20Development%20Kit%20(CDK)/Untitled%204.png)