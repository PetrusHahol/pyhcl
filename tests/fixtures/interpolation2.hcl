resource "openstack_networking_port_v2" "port" {
  name       = "name"
  network_id = id
  value_specs = {
    "binding:vnic_type" = var.cloud_release == "li" ? "normal" : "normal"
  }
   security_group_ids = [
    id1,
    id2,
    "id3"
  ]
  admin_state_up = "true"
}