output "instance_id" {
  value = "${aws_instance.ml_aura.id}"
}

output "instance_public_ip" {
  value = "${aws_instance.ml_aura.public_ip}"
}

output "instance_public_dns" {
  value = "${aws_instance.ml_aura.public_dns}"
}

output "instance_private_ip" {
  value = "${aws_instance.ml_aura.private_ip}"
}
