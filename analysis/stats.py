import pandas as pd

df = pd.read_json("data/benchmark.jsonl", lines=True)

print(df.groupby("category")["compromised"].mean().rename("compromise_rate"))
print("\nTotal trajectories:", len(df))
print("\nBy category:\n", df["category"].value_counts())