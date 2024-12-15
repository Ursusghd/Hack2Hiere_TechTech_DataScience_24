# Hack2Hiere_TechTech_DataScience_24
Hack2Hiere  , ceci est le repository du Binome constituté de DERRA MAMOUNATA ET GBAGUIDI URSUS

Projet d'Analyse et de Classification de Données : German Credit Data

Description du Projet

Ce projet consiste à analyser, prétraiter et modéliser un ensemble de données nommé German Credit Data. L'objectif est de prédire le risque de crédit (étiqueté comme "Risk") pour un ensemble de clients en utilisant des techniques de classification. Le projet inclut des étapes d'analyse exploratoire, de préparation des données, de gestion des valeurs aberrantes et de construction de modèles de machine learning, avec une attention particulière aux modèles d'ensemble (bagging, boosting et stacking).



Étapes Réalisées

1. Prétraitement des Données

Suppression de colonnes inutiles : La colonne "Unnamed: 0" a été supprimée car elle n'apporte aucune information utile.

Encodage des variables catégoriques :

La variable cible "Risk" a été encodée ("good" = 0, "bad" = 1) avec un LabelEncoder.

Les autres variables catégoriques (à savoir : "Sex", "Housing", "Purpose", etc.) ont été transformées en variables numériques.

2. Analyse Exploratoire des Données (EDA)

Visualisation des variables quantitatives :

Variables discrètes : Diagrammes en barres.

Variables continues : Histogrammes et boxplots pour analyser la distribution des données.

Visualisation des variables qualitatives : Diagrammes en secteurs et diagrammes en barres pour les variables nominales et ordinales.

Matrice de corrélation : Une heatmap a été tracée pour étudier les relations entre les variables numériques.

3. Gestion des Outliers
   Nous avons opter pour l'instant pour une standarisation

5. Sélection des Variables Significatives

Les variables ayant une corrélation inférieure à 10 % avec la cible "Risk" ont été supprimées. Les variables significatives conservées sont :

Duration

Credit amount

Checking account

Saving accounts

5. Transformation des Données

Standardisation : Toutes les variables explicatives (X) ont été standardisées pour faciliter l'entraînement des modèles.

6. Entraînement et Évaluation des Modèles

a. Modèles de Base

K-Nearest Neighbors (KNN) : Avec recherche de paramètres (GridSearchCV) pour optimiser le nombre de voisins et les types de distances.

Decision Tree Classifier : Évaluation avec des métriques standards.

b. Modèles d'Ensemble

Bagging : Entraînement avec des base learners comme KNN et Decision Tree.

Boosting : Implémentation avec des algorithmes comme AdaBoost.

Stacking : Combinaison de plusieurs modèles de base (sans GridSearch).

c. Support Vector Machine (SVM)

Recherche de paramètres avec GridSearchCV pour trouver le meilleur noyau et les hyperparamètres optimaux.

Résultats et Analyse

Les performances des modèles ont été évaluées à l'aide des métriques suivantes :

Précision (Accuracy)

Rappel (Recall)

F1-Score

Le meilleur modèle sera sélectionné en fonction de ces métriques, et des recommandations seront faites pour de futures améliorations.

Conclusion

Ce projet a permis de développer une approche systématique pour l'analyse et la classification des données. Il met en évidence l'importance de la préparation des données et de l'exploration des différents modèles pour obtenir des prédictions précises. Le meilleur score obtenue actuelle est de 78,5% . Par la suite nous envisagons verifier la pertinence de la variable feature credit amount afin de voir un possible traitement des valeur abberantes differnetes de celle qu'on a fait , aussi il est prevu de faire une feature creation après des recherches approfondies sur le domaine afin d'augmenter la performance du modele 

