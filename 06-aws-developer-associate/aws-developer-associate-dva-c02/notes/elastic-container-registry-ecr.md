# Elastic Container Registry (ECR)

- AWS managed **private** Docker repository
- **Pay for the storage you use** to store docker images (no provisioning)
- Integrated with ECS & **IAM for security**
- Storage backed by S3
- Can upload Docker images on ECR manually or we can use a CICD service like **CodeBuild**

### Pulling Images from ECR

- `$(aws ecr get-login --no-include-email)` - login to ECR
- `docker pull <repo-url>/<image>`