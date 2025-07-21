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

st.subheader("📊 Incremental ROAS (Simulated)")

# Simulate control/exposed groups
control = tracking[tracking['group'] == 0]
exposed = tracking[tracking['group'] == 1]

ctrl_avg = control.groupby('user_id')['revenue'].sum().mean()
exp_avg = exposed.groupby('user_id')['revenue'].sum().mean()
incremental_roas = round((exp_avg - ctrl_avg) / total_payout, 2) if total_payout else 0

st.write(f"**Control Revenue/User**: ₹{ctrl_avg:.2f}")
st.write(f"**Exposed Revenue/User**: ₹{exp_avg:.2f}")
st.metric("Incremental ROAS", f"{incremental_roas:.4f}x")

# --- Top Influencers ---
st.subheader("🏆 Top Influencers by ROAS")

roas_df = tracking.groupby("influencer_id")['revenue'].sum().reset_index()
roas_df = pd.merge(roas_df, payouts[['influencer_id', 'total_payout']], on="influencer_id")
roas_df['roas'] = roas_df['revenue'] / roas_df['total_payout']
top_inf = pd.merge(roas_df, influencers, left_on='influencer_id', right_on='id')
top_inf = top_inf.sort_values('roas', ascending=False)
st.dataframe(top_inf[['name', 'platform', 'category', 'follower_count', 'roas']].head(5), use_container_width=True)

# Poor ROIs
st.markdown("### ⚠️ Influencers with Poor ROAS (<1x)")
poor_roas_df = top_inf[top_inf['roas'] < 1].sort_values('roas')
if not poor_roas_df.empty:
    st.dataframe(poor_roas_df[['name', 'platform', 'category', 'roas']], use_container_width=True)
else:
    st.success("All influencers are performing above 1x ROAS 🚀")