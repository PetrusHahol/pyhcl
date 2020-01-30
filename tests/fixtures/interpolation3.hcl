output "ls" {
  value = replace("2001:db8:0000:0000:${var.apollo_dcn_cidr}", ".", ":")
}
