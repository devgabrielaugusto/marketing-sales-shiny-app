from functools import partial
from pathlib import Path

import pandas as pd
from datetime import date, timedelta

app_dir = Path(__file__).parent

df_dictionary = pd.read_csv(app_dir / "makerting_data_dictionary.csv")
df_purchase = pd.read_csv(app_dir / "purchase_data_usd.csv")
df_purchase["DATE_DAY"] = pd.to_datetime(df_purchase["DATE_DAY"])
df_marketing = pd.read_csv(app_dir / "marketing_data_usd.csv")
df_marketing["DATE_DAY"] = pd.to_datetime(df_marketing["DATE_DAY"])