resource "aws_iam_user" "users" {
  for_each = {for user in var.users: user.name => user}
  name = each.value.name
}