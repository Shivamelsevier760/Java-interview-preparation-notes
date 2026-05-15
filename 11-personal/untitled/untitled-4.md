# Untitled

Microservices are a software development technique — a variant of the service-oriented architecture architectural style that structures an application as a collection of loosely coupled services. In a microservices architecture, services are fine-grained and the protocols are lightweight

# Before starting:

- Know the advantages and disadvantages of microservices.
- Avoid disastrous mistakes.
- Make better technological decisions regarding microservices.

**When selecting a technology for a microservice, it’s recommended to consider:**

- Maintainability
- Fault-tolerance
- Scalability
- Cost of architecture
- Ease of deployment

**Some examples of frameworks/ technologies team uses for microservices:**

- Scrapy for web crawling
- Celery + RabbitMQ to communicate the microservices

This definition includes three microservice design principles:

- *Single purpose* — each service should focus on one single purpose and do it well.
- *Loose coupling* — services know little about each other. A change to one service should not require changing the others. Communication between services should happen only through public service interfaces.
- *High cohesion* — each service encapsulates all related behaviours *and data*together. If we need to build a new feature, all the changes should be localized to just one single service.

# Microservices Best Practices

1. Keep Independent and loosely coupled Microservices
2. Try to Reach the Glory of REST
3. Use Distributed Configuration
4. Using Spring HATEOAS. This helps you use navigable, restful APIs.
5. Monitor everything and Logging
6. Application performance management(APM). This collects extra details to help you troubleshoot issues. [Zipkin](https://zipkin.io/)
7. Continuous Delivery
8. API gateways to aggregate data to specific clients.
9. Event Sourcing and CQRS (Command and Query Responsibility Segregation)