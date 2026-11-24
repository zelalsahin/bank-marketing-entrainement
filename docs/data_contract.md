# Contrat de données : Bank Marketing

- **Producteur** : équipe CRM de la banque
- **Consommateur** : pipeline `mlops_projet`
- **Format** : CSV, séparateur `;`, exactement 17 colonnes
- **Fréquence** : un fichier après chaque campagne
- **Version** : 1.0

## Règles principales
- age entre 18 et 100 ; y vaut `yes` ou `no`
- catégories dans la liste connue (`unknown` autorisé)
- balance sans limite (un solde peut être négatif)
- Détail complet : `src/mlops_projet/data/schema.py`

## Si le contrat n'est pas respecté
Le pipeline s'arrête, on n'entraîne pas, et on prévient le producteur.
