#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def feature_engineering(df):
    df['revenue_per_unit'] = df['revenue'] / (df['number_sold'] + 1e-5)
    df['cost_per_unit'] = df['order_cost'] / (df['order_quantity'] + 1e-5)
    df['lead_time_buffer'] = df['manufacturing_lead_time'] - df['supplier_lead_time']
    df.dropna(subset=['revenue', 'order_quantity'], inplace=True)
    return df

def build_model(df):
    features = ['product_type', 'shipping_carrier', 'supplier_name',
                'order_quantity', 'shipping_cost', 'manufacturing_cost',
                'lead_time_buffer']
    target = 'revenue'

    X = df[features]
    y = df[target]

    # Train-test split only for evaluation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    categorical_features = ['product_type', 'shipping_carrier', 'supplier_name']
    preprocessor = ColumnTransformer(transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ], remainder='passthrough')

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    # Train model on training data
    pipeline.fit(X_train, y_train)

    # Evaluate on test set
    y_test_pred = pipeline.predict(X_test)
    print(f"MAE: {mean_absolute_error(y_test, y_test_pred):.2f}")
    print(f"R^2 Score: {r2_score(y_test, y_test_pred):.2f}")

    # Predict on full data
    y_full_pred = pipeline.predict(X)
    df["predicted_revenue"] = y_full_pred

    df.to_csv("final_model_results.csv", index=False)
    print("Saved full dataset with predictions to 'final_model_results.csv'")

    joblib.dump(pipeline, 'supply_chain_revenue_model.pkl')
    print("Model saved as 'supply_chain_revenue_model.pkl'")

def main():
    df = pd.read_csv("cleaned_supply_chain_data.csv")
    df = feature_engineering(df)
    build_model(df)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




