provider "aws" {
  region  = "${var.region}"
  profile = "terraform"
}

resource "aws_instance" "ml_aura" {
  ami           = "${var.ami_id}"
  instance_type = "${var.instance_type}"
  associate_public_ip_address = true
  key_name      = "${var.ssh_key}"
  vpc_security_group_ids = ["${aws_security_group.default.id}"]

  #spot_price    = "${var.spot_instance_price}"

  tags {
    Name = "aura_machine_learning_vm"
  }
}

resource "aws_security_group" "default" {
  name = "terraform-test"
 
  # Allow SSH & HTTP in
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "SSH in"
  }
 
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTP in"
  }
 
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
 
  # Enable ICMP
  ingress {
    from_port = -1
    to_port = -1
    protocol = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
