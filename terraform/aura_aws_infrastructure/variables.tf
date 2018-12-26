variable "region" {
  default = "us-east-1"
}

variable "volume_size_gb" {
  description = "number of GB of storage for your volume"
  default     = 50
}

variable "instance_type" {
  default     = "t2.2xlarge"
}

variable "spot_instance_price" {
  default = "0.12"
}

variable "ami_id" {
  default = "ami-0d3348bce8bdde5a6"
}

variable "ssh_key" {
  default = "aura_ssh_key"
}
