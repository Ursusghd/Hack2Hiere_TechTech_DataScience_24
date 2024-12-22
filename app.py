import streamlit as st
import pandas as pd
import joblib

# Charger le modèle
modele = joblib.load("modele_pred_credit_scoring.pkl")

# Titre de l'application
st.title("Prédiction de Scoring de Crédit")

# Formulaire
nom = st.text_input("Nom :")
sexe = st.selectbox("Sexe :", ["Homme", "Femme"])
age = st.number_input("Âge :", min_value=18, max_value=100)
duration = st.number_input("Durée du crédit (en mois) :", min_value=1)
credit_amount = st.number_input("Montant du crédit :", min_value=0)
checking_account = st.selectbox("Compte courant :", [0, 1, 2, 3])
saving_accounts = st.selectbox("Compte d'épargne :", [0, 1, 2, 3, 4])

# Bouton pour faire la prédiction
if st.button("Faire la Prédiction"):
    try:
        # Créer une dataframe avec les données utilisateur
        donnees = pd.DataFrame({
            "Duration": [duration],
            "Credit_amount": [credit_amount],
            "Checking_account": [checking_account],
            "Saving_accounts": [saving_accounts],
        })
        prediction = modele.predict(donnees)[0]
        prob_risque = modele.predict_proba(donnees)[:, 1][0]
        
        st.write(f"**Prédiction :** {'Crédit Accepté' if prediction == 1 else 'Crédit Refusé'}")
        st.write(f"**Probabilité de Risque Élevé :** {prob_risque:.2f}")
    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")
