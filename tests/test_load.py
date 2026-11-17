from bank_marketing_entrainement.data.load import load_bank_data
 
 
def test_shape():
    df = load_bank_data()
    assert df.shape == (45211, 17)
 
 
def test_target_column():
    df = load_bank_data()
    assert "y" in df.columns
