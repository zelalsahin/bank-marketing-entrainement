from pathlib import Path

import pandas as pd

from bank_marketing_entrainement.data.schema import validate_bank_data

# racine du repo : 3 dossiers au-dessus de ce fichier
DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "bank-full.csv"

def load_bank_data(path=DATA_PATH, validate=True):
     """Charge le jeu Bank Marketing (séparateur ;) et vérifie le contrat."""
     df = pd.read_csv(path, sep=";")
     if validate:
         df = validate_bank_data(df)
     return df


