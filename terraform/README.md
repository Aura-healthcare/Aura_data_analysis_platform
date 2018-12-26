# launch an aws EC2 VM for Machine and Deep Learning
Go to the folder containing your terraform scripts

# The terraform init command is used to initialize a working directory containing Terraform configuration files. This is the first command that should be run after writing a new Terraform configuration or cloning an existing one from version control.
terraform init

# Deploy the infrastructur specified in terraform scripts
terraform deploy 
—> answer yes in terminal to launch the VM

Now SSH to your VM and enjoy

# Do not forget to destroy your infrastructure once you're done or you will still pay !
terraform destroy

