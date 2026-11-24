import pandera.pandas as pa
import pytest

from bank_marketing_entrainement.data.load import load_bank_data
from bank_marketing_entrainement.data.schema import validate_bank_data


@pytest.fixture
def df():
    return load_bank_data()


def test_donnees_valides(df):
    validate_bank_data(df)


def test_colonne_renommee(df):
    casse = df.rename(columns={"balance": "solde"})
    with pytest.raises(pa.errors.SchemaErrors):
        validate_bank_data(casse)


def test_age_negatif(df):
    casse = df.copy()
    casse.loc[0, "age"] = -5
    with pytest.raises(pa.errors.SchemaErrors):
        validate_bank_data(casse)


def test_cible_inconnue(df):
    casse = df.copy()
    casse.loc[0, "y"] = "peut-etre"
    with pytest.raises(pa.errors.SchemaErrors):
        validate_bank_data(casse)


def test_duree_impossible(df):
    casse = df.copy()
    casse.loc[0, "duration"] = 36000  # 10 heures
    with pytest.raises(pa.errors.SchemaErrors):
        validate_bank_data(casse)


