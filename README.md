# Water Leak Detector – Détection de fuites d'eau domestiques

🚰 **Projet de détection automatique de fuites d’eau utilisant XGBoost et Python.**

---

## Description

Ce projet permet de **prédire les fuites d’eau domestiques** à partir de mesures de consommation et de pression.
Il inclut :

* Prétraitement et préparation des labels.
* Analyse de la consommation et de la pression.
* Corrélations entre features.
* Entraînement du modèle XGBoost.
* Évaluation du modèle.
* Prédiction et interface utilisateur.

Le projet est conçu pour être modulaire et facile à étendre avec vos propres données.

---

## Structure du projet

```
water_leak_detector/
├── data/                  # Fichiers CSV de données réelles
├── src/                   # Scripts Python modulaires
│   ├── 1-chargement_de_donnees.py         # Chargement des données brutes
│   ├── 2-analyse_consommation.py          # Analyse exploratoire de la consommation
│   ├── 3-analyse_pression.py              # Analyse exploratoire de la pression
│   ├── 4-Corrélations.py                  # Analyse des corrélations entre features
│   ├── 5-preparation_des_labels.py        # Préparation des labels de fuite
│   ├── 6-train_test.py                    # Découpage train/test des données
│   ├── 7-Entraînement_XGBoost.py          # Entraînement du modèle XGBoost
│   ├── 8-Évaluation.py                     # Évaluation des performances du modèle
│   ├── 9-Prédiction.py                     # Script de prédiction sur de nouvelles mesures
│   └── 10-interface.py                     # Interface console/Colab pour saisir les mesures
```

---

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/<votre_utilisateur>/water_leak_detector.git
cd water_leak_detector
```

2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Utilisation

### 1️⃣ Préparer et analyser les données

Exécuter les scripts dans l'ordre :

```bash
python src/1-chargement_de_donnees.py
python src/2-analyse_consommation.py
python src/3-analyse_pression.py
python src/4-Corrélations.py
```

### 2️⃣ Préparer les labels et découper les données

```bash
python src/5-preparation_des_labels.py
python src/6-train_test.py
```

### 3️⃣ Entraîner le modèle XGBoost

```bash
python src/7-Entraînement_XGBoost.py
```

### 4️⃣ Évaluer le modèle

```bash
python src/8-Évaluation.py
```

### 5️⃣ Faire des prédictions

```bash
python src/9-Prédiction.py
```

### 6️⃣ Interface utilisateur

```python
from src.10-interface import interface_console, interface_colab
interface_console()  # Pour console
interface_colab()   # Pour Colab
```

---

## Licence

MIT License – libre pour usage personnel et académique.
