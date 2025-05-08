from src.constants import URL
import pandas as pd
from pydantic import BaseModel, Field


class IngestData(BaseModel):
    url: str = Field(default=URL, description='Link for the Dataset')

    def fetch_data(self):
        try:
            df = pd.read_csv(f'{self.url}')
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            return df