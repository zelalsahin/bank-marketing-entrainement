# Question 2 : un autre fichier cassé

**Règle cassée** : age entre 18 et 100

**Commande** : `sed 's/^58;/-58;/' data/bank-full.csv > data/bank-age-casse.csv`

**Prédiction** : 740 problème(s), car 740 clients ont 58 ans et chaque ligne
avec un âge de -58 viole la règle `in_range(18, 100)`.