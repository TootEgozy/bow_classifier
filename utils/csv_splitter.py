import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("../learning_data/sentiment.csv", errors='replace')

# Split the DataFrame into chunks
chunk_size = int(len(df) / 4)
chunks = [df[i:i + chunk_size] for i in range(0, len(df), chunk_size)]

# Write each chunk to a separate CSV file
for i, chunk in enumerate(chunks):
    chunk.to_csv(f"split_data_{i + 1}.csv", index=False)
