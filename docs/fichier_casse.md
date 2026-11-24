# Question 2 : un autre fichier cassé

**Règle cassée** : age entre 18 et 100

**Commande** : `sed 's/^58;/-58;/' data/bank-full.csv > data/bank-age-casse.csv`

**Prédiction** : 740 problème(s), car 740 clients ont 58 ans et chaque ligne
avec un âge de -58 viole la règle `in_range(18, 100)`.


**Résultat de check** : `CONTRAT NON RESPECTÉ : 740 problème(s)`, tous sur la
colonne `age` avec le check `in_range(18, 100)` et la valeur `-58`.

**Conclusion** : la prédiction était juste. Chaque ligne qui viole une règle
compte pour un problème. Grâce à `lazy=True`, pandera vérifie tout le fichier
et liste les 740 erreurs d'un coup, au lieu de s'arrêter à la première.