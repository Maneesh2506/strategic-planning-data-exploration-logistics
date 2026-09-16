import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("E-Commerce Shipping Data.csv")

# ==========================================
# 2. Basic Dataset Inspection
# ==========================================

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# ==========================================
# 3. Check Missing Values
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# 4. Check Duplicate Records
# ==========================================

print("\nNumber of Duplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

# ==========================================
# 5. Numerical Statistics
# ==========================================

print("\nNumerical Statistics:")
print(df.describe())

# ==========================================
# 6. Outlier Detection using IQR
# ==========================================

Q1 = df["Weight_in_gms"].quantile(0.25)
Q3 = df["Weight_in_gms"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Weight_in_gms"] < lower) |
    (df["Weight_in_gms"] > upper)
]

print("\nNumber of Weight Outliers:", len(outliers))

# ==========================================
# 7. Feature Standardization
# ==========================================

scaler = StandardScaler()

df[["Weight_in_gms", "Cost_of_the_Product"]] = scaler.fit_transform(
    df[["Weight_in_gms", "Cost_of_the_Product"]]
)

print("\nStandardization Completed.")

print("\nFinal Dataset Preview:")
print(df.head())
