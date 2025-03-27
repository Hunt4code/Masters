#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import joblib

def run_prediction():
    try:
        df = pd.read_csv("final_model_results.csv", encoding='utf-8')
        print("CSV loaded:", df.shape)
    except Exception as e:
        print("Error reading CSV:", e)
        return

    try:
        model = joblib.load("/Users/apple/Desktop/Git/Supply_Chain/supply_chain_revenue_model.pkl")
        print("Model loaded")
    except Exception as e:
        print("Error loading model:", e)
        return

    try:
        features = ['product_type', 'shipping_carrier', 'supplier_name',
                    'order_quantity', 'shipping_cost', 'manufacturing_cost',
                    'lead_time_buffer']

        preds = model.predict(df[features])
        df["deployment_prediction"] = preds

        df.to_csv("deployment_output.csv", index=False)
        print("Predictions saved to 'deployment_output.csv'")
    except Exception as e:
        print("Error during prediction:", e)


# In[ ]:





# In[ ]:




