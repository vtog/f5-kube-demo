Deploy the F5 Hello World Container
======================================
All of the following commands and yaml files are contained within the "f5-kube-demo" github repo.
    .. code:: bash

        $ git clone https://github.com/vtog/f5-kube-demo.git

**Basic f5-hello-world application deployment commands:**

#. Create f5 hello world kubernetes deployment
    .. code:: bash

        $ kubectl create -f f5-hello-world-deployment.yaml

    .. include:: ../f5-hello-world-deployment.yaml
        :literal:

#. Create f5 hello world kubernetes configmap
    .. code:: bash

        $ kubectl create -f f5-hello-world-configmap.yaml

    .. include:: ../f5-hello-world-configmap.yaml
        :literal:

#. Create f5 hello world kubernetes service
    **"type" needs to be set based on the mode configured for the f5 /
    kubernetes container connector. Edit the yaml file and change type to
    "NodePort" or "ClusterIP".  The example below shows "NodePort"**

    .. code:: bash

        $ kubectl create -f f5-hello-world-service.yaml

    .. include:: ../f5-hello-world-service.yaml
        :literal:

#. Verify f5-hello-world container is up and running
    .. code:: bash

        $ kubectl get pods -o wide
        goto http://10.1.10.81

#. Add or remove resources to the application.  Edit the yaml file and change the desired number of replicas
    .. code:: bash

        $ vim f5-hello-world-configmap-modify.yaml
        $ kubectl apply -f f5-hello-world-configmap-modify.yaml
