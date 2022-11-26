resource "aws_iam_user" "users" {
  for_each = {for user in var.users: user.name => user}
  name = each.value.name
}

resource "aws_iam_access_key" "keys" {
  for_each = {for user in var.users: user.name => user}
  user = aws_iam_user.users[each.value.name].name
}

resource "local_file" "user_keys" {
  for_each = {for key in aws_iam_access_key.keys: key.user => key}
  content  = each.value.ses_smtp_password_v4
  filename = "../application/keys/users/${each.value.user}-key"
}