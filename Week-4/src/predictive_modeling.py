import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ============================================================
# 1. LOAD DATASET
# ============================================================

data_path = "../data/logistics_delivery_prediction_dataset.csv"

df = pd.read_csv(data_path)

print("Dataset loaded successfully.")
print("Dataset shape:", df.shape)
print("\nFirst 5 records:")
print(df.head())


# ============================================================
# 2. CHECK DATA
# ============================================================

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())


# ============================================================
# 3. DEFINE FEATURES AND TARGET
# ============================================================

X = df.drop(columns=["Delivery_Time_Hours"])
y = df["Delivery_Time_Hours"]

print("\nFeature shape:", X.shape)
print("Target shape:", y.shape)


# ============================================================
# 4. IDENTIFY NUMERIC AND CATEGORICAL FEATURES
# ============================================================

categorical_columns = [
    "Weather",
    "Priority",
    "Day_of_Week"
]

numeric_columns = [
    column for column in X.columns
    if column not in categorical_columns
]


# ============================================================
# 5. DATA PREPROCESSING
# ============================================================

preprocess = ColumnTransformer([
    (
        "num",
        "passthrough",
        numeric_columns
    ),
    (
        "cat",
        OneHotEncoder(handle_unknown="ignore"),
        categorical_columns
    )
])


# ============================================================
# 6. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ============================================================
# 7. MODEL 1 - LINEAR REGRESSION
# ============================================================

linear_model = Pipeline([
    ("preprocessing", preprocess),
    ("model", LinearRegression())
])

linear_model.fit(X_train, y_train)

linear_predictions = linear_model.predict(X_test)

linear_mae = mean_absolute_error(
    y_test,
    linear_predictions
)

linear_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        linear_predictions
    )
)

linear_r2 = r2_score(
    y_test,
    linear_predictions
)


# ============================================================
# 8. MODEL 2 - DECISION TREE
# ============================================================

decision_tree_model = Pipeline([
    ("preprocessing", preprocess),
    (
        "model",
        DecisionTreeRegressor(
            max_depth=8,
            random_state=42
        )
    )
])

decision_tree_model.fit(
    X_train,
    y_train
)

tree_predictions = decision_tree_model.predict(
    X_test
)

tree_mae = mean_absolute_error(
    y_test,
    tree_predictions
)

tree_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        tree_predictions
    )
)

tree_r2 = r2_score(
    y_test,
    tree_predictions
)


# ============================================================
# 9. MODEL 3 - RANDOM FOREST
# ============================================================

random_forest_model = Pipeline([
    ("preprocessing", preprocess),
    (
        "model",
        RandomForestRegressor(
            n_estimators=180,
            max_depth=14,
            min_samples_leaf=3,
            random_state=42,
            n_jobs=-1
        )
    )
])

random_forest_model.fit(
    X_train,
    y_train
)

rf_predictions = random_forest_model.predict(
    X_test
)

rf_mae = mean_absolute_error(
    y_test,
    rf_predictions
)

rf_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        rf_predictions
    )
)

rf_r2 = r2_score(
    y_test,
    rf_predictions
)


# ============================================================
# 10. MODEL COMPARISON
# ============================================================

results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Decision Tree",
        "Random Forest"
    ],

    "MAE": [
        linear_mae,
        tree_mae,
        rf_mae
    ],

    "RMSE": [
        linear_rmse,
        tree_rmse,
        rf_rmse
    ],

    "R2": [
        linear_r2,
        tree_r2,
        rf_r2
    ]
})

print("\n================ MODEL RESULTS ================")
print(results.round(3))


# ============================================================
# 11. RANDOM FOREST HYPERPARAMETER TUNING
# ============================================================

rf_pipeline = Pipeline([
    ("preprocessing", preprocess),
    (
        "model",
        RandomForestRegressor(
            random_state=42,
            n_jobs=-1
        )
    )
])

param_grid = {
    "model__n_estimators": [120, 180],
    "model__max_depth": [10, 14, None],
    "model__min_samples_leaf": [2, 3]
}

grid_search = GridSearchCV(
    rf_pipeline,
    param_grid,
    cv=3,
    scoring="neg_root_mean_squared_error",
    n_jobs=-1
)

grid_search.fit(
    X_train,
    y_train
)

print("\nBest parameters:")
print(grid_search.best_params__)


# ============================================================
# 12. EVALUATE TUNED RANDOM FOREST
# ============================================================

tuned_model = grid_search.best_estimator_

tuned_predictions = tuned_model.predict(
    X_test
)

tuned_mae = mean_absolute_error(
    y_test,
    tuned_predictions
)

tuned_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        tuned_predictions
    )
)

tuned_r2 = r2_score(
    y_test,
    tuned_predictions
)

print("\n============= TUNED RANDOM FOREST =============")
print("MAE :", round(tuned_mae, 3))
print("RMSE:", round(tuned_rmse, 3))
print("R2  :", round(tuned_r2, 3))


# ============================================================
# 13. FIVE-FOLD CROSS-VALIDATION
# ============================================================

cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

cv_rmse = np.sqrt(
    -cross_val_score(
        tuned_model,
        X,
        y,
        cv=cv,
        scoring="neg_mean_squared_error",
        n_jobs=-1
    )
)

cv_mae = -cross_val_score(
    tuned_model,
    X,
    y,
    cv=cv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1
)

print("\n============= CROSS VALIDATION =============")
print(
    "Mean RMSE:",
    round(cv_rmse.mean(), 3)
)

print(
    "Mean MAE:",
    round(cv_mae.mean(), 3)
)


# ============================================================
# 14. FEATURE IMPORTANCE
# ============================================================

feature_names = (
    tuned_model
    .named_steps["preprocessing"]
    .get_feature_names_out()
)

feature_importance = (
    tuned_model
    .named_steps["model"]
    .feature_importances_
)

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": feature_importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\n============= TOP FEATURES =============")

print(
    importance_df.head(10)
)


# ============================================================
# 15. IDENTIFY HIGH-RISK SHIPMENTS
# ============================================================

SLA_THRESHOLD = 30

risk_results = X_test.copy()

risk_results["Actual_Delivery_Time_Hours"] = (
    y_test.values
)

risk_results["Predicted_Delivery_Time_Hours"] = (
    tuned_predictions
)

risk_results["Delay_Risk"] = np.where(
    risk_results[
        "Predicted_Delivery_Time_Hours"
    ] > SLA_THRESHOLD,
    "High Risk",
    "Normal"
)

high_risk_shipments = risk_results[
    risk_results["Delay_Risk"] == "High Risk"
]

print("\n============= DELAY RISK =============")

print(
    "High-risk shipments:",
    len(high_risk_shipments)
)

print(
    "Total test shipments:",
    len(risk_results)
)

print(
    "High-risk percentage:",
    round(
        len(high_risk_shipments)
        / len(risk_results)
        * 100,
        2
    ),
    "%"
)


# ============================================================
# 16. FINAL SUMMARY
# ============================================================

print("\n==============================================")
print("LOGISTICS PREDICTIVE MODELING COMPLETED")
print("==============================================")

print(
    "Tuned Random Forest MAE:",
    round(tuned_mae, 3),
    "hours"
)

print(
    "Tuned Random Forest RMSE:",
    round(tuned_rmse, 3),
    "hours"
)

print(
    "Tuned Random Forest R2:",
    round(tuned_r2, 3)
)

print("\nPossible optimization strategies:")
print("1. Dynamic capacity allocation")
print("2. Hub load balancing")
print("3. Route prioritization")
print("4. Proactive delay management")
print("5. Resource scheduling")
print("6. Cost-aware logistics planning")
