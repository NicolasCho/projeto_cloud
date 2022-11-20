resource "aws_vpc" "vpc"{
    cidr_block           = var.vpcCIDRblock
    
    #Tenancy defines how EC2 instances are distributed across physical hardware and affects pricing
    instance_tenancy     = "default"   

    enable_dns_support   = true
    enable_dns_hostnames = true

    tags = {
        Name = "VPC"
    }
}


resource "aws_subnet" "subnet" {
    vpc_id                  = aws_vpc.vpc.id
    cidr_block              = var.publicsCIDRblock

    #Specify true to indicate that instances launched into the subnet should be assigned a public IP address. 
    map_public_ip_on_launch = true

    availability_zone       = var.availabilityZone

    tags = {
        Name = "Public subnet"
    }
}

resource "aws_internet_gateway" "IGW" {
    vpc_id = aws_vpc.vpc.id
    tags = {
            Name = "Internet gateway"
    }
}

resource "aws_route_table" "Public_RT" {
    vpc_id = aws_vpc.vpc.id
    tags = {
            Name = "Public Route table"
    }
}

resource "aws_route" "internet_access" {
    route_table_id         = aws_route_table.Public_RT.id
    destination_cidr_block = var.publicdestCIDRblock
    gateway_id             = aws_internet_gateway.IGW.id
}

resource "aws_route_table_association" "Public_association" {
    subnet_id      = aws_subnet.subnet.id
    route_table_id = aws_route_table.Public_RT.id
}