# Lab 6 : Déploiement K8s d’un système MLOps Churn

## Étape 1 : Préparer l’environnement Kubernetes
Instructions :
Démarrer Minikube (driver Docker) :
![alt text](screenshots/lab6/image.png)

Créer un namespace dédié au lab :
Basculer le contexte courant sur ce namespace :
Vérifier :
![alt text](screenshots/lab6/image-1.png)

## Étape 2 : Préparer l’image Docker de l’API churn
Créer un environnement virtuel avec Python 3.12
![alt text](screenshots/lab6/image-2.png)

Préciser les dépendances dans requirements.txt
![alt text](screenshots/lab6/image-3.png)
Installer les dépendances :
![alt text](screenshots/lab6/image-4.png)

## Étape 3 : Créer le dossier des manifests Kubernetes
![alt text](screenshots/lab6/image-5.png)

## Étape 4 : Construire l’image Docker (tag versionné)

![alt text](screenshots/lab6/image-6.png)

![alt text](screenshots/lab6/image-7.png)

## Étape 5 : Charger explicitement l’image dans Minikube
![alt text](screenshots/lab6/image-8.png)

## Étape 6 : Deployment Kubernetes pour l’API churn
![alt text](screenshots/lab6/image-9.png)

## Étape 7 : Exposer l’API via un Service NodePort
![alt text](screenshots/lab6/image-10.png)

Tester l’API
![alt text](screenshots/lab6/image-12.png)

## Étape 8 : Injecter la configuration MLOps via ConfigMap
![alt text](screenshots/lab6/image-13.png)

Réappliquer le Deployment :
![alt text](screenshots/lab6/image-14.png)

## Étape 9 : Gérer les secrets (MONITORING_TOKEN)
![alt text](screenshots/lab6/image-15.png)

Réappliquer le Deployment :
![alt text](screenshots/lab6/image-16.png)

## Étape 10 : Mise en place des endpoints de santé et des probes Kubernetes pour l’API Churn
![alt text](screenshots/lab6/image-17.png)

## Étape 11 : Ajouter les probes (liveness / readiness / startup)
![alt text](screenshots/lab6/image-18.png)
![alt text](screenshots/lab6/image-19.png)

Redéployer l’application dans le cluster Kubernetes :
![alt text](screenshots/lab6/image-20.png)

## Étape 12 : Volume persistant pour registry + logs
![alt text](screenshots/lab6/image-21.png)

Monter le PVC dans le Deployment : l’API doit lire le modèle courant et écrire ses logs dans le même stockage persistant.
![alt text](screenshots/lab6/image-22.png)

## Étape 13 : NetworkPolicy
![alt text](screenshots/lab6/image-23.png)


## Étape 14 : Vérifications finales

![alt text](screenshots/lab6/image-24.png)

Tester l’endpoint /health :
![alt text](screenshots/lab6/image-25.png)

Tester l’endpoint /Predict :
![alt text](screenshots/lab6/image-26.png)

Lister les Pods pour choisir un Pod churn :
![alt text](screenshots/lab6/image-27.png)

Exécuter la détection de drift dans le Pod :
![alt text](screenshots/lab6/image-28.png)

