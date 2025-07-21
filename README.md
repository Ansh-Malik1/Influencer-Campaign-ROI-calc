# 📊 Influencer Campaign ROAS Dashboard

A Streamlit dashboard to analyze the performance of influencer marketing campaigns. It supports campaign-level and influencer-level filtering, calculates ROAS (Return on Ad Spend), simulates incremental ROAS (A/B testing style), and provides insights via charts and persona breakdowns.

## Demo Videos : 
1. **Basic Overview of the whole project** : https://www.loom.com/share/261872f8bfb5411dab0ef478f6b208e3?sid=1ce1eb14-bef3-4793-9f56-a3c798b9c779
2. **In depth explanations of all the features:** : https://www.loom.com/share/b10c842040674393b6ff5a1e7d67056c?sid=1a5d6a70-e63e-4bd8-a60c-bbd2a97ff597
3. **Filtering based on differernt parameters:** : https://www.loom.com/share/6b8fd39eaf464959be41d896165ca441?sid=9eca7a1e-05ef-4b33-bdcc-606b6499e9e4
---

## 📦 Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/Ansh-Malik1/Influencer-Campaign-ROI-calc.git
   cd Influencer-Campaign-ROI-calc
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate sample data**
   ```bash
   python data_generation.py
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

---

## 📁 Directory Structure

```
Influencer-Campaign-ROI-calc/
│
├── app.py                    # Streamlit dashboard app
├── data_generation.py       # Synthetic data generator
├── requirements.txt         # Dependencies
├── README.md                # You're here!
└── data/
    ├── influencers.csv
    ├── posts.csv
    ├── tracking_data.csv
    └── payouts.csv
```

---

## 📊 Dashboard Overview

### 🔎 Filters (Sidebar)
- **Platform**
- **Category**
- **Product**
- **Influencer Type**
- **Optional file upload for custom data**

---

### 📈 Key Visuals & Metrics

| Section             | Description                                      |
|---------------------|--------------------------------------------------|
| **Key Metrics**     | Total revenue, payout, ROAS                      |
| **Incremental ROAS**| Simulated A/B test (control vs. exposed)         |
| **Top Influencers** | Based on ROAS                                    |
| **Poor ROI Alerts** | Influencers with ROAS < 1x                       |
| **Best Personas**   | Category × Gender breakdown                      |
| **Scatterplot**     | Revenue vs. Payout                               |
| **Engagement Graph**| Engagement by platform                           |
| **Persona Heatmap** | ROAS grid for personas                           |

---

## 🧪 Incremental ROAS Simulation

This metric estimates the ROI generated from users exposed to influencer campaigns (`group = 1`) compared to a synthetic control group (`group = 0`), using simulated revenue behavior.

---

## 📂 Custom Data Upload (Optional)

You can replace the sample data via the **sidebar file uploader**:

- `influencers.csv`
- `posts.csv`
- `tracking_data.csv`
- `payouts.csv`

⚠️ Ensure the uploaded files follow the required schema below.

---

## 🛠 Data Schema

### `influencers.csv`

| Column           | Description                  |
|------------------|------------------------------|
| `id`             | Unique influencer ID         |
| `name`           | Influencer name              |
| `platform`       | Instagram, YouTube, etc.     |
| `category`       | e.g., Fitness, Beauty        |
| `gender`         | Male, Female, Other          |
| `influencer_type`| Macro, Micro, etc.           |
| `follower_count` | Total followers count        |

---

### `posts.csv`

| Column         | Description              |
|----------------|--------------------------|
| `influencer_id`| FK to influencer         |
| `likes`        | Total likes              |
| `comments`     | Total comments           |
| `reach`        | Total reach              |
| `platform`     | Platform of the post     |
| `url`          | URL of the post          |
| `date    `     | Date of posting          |


---

### `tracking_data.csv`

| Column         | Description                           |
|----------------|---------------------------------------|
| `influencer_id`| FK to influencer                      |
| `product`      | Promoted product                      |
| `revenue`      | Revenue generated                     |
| `user_id`      | Simulated customer ID                 |
| `group`        | 0 = control group, 1 = exposed group  |
| `source  `     | Source of the order                   |
| `date    `     | Date at which order was placed        |
| `orders`       | Total number of orders                |
| `campaign`     | Simulated campaign id                 |


---

### `payouts.csv`

| Column         | Description                  |
|----------------|------------------------------|
| `influencer_id`| FK to influencer             |
| `total_payout` | Total payment to influencer  |
| `basis`        | Order based or post based payout|
| `orders`       | Number of orders generated     |
| `rate`         | Basic rate for payout calculation     |



---

## ⚠️ Known Issues

- Seaborn palette warnings appear on older versions — assign `hue` to suppress.
- Some charts may appear squished on smaller screens. Use **wide layout** in Streamlit for optimal spacing.
- Ensure **Streamlit version ≥ 1.20** for full compatibility.

---

## 🧠 Key Insights

- Identify top revenue-generating influencers.
- Filter by category, platform, or influencer type to refine analysis.
- Quantify marketing uplift through **Incremental ROAS**.
- Track ROI efficiency across different **personas and demographics**.
- Compare platform-level **engagement rates**.

---

## 📌 License

This project is for demonstration and educational purposes only. All data used is **synthetically generated**.
Developed by : Ansh Malik


