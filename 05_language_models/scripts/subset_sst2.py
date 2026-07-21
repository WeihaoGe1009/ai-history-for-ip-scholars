import os
from datasets import load_dataset
import pandas as pd

#Set your token
hf_token = os.getenv("HF_TOKEN")  # or paste directly if local and temporary
assert hf_token, "Please set HF_TOKEN environment variable with your Hugging Face access token."

#Load SST-2
dataset = load_dataset("glue", "sst2", token=hf_token)
df = dataset["train"].to_pandas()

# Define minimum token count for "longer" sentences
MIN_TOKEN_LENGTH = 8

# Filter for long sentences
long_df = df[df["sentence"].str.split().str.len() >= MIN_TOKEN_LENGTH]

# Sample 500 positive and 500 negative from long sentences
pos_long = long_df[long_df["label"] == 1].sample(n=500, random_state=42)
neg_long = long_df[long_df["label"] == 0].sample(n=500, random_state=42)

# Combine and shuffle
subset_long_df = pd.concat([pos_long, neg_long]).sample(frac=1.0, random_state=42)

# Save to CSV
subset_long_df[["sentence", "label"]].to_csv("../data/sst2_long_subset.csv", index=False)

print("Exported dataset with", len(subset_long_df), "rows.")


