# ============================================================
# WEEK 1 – STRATEGIC PLANNING AND DATA EXPLORATION
# Case Study: Delhivery Logistics – Indian E-Commerce Market
# ============================================================

import pandas as pd
import numpy as np

# ============================================================
# 1. LOAD AND INSPECT DATA
# ============================================================

# Example public/proxy logistics dataset files
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
shipments = pd.read_csv("shipments.csv")

print("Orders Shape:", orders.shape)
print("\nOrders Preview:")
print(orders.head())

print("\nOrders Information:")
orders.info()

print("\nMissing Values:")
print(orders.isnull().sum())


# ============================================================
# 2. DELIVERY KPI CALCULATION
# ============================================================

# Convert date columns into datetime format

date_cols = [
    "order_date",
    "promised_date",
    "delivered_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(
        orders[col],
        errors="coerce"
    )

# Keep records where promised and delivered dates are available

df = orders.dropna(
    subset=["promised_date", "delivered_date"]
).copy()

# Calculate delivery time in days

df["delivery_days"] = (
    df["delivered_date"] - df["order_date"]
).dt.total_seconds() / 86400

# Calculate delay in days

df["delay_days"] = (
    df["delivered_date"] - df["promised_date"]
).dt.total_seconds() / 86400

# Create late-delivery flag

df["late_flag"] = (
    df["delay_days"] > 0
).astype(int)


# ============================================================
# 3. CALCULATE BASIC LOGISTICS KPIs
# ============================================================

on_time_rate = 1 - df["late_flag"].mean()

late_rate = df["late_flag"].mean()

average_delivery_days = df["delivery_days"].mean()

print("\n========== LOGISTICS KPIs ==========")

print(
    "On-Time Delivery Rate:",
    round(on_time_rate * 100, 2),
    "%"
)

print(
    "Late Delivery Rate:",
    round(late_rate * 100, 2),
    "%"
)

print(
    "Average Delivery Time:",
    round(average_delivery_days, 2),
    "days"
)


# ============================================================
# 4. INTEGRATE CUSTOMER DATA
# ============================================================

analysis = df.merge(
    customers[
        [
            "customer_id",
            "state",
            "city",
            "pin_code",
            "city_tier"
        ]
    ],
    on="customer_id",
    how="left"
)


# ============================================================
# 5. INTEGRATE SHIPMENT DATA
# ============================================================

analysis = analysis.merge(
    shipments[
        [
            "order_id",
            "courier",
            "weight_kg",
            "distance_km",
            "freight_cost"
        ]
    ],
    on="order_id",
    how="left"
)


# ============================================================
# 6. FREIGHT COST ANALYSIS
# ============================================================

# Avoid division by zero

analysis["freight_per_km"] = (
    analysis["freight_cost"] /
    analysis["distance_km"].replace(0, np.nan)
)

print("\nAverage Freight Cost:")
print(
    analysis["freight_cost"].mean()
)

print("\nAverage Freight Cost per KM:")
print(
    analysis["freight_per_km"].mean()
)


# ============================================================
# 7. REGIONAL KPI ANALYSIS
# ============================================================

state_kpi = (
    analysis
    .groupby("state")
    .agg(
        orders=("order_id", "count"),
        avg_delivery_days=("delivery_days", "mean"),
        late_rate=("late_flag", "mean"),
        avg_freight=("freight_cost", "mean"),
        avg_distance=("distance_km", "mean")
    )
    .sort_values(
        "late_rate",
        ascending=False
    )
)

print("\n========== REGIONAL KPI ANALYSIS ==========")

print(state_kpi.head(10))


# ============================================================
# 8. LATE DELIVERY PREDICTION
# ============================================================

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


# Features that should be available before delivery

features = [
    "weight_kg",
    "distance_km",
    "freight_cost",
    "state",
    "city_tier",
    "courier"
]

model_df = analysis.dropna(
    subset=["late_flag"]
).copy()

X = model_df[features]

y = model_df["late_flag"]


# Numerical features

num_cols = [
    "weight_kg",
    "distance_km",
    "freight_cost"
]


# Categorical features

cat_cols = [
    "state",
    "city_tier",
    "courier"
]


# ============================================================
# 9. PREPROCESSING PIPELINE
# ============================================================

preprocess = ColumnTransformer(
    transformers=[
        (
            "num",
            SimpleImputer(strategy="median"),
            num_cols
        ),
        (
            "cat",
            Pipeline(
                steps=[
                    (
                        "imputer",
                        SimpleImputer(
                            strategy="most_frequent"
                        )
                    ),
                    (
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore"
                        )
                    )
                ]
            ),
            cat_cols
        )
    ]
)


# ============================================================
# 10. LOGISTIC REGRESSION MODEL
# ============================================================

model = Pipeline(
    steps=[
        (
            "preprocess",
            preprocess
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            )
        )
    ]
)


# Split data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Train model

model.fit(
    X_train,
    y_train
)


# Make predictions

pred = model.predict(
    X_test
)


# ============================================================
# 11. MODEL EVALUATION
# ============================================================

print("\n========== MODEL EVALUATION ==========")

print(
    classification_report(
        y_test,
        pred
    )
)


# ============================================================
# 12. IMPORTANT PROJECT NOTE
# ============================================================

print("\n==============================================")
print("Week 1 analytical framework completed.")
print("This code is an illustrative/proposed pipeline.")
print("It does not represent actual confidential")
print("Delhivery operational data or actual Delhivery results.")
print("==============================================")
