import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Sort values by date
df = df.sort_values("Date")

# Display basic information
print("First five rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

# Create line chart
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Sales"], marker="o")

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.savefig("sales_trend.png")

plt.show()
