Deploy the F5 Hello World Container
======================================
All of the following commands and yaml files are contained within the "f5-kube-demo" github repo.
    ``git clone https://github.com/vtog/f5-kube-demo.git``

Setup commands:

#. Create f5 hello world kubernetes deployment
    | :kbd:`$ kubectl create -f f5-hello-world-deployment.yaml`

    .. include:: ../f5-hello-world-deployment.yaml
        :literal:

#. Create f5 hello world kubernetes configmap
    | :kbd:`$ kubectl create -f f5-hello-world-configmap.yaml`

    .. include:: ../f5-hello-world-configmap.yaml
        :literal:

#. Create f5 hello world kubernetes service
    | **"type" needs to be set based on the mode configured for the f5 / kubernetes
      container connector. Edit the yaml file and change type to "NodePort" or "ClusterIP".  The example below shows "NodePort"**
    |
    | :kbd:`$ kubectl create -f f5-hello-world-service.yaml`

    .. include:: ../f5-hello-world-service.yaml
        :literal:

#. Verify f5-hello-world container is up and running
    | :kbd:`$ kubectl get pods -o wide`
