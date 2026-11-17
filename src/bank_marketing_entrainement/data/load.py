from pathlib import Path
 
import pandas as pd
 
# racine du repo : 3 dossiers au-dessus de ce fichier
DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "bank-full.csv"
 
 
def load_bank_data(path=DATA_PATH):
    """Charge le jeu Bank Marketing (séparateur ;)."""
    return pd.read_csv(path, sep=";")
