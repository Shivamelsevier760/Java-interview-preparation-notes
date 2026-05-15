# CloudTrail

---

## Intro

- **Global Service** (a single trail can be applied to multiple regions)
- Provides governance, compliance and audit by recording all the API calls to AWS services made within the account.
- Enabled by default
- **Event retention: 90 days**
- Export CloudTrail logs into
    - CloudWatch Logs
    - S3 (encrypted by default using **SSE-S3**)
- CloudTrail logs up to the last 90 days can be analyzed in CloudTrail Console. Older logs should be present in S3 and can be analyzed using **Athena**.

<aside>
💡 Modifications to log files can be detected by enabling **Log File Validation** on the logging bucket

</aside>

## Event Types

### Management Events

- Events of operations that modify AWS resources. Ex:
    - Creating a new IAM user
    - Deleting a subnet
- **Enabled by default**
- Can separate Read Events (that don’t modify resources) from Write Events (that may modify resources)

### Data Events

- Events of operations that modify data
    - S3 object-level activity
    - Lambda function execution
- **Disabled by default** (due to high volume of data events)

### Insight Events

- Enable **CloudTrail Insights** to detect unusual activity in your account
    - inaccurate resource provisioning
    - hitting service limits
    - bursts of AWS IAM actions
    - gaps in periodic maintenance activity
- CloudTrail Insights analyzes normal management events to create a baseline and then continuously analyzes write events to detect unusual patterns. If that happens, CloudTrail generates insight events that
    - show anomalies in the Cloud Trail console
    - can can be logged to S3
    - can trigger an EventBridge event for automation

## Encryption

<aside>
💡 A single KMS key can be used to encrypt log files for trails applied to all regions

</aside>

## Organization Trail

- Trail that logs events across all the accounts in an organization
- Must be created in the master account
- Member accounts will be able to see the organization trail, but cannot modify or delete it.
- By default, member accounts will not have access to the log files for the organization trail in the S3 bucket.