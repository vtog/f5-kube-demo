Introduction
============
This lab is designed to walk through building a basic kubernetes cluster. The Ravello BP has the following components:
    - Ravello BluePrint = **Kubernetes-Container-Lab-vtog-v1.0.1**
        - 1x Linux Jumphost (Ubuntu Xenial)
        - 1x F5 Big-IP (v13.1.0.3)
        - 1x Master (Ubuntu Xenial)
        - 2x Minions (Ubuntu Xenial)

|

    .. list-table::
        :widths: 10 20 20 10
        :header-rows: 1

        * - **Component**
          - **IP-ADDR**
          - **VLAN**
          - **Credentials**
        * - jumphost
          - | dhcp
          - | mgmt: 10.1.1.0/24
          - | ubuntu/ubuntu
            | root/default
        * - bigip1
          - | 10.1.1.10
            | 10.1.10.10
            | 10.1.20.10
            | 10.1.30.10
            | 10.244.20.10
            | 10.244.20.11 (float)
          - | mgmt: 10.1.1.0/24
            | external 10.1.10.0/24
            | internal 10.1.20.0/24
            | ha 10.1.30.0/24
            | flannel: 10.244.20.0/16
          - | admin/admin
            | root/default
        * - kube-master
          - | 10.1.20.21
          - | internal: 10.1.20.0/24
          - | ubuntu/ubuntu
            | root/default
        * - kube-node1
          - | 10.1.20.22
          - | internal: 10.1.20.0/24
          - | ubuntu/ubuntu
            | root/default
        * - kube-node2
          - | 10.1.20.23
          - | internal: 10.1.20.0/24
          - | ubuntu/ubuntu
            | root/default
