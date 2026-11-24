import pandas as pd

from bank_marketing_entrainement.data.load import load_bank_data
from bank_marketing_entrainement.features.build import build_features, build_target


def test_pas_de_fuite():
    features = build_features(load_bank_data())
    assert "duration" not in features.columns
    assert "y" not in features.columns


def test_nouvelles_features():
    features = build_features(load_bank_data())
    assert set(features["deja_contacte"]) == {0, 1}
    assert set(features["solde_negatif"]) == {0, 1}
    assert set(features["tranche_age"]) == {"18-29", "30-45", "46-60", "61+"}


def test_cible():
    cible = build_target(load_bank_data())
    assert round(cible.mean(), 3) == 0.117


def test_meme_calcul_entrainement_et_prediction():
    df = load_bank_data()
    # à l'entraînement : tout le fichier
    entrainement = build_features(df).iloc[[0]].reset_index(drop=True)
    # en production : UN nouveau client, sans duration ni y
    client = df.iloc[0].drop(["duration", "y"]).to_dict()
    prediction = build_features(pd.DataFrame([client]))
    pd.testing.assert_frame_equal(entrainement, prediction)