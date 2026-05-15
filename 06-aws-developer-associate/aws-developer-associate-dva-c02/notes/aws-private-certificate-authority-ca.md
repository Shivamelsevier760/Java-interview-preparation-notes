# AWS Private Certificate Authority (CA)

- **Used to create Private CA** (root or subordinate) which can then issue and deploy **X.509 certificates** (can only be used by applications, cannot be used to create other certificates)
- Private TLS certificates are trusted only within your organization (not the public internet)
- Private CA integrates with ELB, API Gateway, CloudFront and **EKS** to load private certificates.
- Usually used to build a **Public Key Infrastructure (PKI)** within an enterprise.

![Untitled](AWS%20Private%20Certificate%20Authority%20(CA)/Untitled.png)