import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Influencer ROAS tracking Dashboard", layout="wide")
@st.cache_data
def load_data():
    inf = pd.read_csv("data/influencers.csv")
    posts = pd.read_csv("data/posts.csv")
    tracking = pd.read_csv("data/tracking_data.csv")
    payouts = pd.read_csv("data/payouts.csv")
    return inf, posts, tracking, payouts

influencers,posts,tracking,payouts = load_data()

st.title("📊 HealthKart Influencer Campaign Dashboard")
st.subheader("📈 Key Metrics")
total_revenue = tracking['revenue'].sum()
total_payout = payouts['total_payout'].sum()
roas = round(total_revenue / total_payout, 2) if total_payout else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{total_revenue:,.2f}")
col2.metric("Total Payout", f"₹{total_payout:,.2f}")
col3.metric("ROAS", f"{roas}x")