import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Food Delivery Dashboard",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #f6f8fb;
}

.kpi-card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    border-left: 6px solid #ff6b6b;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.kpi-title {
    font-size: 14px;
    color: #6c757d;
}

.kpi-value {
    font-size: 28px;
    font-weight: bold;
    color: #212529;
}

</style>
""", unsafe_allow_html=True)

st.title("🍔 Online Food Delivery Analytics Dashboard")

# -------------------------------
# MYSQL CONNECTION
# -------------------------------
username = "root"
password = "12345678"
host = "localhost"
database = "FoodDelivery"

engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
)

# -------------------------------
# LOAD DATA FROM MYSQL
# -------------------------------
query = "SELECT * FROM onlinefoods"
df = pd.read_sql(query, engine)

# -------------------------------
# KPI CALCULATIONS
# -------------------------------
total_orders = len(df)

total_revenue = df["Order_Value"].sum()

avg_order_value = df["Order_Value"].mean()

avg_delivery_time = df["Delivery_Time_Min"].mean()

cancellation_rate = (df["Order_Status"] == "Cancelled").mean() * 100

avg_delivery_rating = df["Delivery_Rating"].mean()

profit_margin_pct = (df["profit_margin_pct"].sum())

st.subheader("📊 Key Business Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Orders</div>
        <div class="kpi-value">{total_orders:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Revenue</div>
        <div class="kpi-value">${total_revenue:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Average Order Value</div>
        <div class="kpi-value">${avg_order_value:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Avg Delivery Time</div>
        <div class="kpi-value">{avg_delivery_time:.1f} mins</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
col5, col6, col7, col8 = st.columns(4)

with col5:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Cancellation Rate</div>
        <div class="kpi-value">{cancellation_rate:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Delivery Rating</div>
        <div class="kpi-value">{avg_delivery_rating:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col7:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Profit Margin</div>
        <div class="kpi-value">{profit_margin_pct:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col8:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Orders per Dataset</div>
        <div class="kpi-value">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# DATA PREVIEW
# -------------------------------

st.markdown("---")
st.subheader("📋 Data Preview")


st.dataframe(
    df.head(100000),
    use_container_width=True,
    height=400
)

st.markdown("---")