import pandas as pd
file_path = "zomato_resturents_29-11-2025.csv"
df = pd.read_csv(file_path)

columns_to_remove = [
    'url',
    'sc-hqGPoI href',
    'sc-s1isp7-5 src',
    'sc-rbbb40-0',
    'sc-hqGPoI href 2',
    'sc-s1isp7-5 src 2',
    'sc-rbbb40-0 2',
    'sc-hqGPoI href 3',
    'sc-s1isp7-5 src 3',
    'sc-rbbb40-0 3',
    'Sc-rbbb40-0 3'
]
df = df.rename(columns={
    'sc-1hez2tp-0':'offer-1 %',
    'sc-1hp8d8a-0':'hotel-1',
    'sc-1q7bklc-1':'rating-1',
    'sc-1hez2tp-0 2':'menu-1',
    'sc-1hez2tp-0 3':'rate-1',
    'min-basic-info-right':'delivertime-1',
    'sc-1hez2tp-0 4':'offer-2 %',
    'sc-1hp8d8a-0 2':'hotel-2',
    'sc-1q7bklc-1 2':'rating-2',
    'sc-1hez2tp-0 5':'menu-2',
    'sc-1hez2tp-0 6':'rate-2',
    'min-basic-info-right 2':'delivertime-2',
    'sc-1hez2tp-0 7':'offer-3 %',
    'sc-1hp8d8a-0 3':'hotel-3',
    'sc-1q7bklc-1 3':'rating-3',
    'sc-1hez2tp-0 8':'menu-3',
    'sc-1hez2tp-0 9':'rate-3',
    'min-basic-info-right 3':'delivertime-3'
    })

df = df.drop(columns=[col for col in columns_to_remove if col in df.columns])

cols_to_clean = [
    'offer-1 %', 'offer-2 %', 'offer-3 %',
    'rate-1', 'rate-2', 'rate-3', 
    'delivertime-1', 'delivertime-2', 'delivertime-3'
]
for col in cols_to_clean:
    if col in df.columns:
        df[col] = df[col].astype(str).str.extract(r'(\d+)').astype(float)
rating_cols=['rating-1','rating-2','rating-3']
df[rating_cols]=df[rating_cols].fillna(0)
rate_cols=['rate-1','rate-2','rate-3']
rate_means=df[rate_cols].mean()
df[rate_cols]=df[rate_cols].fillna(rate_means)
df[rate_cols]=df[rate_cols].astype(int)
offer_cols=['offer-1 %', 'offer-2 %', 'offer-3 %']
df[offer_cols]=df[offer_cols].fillna('0')
new_file = "zomato_cleaned.csv"
df = df.drop(df.index[0]).reset_index(drop=True)
df.to_csv(new_file, index=False)
print("\nCleaned dataset saved as:", new_file)
import pandas as pd
import sqlite3
df = pd.read_csv("zomato_cleaned.csv")
conn=sqlite3.connect("zomato.db")
df.to_sql("restaurants",conn,if_exists="replace",index=False)
print("Data stored in database")
conn.close



