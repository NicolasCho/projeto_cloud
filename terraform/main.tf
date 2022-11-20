terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region     = "${var.region}"
}

module "vpc"{
  source = "./modules/vpc"
}

module "instances"{
  source = "./modules/instances"
  subnet_id = module.vpc.subnet_id
  configuration = var.instance_conf
}

module "users"{
  source = "./modules/users"
  users = var.users
}

module "sec_groups"{
  source = "./modules/sec_groups"
  sec_groups = var.sec_groups
  vpc_id = module.vpc.vpc_id
}

module "sec_inst_association"{
  source = "./sec_inst_association"
  association = var.association
}