variable "aws_access_key" {
    type = string
    sensitive = true
}

variable "aws_secret_key" {
    type = string
    sensitive = true
}

variable "region" {
    default = "us-east-1"
}

#Usuarios
variable "users" {
    type = list(object({
        name = string
    }))
}

#Instancias
variable "instance_conf"{
    type = list(object({
        instance_name = string,
        instance_type = string  
    }))
}

#Grupos de seguranca
variable "sec_groups"{
    type = list(object({
        name = string,
        description = string,
        ingress = list(object({
            from_port = number,
            to_port = number,
            protocol = string,
            cidr_blocks = list(string)
        }))
    }))
}

#Associação de instancia com grupo de seguranca
variable "association"{
    type = list(object({
        name = string,
        instance_id = string,
        security_group_id = string
    }))
}

