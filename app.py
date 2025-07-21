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

st.sidebar.header("📂 Upload Custom Data (Optional)")
uploaded_files = {
    "influencers": st.sidebar.file_uploader("Influencers CSV", type=["csv"]),
    "posts": st.sidebar.file_uploader("Posts CSV", type=["csv"]),
    "tracking": st.sidebar.file_uploader("Tracking Data CSV", type=["csv"]),
    "payouts": st.sidebar.file_uploader("Payouts CSV", type=["csv"])
}

def load_or_upload(file, fallback):
    if file:
        return pd.read_csv(file)
    return fallback

inf_generated, posts_generated, tracking_generated, payouts_generated = load_data()
influencers = load_or_upload(uploaded_files["influencers"], inf_generated)
posts = load_or_upload(uploaded_files["posts"], posts_generated)
tracking = load_or_upload(uploaded_files["tracking"], tracking_generated)
payouts = load_or_upload(uploaded_files["payouts"], payouts_generated)

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
    
st.markdown("### 💡 Best Personas by Average ROAS")

persona_df = pd.merge(roas_df, influencers, left_on="influencer_id", right_on="id")
persona_group = persona_df.groupby(["category", "gender"]).agg({
    "revenue": "sum",
    "total_payout": "sum"
}).reset_index()
persona_group["roas"] = persona_group["revenue"] / persona_group["total_payout"]
persona_group = persona_group.sort_values("roas", ascending=False)

st.dataframe(persona_group[['category', 'gender', 'roas']], use_container_width=True)


plt.figure(figsize=(10, 4))
sns.barplot(data=persona_group, x="category", y="roas", hue="gender")
plt.ylabel("Average ROAS")
plt.title("Best Personas by ROAS")
st.pyplot(plt.gcf())
plt.clf()

st.subheader("Engagement Rate by Platform")

posts['engagement_rate'] = (posts['likes'] + posts['comments']) / posts['reach']
plt.figure(figsize=(10, 4))
sns.boxplot(data=posts, x='platform', y='engagement_rate')
st.pyplot(plt.gcf())
plt.clf()
