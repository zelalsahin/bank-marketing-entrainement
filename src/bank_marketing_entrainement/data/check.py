"""Vérifie qu'un fichier respecte le contrat de données.
Usage : uv run python -m mlops_projet.data.check data/bank-full.csv
"""
import sys


import pandera.pandas as pa

from bank_marketing_entrainement.data.load import load_bank_data

def main() :
     chemin = sys.argv[1]
     try:
        df = load_bank_data(chemin)
     except pa.errors.SchemaErrors as erreurs:
        print(f"CONTRAT NON RESPECTÉ : {len(erreurs.failure_cases)} problème(s)")
        print(erreurs.failure_cases[["column", "check", "failure_case"]].head(10))
        sys.exit(1)
     print(f"Contrat respecté : {len(df)} lignes, {df.shape[1]} colonnes")


if __name__ == "__main__":
 main()
