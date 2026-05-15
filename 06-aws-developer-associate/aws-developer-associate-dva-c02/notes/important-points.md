# Important Points

- AWS requires approximately 5 weeks of usage data to generate budget forecasts.
- **Never store AWS credentials in your code.** If your code is running inside AWS, use IAM roles to access AWS services. If your code is running outside AWS, use environment variables or named AWS profiles.