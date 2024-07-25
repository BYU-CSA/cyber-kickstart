[AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html) for overview of individual services.
# AWS S3 Bucket
Simple Storage Service. Can store literally anything.
Used for:
- Centralizing data (data lakes)
- Backups
- Archive (Glacier)
- Cloud native apps (lower latency)
Object storage is completely flat, as opposed to hierarchical file systems.
# AWS SNS
Simple Notification Service, A2A (Application2Application) notifications to a few different targets including:
- Amazon SQS
- Amazon Kinesis Data Firehose
- AWS Lambda
- HTTPS endpoints
A2P (Application2Person) includes:
- SMS texts
- Push notifs
- Email
# AWS SQS
Simple Queue Service. Sends, stores, and receives messages between software components without losing messages.
Offers two types of queues:
- Standard Queues:
	- Practically unlimited throughput (not actually, but when freaking AWS says you're not gonna hit bandwidth limit, you're not gonna hit that limit)
	- At-Least-Once Delivery: Everything is delivered once, could be delivered more than once
	- Best-effort Ordering: Messages might be delivered in an order different from which they were sent.
	- Use cases:
		- Decouple live requests from background work, think uploading media while encoding/resizing it
		- Allocate tasks to multiple nodes
		- Batch messages for future processing
- FIFO Queues:
	- High Throughput: default 3k messages/second w/ batching, 300 w/o batching. Higher throughput is available, up to 70k messages per second.
	- Exactly-Once Processing: A message is only delivered once
	- FIFO Delivery: Strictly preserved order
	- Use cases:
		- Order sensitive messages like user commands
		- Display correct product price by sending price mods in the right order
		- Prevent a student from enrolling in a course before registration is finished
Messages can contain up to 256KB of data.
On certain events, can be configured to send notification to SQS Queue, SNS Topic, or Lambda Function(s).
# AWS Lambda
Manage serverless compute, executing code in response to events, handling compute resources. Can instantly scale. Can be run in response to a whole slew of AWS operations, including HTTP Requests to API Gateway, modifications to S3 buckets, table updates in DynamoDB, and state transitions in AWS Step Functions.

Used to extend other AWS services with custom logic.

```js
export const handler = async (event, context) => {
  
	function calculateArea(length, width) {
	    return length * width;
	}
  
	const length = event.length;
	const width = event.width;
  
	let area = calculateArea(length, width);
  
	console.log(`The area is ${area}`);
  
	console.log(`CloudWatch log group: ${context.logGroupName}`)
  
	let data = {
		"area": area,
	}
  
	return JSON.stringify(data);
}
```

# AWS DynamoDB
Serverless NoSQL database with claimed good performance. Only pay for what you use. 

# AWS Aurora
MySQL/PostgreSQL compatible RDS. Duplicated data across 3 AZ (Availability Zones) automatically. Claims to be very cost-effective with serverless. Gets integer multiple better throughputs than a typical PostgreSQL/MySQL. Max 128TB. Support autoscaling. [Typically more](https://medium.com/awesome-cloud/aws-difference-between-amazon-aurora-and-amazon-rds-comparison-aws-aurora-vs-aws-rds-databases-60a69dbec41f) expensive than an equivalent RDS.

# AWS RDS
RDS with multiple choices for engines. Not serverless. [Supports](https://medium.com/awesome-cloud/aws-difference-between-amazon-aurora-and-amazon-rds-comparison-aws-aurora-vs-aws-rds-databases-60a69dbec41f) Aurora, MySQL, PostgreSQL, MariaDB, Microsoft SQL, and Oracle. Kind of like installing a database on EC2, except AWS takes care of that. Replicability needs to be enabled. Max 4TB (16TB if Microsoft SQL). Does not support autoscaling.

# AWS API Gateway
"Front door" for APIs. Can handle both RESTful/Websocket. Tools to publish, maintain, monitor, secure, and operate APIs. Pay-as-you-go. Can route to private resources in a VPC. Lifecrycle management.

# ARN
Amazon Resource Names, used to uniquely identify AWS resources. `arn:partition:service:region:account-id:resource-id`
`arn:partition:service:region:account-id:resource-type/resource-id`
`arn:partition:service:region:account-id:resource-type:resource-id`
- `partition`: Group of regions
	- `aws`: AWS Regions
	- `aws-cn`: AWS China
	- `aws-us-gov`: Government
- `service`: Identifies AWS product
- `region`: Region code, think `us-east-2`
- `account-id`: ID of AWS account that owns the resource.
- `resource-type`: Resource type, think `vpc` for a VPC
- `resource-id`: Resource path/name. Could have an 
Examples:
- IAM user: `arn:aws:iam::123456789012:user/johndoe`
- SNS Topic: `arn:aws:sns:us-east-1:123456789012:example-sns-topic-name`
- VPC: `arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE`

# AWS IAM
Manages AWS resource access.
At work we avoid users because of the whole permanent API key, instead use roles.

# AWS Elastic Kubernetes Service (EKS)
Start, run, and scale Kubernetes.

# AWS Elastic Container Service (ECS)
Older containerization model. According to [this](https://www.reddit.com/r/aws/comments/vd3izl/ecs_vs_eks/) post, ECS is older/clunkier than EKS. Requires ECS, Parameters Store, Secrets Manager, ACM, SSM, Cloudwatch + more to do what comes inline with Kubernetes. Doesn't support Helm, so it's not as easy to extend as EKS. General wisdom seems to be to build new stuff in EKS, but don't worry about wholly replacing ECS.

# AWS Cloudfront
Content Delivery Network by AWS.

# AWS EBS
Cloud block storage. Used for SQL/NoSQL. Can be attached to Amazon EC2 instances.

# AWS Elastic Container Registry (ECR)
Docker hub for EKS/ECS