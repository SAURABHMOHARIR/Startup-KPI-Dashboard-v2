import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Load Data ---
df = pd.read_csv('kpi_data.csv')

# --- Page Title ---
st.title("🚀 Startup KPI Dashboard - Data-Driven OKR Tracking")
st.caption("Simulated business metrics for a growing SaaS startup (like SalesCode.ai)")

# --- Key Metrics ---
st.subheader("📈 Key Highlights")
col1, col2, col3 = st.columns(3)
col1.metric("Avg. Monthly Revenue", f"${df['Revenue'].mean():,.0f}")
col2.metric("Avg. Active Users", f"{df['ActiveUsers'].mean():,.0f}")
col3.metric("Avg. Churn Rate", f"{df['ChurnRate'].mean():.2f}%")

# --- Charts ---
# --- Charts ---
st.subheader("📊 Revenue and Active Users Over Time")

# Create better formatted line charts
st.line_chart(data=df[['Revenue', 'ActiveUsers']].set_index(df['Month']))

st.subheader("💰 CAC and LTV Comparison")
chart_data = df[['Month', 'CAC', 'LTV']].set_index('Month')
st.line_chart(chart_data)

st.subheader("📉 Churn Rate Trend")
st.bar_chart(df.set_index('Month')['ChurnRate'])


# --- Strategic Insight Simulation ---
st.subheader("🧭 Strategic Scenario Analysis")
churn_input = st.slider("Simulate Churn Improvement (%)", min_value=-2.0, max_value=2.0, step=0.1, value=0.0)
df['AdjustedLTV'] = (df['Revenue'] / df['ActiveUsers']) * (1 / ((df['ChurnRate'] + churn_input) / 100))
avg_change = ((df['AdjustedLTV'].mean() - df['LTV'].mean()) / df['LTV'].mean()) * 100

if churn_input != 0:
    if churn_input < 0:
        st.success(f"💡 Improving churn by {abs(churn_input):.1f}% increases LTV by {avg_change:.2f}%")
    else:
        st.warning(f"⚠️ Increasing churn by {churn_input:.1f}% decreases LTV by {abs(avg_change):.2f}%")

st.line_chart(df.set_index('Month')[['LTV', 'AdjustedLTV']])

# --- Insights ---
st.subheader("🧠 Business Insights")
st.write("""
- **Revenue** shows consistent growth, averaging 10% month-on-month.  
- **LTV consistently exceeds CAC**, signaling strong unit economics.  
- **Low churn (<5%)** ensures retention-driven profitability.  
- The simulation above shows how even a **1% churn improvement** can boost LTV significantly — 
  the kind of decision insight a Founder’s Office tracks closely.
""")

# --- Footer ---
st.markdown("---")
st.caption("Built by Saurabh Moharir | MDI Gurgaon | Founder’s Office MT Project")
