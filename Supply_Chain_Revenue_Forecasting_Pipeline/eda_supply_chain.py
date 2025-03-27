#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(csv_path="cleaned_supply_chain_data.csv"):
    return pd.read_csv(csv_path)

def run_eda(df):
    print("Basic Info:")
    print(df.info())
    
    print("\nSummary Statistics:")
    print(df.describe())

    print("\nNull Value Counts:")
    print(df.isnull().sum())

def visualize(df):
    # Top 10 products by revenue
    top_products = df.groupby('sku')['revenue'].sum().nlargest(10)
    top_products.plot(kind='barh', title="Top 10 Products by Revenue")
    plt.xlabel("Total Revenue")
    plt.tight_layout()
    plt.show()

    # Defect rates by supplier
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='supplier_id', y='defect_rate')
    plt.title("Defect Rate by Supplier")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Shipping cost distribution
    sns.histplot(df['shipping_cost'], bins=20, kde=True)
    plt.title("Shipping Cost Distribution")
    plt.tight_layout()
    plt.show()

def main():
    df = load_data()
    run_eda(df)
    visualize(df)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




