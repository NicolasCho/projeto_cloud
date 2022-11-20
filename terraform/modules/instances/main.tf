locals {
  serverconfig = [
    for srv in var.configuration : [
      for i in range(1, srv.no_of_instances+1) : {
        instance_name = "${srv.application_name}-${i}"
        instance_type = srv.instance_type
        subnet_id   = var.subnet_id
        ami = data.aws_ami.ubuntu.id
      }
    ]
  ]
}

locals {
    instances = flatten(local.serverconfig)
}

resource "aws_key_pair" "tf-key-pair" {
    for_each = {for server in local.instances: server.instance_name => server}
    key_name = each.value.instance_name
    public_key = tls_private_key.rsa.public_key_openssh
}

resource "tls_private_key" "rsa" {
    algorithm = "RSA"
    rsa_bits  = 4096
}

resource "local_file" "tf-key" {
    content  = tls_private_key.rsa.private_key_pem
    filename = "tf-key-pair"
}


resource "aws_instance" "instance" {
    for_each = {for server in local.instances: server.instance_name =>  server}
    
    ami           = each.value.ami
    instance_type = each.value.instance_type
    subnet_id = each.value.subnet_id
    tags = {
        Name = "${each.value.instance_name}"
    }
}