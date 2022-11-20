resource "aws_network_interface_sg_attachment" "sg_attachment" {
  for_each = {for relation in var.association: relation.name => relation}
  security_group_id    = each.value.security_group_id
  network_interface_id = each.value.instance_id
}