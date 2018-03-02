Deploy the F5 / Kubernetes Container Connecter
=================================================
All of the following commands and yaml files are contained within the "f5-kube-demo" github repo.
    ``git clone https://github.com/vtog/f5-kube-demo.git``

For a more thorough explanation see http://clouddocs.f5.com/containers/v2/kubernetes/index.html

Basic container connector setup commands:

#. Create bigip login secret
    | :kbd:`$ kubectl create secret generic bigip-login -n kube-system --from-literal=username=admin --from-literal=password=admin`
#. Create kubernetes service account for bigip controller
    | :kbd:`$  kubectl create serviceaccount k8s-bigip-ctlr -n kube-system`
#. Create cluster role for bigip service account (admin rights, but can be modified for your environment)
    | :kbd:`$ kubectl create clusterrolebinding k8s-bigip-ctlr-clusteradmin --clusterrole=cluster-admin --serviceaccount=kube-system:k8s-bigip-ctlr`

Use one or the other of the following commands depending on deployment type. nodeport vs. cluster  (see http://clouddocs.f5.com/containers/v2/kubernetes/kctlr-modes.html)

#. **NodePort** example
    | :kbd:`$ kubectl create -f  f5-nodeport-deployment.yaml`

    .. include:: ../f5-nodeport-deployment.yaml
        :literal:

#. **ClusterIP** example
    | :kbd:`$ kubectl create -f f5-cluster-deployment.yaml`

    .. include:: ../f5-cluster-deployment.yaml
        :literal:

    | :kbd:`$ kubectl create -f f5-bigip-node.yaml`

    .. include:: ../f5-bigip-node.yaml
        :literal:

#. Verify f5 container connector is up and running
    | :kbd:`$ kubectl get pods -n kube-system -o wide`
