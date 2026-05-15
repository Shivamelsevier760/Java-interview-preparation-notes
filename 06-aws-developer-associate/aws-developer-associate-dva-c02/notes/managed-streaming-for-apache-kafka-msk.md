# Managed Streaming for Apache Kafka (MSK)

---

![Untitled](Managed%20Streaming%20for%20Apache%20Kafka%20(MSK)/Untitled.png)

## Intro

- Managed Apache Kafka cluster on AWS
- Used to stream data (alternative to KDS)
- Creates and **manages Kafka broker nodes and Zookeeper nodes**
- MSK cluster is deployed in the VPC (3 AZ for HA)
- Automatic recovery from common Kafka failures
- **Data is stored on EBS volumes as long as needed**
- **MSK Serverless**: auto-scaling MSK cluster without provisioning or managing capacity
- KMS for at-rest encryption
- No in-flight encryption

## KDS vs MSK

| KDS | MSK |
| --- | --- |
| 1 MB message size limit | 1 MB default (max 10 MB) |
| Uses data streams with shards | Uses Kafka topics with partitions (similar) |
| Shard splitting and merging for scaling | Partitions can only be added to a topic |
| TLS for in-flight encryption | Plaintext (no in-flight encryption) or TLS |

## MSK Consumers

![Untitled](Managed%20Streaming%20for%20Apache%20Kafka%20(MSK)/Untitled%201.png)