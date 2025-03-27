#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from sqlalchemy import create_engine

def fetch_table(engine, table_name):
    try:
        df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
        print(f"Fetched {table_name}: {df.shape}")
        return df
    except Exception as e:
        print(f"Failed to fetch {table_name}: {e}")
        return pd.DataFrame()

def merge_tables(products, suppliers, orders, quality):
    # Merge products with orders on 'sku'
    merged_df = pd.merge(products, orders, on='sku', how='left')

    # Merge with quality checks on 'sku' and 'supplier_id'
    merged_df = pd.merge(merged_df, quality, on='sku', how='left')

    # Merge with suppliers on 'supplier_id'
    merged_df = pd.merge(merged_df, suppliers, on='supplier_id', how='left')

    print(f"Final merged shape: {merged_df.shape}")
    return merged_df

def clean_data(df):
    # Example cleaning: drop rows with missing SKU or supplier_id
    df = df.dropna(subset=['sku', 'supplier_id'])
    df = df.drop_duplicates()
    print(f"Cleaned data shape: {df.shape}")
    return df

def main():
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')

    products_df = fetch_table(engine, "products")
    suppliers_df = fetch_table(engine, "suppliers")
    orders_df = fetch_table(engine, "orders")
    quality_df = fetch_table(engine, "quality_checks")

    merged_df = merge_tables(products_df, suppliers_df, orders_df, quality_df)
    cleaned_df = clean_data(merged_df)

    cleaned_df.to_csv("cleaned_supply_chain_data.csv", index=False)
    print("Saved cleaned data to 'cleaned_supply_chain_data.csv'")

if __name__ == "__main__":
    main()


# In[ ]:




