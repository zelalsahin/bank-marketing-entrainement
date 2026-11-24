"""Contrat de données du jeu Bank Marketing."""

import pandera.pandas as pa

OUI_NON = ["yes", "no"]

bank_schema = pa.DataFrameSchema(
    {
        "age": pa.Column(int, pa.Check.in_range(18, 100)),
        "job": pa.Column(str, pa.Check.isin([
            "admin.", "blue-collar", "entrepreneur", "housemaid",
            "management", "retired", "self-employed", "services",
            "student", "technician", "unemployed", "unknown",
        ])),
        "marital": pa.Column(str, pa.Check.isin(["married", "single", "divorced"])),
        "education": pa.Column(str, pa.Check.isin(["primary", "secondary", "tertiary", "unknown"])),
        "default": pa.Column(str, pa.Check.isin(OUI_NON)),
        "balance": pa.Column(int),
        "housing": pa.Column(str, pa.Check.isin(OUI_NON)),
        "loan": pa.Column(str, pa.Check.isin(OUI_NON)),
        "contact": pa.Column(str, pa.Check.isin(["cellular", "telephone", "unknown"])),
        "day": pa.Column(int, pa.Check.in_range(1, 31)),
        "month": pa.Column(str, pa.Check.isin([
            "jan", "feb", "mar", "apr", "may", "jun",
            "jul", "aug", "sep", "oct", "nov", "dec",
        ])),
        "duration": pa.Column(int, pa.Check.ge(0)),
        "campaign": pa.Column(int, pa.Check.ge(1)),
        "pdays": pa.Column(int, pa.Check.ge(-1)),
        "previous": pa.Column(int, pa.Check.ge(0)),
        "poutcome": pa.Column(str, pa.Check.isin(["success", "failure", "other", "unknown"])),
        "y": pa.Column(str, pa.Check.isin(OUI_NON)),
    },
    strict=True,  # aucune colonne en plus, aucune en moins
)


def validate_bank_data(df):
    """Vérifie le contrat. Lève une erreur qui liste TOUS les problèmes."""
    return bank_schema.validate(df, lazy=True)