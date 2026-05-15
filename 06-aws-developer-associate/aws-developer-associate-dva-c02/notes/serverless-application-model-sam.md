# Serverless Application Model (SAM)

---

## Intro

- IaC (YAML) for deploying serverless applications easily
- Abstraction over [CloudFormation](cloudformation.md) to allow developers to easily deploy their code
- Can deploy Lambda, API Gateway and DynamoDB locally for development using **SAM CLI** and **AWS Toolkits**
- Uses **CodeDeploy** under the hood to update Lambda functions

## Workflow & Commands

![Untitled](Serverless%20Application%20Model%20(SAM)/Untitled.png)

- `sam build` - Fetch dependencies & build the application. If the application code does not require building, skip this command and run `sam package` directly.
- `aws cloudformation package` or `sam package` - Convert the SAM template to CloudFormation template, package the application code and the CloudFormation template and upload to an S3 bucket (must be created beforehand).
- `aws cloudformation deploy` or `sam deploy` - Deploy the application package from S3 (creates and executes Change Set in CloudFormation)
- `sam publish` - publish serverless app to SAR (only needs the CF template, the code is referenced from S3)

## Template

- `Transform: "AWS::Serverless-2016-10-31'` - indicates that the YAML file is a SAM template (required)
- `Resources` - resources to be created (required)
    - `AWS::Serverless::Function` - define a Lambda function
    - `AWS::Serverless::Api` - define an API gateway
    - `AWS::Serverless::SimpleTable` - define a DynamoDB table
    - `AWS::Serverless::Application` - use an application from SAR

### Policy Templates

- List of templates to grant permissions to Lambda functions easily
- Important policy templates:
    - `S3ReadPolicy` - read-only permission to objects in an S3 bucket
    - `SQSPollerPolicy` - allow the function to poll an SQS queue
    - `DynamoDBCrudPolicy` - allow CRUD operations on a DynamoDB table
    - `DynamoDBReadPolicy` - allow read operations on a DynamoDB table

![Untitled](Serverless%20Application%20Model%20(SAM)/Untitled%201.png)

## SAM + [CodeDeploy](codedeploy.md)

- SAM uses CodeDeploy under the hood to update Lambda functions every time we update the code and deploy.
- Gradually shifts traffic to the new Lambda version using **Aliases**
- Optional **Pre & Post Traffic Hooks** (run on separate Lambda functions) to validate the deployment before the traffic shift starts and after it ends
- Optional **Automated Rollback** using CloudWatch Alarms
- Configure the deployment strategy in the `Properties` section of the Lambda function.
    
    ![Untitled](Serverless%20Application%20Model%20(SAM)/Untitled%202.png)
    

![Untitled](Serverless%20Application%20Model%20(SAM)/Untitled%203.png)

## Local Deployment

- Can deploy Lambda, API Gateway and DynamoDB locally for development using **SAM CLI** and **AWS Toolkits**
- `sam local start-lambda` - start a lambda function locally (local endpoint)
- `sam local invoke` - invoke the local lambda endpoint with a payload
    - If the function makes API calls to AWS, make sure to specify `--profile` option
- `sam local start-api` - starts a local HTTP server along with the lambda code as backend
    - Changes made to the function code are automatically reloaded
- `sam local generate-event` - generate local mock events for lambda functions
    - Example: generate an S3 PutObject event and use it to invoke the lambda function
        
        `sam local generate-event s3 put --bucket <bucket> --key <key> |
        sam local invoke -e - <function_id>`
        

## Serverless Application Repository (SAR)

- Repository for serverless applications packaged using SAM
- Packaged applications can be shared
    - Publicly
    - With specific AWS accounts
- The packaged applications can be directly deployed (no duplicate work)
- Application can be customized using **environment variables**