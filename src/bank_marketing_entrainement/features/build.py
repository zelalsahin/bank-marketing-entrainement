"""Jeu de features : le MÊME code pour l'entraînement et pour la prédiction.

Usage : uv run python -m bank_marketing_entrainement.features.build
"""

from pathlib import Path

import pandas as pd

from bank_marketing_entrainement.data.load import DATA_PATH, load_bank_data

FEATURES_PATH = Path(DATA_PATH).parent / "features.parquet"


def build_features(df):
    """Transforme des données clients en features pour le modèle."""
    # duration : connue seulement après l'appel (fuite) ; y : la cible
    features = df.drop(columns=["duration", "y"], errors="ignore")
    features["deja_contacte"] = (df["pdays"] != -1).astype(int)
    features["solde_negatif"] = (df["balance"] < 0).astype(int)
    features["nb_contacts_total"] = df["campaign"] + df["previous"]
    features["tranche_age"] = pd.cut(
        df["age"],
        bins=[17, 29, 45, 60, 100],
        labels=["18-29", "30-45", "46-60", "61+"],
    ).astype(str)
        # a_un_pret : 1 si prêt immobilier OU prêt perso (connu avant l'appel)
    features["a_un_pret"] = ((df["housing"] == "yes") | (df["loan"] == "yes")).astype(int)
    return features


def build_target(df):
    """La cible : 1 si le client a souscrit, 0 sinon."""
    return (df["y"] == "yes").astype(int)


def main():
    df = load_bank_data()
    table = build_features(df)
    table["target"] = build_target(df)
    table.to_parquet(FEATURES_PATH, index=False)
    print(f"Jeu de features écrit dans {FEATURES_PATH.name} : {table.shape}")


if __name__ == "__main__":
    main()