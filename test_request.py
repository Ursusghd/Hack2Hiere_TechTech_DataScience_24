import requests

# URL de base de l'API
url_base = 'http://127.0.0.1:8000'

# Test du endpoint d'accueil
response = requests.get(f"{url_base}/")
print("Réponse du endpoint d'accueil:", response.json())  # Assurez-vous que l'API renvoie un JSON

# Données d'exemple pour la prédiction
donnees_predire = {
    "Duration": 24,
    "Credit_amount": 5000,
    "Checking_account": 1,  # Exemple : 1 pour "faible", 2 pour "modéré", 3 pour "élevé"
    "Saving_accounts": 2   # Exemple : 1 pour "faible", 2 pour "modéré", 3 pour "élevé"
}

# Test du endpoint de prédiction
response = requests.post(f"{url_base}/predire", json=donnees_predire)

# Vérifiez le statut de la réponse et affichez le résultat
if response.status_code == 200:
    print("Réponse du endpoint de prédiction:", response.json())
else:
    print(f"Erreur {response.status_code}: {response.text}")
