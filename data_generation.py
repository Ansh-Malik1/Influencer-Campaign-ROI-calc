import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random

np.random.seed(42)
os.makedirs("data", exist_ok=True)

def generate_influencers(n=10):
    platforms = ['Instagram', 'YouTube', 'Twitter']
    categories = ['Fitness', 'Health', 'Lifestyle']
    genders = ['Male', 'Female', 'Other']
    
    data = []
    for i in range(n):
        follower_count = np.random.randint(10000, 1000000)

        if follower_count >= 500000:
            influencer_type = 'Mega'
        elif follower_count >= 100000:
            influencer_type = 'Macro'
        elif follower_count >= 50000:
            influencer_type = 'Micro'
        else:
            influencer_type = 'Nano'

        data.append([
            i + 1,
            f"Influencer_{i+1}",
            random.choice(categories),
            random.choice(genders),
            follower_count,
            random.choice(platforms),
            influencer_type
        ])

    df = pd.DataFrame(data, columns=[
        'id', 'name', 'category', 'gender', 'follower_count', 'platform', 'influencer_type'
    ])
    df.to_csv("data/influencers.csv", index=False)
    return df