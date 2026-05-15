# Security Token Service (STS)

- Used to **grant limited and temporary access** (**15 min - 1 hour**) to AWS resources

## APIs

- `AssumeRole` - assume an IAM Role within your account or **cross account** and return temporary credentials for that role
- `AssumeRoleWithSAML` - return credentials for users logged in with SAML
- `AssumeRoleWithWebldentity` - return credentials for users logged in via a web identity provider like Facebook, Google, OIDC compatible IDP, etc.
- `GetSessionToken` - get session token for MFA
- `GetFederationToken` - obtain temporary credentials for a federated user
- `GetCallerldentity` - return details about the lAM user or role
- `DecodeAuthorizationMessage` - decode error message when an AWS API is denied

### `AssumeRole`

- Steps to assume a Role
    - Define an IAM Role (within your account or cross-account)
    - **Trust Policy**: Define which principals can assume this IAM Role
    - Call `AssumeRole` API to impersonate the IAM Role and retrieve credentials

![Untitled](Security%20Token%20Service%20(STS)/Untitled.png)

![Untitled](Security%20Token%20Service%20(STS)/Untitled%201.png)

### `GetSessionToken`

- Used to get session token for MFA
- Returns
    - Access ID
    - Secret Key
    - Session Token
    - Expiration Date
- IAM policy can be created to allow some actions only if the user is multi-factor authenticated (`aws:MultiFactorAuthPresent: true`)

![Untitled](Security%20Token%20Service%20(STS)/Untitled%202.png)