from src.components.DataIngestion import IngestData

try:
    obj = IngestData()
except Exception as e:
    print(e)
else:
    try:
        df = obj.fetch_data()
    except FileNotFoundError as e:
        print(e)


def test_columns():
    assert df.shape[1] == 12

def test_na():
    assert sum(df.isna().sum().values) > 0 