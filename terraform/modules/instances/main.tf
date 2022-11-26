resource "aws_key_pair" "tf-key-pair" {
    for_each = {for server in var.configuration: server.instance_name => server}
    key_name = "${each.value.instance_name}-key"
    public_key = tls_private_key.rsa.public_key_openssh
}

resource "tls_private_key" "rsa" {
    algorithm = "RSA"
    rsa_bits  = 4096
}

resource "local_file" "tf-key" {
    content  = tls_private_key.rsa.private_key_pem
    filename = "../application/keys/instances/instance_key_pair"
}

resource "aws_instance" "instance" {
    for_each = {for server in var.configuration: server.instance_name =>  server}
    
    ami           =  data.aws_ami.ubuntu.id
    instance_type = each.value.instance_type
    subnet_id =  var.subnet_id
    key_name = "${each.value.instance_name}-key"
    tags = {
        Name = "${each.value.instance_name}"
    }
}