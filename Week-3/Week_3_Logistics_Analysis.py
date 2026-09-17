import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Week_3_Hypothetical_Logistics_Dataset.csv")
print("Dataset shape:", df.shape)
print(df.head())
print("\nDescriptive statistics:\n", df.describe())
print("\nMissing values:\n", df.isna().sum())

numeric_cols = [
    "Distance_km", "Shipment_Volume_kg", "Delivery_Time_hr",
    "Transportation_Cost_INR", "Fuel_Cost_INR", "Delay_Hours",
    "Customer_Rating"
]
print("\nCorrelation matrix:\n", df[numeric_cols].corr())

plt.figure(figsize=(8,5))
plt.hist(df["Delivery_Time_hr"].dropna(), bins=25, edgecolor="black")
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery Time (hours)")
plt.ylabel("Number of Shipments")
plt.tight_layout()
plt.show()

mode_cost = df.groupby("Transport_Mode")["Transportation_Cost_INR"].mean()
plt.figure(figsize=(8,5))
plt.bar(mode_cost.index, mode_cost.values)
plt.title("Average Transportation Cost by Transport Mode")
plt.xlabel("Transport Mode")
plt.ylabel("Average Cost (INR)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
for mode in df["Transport_Mode"].unique():
    sub = df[df["Transport_Mode"] == mode]
    plt.scatter(sub["Distance_km"], sub["Transportation_Cost_INR"],
                s=18, alpha=0.55, label=mode)
plt.title("Transportation Cost vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Transportation Cost (INR)")
plt.legend()
plt.tight_layout()
plt.show()
