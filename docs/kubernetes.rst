Build a Kubernetes Cluster
==========================
The following steps will walk you through building the kubernetes cluster. The Ravello BP has:
    - 1x Master (kube-master)
    - 2x Minions (kube-node1 & kube-node2)

Each of the following commands need to be run on all three servers unless otherwise specified.

#. From the jumphost using putty open a new SSH session to each of the following servers:
    | kube-master
    | kube-node1
    | kube-node2
#. Edit /etc/hosts and add the following static host entries:
    | 10.1.20.21    kube-master
    | 10.1.20.22    kube-node1
    | 10.1.20.23    kube-node2
#. Upgrade Ubuntu to ensure an up-to-date OS
    | apt update && apt upgrade -y
#. Add the docker repo
    | curl \-fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add \-
    | add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#. Add the kubernetes repo
    | curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    | cat <<EOF > /etc/apt/sources.list.d/kubernetes.list
    | deb http://apt.kubernetes.io/ kubernetes-xenial main
    | EOF
#. Install docker
    | apt update && apt install -y docker-ce
#. Check docker is up and running?
    | docker run hello-world
#. Install kubernetes
    | apt install -y kubelet kubeadm kubectl
#. Setup the master, **master only** (default flannel network 10.244.0.0/16)
    | kubeadm init --pod-network-cidr=10.244.0.0/16
#. This following should be run on the master for any user account needing to issue "kubectl" commands
    | mkdir -p $HOME/.kube
    | sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    | sudo chown $(id -u):$(id -g) $HOME/.kube/config
#. Install flannel on the master, **master only** (default flannel network 10.244.0.0/16)
    | kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
#. Check Kubernetes is up and running on the master?
    | kubectl get pods --all-namespaces
#. Add the kubernetes "Nodes" to the cluster. **nodes only** (cut and past the command from the previous kubeadm init output) It will look something like this...
    | kubeadm join --token 7f92b3... 10.1.20.21:6443 --discovery-token-ca-cert-hash sha256:9c4...
