# AWS CLI & SDK

# AWS CLI

- AWS CLI is written in Python SDK (boto3)
- When no region is specified in the CLI or SDK, the default region is `us-east-1`
- Before making API calls against MFA-protected APIs, you need to use `sts:GetSessionToken` to get temporary credentials.

### Commands

- Configure AWS CLI - `aws configure`
- `--dry-run` flag lets us dry run AWS CLI commands
- `aws sts decode-authorization-message --encoded-message <encoded-message>` - Decode encoded authorization message. Need permission `sts:DecodeAuthorizationMessage` to be able to run the above command.

### CLI Profiles

- Allows us to use multiple AWS accounts using the CLI.
- Configure AWS CLI with a profile info - `aws configure --profile <profile-name>`
- Specify a profile in AWS command using `--profile <profile-name>` otherwise the `default` profile will be used.
- The credentials for different profiles are stored at `~/.aws/credentials`
    
    ```yaml
    [default]
    aws_access_key_id = ASIAW4X6ZFPB74QH6E64
    aws_secret_access_key = egwe43h45jhw5jwhaergergeh5w
    AWS_SESSION_TOKEN = asdfadsfadcaeghwerbweh43tq4twgrbg4hqgev4weagh43q
    
    [dev]
    aws_access_key_id = ASIAW4X6ZFPB74QH6E64
    aws_secret_access_key = egwe43h45jhw5jwhaergergeh5w
    AWS_SESSION_TOKEN = asdfadsfadcaeghwerbweh43tq4twgrbg4hqgev4weagh43q
    ```
    
- The config for different profiles are stored at `~/.aws/config`
    
    ```yaml
    [default]
    region = us-east-1
    
    [dev]
    region = us-west-1
    ```
    

# Limits & Quotas

### API Rate Limits

- Limits how many API calls we can make to a given service endpoint
- Example:
    - `Describelnstances` on EC2 → 100 calls per seconds
    - `GetObject` on S3 → 5500 GET per second per prefix
- Intermittent errors (ThrottlingExceptions) - use **Exponential Backoff**
    - Wait for 1s, 2s, 4s, 8s, and so on before making calls again.
    - Already built into the AWS SDK (no need to implement externally)
    - If implemented manually, should be used only when the error is 5xx (server side error)
- Consistent error - request API throttling limit increase

### Service Quotas (Service Limits)

- Limits how much resource we can use in our AWS account
- Example: 1152 vCPU limit for running on-demand standard instances
- We can increase service quota or service limits by **opening a ticket** or using **Service Quotas API**

# Credentials Provider Chain

The CLI or SDK looks for the credentials in the following order:

- CLI or SDK options
- Environment Variables
- `~/.aws/credentials` file
- `~/.aws/config` file
- ECS Container Credentials or EC2 Instance Profile Credentials

# Signature V4 (SigV4)

- The CLI or SDK automatically signs the request made by you to the AWS HTTP APIs so that AWS can verify whether or not the request came from you.
- **The request is signed using your AWS credentials** using AWS proprietary **SigV4 signing algorithm**.
- Custom **HTTP requests** made to the AWS API must be signed by the user.