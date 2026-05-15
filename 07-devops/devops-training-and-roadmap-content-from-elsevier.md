# Devops training and Roadmap content from Elsevier

# **How to use this guide**

As you might have noticed, the contents of this guide is organised in the form of checklists and this is done on purpose so that you could copy this page to your personal space in confluence and go over the topics in your own pace by researching the proposed questions and ticking the boxes. You don’t have to stick to the order of the topics on this page, but [DevOps](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#DevOps) is a good place to start for understanding the overall challenge and how not to feel overwhelmed about it.

As you will learn from reading about DevOps “onion”, it has many layers and tools being only one of the layers. And for you to be effective in your role and able to come up with better solutions to the problems we face, you need to have basic understanding of all of the DevOps layers. Each chapter is labeled with one or more of the DevOps “layers”, supplemented with a “hands-on“ label to mark chapters that involve some practical exercises:

Please don’t feel discouraged by the number of tools to learn, you are likely to work only with a subset of them and you can learn them gradually.

---

# **Navigation**

- [How to use this guide](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#How-to-use-this-guide)
- [Navigation](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Navigation)
- [DevOps](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#DevOps)
- [Agile](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Agile)
- [Automation](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Automation)
    - [Infrastructure as code (IaC)](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Infrastructure-as-code-(IaC))
    - [Configuration as code (CasC)](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Configuration-as-code-(CasC))
    - [Version control and release management](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Version-control-and-release-management)
    - [CI/CD](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#CI%2FCD)
    - [GitOps](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#GitOps)
    - [Self-service](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Self-service)
- [Computational platform](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Computational-platform)
- [Operations](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Operations)
- [Site Reliability Engineering (SRE)](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Site-Reliability-Engineering-(SRE))
- [Investigating issues](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Investigating-issues)
- [Debugging](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Debugging)
- [Standards and compliance](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Standards-and-compliance)
- [TPR process](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#TPR-process)
- [Software engineering](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Software-engineering)
- [Testing](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Testing)
- [Software architecture](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Software-architecture)
- [Command line and shell scripting](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Command-line-and-shell-scripting)
- [Managing local credentials](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Managing-local-credentials)
- [SSH keys](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#SSH-keys)
- [TLS](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#TLS)
- [Core technologies](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Core-technologies)
    - [GitHub](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#GitHub)
    - [Terraform](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Terraform)
    - [Packer](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Packer)
    - [Ansible](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Ansible)
    - [Jenkins](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Jenkins)
    - [NewRelic](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#NewRelic)
    - [Kubernetes](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Kubernetes)
    - [Docker](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Docker)
    - [ElasticSearch and OpenSearch](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#ElasticSearch-and-OpenSearch)
    - [Kafka](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Kafka)
    - [Active Directory](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600980191351/DevOps+Training#Active-Directory)

# **DevOps**

Mindset & Values

- [ ]  [DevOps: Peeling the onion](https://stefanvanoirschot.medium.com/devops-peeling-the-onion-7d92245ce343)
- [ ]  What problem does DevOps solve?
- [ ]  [How I learn new technologies as a DevOps Engineer (without being overwhelmed 👏)](https://dev.to/techworld_with_nana/how-i-learn-new-technologies-as-a-devops-engineer-without-being-overwhelmed--495e)
- [ ]  The Phoenix Project [Percipio](https://relx.percipio.com/books/ed14e1f6-0916-48f5-9cdd-ce5ad2d91737)
- [ ]  [More Than Just Dev & Ops](https://relx.percipio.com/courses/c211ce5f-a06d-4ce2-a48b-3c78c60beef7), [Optimizing Flow](https://relx.percipio.com/courses/e9c89c2a-a9af-431a-8fa1-98d09c713607), [Amplifying Feedback](https://relx.percipio.com/courses/f265226d-2cb9-436b-abe0-41b0a082a104)

# **Agile**

Principles & Practices

- [ ]  [Manifesto for Agile Software Development](https://agilemanifesto.org/)
- [ ]  Agile ceremonies and their purpose
- [ ]  What are some of the agile metrics and how they could be useful?
- [ ]  Leading the Transformation: Applying Agile and DevOps Principles at Scale [Percipio](https://relx.percipio.com/audiobooks/0980de46-c7bf-42a5-a83d-f50b15b04983?i=11)

# **Automation**

## **Infrastructure as code (IaC)**

- [ ]  Advantages of IaC
- [ ]  What tools for managing IaC are there?
- [ ]  What are some of the good practices that apply for managing IaC?

## **Configuration as code (CasC)**

- [ ]  What is good in writing configuration as code?
- [ ]  What tools are there for configuration management?
- [ ]  Ansible vs Puppet vs Chef. Pros and cons of each tool. When to choose one over another?
- [ ]  What are some of the good practices that apply for managing configuration as code?

## **Version control and release management**

- [ ]  What is a version control system? What is the purpose of version control?
- [ ]  What version control systems do you know?
- [ ]  Different types of git workflows: [5 Different Git Workflows](https://medium.com/javarevisited/5-different-git-workflows-50f75d8783a7)
- [ ]  Conventional commits [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

## **CI/CD**

- [ ]  What is the difference between Continuous Integration, Continuous Delivery and Continuous Deployments?
- [ ]  What tools exist for CI/CD?
- [ ]  What can serve as a trigger for a CI/CD process?
- [ ]  How CI/CD process is defined? What are the building blocks?
- [ ]  How does the orchestration of CI/CD workflows and their parts managed?
- [ ]  Where CI/CD workflows are executed? How do you define and manage runner nodes?
- [ ]  How CI/CD workflow parallelisation is achieved?

## **GitOps**

- [ ]  What is GitOps?
- [ ]  What tools can be used to implement it?
- [ ]  What tools enforce GitOps approach?

## **Self-service**

- [ ]  What is an internal developer platform (IDP)? What advantages does it provide?
- [ ]  Learn about [Cortex](https://elsevier.atlassian.net/wiki/spaces/TIOCORTEX) and the problems it is addressing

# **Computational platform**

Principles & Practices

Tools

- [ ]  Cloud technology and its benefits
- [ ]  What cloud providers do you know?
- [ ]  What are the alternatives to public cloud?
- [ ]  What is virtualisation?
- [ ]  What is the difference between bare metal, virtual machine and container?
- [ ]  Orchestration and scheduling tools and how they can benefit you?

# **Operations**

- [ ]  What is SLO, SLA and SLI? What is the purpose of each?
- [ ]  What is observability and why is it important?
- [ ]  What is the purpose of monitoring and alerting? Some of the good and bad practices for monitoring and alerting?
- [ ]  Incident management best practices
- [ ]  What is ITIL?
- [ ]  Operations Anti-Patterns, DevOps Solutions, read [Percipio](https://relx.percipio.com/books/59950cb9-3b03-481d-9e61-8be1c8f18f10)  or listen [Percipio](https://relx.percipio.com/audiobooks/3084d1ec-1697-4ee6-b2fe-176138a42cf9)

# **Site Reliability Engineering (SRE)**

- [ ]  SRE by Goole: [https://sre.google/books/,](https://sre.google/books/,) read online [Google SRE - Site reliability engineering book Google index](https://sre.google/sre-book/table-of-contents/)
- [ ]  The DevOps Handbook, read [Percipio](https://relx.percipio.com/books/bcf66220-f40b-11e6-b0e2-0242c0a80804)  or listen [Percipio](https://relx.percipio.com/audiobooks/f80a2014-dc74-4315-a85d-654c251f5f51)
- [ ]  In your functional area, pick one service and try answering these questions:
1. What is our promise to customer? (SLOs and SLAs)
2. How do we know if we are not breaking it? (SLIs)
3. What do we do about it? (error budgets, release management, application design...)

# **Investigating issues**

Processes & Standards

- [ ]  Learn and practice investigating technical issues. Below is an example of how one could approach for doing investigations:
1. Avoid making assumptions and guesses if possible. Base your decisions on data.
2. Was there and alarm triggered? What caused the alarm?
3. Find corresponding log messages. Read them and understand. Classify the error. Is it a programming error, permissions error, connectivity error, resource usage error?
4. What components of the system are unhealthy or failing? Consider checking health checks, New Relic monitoring, application logs in the logging system, system logs.
5. Were there any recent changes made to the system? Consider checking release markers in New Relic, GitHub commit history. Consider possibility of a manual change outside of IaC workflow.
6. Can the issue be reproduced? Can it be reproduced in another environment? Can it be reproduced when executed locally? What is different between those environments?
7. Is the failure caused by a known issue? Did someone else encounter a similar issue in the company/community? How did they solve the issue?

# **Debugging**

Hands-on

- [ ]  Learn and practice debugging. Below is an example of how one could approach for debugging:
1. Find the place where it fails. Find the error trace from this point.
2. What does the error say? Read and understand the message.
3. Classify the error. Is it a programming error, permissions error, connectivity error, resource usage error?
4. Can the error be reproduced? Can the error be reproduced in another environment? Can it be reproduced when executed locally? What are the differences between those environments? Is there any difference in deployed versions? Is environment misconfiguration at fault?
5. If the behaviour of the system is not straightforward, consider enabling lower level logs and try deriving the reason for failure from the preceding messages.
- [ ]  Practice troubleshooting. [SadServers - Linux & DevOps Troubleshooting Interviews](https://sadservers.com/scenarios)

# **Standards and compliance**

- [ ]  What is good in having and following defined standards?
- [ ]  What company standards are defined for your functional area? Where can you find them?
- [ ]  When do you need to follow defined standards?
- [ ]  How to ensure compliance with defined standards?
- [ ]  What are the advantages of using standard tooling? [Service Catalog](https://backstage.elsevier.net/catalog?filters%5Bkind%5D=component&filters%5Btags%5D=tag-inclusion%3Aand&filters%5Buser%5D=all)

# **TPR process**

- [ ]  What is Technology Project Review (TPR)?
- [ ]  What stages does BTS TPR process have?
- [ ]  [TPR Process](https://elsevier.atlassian.net/wiki/spaces/arch/pages/87665680378)
- [ ]  What tools exist to assist one in doing a TPR? [TPR Template](https://elsevier.atlassian.net/wiki/spaces/arch/pages/89741174999)

# **Software engineering**

- [ ]  What is DRY?
- [ ]  Immutability and immutable release artifacts
- [ ]  What is an idempotent operation and why idempotence is important for managing IaC and CasC?
- [ ]  SOLID & GRASP [Percipio](https://relx.percipio.com/courses/92e77c53-14c0-11e7-92d9-0242c0a80b07/videos/92e7a36f-14c0-11e7-92d9-0242c0a80b07)
- [ ]  What is declarative approach?
- [ ]  What is desired state? Give some usage examples
- [ ]  What is the difference between stateless and stateful applications? Application state management
- [ ]  What is an interface? Advantages of well defined interfaces
- [ ]  OOP vs functional programming. Pros and cons. When to use one over another?
- [ ]  What is and API. Give examples. Do you know any Web API design best practices?
- [ ]  Design patterns [Design Patterns and Refactoring](https://sourcemaking.com/design_patterns)

# **Testing**

- [ ]  Software quality assurance. Testing pyramid. Shifting left.
- [ ]  Types of testing. Unit tests. Contract tests. Integration tests. User acceptance tests or end to end tests. Manual tests. A/B or split testing.
- [ ]  Code coverage. Quality gates.
- [ ]  Strategies for testing infrastructure. What and why could be tested in IaC?
- [ ]  [Testing HashiCorp Terraform](https://www.hashicorp.com/blog/testing-hashicorp-terraform)
- [ ]  IaC testing tools, e.g. terratest, InSpec Packer provisioner, etc.

# **Software architecture**

- [ ]  [Ultimate AWS Certified Solutions Architect Associate 2022](https://relxlearning.udemy.com/course/aws-certified-solutions-architect-associate-saa-c02/)
- [ ]  What application can be considered scalable? How to ensure application scalability?
- [ ]  What defines application availability? How to ensure high availability of an application?
- [ ]  [Elsevier Hosting Tiering Model Standard](https://elsevier.atlassian.net/wiki/spaces/arch/pages/87651888533)
- [ ]  What impacts application performance?
- [ ]  Study examples of infrastructure design diagrams for Elsevier applications. How to they translate into infrastructure as code?
- [ ]  Microservices vs monolithic applications
- [ ]  Distributed applications
- [ ]  What is a cluster? Give some examples of cluster applications?
- [ ]  Event-based systems
- [ ]  What is ETL?
- [ ]  [System Design — SQL vs NoSQL](https://medium.com/must-know-computer-science/system-design-sql-vs-nosql-4cdfb9f53d69)
- [ ]  Coupling and cohesion

# **Command line and shell scripting**

- [ ]  getting command help
- [ ]  checking command man pages
- [ ]  learn to use commands `cat`, `tail`, `less`, `more`
- [ ]  what command line text editors exist for linux? Learn how to edit a text file in `vim`, how to search for a string, how to delete a whole line, how to undo the last change, how to enter and exit "insert" mode, how to exit editor with or without saving changes to the file.
- [ ]  `chmod` and linux file permissions
- [ ]  learn `mkdir`, `touch`, `rm`
- [ ]  redirecting command output to a file, appending and rewriting the content on an existing file
- [ ]  pipe, `grep` and `sort`
- [ ]  `jq`
- [ ]  how to view, set and unset environment variables
- [ ]  learn about `.bashrc`, `.bash_profile`, `.profile`, `.zshrc`
- [ ]  learn about `source` and `.` command
- [ ]  declaring custom user functions

# **Managing local credentials**

- [ ]  AWS credentials file, saml2aws
- [ ]  Kubeconfig

# **SSH keys**

What are SSH keys?

- [ ]  How to generate a new ssh key pair?
- [ ]  How do ssh key pairs work?
- [ ]  Provide some example use cases for ssh keys in our infrastructure?
- [ ]  Managing multiple ssh keys locally, `ssh-add` command and its options.
- [ ]  learn about `aws ec2 instance connect` and how to use it

# **TLS**

What is TLS?

- [ ]  Why should I care about TLS?
- [ ]  How does TLS work?
- [ ]  What is a CA?
- [ ]  What is Amazon ACM?

# **Core technologies**

**GitHub**

how does a distributed version control system work? What is git remote and origin? What is a local repo in git?

- [ ]  working with git. Clone, pull, commit, push, merge, tag...
- [ ]  git config and global config. Where is git configuration stored?
- [ ]  `.gitignore` file, what can you put in it? how to ignore 1 file, a directory or multiple files matching a pattern?
- [ ]  Resolving merge conflicts
- [ ]  pre-commit and other git hooks [Git - githooks Documentation](https://git-scm.com/docs/githooks)
- [ ]  GitHub webhooks and events. How to create a GitHub repository webhook and link it to your Jenkins server
- [ ]  Access permissions on GitHub. Repository roles, teams, organisations.

# **Terraform**

Why DBS TIO has made Terraform its tools of choice for infrastructure provisioning?

- [ ]  Terraform cli. Terraform init, plan, apply, import, targeted apply
- [ ]  What is terraform state? Setting up remote backend
- [ ]  Working with different terraform versions, `tfswitch`
- [ ]  Setting version constraints in terraform [Version Constraints - Configuration Language | Terraform | HashiCorp Developer](https://www.terraform.io/language/expressions/version-constraints)
- [ ]  What is the purpose of `.terraform.lock.hcl` files? [Dependency Lock File (.terraform.lock.hcl) - Configuration Language | Terraform | HashiCorp Developer](https://www.terraform.io/language/files/dependency-lock)
- [ ]  What is terraform provider? aws provider, newrelic provider, helm provider...
- [ ]  What is terraform module? How do you go about creating your own terraform module?
- [ ]  How can you generate documentation from terraform modules? How can you embed it in a certain place on your README page? Learn about `terraform-docs` command.
- [ ]  How can you make your terraform code DRY? Leveraging the power of `.tfvars` files
- [ ]  [Service Catalog (Deprecated) | ServiceCatalog(Deprecated) Terraform](https://elsevier.atlassian.net/wiki/spaces/TIOCE/pages/53241059003#ServiceCatalog(Deprecated)-Terraform) Use one of the Core Engineering terraform modules to provision infrastructure
- [ ]  Practice: [https://github.com/elsevier-bts/terraform-ta-training](https://github.com/elsevier-bts/terraform-ta-training)

# **Packer**

What Packer is made for?

- [ ]  [Getting started configuring Packer with HCL2 files | Packer | HashiCorp Developer](https://www.packer.io/guides/hcl)
- [ ]  Learn about different Packer provisioners
- [ ]  When writing Packer templates, when should I use Ansible over shell script and vice versa?

# **Ansible**

- [ ]  What Ansible is made for?
- [ ]  Why Ansible is the tool of choice in DBS TIO? How does it compare to its rivals?
- [ ]  What is task, role and playbook?
- [ ]  Where can you find Ansible documentation?
- [ ]  Does the structure of the directory with your Ansible code matter?
- [ ]  What are some of the good practices for writing Ansible playbooks?
- [ ]  Where can you put variables, templates and ordinary files for copying to the target host?
- [ ]  Control execution flow with conditionals, iterators and tags
- [ ]  How can you define role dependencies and handlers?
- [ ]  Learn about Ansible facts
- [ ]  Ansible configuration file and inventory
- [ ]  Ansible core modules and Ansible Galaxy
- [ ]  Learn about parallel execution in Ansible
- [ ]  How can you debug your Ansible code?

# **Jenkins**

- [ ]  What is Jenkins and why we use it over other tools?
- [ ]  What are some of the Jenkins alternatives and their advantages and drawbacks?
- [ ]  Jenkins Declarative Pipeline
- [ ]  Jenkins CasC plugin
- [ ]  Jenkins shared libraries
- [ ]  Jenkins jobs DSL
- [ ]  Managing secrets in Jenkins
- [ ]  Managing nodes and clouds in Jenkins
- [ ]  Core Engineering module for managing Jenkins deployment
- [ ]  Plugin management in Jenkins
- [ ]  Jenkins good practices

# **NewRelic**

[https://learn.newrelic.com/](https://learn.newrelic.com/)

- [ ]  TIO Tools Engineering page: [New Relic](https://elsevier.atlassian.net/wiki/spaces/TIOCE/pages/62977852939)
- [ ]  Learn about [New Relic Provider](https://registry.terraform.io/providers/newrelic/newrelic/latest/docs) in Terraform.
- [ ]  CE terraform modules [https://github.com/elsevier-centraltechnology/core-terraform-newrelic-monitoring](https://github.com/elsevier-centraltechnology/core-terraform-newrelic-monitoring)Connect your Github account

# **Kubernetes**

- [ ]  `kubectl`
- [ ]  `helm` and helm provider for Terraform. CE terraform modules for provisioning helm charts
- [ ]  `k9s`

## **Docker**

[Container Training](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/90792966693)

- [ ]  [Docker Useful Hacks](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600987410159)
- [ ]  [Docker & Ansible configuration - MAC](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119600978664635)

## **Elastic Search and OpenSearch**

What is Elasticsearch? What advantages does ElasticSearch provide?

- [ ]  Managed vs self-managed Elasticsearch deployments. How AWS Opensearch is different from Elasticsearch?
- [ ]  What is ELK stack? Lean about the role of each component in this stack

# **Kafka**

What is Apache Kafka?

- [ ]  What is the main purpose of having Kafka in your system? What problem does this tool solve?
- [ ]  Apache Kafka architecture and its components, basic concepts, brokers, producers, consumers, topics and offsets.
- [ ]  What is Zookeeper and what is its purpose in Kafka cluster?
- [ ]  How does Kafka ensure resiliency and fault tolerance? How does it maintain high availability of data? What is replication factor?
- [ ]  Kafka performance. What is the purpose of data partitions in Kafka?
- [ ]  Generating and running partition assignments. What does each procedure do?
- [ ]  What does preferred replica election do? What is a partition leader in Kafka?
- [ ]  What is managed Kafka service?
- [ ]  Learn about AWS Kinesis
- [ ]  What are some of the alternatives to Kafka (managed or self-hosted)? Can you build an event streaming platform without Kafka?

# Active Directory

What is Active Directory?

- [ ]  What process should you follow for making/requesting AD changes in our company?

# Container Training

### **Stage 1.**

I don't know anything about containers. What are they? To find out first head over to Udemy and take the introduction course to Containers and Docker.

[Docker for the Absolute Beginner - Hands On - DevOps](https://relxlearning.udemy.com/course/learn-docker/)

### **Stage 2.**

So you know what Docker is now? Ok. Try looking at Kubernetes. Here’s an intro and admin course. The admin course It’s long but it has ALL the useful info that K8S admins need to get certified

[https://relxlearning.udemy.com/course/learn-kubernetes/learn/lecture/9723214#overview](https://relxlearning.udemy.com/course/learn-kubernetes/learn/lecture/9723214#overview)

[https://relxlearning.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/learn/lecture/15670780#overview](https://relxlearning.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/learn/lecture/15670780#overview)

### **Stage 3.**

K8S understood you can take a look at EKS, AWS own managed K8S service. The control plane is managed but worker nodes are still yours to configure and deploy to.

[https://aws.amazon.com/eks/getting-started/](https://aws.amazon.com/eks/getting-started/)

[AWS re:Invent 2017: NEW LAUNCH! Introducing Amazon EKS (CON215)](https://youtu.be/WHTejF3W0s4)

[AWS re:Invent 2017: Deep Dive into Amazon EKS (CON409)](https://youtu.be/vrYLrx-a_Wg)

### **Stage 4.**

Cortex - what is it providing? How does it change what we would do as engineers?

What are the Core team taking responsibility for?

What’s coming next and how? Roadmap

[Cortex](https://elsevier.atlassian.net/wiki/spaces/TIOCORTEX/pages/89737119120)

And they are working on an onboarding guide to help teams gain familiarity and get onto the platform

[Cortex Onboarding Journey](https://elsevier.atlassian.net/wiki/spaces/TIOCORTEX/pages/90793077030)

### **Stage 5.**

Embedded SRE / DevOps for CWS. What would I be doing? Taking responsibility for what?

Deployments?  CI/CD, Sizing, Capacity Planning, Performance, Monitoring

< Scott TBD>

CWS Cortex Clinic for TIO BTS.  Drop in sessions

# AWS related quuestions

**Region:** Is this a multi-region or single region deployment? What is a region in AWS? Could you name regions shown in this diagram?

- [ ]  **VPC:** How many VPCs are shown in the diagram? Name them. What is a VPC in AWS? Find some examples in `elsevier-bts`/ `elsevier-centraltechnology` / `your org space` IaC repositories for creating VPCs using terraform.
- [ ]  **AZ:** How many availability zones are used to provision such components as EC2s, Varnish, MariaDB RDS?.. What is an availability zone in AWS? What is the reason for spreading infrastructure across multiple AZs?
- [ ]  **Subnet:** Why does each AZ have its own private and public subnet? What is the difference between VPC and subnet? What is subnet in cloud? What is the difference between private and public subnet? What resources in this diagram are provisioned in private subnets and what is in public subnets? What is the reason for this?
- [ ]  Find IaC examples for provisioning private and public subnets using terraform.
- [ ]  **Hosted Zones:** How many hosted zones are shown in this diagram? What is a hosted zone in AWS? Find IaC examples for provisioning a hosted zone using terraform.
- [ ]  **Internet Gateway:** How is the internet traffic routed to this VPC? What needs to be attached to the VPC to enable resources in this VPC to send and receive traffic from the internet? What is an Internet Gateway? Find examples where Internet Gateway is created using terraform (in CE tf modules).
- [ ]  **Route Tables:** What else ends to be in place for the traffic to find the route in and out of your VPC subnets? What is a route table? Find examples in terraform code where we create AWS route tables.
- [ ]  **Gateways:** What do you need to have in place to allow instances with no public IPs to access the internet? What is the difference between a NAT Gateway and Internet Gateway?
- [ ]  **Cloudflare:** What is Cloudflare and what is it used for? How could one get access to Cloudflare console in DBS-TIO?
- [ ]  **Direct Connect:** How is the traffic originating from Elsevier network routed to this VPC? What is Direct Connect?
- [ ]  What is used to balance traffic load amongst instances according to this diagram?
- [ ]  **Security Groups:** How many security groups do you see in this diagram> What is a security group in AWS? What is SG used for? What components have their own security group? Why is that? Examine the accompanying table listing Security Groups. What can you say about the defined SG access rules?
- [ ]  **Database:** How would you approach provisioning a certain component from this diagram, for example, MariaDB RDS? Is there a CE terraform module available for provisioning RDS? Explore [Service Catalog (Deprecated) | ServiceCatalog(Deprecated) Database](https://elsevier.atlassian.net/wiki/spaces/TIOCE/pages/53241059003#ServiceCatalog(Deprecated)-Database) . What tf module has your team used for provisioning RDS in other product areas?

AWS Elastic search
[https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119601063457314/ElasticSearch+AWS+OpenSearch](https://elsevier.atlassian.net/wiki/spaces/TIOCDT/pages/119601063457314/ElasticSearch+AWS+OpenSearch)

                                                       Interview Questions and there answers

DevOps Engineer Team Lead Interview
Technical Assessment/Project
I am a CEO starting a new company and I own a large amount of cat pictures as well as hat pictures.
I want the service to work as follows:
• A user goes to my website, chooses a cat picture, chooses a hat picture
• We process these two things and create a picture of a cat wearing a hat
Keep in mind:
• Security
• Different environments
• Costs
• Scalability (team growth and user growth)
Please provide:

1. Architectural schema
2. CICD pipeline diagram for the app to be deployed
Get ready to describe and discuss both items during the inteview

- Can you explain your understanding of CI CD?
    - What tooling have you used?
    - How have you used x or y to build automation in to your environments?
- Talk me through your experiences of creating infrastructure as code, what tooling have you used? What challenges have you encountered?
- What cloud providers have you experience with? What are their pros and cons? What did you like best about x cloud?
- Thinking about operating systems, can you describe your experiences with various operating systems? How would you troubleshoot a memory issue on a Windows server?
- Describe a highly available, resilient web application architecture - think about standard compute (ec2, physical servers etc) as opposed to using a K8’s service.
- What benefits does K8s offer? Describe a use case and a deployment architecture
- Tell me about a time you worked as part of a team to deliver a critical project / resolve a major application or service outage?

## **INTERVIEW QUESTIONS**

1. Can you explain your understanding of CI CD? What tooling have you used?
    1. You can follow this up by asking if the tool was an architectural / organisational choice or their preference
    2. How / why did you use this tool
    3. What are the benefits of effective CI / CD
2. Talk me through your experiences of creating infrastructure as code, what tooling have you used? What challenges have you encountered?
    1. How did you structure your terraform / codeformation?
    2. How was drift managed?
3. Terraform - write some code to launch multiple EC2 instances across multiple AZs?
4. Write me some ansible to install a binary

**SECTION 2: Operating Systems, applications, infrastructure**

## **INTERVIEW QUESTIONS**

1. What cloud providers have you experience with? What are their pros and cons? What did you like best about x cloud?
2. Thinking about operating systems, can you describe your experiences with various operating systems? How would you troubleshoot a memory issue on a Windows server?
3. Describe a highly available, resilient web application architecture - think about standard compute (ec2, physical servers etc) as opposed to using a K8’s service.
4. What benefits does K8s offer? Describe a use case and a deployment architecture
5. Tell me about a time you worked as part of a team to deliver a critical project / resolve a major application or service outage?
6. Have you mentored any junior engineers? How did you approach their development? What tools or skills did you employ to help them on their journey?

# TA screening questions

The TA team can use these questions to help filtering candidates before the CV's are submitted for review in WorkDay.

| Level | Key Skills | **Question** | **Expected answer** |
| --- | --- | --- | --- |
| Easy | AWS | On AWS, how can an instance hosted in a private subnet be provided with outbound internet access? | NAT gateway (AWS service managed) and/or
Proxy (EC2 instance AWS unmanaged) |
| Easy | Networking | In DNS, what’s the difference between an “A” record and a CNAME record? | An “A” record points a name to an IP. “CNAME” points a name to another name (or hostname) |
| Easy | Terraform | In Terraform if you are working with other colleagues what is important about the terraform state? | Terraform state should be stored in S3 or some other highly resilient and shared storage. It should not be committed to source control or only stored locally. |
| Easy | Linux | How would I check memory and on a server | One of these commands: free, top, sar, iostat |
| Easy | Linux | If you’re writing a bash script, how can you get the number of cpu cores a server has? | /proc/cpuinfo |
| Easy | Linux | How can I check the disk space on a server | One of these commands: df, du |
| Easy | Linux | In linux, how do you check if previously executed command is successful | exit status or echo $? is 0 |
| Medium | Terraform | How do you create Multiple Resources of similar type in terraform | Using count |
| Easy |  | How do you check all running process in linux | ps, htop, top |
| Medium |  | How to manage pre-existing resource with terraform, which was not created by terraform | terraform import |
| Medium |  | what is the difference between security group and NACL in AWS | Security group controls both inbound and outbound traffic at the instance level and NACL controls both inbound and outbound traffic at the subnet level. |
| Easy |  | How do you convert a folder to git folder | git init |
| Medium |  | How do you check open ports in linux | netstat, lsof, nc, ss, nmap |

# Networking

| Level | **Question** | **Expected answer** | **Bonus points** |
| --- | --- | --- | --- |
| Easy | Explain in much detail what happens when you curl [https://elsevier.com](http://elsevier.com/) in your browser? | • DNS resolving
• TCP connection
• SSL/TLS connection
• HTTP protocol and methods | • TCP handshake syn, ack, syn+ack…
• SSL/TLS handshake negotiate ciphers, CA
• if candidate can describe how to get a page using telnet: GET / HTTP/1.[01]\nHost: [elsevier.com](http://elsevier.com/)\n\n
• http → https 301 permanent or 302 temporary redirect or meta refresh on .html |
| Medium | What’s does a /24 on a subnet means? | • it’s subnet mask that contains 255 IP addresses
• it can be written as 255.255.255.0
• it starts with a .0 and ends with a .255. | • How it can be sliced. Per example it fits 2 x /25 or 4 x /26.
• If the candidate goes into binary notation. |
| Hard | Explain the differences between stateless and stateful firewall. | • stateless is when you don’t track retries. you have to ALLOW both ingress and egress
• stateful firewall will keep a connection tracking table that when a connection is made, it will allow returning traffic without having to specify. | • iptables conntrack
• maximum conntrack entries and connections being dropped |

# AWS

| Level | **Question** | **Expected answer** | **Bonus points** |
| --- | --- | --- | --- |
| Easy | Tell me about load balancing on AWS?
How many types of load balancer are there?
Which layers of the OSI stack do they operate on?
What is cross-zone load balancing? | • Health check
• Classic Load balancer - layer 4
• Network load balancer - layer 4
• Application load balancer - layer 7
• Gateway load balancer - layer 3 gateway + layer 4 load balancing
• When enabled, distributes traffic evenly across instances across different AZs | • SSL certificate management, automated rotation
• ALB with target group and virtual host. [www.elsevier.com](http://www.elsevier.com/) , [api.elsevier.com](http://api.elsevier.com/) send requests to different target groups |
| Easy | What benefit do you get from an auto-scaling group with a sizing of 1? | • Automatic instance replacement when health check is failing | • Custom health check on ASG that will set instance to Unhealthy: aws autoscaling set-instance-health --instance-id i-123abc45d --health-status Unhealthy |
| Easy | What is the relationship between region and AZ? | • AWS Regions are large and widely dispersed into separate geographic locations.
• Availability Zones are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones. | • Cost is different for different regions, like Brazil São Paulo is more expensive than US Virginia.
• Cross region traffic cost |
| Easy | How can an instance hosted in a private subnet be granted outbound internet access? | NAT gateway (AWS service managed) and/or proxy (ec2 instance AWS unmanaged) | Explain why NAT gateway is better because it’s managed by AWS. |
| Easy | What’s the difference between an IAM Role and IAM User? | IAM Role have an ARN that can be attached to AWS resources. IAM User have access and secret keys that needs to be shared. | Inside AWS resources, it should only use IAM Role because IAM User credentials can be leaked. |
| Easy | How do you allow an EC2 instance access to an S3 Bucket with read only permissions? | Create an IAM Role, attach an S3 read only policy and attache the IAM Role to the EC2 instance. | What about if the S3 bucket was in another account?
Preferably bucket policy |
| Easy | Using aws cli, how do you list all instances. | aws ec2 describe-instances |  |
| Medium | I am logged into an EC2 instance via ssh, how can I retrieve information regarding things such as instance id, ami without exiting the instance? | Curl/wget instance meta data | curl http://169.254.169.254/latest/meta-data |
| Medium | In AWS what is user-data (hint it is related to EC2) | When an EC2 instance is launched you can pass it user data which can be used to perform common automated configuration tasks or scrips when an instance starts. Can be a shell script or cloud-init directives |  |
| Medium | In EC2 cloudwatch what is the difference between instance and system status check? | System status checks monitor the AWS systems on which the instance runs - physical host problems, power, network connectivity. Generally fixed by AWS or can be fixed by doing a stop and start which should bring the instance up on a different physical host
Instance status checks monitor the software and network configuration of the individual instance - startup config, exhausted memory, corrupt file system, incompatible kernel. Generally fixed by the user by restarting the instance or making configuration changes |  |
| Medium | Explain how I would do a restore on an RDS instance? | Restore a snapshot
This will restore the RDS instance so it will need to be named uniquely
Route53 does not charge for alias queries to AWS resources, it will charge for CNAME queries | Having a new instance could cause a lot of changes in code etc, how could this be avoided? CNAME pointing to the DB, then you just need to change the CNAME to point to the new instance |
| Medium | Explain how you can save money in AWS | • Savings Plan, Reserved Instances, Spot instances
• Right sizing of servers - over spec'd servers
• Leveraging newer instances types M5 instead of M3 because is newer hardware for the same price
• stopping Dev environments when not in use
• GP2 → GP3 volumes
• S3 bucket lifecycle rules to move to glacier or lower cost storage classes
• use Trusted Advisor! | • Housekeeping of stale unused resources - unattached EBS, redundant ELB's, old Snapshots
• lambda function scheduled to stop dev environments outside business hours
• ARM instances are lower cost, but he needs to explain is a different architecture that would require application to be made for it |
| Hard | Explain the difference between Security Groups and Network ACLs?
Which components can they be applied to?
Explain which of them is stateful, and stateless? | • Security Groups are for EC2, ELBs, RDS
• Network ACLs for Subnets only | • Security Groups Stateful: Egress traffic associated with ingress traffic is automatically permitted.
• Network ACLs Stateless: return traffic needs to be whitelisted. |
| Hard | For an instance hosted in a private subnet which makes heavy use of S3, how might I be able to save on NAT gateway costs? | Create a VPC endpoint for S3 | What type of VPC endpoint for S3 - gateway.
Describe VPC endpoint types:
• Gateway - for S3 or DynamoDB, there is no charge for these
• Interface - ENI with a private IP address from the IP address range of your subnet. Point at AWS services
• Gateway Load Balancer service - ENI with a private IP address from the IP address range of your subnet. Servers to intercept and route traffic to a network or security service a customer has configured with a Gateway Load Balancer |
| Hard | In AWS what is an Alias record in route53 | Alias records let you route traffic to selected AWS resources
Unlike a CNAME record you can create an alias record at the top node of a DNS namespace / zone apex | Name some AWS resources you can use an Alias on:
• Load balancer
• Cloudfront
• S3 bucket
• API gatweway
• VPC interface endpoint
• Elastic beanstalk
• Another route53 record in the same hosted zone
• AWS Global Accelerator |

# Terraform

| Level | **Question** | **Expected answer** | **Bonus points** |
| --- | --- | --- | --- |
| Easy | What is a Terraform module? | A collection of Terraform resources that can be deployed in a repeatable way. | Where the modules can be stored?
Mention modules versioning using git tags and/or branches per example. |
| Easy | What is a Terraform state? | Terraform state is terraform's view of the world. It is a text file written in JSON. | • Where it’s stored and best practices (not storing locally)
• How would we stop two people running at the same time
    ◦ Locking via DynamoDB |
| Easy | What is a provider? | Plugins that interact with cloud providers, SaaS providers and other APIs |  |
| Medium | I have written a module and have some outputs, what are these and what would I use them for | • Provide information about infrastructure at end of run or omn command line
• Output may be required in subsequent resources/modules and it controls the program flow |  |
| Medium | How can I ensure runs are consistent across different machines at different times? | Tie down versions (at least major version) of:
• Terraform client
• Terraform providers
• Terraform modules |  |
| Medium | Suppose I already had existing resources how could I enroll them into the terraform state | • Write code for the resource
• Use terraform import <resource> <id> |  |
| Hard | If I wanted to remove something from terraform control but leave the resources in place how would I do this | • terraform state rm <resource>
• Remove code for resource |  |
| Hard | Suppose I have a resource in the state "aws_instance" "nonprod" and wanted to change it to "aws_instance" "prod" how would I do this | terraform state mv aws_instance.nonprod aws_instance.prod |  |
| Hard | What is count used for | Create a specific number of resources
Can be used to conditionally create resources | Why you would use for_each instead:
• If some arguments require distinct values
• Named indexing i.e. aws_s3_bucket["bucket_name"] as opposed to aws_s3_bucket[0] etc |
| Hard | What is the splat expression | A more concise way to express a common operation that could otherwise be performed with a for expression (e.g aws_instance[*].instance_id) |  |

# Linux / Troubleshooting

| Level | **Question** | **Expected answer** | **Bonus points** |
| --- | --- | --- | --- |
| Easy | How can I log into a server without password authentication? | • generate a key using ssh-keygen
• a private and a public key is created
• you send the public key to the server and store it in ~/.ssh/authorized_keys |  |
| Easy | Give two examples of some environment variables and what do they mean? | • $HOME
• $OLDPWD
• $PATH
• $PWD
• $USER | More than 4 environment variables. |
| Easy | You have an EC2 instance, and you created an EBS volume and attached to it. How do you format, mount and how can it survive a reboot? | • mkfs.ext4 /dev/sda
• mount /dev/sda /mnt/backup
• add to /etc/fstab |  |
| Medium | What is a umask | Controls how file permissions are set for newly created file |  |
| Medium | What is an inode | An inode is a file data structure that stores information about any Linux file except its name and data. |  |
| Medium | What command would you use to tune a linux kernel | sysctl | How to make this persistent
sysctl -p
Write to sysctl.conf |
| Medium | What is strace and why would you use it | strace is a diagnostic, debugging and instructional userspace utility for Linux. It is used to monitor and tamper with interactions between processes and the Linux kernel, which include system calls, signal deliveries, and changes of process state |  |
| Medium | What is systemd | systemd is a suite of basic building blocks for a Linux system. It provides a system and service manager that runs as PID 1 and starts the rest of the system | How can I start a service?
systemctl start <service> |
| Medium | What is journalctl | Logging on the machine | How can I view logs for a particular application:
journalctl -u docker
Difference of journalctl over syslog:
• Binary file rather than plain text
• Different ways to interact with the log --since, --until etc
• Compression
• Rate limiting |
| Medium | Which command will show you a list of open ports with applications listening on them? | • netstat
• ss | if candidate knows the exactly command line for listening and PIDS: netstat|ss -ntap |
| Hard | What is a sticky bit | At a directory level it restricts file deletion, only the owner and root can remove files in directory |  |
| Hard | What are the differences between symbolic and hard links? | Hard links point specifically to an inode. They can't cross filesystems.
Symbolic links are a link to another name in the filesystem. | If candidate can describe what is an inode. |
| Hard | What are the differences between symbolic and hard links? | Hard links point specifically to an inode. They can't cross filesystems.
Symbolic links are a link to another name in the filesystem. | If candidate can describe what is an inode. |

# Containers

| Level | **Question** | **Expected answer** | **Bonus points** |
| --- | --- | --- | --- |
| Easy | Build a new container image from a Dockerfile inside current directory and tag it. | docker build -t test:1.0 . |  |
| Easy | Start a container from a given image | docker run --name hello test:1.0 |  |
| Easy | How do you list all running and stopped containers? | docker ps -a |  |
| Easy | create a new bash process inside a container and connect to it via terminal? | docker exec -it cont_name bash |  |
| Medium | Explain high level differences between containers and virtual machine hypervisors. | Virtual machines and hypervisors abstract away hardware and enable you to run operating systems
Containers (technically container engines) abstract away operating systems and enable you to run applications |  |
| Hard | What is the difference between the ADD and COPY command in a Dockerfile | COPY takes a source and destination. ADD also lets you do that but you can also use a URL or do extraction of files (tar balls etc) | If they mention you should always use COPY if you are explicitly copying a file |
| Hard | In a dockerfile what  are the purposes of CMD vs ENTRYPOINT | CMD defines the default commands and/or parameters to run a container. It is easily overridden in docker run
ENTRYPOINT is preferred if you want to define a container with a specific executable and is only overridden with --entrypoint
You can combine ENTRYPOINT and CMD. E.g. run a script as the entrypoint and the command is the different flags |  |

# Kubernetes

| Level | **Question** | **Expected answer** | **Bonus points** |
| --- | --- | --- | --- |
| Easy | What’s the difference between a pod and a container? | Pod is a logical virtual machine, a container resides within the pod. | • init containers
• multiple containers on a pod
• sidecar |
| Easy | Can you say some different service types in Kubernetes? | • ClusterIP - provides availability for the service to be accessed by pods within the cluster only
• NodePort - Opens up a specific port on all nodes and forwards any traffic from this port to the service
• LoadBalancer - Exposes the service externally using the load balancer of your cloud provider
• **ExternalName.** This type maps the service to the contents of the externalName field (e.g., [foo.bar.example.com](http://foo.bar.example.com/)). It does this by returning a value for the CNAME record. |  |
| Easy | How do you list all pods in a namespace? | kubectl get pods -n namespace_name |  |
| Easy | How do you get the logs of a pod? | kubectl logs pod_name | What happens if the pod have multiple containers? |
| Easy | How to create a bash process inside a container and connect to it via terminal using kubectl? | kubectl exec -it pod_name --  /bin/bash |  |
| Medium | How can you start a rollback for an application? | The Rollback and rolling updates feature in Kubernetes is in-built with the Deployment object. If the existing state of a Deployment is unstable due to configuration or application code, then you can Rollback to earlier Deployment version. With every rollback, you can update the version of the Deployment. | If there not getting it a |
| Medium | What are the differences between a kubernetes Deployment and StatefulSet | • Generally use deployments for stateless applications and StatefulSets for stateful applications (although not a requirement)
• Pods in a stateful set are ordered and consistently named, pods in a deployment are not
• In a deployment the replicas all share a volume and PVC, while in a StatefulSet each pod has its own volume and PVC
• A headless service handles the pods network ID in StatefulSets while deployments require a service to enable interactions with pods |  |
| Medium | Where are (default kubernetes) secrets stored | etcd | How could you secure these:
• Envelope encryption with AWS KMS
• External secrets lookup (AWS Secrets Manager / SSM) |
| Medium | Describe the components in a Kubernetes cluster | Control plane:
• etcd - storage for all data (configuration, state, metadata)
• controller manager - daemon that embeds the core control loops shipped with kubernetes
• scheduler - Watches newly created pods that have no node assigned and selets node for them to run on 
• kube-apiserver - The Kubernetes API server validates and configures data for the api objects which include pods, services, replicationcontrollers, and others
Workers:
• kubelet - Makes sure containers are running in a pod
• container runtime - dockerd, containerd
• kube-proxy - Enables service abstraction by maintaining network rules on the host and performing connection forwarding |  |
| Medium | If you needed to perform some maintenance on a worker how would you go about this | Cordon
Drain
Perform maintenance
Uncordon |  |
| Hard | What is an ingress, why would I use it | An API object that manages external access to the services in a cluster, typically HTTP.
Ingress may provide load balancing, SSL termination and name-based virtual hosting
Why:
• Cost - less load balancers
• Security - SSL termination
• Usability - name-based virtual hosting | How does an ingress work:
• Expose HTTP and HTTPS routes from outside the cluster to services in the cluster
• Ingress-nginx - runs as a LoadBalancer service with a Deployment running the ingress-nginx software
• Each app that needs access has an Ingress object which has a rule to route the traffic to the Service
• The Service for the app has a ClusterIP so the ingress knows where to route the request |
| Hard | What is a service account | A **ServiceAccount** is used by containers running in a Pod, to communicate with the API server of the **Kubernetes** cluster | Describe a use case for a serviceAccount |
| Hard | What are the differences between a Role and ClusterRole | • **Role** - A Role always sets permissions within a particular namespace. When you create a Role, you have to specify the namespace it belongs in.
• **ClusterRole**, by contrast, is a non-namespaced resource. The resources have different names (Role and ClusterRole) because a Kubernetes object always has to be either namespaced or not namespaced; it can't be both. |  |
| Hard | How would you assign a pod to a node | • Use nodeSelector. Node needs to have a label, add nodeSelector with the label to the pod spec
• nodeAffinity
    ◦ hard - requiredDuringSchedulingIgnoredDuringExecution
    ◦ soft - preferredDuringSchedulingIgnoredDuringExecution
    ◦ No guarantee though |  |
| Hard | Explain taints and tolerations | You taint a node to ensure only particular pods run there
You add tolerations to a pod to allow them to schedule onto nodes with taints |  |
| Hard | What is an admission controller | An admission controller is a piece of code that intercepts requests to the Kubernetes API server prior to persistence of the object, but after the request is authenticated and authorized. Admission controllers may be "validating", "mutating", or both. Mutating controllers may modify the objects they admit; validating controllers may not |  |

# CI/CD

## General

| Level | Question | Expected answer | Bonus points |
| --- | --- | --- | --- |
| Medium | What is blue-green deployment | Have two production environments both identical, only one is live. As you prepare a new version of software rollout to non-live environment (e.g. green), once fully tested route requests to this environment. If something unexpected happens you can easily switch back to other environment |  |
| Medium | What is a canary deployment | Deployment strategty that releases and application or service incrementally to a subset of users |  |
| Hard | What is A/B testing | Running different versions of the same service as experiments in the same environment for a period of time |  |

## Jenkins

Assuming they've worked with it

| Level | Question | Expected answer | Bonus points |
| --- | --- | --- | --- |
| Easy | Provide some examples of different job types and whast they are | Freestyle - set of instructions using code e.g. bash
Pipeline - Created with Jenkinsfile in the root of the project groovy based DSL
Multi-branch - Run across multiple branches |  |
| Easy | What might be a typical jenkins architecture? Where would jobs run? | Master / Agent (or slave) setup where Agents (or slaves) run the jobs | Why wouldn't you run jobs on the master?
• Security
• Load
• Single point of failure
What happens if an agent is offline? |
| Medium | What is a shared libarary | Reusable pipeline or code to use in a pipeline | How could I use one in my pipeline:
• Setup Global pipeline library, with a name, default version pointed at a code repository
• Have the following code at the top of the Jenkinsfile

`@Library('libraryname') _` |

## Github Actions

Assuming they've worked with it

| Level | Question | Expected answer | Bonus points |
| --- | --- | --- | --- |
| Easy | Where in my code repository would I put a workflow | .github/workflows |  |
| Medium | How can a workflow be paused to get approval | Using the environments feature with required reviewers |  |
| Medium | How can I reduce repeating myself in github actions pipelines | Using workflow_call to call a pipeline in a remote repository or creating workflow templates |  |

# Configuration management

Depending on candidate CV, ask about the one he knows, ansible, puppet or skip if none.

## Puppet

| Level | **Question** | **Expected answer** | **Bonus points** |
| --- | --- | --- | --- |
| Easy | What is the purpose of hiera? | To separate configuration from the code. Puppet modules are to be environment-agnostic, hiera is for values that are specific to an environment. |  |
| Medium | How might you store encrypted values in hiera? | Using eyaml |  |
| Medium | What is r10k used for? | To control the deployment of Puppet modules across multiple environments. |  |

## Ansible

|  | **Question** | **Expected answer** | **Bonus points** |
| --- | --- | --- | --- |
| Easy | What are facts? | Facts in ansible is a way to represent data about hosts (IP addresses, hostname, attached volumes, OS version, etc.) |  |
| Easy | In a playbook, what is the relationship between tasks and handlers? | A task is something that you want ansible to do, for example, to lay down a configuration file.
A handler is an action you would want to perform when that task has run. For example, task to update httpd.conf might require handler to restart apache. |  |
| Easy | What can you use with ansible to store passwords securely? | Ansible Vault |  |
| Easy | What is an ansible module | Discrete units of code that can be used from the command line or in a playbook task | Written in Python |
| Medium | What would you use tags for in a playbook | You can run part of a playbook with tags by using tags or skip tags |  |
| Medium | How would you run the same task multiple times with different values | loop or with_* (with_items etc) |  |
| Medium | What is a block | Logical groups of tasks. Offers a way to control code execution using "when" and handle errors "always" and "rescue" |  |
| Medium | What is dynamic inventory? | Dynamic inventory is a way for Ansible to compose inventory (list of hosts) by querying 3rd-party API (AWS/GCP/etc.) |  |

# Scripting

## Bash

| Level | Question | Expected Answer | Bonus Points |
| --- | --- | --- | --- |
| Easy | What does echo $? do | Give a return code |  |
| Easy | In a bash script if I have set -e at the top what does this do | Will halt execution of the script if an error occurs |  |
| Easy | What does the command trap do in a bash script | Traps different error codes and runs code | Used for cleaning up in particular conditions |
| Easy | How would you do an if statement in bash | if [ <some test> ]
then
<commands>
fi |  |
| Medium | How would I change all instances of the word "orange" with "apple" in a file named "fruits" | sed -i 's/orange/apple/g' fruits |  |
| Medium | What does the command eval do | eval takes a string as an argument and evaluates it as if you'd typed that string on a command line. | It executes the command in the current shell environment rather than creating a child shell process. You would use it to get around issues such as resolving a variable to run a command against where it does not like the normal bash variable syntax |
| Medium | What does $@ mean | The parameters for a script returned in an array |  |
| Medium | In a file with three words separated by spaces how could i print just the second | awk '{print $2}' file
or
cut -f2 -d" " file |  |

## Python

| Level | Question | Expected Answer | Bonus Points |
| --- | --- | --- | --- |
| Medium | What is the difference between a list and a tuple | List - mutable, can be edited
Tuple - Immutable | How do you define a list and tuple
List:
list_name = []
Tuple:
tuple_name = (1, 2, 3)
What is a set, how does it compare to lists and tuples:
A set is an unordered collection of distinct immutable objects. Although sets are mutable the elements of sets must be immuable |
| Medium | What is the difference between a list and an array | Arrays must contain elements that are all the same type, lists can be anything |  |
| Medium | How do you define a dictionary | varname = {}
or
varname = dict() |  |
| Medium | What does import do | Imports modules | What is a module? Contain python code that can be used by importing
Why you shouldn't use import *
• Pollutes the namespace
• Imports all functions and classed into your own namespace |

# **DevOps Engineer I, II Candidate Exercise**

## **Objective**

This exercise is designed to evaluate your hands-on experience with DevOps tools, particularly Terraform, common AWS services, and CI/CD practices. The goal is to assess your ability to create Infrastructure as Code (IaC), deploy and manage resources on AWS, set up a basic web server, and follow best practices in automation and documentation.

## **Instructions**

1. **GitHub Repository:**
    1. Create a new public GitHub repository to host all the files and code related to this exercise.
2. **Infrastructure as Code (IaC):**
    1. Use Terraform to write infrastructure as code to:
        1. Spin up an EC2 Linux instance of type t2.micro within the default VPC and default public subnet.
        2. Configure appropriate security groups to allow HTTP (port 80) and SSH (port 22) traffic only.
        3. Ensure the EC2 instance is accessible within the AWS Free Tier limits.
3. **Web Server Setup:**
    1. Deploy a web server on the EC2 instance that serves a basic HTML page such as Hello, World! when accessed via the instance’s public IP on port 80.
4. **System Automation**
    1. Automate the installation and setup of the web server
5. **Monitoring and Logging** (***Optional for bonus points***):
    1. Enable CloudWatch monitoring for the EC2 instance to track CPU and memory utilisation.
6. **CI/CD Workflow** (***Optional for bonus points***):
    1. Set up a simple GitHub Actions workflow to:
        1. Lint or validate the Terraform code using a tool like terraform fmt or terraform validate
7. **Documentation**:
    1. Provide a README.md file in your repository, which includes:
        1. Step-by-step instructions to execute your code and validate the setup.
        2. Assumptions made or prerequisites required.

## **Submission**

- Share the link to your public GitHub repository containing all relevant files.
- Be prepared to discuss your approach, reasoning, and any challenges faced during the face-to-face interview.

## **Additional Notes**

- This exercise is expected to be completed within the AWS Free Tier. Please be mindful of any resources you provision to avoid incurring costs.
- The optional tasks for monitoring and CI/CD are not mandatory but will be considered as a bonus if implemented well.
- Please ensure you treat this exercise as a real world request and implement as you would in a production like environment.

---

## **Evaluation Criteria**

- **Correctness**: The infrastructure is correctly deployed, and the web server serves the expected HTML page on port.
- **Code Quality**: The Terraform code is well-structured, if modular, and follows best practices.
- **Automation**: Effective use of automation for server setup and web server deployment.
- **Version Control**: Proper use of Git, including meaningful commit messages and a clear history of changes.
- **Documentation**: Clear, concise, and complete documentation in the README file.
- **Security**: Secure use of AWS services, such as appropriately configured security groups and IAM roles (if applicable).
- **Monitoring (Bonus):** CloudWatch monitoring and logs configuration for additional observability.
- **CI/CD (Bonus)**: GitHub Actions workflow to validate the code automatically.

## **We can ask questions like these Elements?**

- **Security Groups**: Tests understanding of network security configurations.
- **Automation**: Ensures candidates can automate repetitive tasks, a key DevOps skill.
- **Monitoring**: Demonstrates familiarity with observability and AWS monitoring tools.
- **CI/CD**: Validates basic knowledge of GitHub Actions and workflow automation.
- **Documentation**: Highlights communication skills and attention to detail.

## During the interview, one can always ask (below are just assisting questions and you can always ask whatever one would like to):

- Can you show us by destroying the whole stack and recreating it?
- How about if you can show destroying only EC2 instance? By asking this, we can analyse whether candidate is capable playing with the terraform state
- How about if you can show us removing the EC2 instance from the TF state and perhaps adding it again? Again, the demo can show us candidates' TF skills.
- How about if you can modify a file and commit in the repo? Can show is git skills.

# **Senior DevOps Engineer Candidate Exercise**

For a **Senior DevOps Engineer**, the exercise can be made more challenging and comprehensive to test their advanced skills in **cloud architecture, automation, observability, and CI/CD pipelines**. Here’s an enhanced version of the exercise for such a candidate:

## **Objective**

This exercise is designed to evaluate your hands-on experience with advanced DevOps practices, cloud architecture design, automation, monitoring, and CI/CD workflows. The goal is to assess your ability to build scalable, secure, and automated infrastructure while following best practices.

## **Instructions**

1. **GitHub Repository**
    1. Create a **public GitHub repository** to host all files and code for this exercise.
    2. Use meaningful commit messages that clearly explain the changes made at each step.
2. **Infrastructure as Code (IaC)**
    1. Use **Terraform** to:
        1. Provision an **AWS environment** with the following:
        2. An **EC2 instance** (t2.micro) in a custom **VPC** with private and public subnets.
        3. A **Bastion host** in the public subnet for secure access to instances in private subnets.
        4. A **web server** running on an EC2 instance in the private subnet.
    2. Configure **security groups** to:
        1. Allow HTTP traffic (port 80) to the web server from the Bastion host only.
        2. Allow SSH access to the Bastion host from your IP.
        3. Use **IAM roles** and policies to grant the least privilege needed for the instances.
3. **Web Application Deployment**
    1. Deploy a web application on the web server that serves a **“Hello, World!”** HTML page.
    2. Automate the deployment of the web server and application using **Terraform provisioners**, **cloud-init**, or a configuration management tool like **Ansible**.
4. **Load Balancing and Auto Scaling**:
    1. Add an **Application Load Balancer (ALB)** in front of the web server.
    2. Implement an **Auto Scaling Group (ASG)** with a minimum of 1 instance and a maximum of 3 instances, triggered by CPU usage.
5. **Monitoring and Alerts**:
    1. Set up **CloudWatch monitoring** to:
        1. Track the CPU and memory usage of the web servers.
        2. Enable **CloudWatch Alarms** to notify you if the CPU usage exceeds 70%.
        3. Configure an alarm notification via **SNS** (email or topic subscription).
6. **Cost Optimisation**
    1. Ensure the architecture fits within the **AWS Free Tier** wherever possible.
    2. Document any considerations taken to reduce costs or remain within limits.
7. **CI/CD Pipeline**
    1. Implement a **GitHub Actions** or **Jenkins pipeline** to:
        1. Validate Terraform code using terraform fmt and terraform validate.
        2. Plan and apply Terraform code (manual approval step for apply).
        3. Automate testing to ensure the web application is accessible via the ALB.
8. **Documentation**
    1. Create a detailed **README.md** in your repository, including:
        1. Steps to deploy the infrastructure.
        2. Details on how to test the deployed solution.
        3. Any assumptions or prerequisites.
        4. Instructions to clean up resources to avoid unnecessary costs.
9. **Optional (Bonus Points)**:
    1. **Containerisation**: Package the web application in a **Docker container** and deploy it using **Amazon ECS** or **EKS**.
    2. **Infrastructure Testing**: Write automated tests using tools like **Terratest** or **AWS CLI scripts** to validate the deployment.
    3. **Secret Management**: Use **AWS Secrets Manager** to securely store and retrieve sensitive information (e.g., web server credentials).

## **Submission**

- Share the link to your public GitHub repository containing all relevant code and documentation.
- Be prepared to discuss your design decisions, challenges faced, and how you addressed them during the interview.

---

## **Evaluation Criteria**

1. **Architecture Design**:
    1. Demonstrates scalability, security, and adherence to best practices.
    2. Efficient use of AWS services (e.g., ALB, ASG, and IAM roles).
2. **Code Quality**:
    1. Terraform code is modular, reusable, and follows best practices.
    2. Use of variables, modules, and outputs to ensure maintainability.
3. **Automation**:
    1. Effective automation of tasks such as web server setup, application deployment, and monitoring.
4. **CI/CD Workflow**:
    1. Proper implementation of a pipeline for validation, deployment, and testing.
5. **Monitoring and Observability**:
    1. Comprehensive setup of monitoring, alarms, and notifications.
6. **Documentation**:
    1. Clear, concise, and comprehensive documentation of the solution.
7. **Bonus (Optional)**:
    1. Use of Docker/ECS/EKS for containerisation.
    2. Infrastructure testing and secret management.

## **Why These Additions?**

- **Custom VPC, Bastion Host, and Security Groups**: Tests understanding of secure network design and AWS networking.
- **Load Balancer and Auto Scaling**: Evaluates ability to build scalable and fault-tolerant systems.
- **Monitoring and Alarms**: Demonstrates expertise in observability and proactive issue detection.
- **CI/CD**: Validates advanced DevOps practices and automation skills.
- **Bonus Tasks**: Tests knowledge of modern containerisation and infrastructure testing techniques.

This enhanced exercise ensures a thorough evaluation of a senior DevOps engineer’s expertise while allowing them to showcase their skills comprehensively.

# Platform Phone Interview

# Things we look for in a new DevOps candidate

- Infrastructure / Architectural knowledge (ideally in a cloud based environment)
- Programming experience
- Agile experience / knowledge
- Team player
- Motivated to learn

# Introduction (2min)

- Interviewers (who's in the room)
- Do you have any question you'd like to ask us before we go through the interview

# ScienceDirect / Elsevier Technology (3min)

- migration project, almost greenfield, about ~5 years old
- arhitecture, AWS mainly Java & Node.js
- platform team working close with dev teams (7, 8 teams)
- lots of smart people to work with and learn from :)
- work in an agile environment / sprints / scrums

# About the candidate (5min)

"Tell us briefly about your experiences in your current / past role"

# General technical / experience (15-20min)

## Junior

- What Linux distirubition do you know of?
- Do you know what a CDN is?
- Name at least 3 HTTP Methods
    - (If answered: GET, PUT, POST, DELETE, OPTIONS, HEAD, PATCH, ask what they do).

## Senior

### Linux

| Scripting | Give me two ways of interpreting command line parameters to a bash script? | $1 $2 $3, $@ |
| --- | --- | --- |
|  | Give an example of some other $something variables? What do they mean? | $# $? $HOME $USER $$ |
|  | What command would you use to find what was the last command exit code? | $? |
|  | What is the difference between break and continue | break (exit the loop), continue (stop at this line, and continue with the next iteration of the loop) |
| Python
Ask only if the candidate has Python experience in his CV | What package management system would you use to install a library? | pip |
|  | What library would you use in python to make HTTP requests | requests, httplib, urllib |
|  | (Python + AWS) What is the library you would use in python to talk to the AWS API | boto, boto3, botocore |
| Disk | What file system types there are on linux? | ext* family (ext2, ext3 and ext4), XFS, JFS, ReiserFS, brtfs |
|  | How do you find mounted disks? | mount
cat /proc/mounts
cat /etc/mtab |
|  | Where would you specify the mount options for a disk? | mount command
If persistent: /etc/fstab |
|  | What are the differences between the df and du commands? | df - List free space on mounted disk volumes
du - Display file sizes and disk usage in current directory |
|  | You get the error "No space left on device" but you still have 18GB free left. What is the problem? | You are running out of inodes. Check with df -iFiles have been deleted but they are still in use by some applications. Check with lsof | grep deleted |
|  | What is an inode? | A data structure that stores information about a file, including pointers to the blocks storing the file's contents |
|  | What are the differences between symbolic and hard links? | Hard links point specifically to an inode. They can't cross filesystems.
Symbolic links are a link to another name in the filesystem |
|  | What command would you use to make a file immutable | chattr +i <file> |
|  | Beyond RWX for user, group, all, what other bits can you set in POSIX permissions? | stickybit, setuid, setgid, ACLs |
| Authentication | How can I log into a server without password authentication? | ssh keys |
|  | Where should my public key be placed for me to have SSH access to that host? | authorized_keys file |
|  | When a user logs in, where is that information stored? | /var/log/secure |
| Debugging | What command will show you a list of open ports with applications listening on them? | netstat / ss |
|  | On a 2 vCore server I have a load average of 4. What does that mean? |  |
|  | Web server is unresponsive. What tools would you use to diagnose? |  |
|  | You get the error "Too many open files". What does it mean and do you fix it? | You can specify limits per user
/etc/security/limits.conf
See current max limit of file descriptors:
cat /proc/sys/fs/file-max
Display hard limit
ulimit -Hn
Display soft limit
ulimit -Sn
Add the new limit to /etc/sysctl.conf
fs.file-max = 100000
then run sysctl -p to apply the change |

### AWS

- 2 machines can't talk to each other in AWS. What steps would you take to debug?
- What is an instance profile/role?
- What is the role of AWS CloudTrail?
- What are the edge locations?
- Can you ssh to an AWS instance if selecting not to create a key pair on creation?
- What is EC2 instance metadata?

### Kubernetes / Docker

- Describe what a deployment is
- What command would you use to show all containers in Docker

### Other

- What is a CDN and how would you use it for?
- Difference between TCP and UDP ? (Transmission Control Protocol vs User Datagram Protocol, TCP is connection orientated, packets are checked on send/receive, UDP is "fire and forget", no checking is done to e.g. confirm the packet arrived)
- Give me an example of how you use a configuration management!
- Why would you use a monitoring/alerting system?
- What webserver would you use to host a static website (apache, nginx, iis, lighttpd, tomcat)
- How would you load balance over multiple webservers?
- Explain how Ansible (or alternative on CV) works and what are the components of it?
- What advantage does a cloud provider give you over traditional data centre hosted infrastructure?

# Finalising (3min)

- Why change job/company?
- Happy with relocation?
- Any questions for us?