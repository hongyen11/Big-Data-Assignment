import pandas as pd

# Load the cleaned CSV file
df = pd.read_csv("craigslist_cleaned.csv")

# Drop rows with missing values in key columns
df.dropna(subset=["price", "manufacturer", "state"], inplace=True)

# Ensure price is numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df.dropna(subset=["price"], inplace=True)

# Task 1: Count of listings by state
state_counts = df["state"].value_counts().sort_values(ascending=False)
state_counts_df = state_counts.reset_index()
state_counts_df.columns = ["state", "listing_count"]
state_counts_df.to_csv(r"C:\Users\notco\Documents\statecount_nonmap.csv", index=False)

# Task 2: Average price by manufacturer
avg_prices = df.groupby("manufacturer")["price"].mean().sort_values(ascending=False)
avg_prices_df = avg_prices.reset_index()
avg_prices_df.columns = ["manufacturer", "average_price"]
avg_prices_df.to_csv(r"C:\Users\notco\Documents\averageprice_nonmap.csv", index=False)

# Display top 10 from both
print("=== Top 10 States by Number of Listings ===")
print(state_counts_df.head(10))
print()

print("=== Average Price by Manufacturer (Top 10) ===")
print(avg_prices_df.head(10))
