# 🧪 MLOps Lab 01 — Pipeline de Churn de bout en bout

## Objectif du lab

Ce lab a pour objectif de mettre en place un **pipeline MLOps minimal mais réaliste**, couvrant :

* la génération et préparation des données,
* l’entraînement et la validation d’un modèle,
* la gestion des versions (model registry),
* le déploiement via une API,
* le monitoring (logs & data drift),
* le rollback de modèle.

---

## 📁 Étape 1 — Initialisation de la structure du projet

### Commandes exécutées

```bash
mkdir mlops-lab-01
cd mlops-lab-01

mkdir data
mkdir models
mkdir registry
mkdir logs
mkdir src

echo "" > registry\current_model.txt
```

### Arborescence attendue

```
mlops-lab-01/
 ├── data/
 ├── logs/
 ├── models/
 ├── registry/
 │    └── current_model.txt
 └── src/
```

---

## 🐍 Étape 2 — Préparation de l’environnement Python

### Création de l’environnement virtuel

```powershell
python -m venv venv_mlops
.\venv_mlops\Scripts\Activate.ps1
```

### Mise à jour de pip et installation des dépendances

```bash
pip install --upgrade pip
pip install pandas numpy scikit-learn fastapi uvicorn joblib
```

📸 **Screenshot – environnement activé et packages installés**

> ![alt text](screenshots\lab1\1.png)

---

## 📊 Étape 3 — Génération du dataset synthétique

### Script

* Fichier : `src/generate_data.py`
* Objectif : générer un dataset synthétique de churn reproductible

### Exécution

```bash
python src/generate_data.py
```

### Résultat

* Fichier généré : `data/raw.csv`
* Environ 1200 lignes de données clients

📸 **Screenshot – aperçu du fichier raw.csv**

> ![alt text](screenshots\lab1\2.png)

---

## 🔄 Étape 4 — Préparation des données (processed.csv)

> Cette étape transforme `raw.csv` en `processed.csv` et génère les statistiques d’entraînement (`train_stats.json`) utilisées pour le monitoring.

📸 **Screenshot – fichier processed.csv**

> ![alt text](screenshots\lab1\3.png)

📸 **Screenshot – train_stats.json**

> ![alt text](screenshots\lab1\4.png)

---

## 🤖 Étape 5 — Entraînement, versioning et validation du modèle

### Script

* Fichier : `src/train.py`
* Modèle : Régression logistique (pipeline scikit-learn)
* Gate de validation : `F1 ≥ 0.65` et meilleure que la baseline

### Exécution

```bash
python src/train.py
```

### Résultats

* Modèle sauvegardé dans `models/`
* Métadonnées ajoutées dans `registry/metadata.json`
* Modèle activé dans `registry/current_model.txt` si le gate est validé

📸 **Screenshot – métriques affichées**

> ![alt text](screenshots\lab1\5.png)

📸 **Screenshot – dossier models/**

> ![alt text](screenshots\lab1\6.png)

📸 **Screenshot – current_model.txt**

> ![alt text](screenshots\lab1\7.png)

---

## 📋 Étape 6 — Inspection de la registry et évaluation avancée

### Script

* Fichier : `src/evaluate.py`
* Ajout : optimisation du seuil de décision (F1 maximale)

### Exécution

```bash
python src/evaluate.py
```

### Résultats

* Nouveau modèle enregistré
* Seuil optimal calculé
* Registry mise à jour

📸 **Screenshot – seuil optimal et F1**

> ![alt text](screenshots\lab1\8.png)

📸 **Screenshot – metadata.json**

> ![alt text](screenshots\lab1\9.png)

---

## 🚀 Étape 7 — Déploiement via une API FastAPI

### Script

* Fichier : `src/api.py`
* Endpoints :

  * `/health`
  * `/predict`

### Lancement de l’API

```bash
uvicorn src.api:app --reload
```

### Tests

#### Health check

```http
GET http://127.0.0.1:8000/health
```

📸 **Screenshot – endpoint /health**

> ![alt text](screenshots\lab1\10.png)
> ![alt text](screenshots\lab1\11.png)

#### Prédiction

```json
{
  "tenure_months": 6,
  "num_complaints": 3,
  "avg_session_minutes": 12.5,
  "plan_type": "basic",
  "region": "AF",
  "request_id": "req-001"
}
```

📸 **Screenshot – réponse /predict**

> ![alt text](screenshots\lab1\12.png)
> ![alt text](screenshots\lab1\13.png)

📸 **Screenshot – logs/predictions.log**

> ![alt text](screenshots\lab1\14.png)

---

## 📈 Étape 8 — Détection de dérive des données (Data Drift)

### Script

* Fichier : `src/monitor_drift.py`
* Méthode : score Z entre données d’entraînement et données en production

### Exécution

```bash
python src/monitor_drift.py
```

### Résultat

* Analyse des dernières prédictions
* Détection (ou non) de drift sur les features numériques

📸 **Screenshot – sortie drift check**

> ![Valeurs z-score et alertes éventuelles](screenshots\lab1\15.png)

---

## 🔁 Étape 9 — Versioning avancé et rollback du modèle

### Entraînement d’une nouvelle version

```bash
python -c "from src.train import main; main(version='v2', gate_f1=0.60)"
```

📸 **Screenshot – entraînement v2**

> ![Nouvelle entrée dans metadata.json](screenshots\lab1\16.png)

---

### Script de rollback

* Fichier : `src/rollback.py`

#### Rollback automatique (version précédente)

```bash
python src/rollback.py
```

#### Rollback vers une version spécifique

```bash
python -c "from src.rollback import main; main('churn_model_v1_20251213_122625.joblib')"
```

📸 **Screenshot – rollback effectué**

> ![rollback](screenshots\lab1\17.png)
> ![current_model.txt mis à jour](screenshots\lab1\18.png)


---

## ✅ Conclusion

Ce lab démontre la mise en œuvre complète d’un **pipeline MLOps fonctionnel**, intégrant :

* reproductibilité,
* gouvernance de modèles,
* déploiement,
* monitoring,
* rollback.

Il constitue une base solide pour des systèmes ML industriels à plus grande échelle.
