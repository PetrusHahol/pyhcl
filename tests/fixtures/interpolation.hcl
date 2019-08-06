data "resource" "object" {
  vars = {
    cluster_1         = join("\n", data.template_file.cluster_1.*.rendered)
    cluster_2         = join("\n", data.template_file.cluster_2.*.rendered)
    cluster_3         = format("name_%02d", count.index + 1)
    jumphost_ip       = openstack_compute_instance_v2.jumphost.access_ip_v4
  }
}

