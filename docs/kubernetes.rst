Setup Kubernetes
----------------
The following steps will walk you through building your own kubernetes cluster utilizing the Ravello BP.

Each command need to be run on each **Node** unless otherwise specified.

#. From the jumphost using putty open a new SSH session to each of the following nodes:
    | kube-master
    | kube-node1
    | kube-node2
#. On each node edit /etc/hosts and add the following static host entries:
    | 10.1.20.21  kube-master
    | 10.1.20.22  kube-node1
    | 10.1.20.23  kube-node2
#. On each node update Ubuntu
    | # apt update
    | # apt upgrade -y
#. On each node add the docker repo
    | # curl \-fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add \-
    | # add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#. On each node add the kubernetes repo
    | # curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    | # cat <<EOF > /etc/apt/sources.list.d/kubernetes.list
    | deb http://apt.kubernetes.io/ kubernetes-xenial main
    | EOF
#. On each node install docker
    | # apt update
    | # apt install -y docker-ce
#. Is docker up and running?
    | # docker run hello-world
#. Install kubernetes
    | # apt install -y kubelet kubeadm kubectl
#. Setup the master (default flannel network 10.244.0.0/16)
    | # kubeadm init --pod-network-cidr=10.244.0.0/16
#. This following should be run on the master node for any user account needing to issue "kubectl" commands
    | # mkdir -p $HOME/.kube
    | # sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    | # sudo chown $(id -u):$(id -g) $HOME/.kube/config
#. Install flannel on the Master node (default flannel network 10.244.0.0/16)
    | # kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
#. Is Kubernetes up and running on the Mater?
    | # kubectl get pods --all-namespaces
#. Add the kubernetes "Nodes" to the cluster. (cut and past the command from the previous kubeadm init output) It will look something like this...
    | kubeadm join --token 7f92b3... 10.1.20.21:6443 --discovery-token-ca-cert-hash sha256:9c4...
