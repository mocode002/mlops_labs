# 🧪 MLOps Lab 05 — Du Notebook au Déploiement Conteneurisé d’un Modèle ML

## Objectif du lab

Ce lab a pour objectif de **passer d’un projet Machine Learning local à un déploiement conteneurisé**, en utilisant **Docker** puis **Docker Compose**, jusqu’à l’exécution de l’API churn dans un environnement reproductible.

---

## ⚙️ Étape 1 — Vérification de Docker et premier conteneur

Docker est correctement installé et fonctionnel.
Les commandes de base (`docker version`, `docker ps`, `docker run`) ont été testées avec succès.

📸 **Docker version, docker ps et lancement de Nginx**

> ![alt text](screenshots/lab5/image.png)

📸 **Interface web par défaut de Nginx**

> ![alt text](screenshots/lab5/image-1.png)

📸 **Arrêt et suppression du conteneur Nginx**

> ![alt text](screenshots/lab5/image-2.png)

**Constat :**

* Docker fonctionne correctement
* Le mapping de ports est opérationnel
* Les conteneurs peuvent être arrêtés et supprimés sans erreur

---

## 🐧 Étape 3 — Shell Linux isolé dans un conteneur Ubuntu

Un conteneur Ubuntu interactif a été lancé afin d’exécuter des commandes Linux de base.

📸 **Commandes Linux dans le conteneur**

> ![alt text](screenshots/lab5/image-3.png)

📸 **Installation d’un paquet dans le conteneur**

> ![alt text](screenshots/lab5/image-4.png)

📸 **Sortie du conteneur Ubuntu**

> ![alt text](screenshots/lab5/image-5.png)

**Constat :**

* Le conteneur fournit un environnement Linux isolé
* Les paquets peuvent être installés dynamiquement
* Le conteneur persiste après arrêt

---

## 📦 Étape 5 — Vérification de l’API churn existante

L’API churn du projet **mlops-lab-01** fonctionne correctement en local avant la conteneurisation.

📸 **API churn fonctionnelle**

> ![alt text](screenshots/lab5/image-6.png)

---

## 📄 Étape 6 — Création du fichier `requirements.txt`

Les dépendances nécessaires à l’API ont été listées pour permettre une installation automatique dans l’image Docker.

📸 **Fichier requirements.txt**

> ![alt text](screenshots/lab5/image-7.png)

---

## 🐳 Étape 7 — Création du Dockerfile

Un `Dockerfile` a été créé pour définir l’image Docker de l’API churn.

📸 **Dockerfile de l’API churn**

> ![alt text](screenshots/lab5/image-8.png)

---

## 🧠 Étape 8 — Vérification du modèle actif

Un modèle entraîné est bien présent et référencé comme modèle courant dans le registry.

📸 **Modèle actif dans le registry**

> ![alt text](screenshots/lab5/image-9.png)

---

## 🏗️ Étape 9 — Construction de l’image Docker

L’image Docker de l’API churn a été construite avec succès.

📸 **Construction de l’image Docker**

> ![alt text](screenshots/lab5/image-10.png)

📸 **Vérification de l’image dans Docker**

> ![alt text](screenshots/lab5/image-11.png)

**Constat :**

* L’image `churn-api:latest` est correctement créée
* Toutes les dépendances sont intégrées dans l’image

---

## 🚀 Étape 10 — Lancement de l’API churn dans un conteneur

L’API est lancée dans un conteneur Docker et exposée sur le port 8000.

📸 **Conteneur API churn en cours d’exécution**

> ![alt text](screenshots/lab5/image-12.png)

---

## 🧪 Étape 11 — Vérification des logs dans le conteneur

Les logs générés par l’API sont bien présents à l’intérieur du conteneur.

📸 **Logs de l’API churn**

> ![alt text](screenshots/lab5/image-13.png)

---

## 🔁 Étape 12 — Orchestration locale avec Docker Compose

Un fichier `docker-compose.yml` a été créé pour orchestrer l’API churn.

📸 **Fichier docker-compose.yml**

> ![alt text](screenshots/lab5/image-14.png)

---

## ▶️ Étape 13 — Démarrage de l’API via Docker Compose

L’API est lancée à l’aide de Docker Compose.

📸 **Démarrage des services**

> ![alt text](screenshots/lab5/image-15.png)

📸 **Conteneur actif via Docker Compose**

> ![alt text](screenshots/lab5/image-16.png)

---

## 📊 Étape 14 — Observation des logs en temps réel

Les logs de l’API sont observés en temps réel pendant l’exécution.

📸 **Logs Docker Compose**

> ![alt text](screenshots/lab5/image-17.png)

📸 **API active avec logs**

> ![alt text](screenshots/lab5/image-18.png)

---

## ✅ Conclusion

Ce lab valide la **conteneurisation complète de l’API churn**, depuis le projet ML local jusqu’à un **déploiement reproductible avec Docker Compose**.

Il permet d’assurer :

* un environnement d’exécution isolé,
* une API facilement déployable,
* une intégration cohérente avec Git et les labs MLOps précédents.