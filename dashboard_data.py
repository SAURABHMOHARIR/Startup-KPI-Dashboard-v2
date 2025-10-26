import pandas as pd
import numpy as np

# ------------------------------------------------------
# 🔗 STEP 1: Connect to Google Sheets (Published CSV Link)
# ------------------------------------------------------
# Replace this link with your own published Google Sheet link
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSVfWFKVbiQ3bnvaTn0I7NCjAMddv1ezKRm7lWGctNI01PCAFNAwhsFNVEHrD9DNUHRggW8LOWy0jzA/pub?output=csv"

# Read live data from Google Sheet
df = pd.read_csv(SHEET_URL)

# ------------------------------------------------------
# 🧮 STEP 2: (Optional) Perform Calculations or Add Columns
# ------------------------------------------------------
# If your Google Sheet already includes Revenue, ActiveUsers, CAC, and ChurnRate columns,
# you can dynamically compute LTV and other derived metrics here.

df['LTV'] = (df['Revenue'] / df['ActiveUsers']) * (1 / (df['ChurnRate'] / 100))
df['CustomerGrowthRate'] = df['CustomerGrowthRate'].round(2)
df['ChurnRate'] = df['ChurnRate'].round(2)
df['LTV'] = df['LTV'].round(2)

# ------------------------------------------------------
# 📊 STEP 3: Display or Use in Streamlit Dashboard
# ------------------------------------------------------
print("✅ Live data successfully fetched from Google Sheets!\n")
print(df.head())

# If you're using Streamlit:
# import streamlit as st
# st.title("🚀 Startup KPI Dashboard — Live from Google Sheets")
# st.dataframe(df)

