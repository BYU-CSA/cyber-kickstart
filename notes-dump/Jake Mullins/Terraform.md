Terraform, typically denoted by a `.tf` file extension, is an Infrastructure as Code tool by HashiCorp that defines data center infrastructure using a language called HashiCorp Configuration Language, or HCL, with relatively simple syntax:
```tf
resource "aws_vpc" "main" {
	cidr_block = var.base_cidr_block
}

<BLOCK TYPE> "<BLOCK LABEL>" "<BLOCK LABEL>" {
	# Block body
	<IDENTIFIER> = <EXPRESSION> # Argument
}
```

Here's a more complicated example:
```tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 1.0.4"
    }
  }
t}

variable "aws_region" {}

variable "base_cidr_block" {
  description = "A /16 CIDR range definition, such as 10.1.0.0/16, that the VPC will use"
  default = "10.1.0.0/16"
}

variable "availability_zones" {
  description = "A list of availability zones in which to create subnets"
  type = list(string)
}

provider "aws" {
  region = var.aws_region
}

resource "aws_vpc" "main" {
  # Referencing the base_cidr_block variable allows the network address
  # to be changed without modifying the configuration.
  cidr_block = var.base_cidr_block
}

resource "aws_subnet" "az" {
  # Create one subnet for each given availability zone.
  count = length(var.availability_zones)

  # For each subnet, use one of the specified availability zones.
  availability_zone = var.availability_zones[count.index]

  # By referencing the aws_vpc.main object, Terraform knows that the subnet
  # must be created only after the VPC is created.
  vpc_id = aws_vpc.main.id

  # Built-in functions and operators can be used for simple transformations of
  # values, such as computing a subnet address. Here we create a /20 prefix for
  # each subnet, using consecutive addresses for each availability zone,
  # such as 10.1.16.0/20 .
  cidr_block = cidrsubnet(aws_vpc.main.cidr_block, 4, count.index+1)
}
```

[These](https://developer.hashicorp.com/terraform/tutorials/configuration-language) tutorials from the official HashiCorp site actually look really good.

Resources follow this template:
```terraform
resource <resource_type> <resource_name> {}
```

And form a resource ID with format `<resource_type>.<resource_name>`

In the case of:
```terraform
resource "random_pet" "name" {}
```

The ID is `random_pet.name`. The [Terraform Registry](https://registry.terraform.io/) stores all data related to Terraform providers and associated resources. Each resource has:
- Arguments: Can be `required` or `optional`
- Attributes: Values exposed by an existing resource, accessed with format `<resource_type>.<resource_name>.<attribute_name>`.
- Meta-arguments: Change resources behavior, like the `count` arg that creates multiple resources.

According to the [random pet registry entry](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/pet?ajs_aid=2631af12-4128-4fc9-b45e-09465ba9fac9&product_intent=terraform) there is a single attribute called `id` that can be reached by other resources.

In the example of a simple AWS instance:
```terraform
resource "aws_instance" "web" {
	ami                    = "ami-a0cfeed8"
	instance_type          = "t2.micro"
	user_data              = file("init-script.sh")

	tags = {
		Name = random_pet.name.id
	}
}
```

For each argument:
`ami`: Use the `ami-a0cfeed8` Amazon Machine Image.
`instance_type`: Select a `t2.micro` EC2 instance
`user_data`: pass the contents of `init-script.sh` in this directory to the `user-data` argument.
`tags`: A map of tags to assign to this instance. 
- `Name`: arbitrary tag
`modules`: classes
`envs`: Instances of 

# Providers
Terraform providers are plugins that enables interaction with an API, including Cloud and SAAS providers. Acts as a go between from the Terraform runtime and the target API.
# Resources
## AWS S3 Bucket
Required (at least for my use case):
- `bucket`: Name of bucket.
- `bucket_prefix`: Unique bucket name with specified prefix.
Attributes:
- `id`: Name of the bucket.
- `arn`: ARN of the bucket.
- `bucket_domain_name`: The bucket domain name, of format `bucketname.s3.amazonaws.com`.
- `bucket_regional_domain_name`: Region specific domain name.
- `hosted_zone_id`: The Route 53 Hosted Zone ID.
- `region`: AWS region the bucket lives in.
- `tags_all`: All tags assigned to resource.
- `website_endpoint`: If bucket is configured with a website.
- `website_domain`: If bucket is configured with a website.

## AWS SQS Queue
Required (at least for my use case):
- `name`: Name of the queue
- `name_prefix`: Random name with specified prefix.
Optional:
- `visibility_timeout_seconds`: Visibility timeout for the queue. Default `30` seconds.
- `message_retention_seconds`: Number of seconds SQS retains a message. Default is `345600` seconds, 4 days.
- `max_message_size`: The limit of how many bytes a message can contain before SQS rejects it. Default is `256 KiB`.
- `delay_seconds`: Time in seconds that delivery is delayed. Default is `0` seconds.
- `receive_wait_time_seconds`: The time for which a ReceiveMessage call will wait for a message to arrive before returning. Default is `0`.
- `policy`: Policy object.
- `fifo_queue`: Designating a FIFO queue. Default is `false`.
- `content_based_deduplication`: Enables content-based deduplication for FIFO queues.
Attributes:
- `id`: The URL for SQS queue.
- `arn`: The ARN of SQS queue.
- `tags_all`: Map of tags assigned to the resource.
- `url`: Same as `id`.

## AWS S3 Bucket Notification
Required (at least for my use case):
- `bucket`: Name of bucket to put notification configuration
Optional:
- `topic`: Notification configuration to SNS Topic.
- `lambda_function`: Notification to Lambda Function.
- `queue`: Notification to SQS Queue:
	- `queue_arn`: Target SQS ARN
	- `events`: Which [event](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html#notification-how-to-event-types-and-destinations) to send notification
	- `id`: Unique identifier for each notification configuration
	- `filter_prefix`: Specifies object key name prefix.
	- `filter_suffix`: Specifies object key name suffix.

