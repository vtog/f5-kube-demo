Prepare BIG-IP for Kubernetes
=============================
| :kbd:`$ tmsh create auth partition kubernetes`
| :kbd:`$ tmsh create net tunnels vxlan fl-vxlan port 8472 flooding-type none`
| :kbd:`$ tmsh create net tunnels tunnel fl-vxlan key 1 profile fl-vxlan local-address 10.1.20.10`
| :kbd:`$ tmsh create net self 10.244.20.10 address 10.244.20.10/255.255.0.0 allow-service none vlan fl-vxlan`
| :kbd:`$ tmsh create net self 10.244.20.11 address 10.244.20.11/255.255.0.0 allow-service none vlan fl-vxlan traffic-group traffic-group-1`
