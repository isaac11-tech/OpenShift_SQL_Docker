step 1:
    get the namespace:
    oc get project
 result:
    NAME                                 DISPLAY NAME       STATUS
    itzchaktunik-dev                     itzchaktunik-dev   Active
    openshift-virtualization-os-images                      Active

step 2:
    creating MYSQL_DATABASE with new-app (deployment + pull image)

     oc new-app mysql:8 \
  -e MYSQL_ROOT_PASSWORD=1234 \
  -e MYSQL_DATABASE=MYSQL_DATABASE \
  -e MYSQL_USER=isaac \
  -e MYSQL_PASSWORD=0000 \
  --name=mysql


step 3:

  creating yamal file that creating pvc

           oc create -f - <<EOF
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: mysql-pvc
   spec:
     accessModes:
       - ReadWriteOnce
     resources:
       requests:
         storage: 1Gi
   EOF


step 4:

concerting the pvc to the mysql server

oc set volume deployment/mysql \
  --add \
  --name=mysql-storage \
  --mount-path=/var/lib/mysql \
  --type=pvc \
  --claim-name=mysql-pvc


