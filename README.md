# Hack2Hiere_TechTech_DataScience_24
Hack2Hiere  , ceci est le repository du Binome constituté de DERRA MAMOUNATA ET GBAGUIDI URSUS

https://binome24.streamlit.app/

Projet d'Analyse et de Classification de Données : German Credit Data

Description du Projet

Ce projet consiste à analyser, prétraiter et modéliser un ensemble de données nommé German Credit Data. L'objectif est de prédire le risque de crédit (étiqueté comme "Risk") pour un ensemble de clients en utilisant des techniques de classification. Le projet inclut des étapes d'analyse exploratoire, de préparation des données, de gestion des valeurs aberrantes et de construction de modèles de machine learning, avec une attention particulière aux modèles d'ensemble (bagging, boosting et stacking).


# Projet de Prédiction de Scoring de Crédit

Ce projet vise à créer une application permettant de prédire si un crédit sera accepté ou refusé en fonction de différentes données financières d'un utilisateur. L'application utilise un modèle de Machine Learning pour effectuer la prédiction à partir de paramètres fournis par l'utilisateur via un formulaire en ligne.

## Fonctionnalités

- Prédiction du scoring de crédit basé sur des critères financiers tels que :
  - Durée du crédit
  - Montant du crédit
  - État du compte courant
  - État des comptes d'épargne
- Interface utilisateur interactive réalisée avec Streamlit.
- API backend basée sur FastAPI pour gérer les requêtes et la prédiction.

## Technologies Utilisées

- **Backend** : FastAPI
- **Frontend** : Streamlit
- **Machine Learning** : Modèle KNeighborsClassifier pour la prédiction
- **Outils de Déploiement** : GitHub, Streamlit Cloud

## Prérequis

1. Python 3.7 ou supérieur
2. Installez les dépendances requises :

```bash
pip install -r requirements.txt

```
Il est accessible en ligne sur le lien https://binome24.streamlit.app/
Conclusion

Ce projet a permis de développer une approche systématique pour l'analyse et la classification des données. Il met en évidence l'importance de la préparation des données et de l'exploration des différents modèles pour obtenir des prédictions précises. Le meilleur score obtenue actuelle est de 78,5% . Par la suite nous envisagons verifier la pertinence de la variable feature credit amount afin de voir un possible traitement des valeur abberantes differnetes de celle qu'on a fait , aussi il est prevu de faire une feature creation après des recherches approfondies sur le domaine afin d'augmenter la performance du modele 

