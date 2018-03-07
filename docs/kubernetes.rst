Build a Kubernetes Cluster
==========================
Each of the following commands need to be run on all three servers unless otherwise specified.

#. From the jumphost using putty open a new SSH session to each of the following servers. Putty sessions are pre-configured to connect with the default user "ubuntu" and cert.
    | - kube-master
    | - kube-node1
    | - kube-node2
#. Connect as root
    .. code:: bash

        $ su -
        $ passwd = default

#. Edit /etc/hosts and add the following static host entries
    .. code:: bash

        10.1.20.21    kube-master
        10.1.20.22    kube-node1
        10.1.20.23    kube-node2

#. Upgrade Ubuntu to ensure an up-to-date OS
    .. code:: bash

        $ apt update && apt upgrade -y

#. Add the docker repo
    .. code:: bash

        $ curl \-fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add \-
        $ add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

#. Add the kubernetes repo
    .. code:: bash

        $ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
        $ cat <<EOF > /etc/apt/sources.list.d/kubernetes.list
        deb http://apt.kubernetes.io/ kubernetes-xenial main
        EOF

#. Install docker
    .. code:: bash

        $ apt update && apt install -y docker-ce

#. Configure docker to use the correct cgroupdriver
    .. code:: bash

        $ cat << EOF > /etc/docker/daemon.json
        {
        "exec-opts": ["native.cgroupdriver=cgroupfs"]
        }
        EOF
#. Verify docker is up and running? (should see the hello-world container pulled and ran with a "hello world" message.)
    .. code:: bash

        $ docker run hello-world

#. Install kubernetes
    .. code:: bash

        $ apt install -y kubelet kubeadm kubectl

#. Initialize kubernetes with default network, **master only**. (default flannel network 10.244.0.0/16)
    .. code:: bash

        $ kubeadm init --pod-network-cidr=10.244.0.0/16

    | **Take note of the output.  It will be needed to join the nodes to the master in a later step.**
#. Configure kubernetes management, **master only**.  At this point you should be logged in as root.  The following will update both root and ubuntu user accounts.
    .. code:: bash

        $ mkdir -p $HOME/.kube
        $ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        $ sudo chown $(id -u):$(id -g) $HOME/.kube/config
        $ logout
        $ mkdir -p $HOME/.kube
        $ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        $ sudo chown $(id -u):$(id -g) $HOME/.kube/config

#. Install flannel on the master, **master only**. (default flannel network 10.244.0.0/16)
    .. code:: bash

        $ kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

#. Verify Kubernetes is up and running? (should see several kubernetes pods up and running.)
    .. code:: bash

        $ kubectl get pods --all-namespaces

    | **Before running next step wait for all system pods to show status "Running"**
#. Add the kubernetes "Nodes" to the cluster, **nodes only**. (cut and past the command from the previous "kubeadm init" output. It will look something like this...
    .. code:: bash

        $ kubeadm join --token 7f92b3... 10.1.20.21:6443 --discovery-token-ca-cert-hash sha256:9c4...

#. Verify kube-node 1 & 2 are up and running
    .. code:: bash

        $ kubectl get nodes
