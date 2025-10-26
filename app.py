import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# -------------------------------
# ⚙️ App Configuration
# -------------------------------
st.set_page_config(page_title="Startup KPI Dashboard", layout="wide")

# -------------------------------
# 🔁 Auto-refresh every 5 seconds
# -------------------------------
count = st_autorefresh(interval=5000, limit=None, key="datarefresh")

# -------------------------------
# 🔗 Google Sheets Live Data
# -------------------------------
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSVfWFKVbiQ3bnvaTn0I7NCjAMddv1ezKRm7lWGctNI01PCAFNAwhsFNVEHrD9DNUHRggW8LOWy0jzA/pub?output=csv"  # <--- replace with your link

@st.cache_data(ttl=5)
def load_data():
    try:
        df = pd.read_csv(SHEET_URL)
        df.columns = df.columns.str.strip()  # remove stray spaces
        return df
    except Exception as e:
        st.error(f"Error fetching or parsing data: {e}")
        return pd.DataFrame()  # return empty dataframe safely

# Load the live data
data = load_data()

# -------------------------------
# 🚀 Title
# -------------------------------
st.title("🚀 Startup KPI Dashboard — Live Google Sheets Sync")

# -------------------------------
# 🧩 KPI Metrics Section
# -------------------------------
if not data.empty:
    st.subheader("📊 Key Performance Indicators")

    total_revenue = data["Revenue"].sum()
    avg_churn = data["ChurnRate"].mean()
    avg_ltv = data["LTV"].mean()
    latest_month = data["Month"].iloc[-1]
    latest_revenue = data["Revenue"].iloc[-1]
    latest_users = data["ActiveUsers"].iloc[-1]

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
    col2.metric("📈 Avg LTV", f"${avg_ltv:,.0f}")
    col3.metric("💧 Avg Churn Rate", f"{avg_churn:.2f}%")

    col4, col5, col6 = st.columns(3)
    col4.metric("🗓️ Latest Month", latest_month)
    col5.metric("👥 Active Users", f"{latest_users:,}")
    col6.metric("💵 Revenue (Latest)", f"${latest_revenue:,}")

    st.divider()

    # -------------------------------
    # 📈 Charts
    # -------------------------------
    st.subheader("📈 Revenue and Active Users Over Time")
    st.line_chart(data.set_index("Month")[["Revenue", "ActiveUsers"]])

    st.subheader("💹 CAC vs LTV Comparison")
    st.line_chart(data.set_index("Month")[["CAC", "LTV"]])

    st.subheader("⚠️ Churn Rate Trend")
    st.line_chart(data.set_index("Month")[["ChurnRate"]])

    # -------------------------------
    # 🧠 Insights
    # -------------------------------
    st.subheader("🧠 Quick Insights")
    st.write(f"""
    - The dashboard is synced live with Google Sheets — updates appear within **5 seconds**.
    - **LTV/CAC ratio** shows customer monetization efficiency.
    - **Low churn rate** = better retention. **High growth rate** = improved user acquisition.
    """)

    st.dataframe(data, use_container_width=True)
    st.caption(f"Data auto-refreshes every 5 seconds. Refresh count: {count}")
else:
    st.warning("⚠️ No data found or failed to load. Please check your Google Sheet link.")

# -------------------------------
# 🧾 Footer
# -------------------------------
st.markdown("---")
st.caption("🚀 Built by **Saurabh Moharir** | PGDM (MDI Gurgaon) | Ex-Railways Engineer")
