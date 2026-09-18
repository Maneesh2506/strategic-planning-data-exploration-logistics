# Week 4 – Predictive Modeling and Optimization in Logistics Systems

## Project Overview

This project focuses on applying predictive modeling and optimization techniques to a logistics problem.

The objective is to develop a machine learning model that predicts **shipment delivery time** and use the prediction results to identify potential delays and propose logistics optimization strategies.

A simulated logistics dataset was created using Python because real company shipment data was not available. The dataset contains shipment, transportation, hub, weather, traffic, and warehouse-processing information.

---

## Objectives

The main objectives of this project are:

- Define a logistics forecasting problem.
- Create and analyze a simulated logistics dataset.
- Predict shipment delivery time using machine learning.
- Compare multiple regression algorithms.
- Evaluate model performance using MAE, RMSE, and R².
- Apply cross-validation and hyperparameter tuning.
- Identify important factors affecting delivery time.
- Develop optimization strategies based on model predictions.
- Demonstrate how predictive analytics can support logistics decision-making.

---

## Problem Statement

Delivery time in logistics can be affected by several factors such as:

- Transportation distance
- Package weight
- Traffic conditions
- Weather
- Hub utilization
- Shipment priority
- Number of delivery stops
- Vehicle age
- Warehouse processing time
- Day of the week

The project aims to predict:

**Target Variable: `Delivery_Time_Hours`**

The predicted delivery time can then be used to identify shipments that may require operational attention.

---

## Dataset

A synthetic dataset containing **3,000 shipment records** was generated using Python.

### Features

| Feature | Description |
|---|---|
| Distance_km | Shipment transportation distance |
| Package_Weight_kg | Weight of the shipment |
| Traffic_Level | Traffic intensity from 1–5 |
| Weather | Weather condition |
| Hub_Load | Relative hub utilization |
| Priority | Standard or Express shipment |
| Stops | Number of delivery stops |
| Vehicle_Age_Years | Age of the assigned vehicle |
| Warehouse_Processing_Hours | Processing time before dispatch |
| Day_of_Week | Shipment dispatch day |
| Delivery_Time_Hours | Actual delivery duration / target |

> Note: The dataset is simulated for educational purposes and does not represent actual confidential logistics-company data.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- Git
- GitHub

---

## Machine Learning Models

Three regression models were evaluated:

### 1. Linear Regression

Used as a baseline model because it is simple and easy to interpret.

### 2. Decision Tree Regression

Used to capture nonlinear relationships between logistics variables and delivery time.

### 3. Random Forest Regression

Used as an ensemble model capable of capturing more complex relationships between operational variables.

---

## Model Evaluation

The models were evaluated using:

### MAE – Mean Absolute Error

Measures the average absolute difference between actual and predicted delivery time.

### RMSE – Root Mean Squared Error

Measures prediction error while giving greater importance to larger errors.

### R² – R-squared

Measures the amount of variation in delivery time explained by the model.

---

## Model Results

The simulated experiment produced the following test-set results:

| Model | MAE (Hours) | RMSE (Hours) | R² |
|---|---:|---:|---:|
| Linear Regression | 2.19 | 2.74 | 0.788 |
| Random Forest | 2.57 | 3.21 | 0.709 |
| Decision Tree | 3.30 | 4.22 | 0.497 |

The results demonstrate that model complexity does not automatically guarantee better performance. The model should be selected based on measured validation performance and operational requirements.

---

## Hyperparameter Tuning

Random Forest was further optimized using `GridSearchCV`.

The tuning process evaluated:

- Number of trees
- Maximum tree depth
- Minimum samples per leaf

The tuned Random Forest achieved approximately:

- **MAE:** 2.55 hours
- **RMSE:** 3.19 hours
- **R²:** 0.712

A 5-fold cross-validation procedure was also performed to assess model stability.

---

## Feature Importance

Feature importance was analyzed using the trained Random Forest model.

Important operational factors can help logistics teams investigate:

- Traffic congestion
- Hub workload
- Transportation distance
- Warehouse processing
- Number of delivery stops

Feature importance indicates predictive contribution and should not be interpreted as proof of causation.

---

## Optimization Strategies

The prediction model can support several logistics optimization strategies.

### 1. Dynamic Capacity Allocation

Identify shipments with high predicted delivery times and allocate additional resources when justified.

### 2. Hub Load Balancing

Use predicted delivery times and hub utilization to identify potential congestion and redistribute workload where feasible.

### 3. Route Prioritization

Prioritize shipments with high predicted delivery duration or strict service commitments.

### 4. Proactive Exception Management

Flag potentially delayed shipments before they become service failures.

### 5. Resource Scheduling

Use predicted workload to improve driver, vehicle, and warehouse staffing decisions.

### 6. Cost Optimization

Balance additional resource costs against potential delay penalties and service-level requirements.

---

## Project Workflow

```text
Logistics Data
      ↓
Data Preparation
      ↓
Feature Engineering
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Cross-Validation
      ↓
Hyperparameter Tuning
      ↓
Delivery-Time Prediction
      ↓
Delay-Risk Identification
      ↓
Logistics Optimization
      ↓
Operational Recommendations
```

---

## Business Value

The project demonstrates how predictive analytics can help logistics operations move from reactive decision-making to proactive planning.

Instead of waiting until a shipment is delayed, the organization can use predicted delivery time to identify potential problems earlier and investigate possible actions.

---

## Project Files

```text
Week-4-Predictive-Modeling-Logistics/
│
├── README.md
├── data/
├── notebooks/
├── src/
├── outputs/
├── requirements.txt
└── Week_4_Predictive_Modeling_and_Optimization_in_Logistics_Systems_Detailed.docx
```

---

## Limitations

- The dataset is simulated.
- Real GPS and road-network data are not included.
- Real-time traffic information is not included.
- Real company SLA information is not available.
- The optimization impact has not been validated through a real operational pilot.
- Production deployment would require real historical logistics data and continuous model monitoring.

---

## Future Improvements

Future versions could include:

- Real historical shipment data
- GPS and route information
- Real-time traffic data
- Weather APIs
- Fuel consumption
- Vehicle capacity
- Hub scan events
- Customer SLA information
- Real-time prediction APIs
- Route optimization algorithms
- Dashboard integration using Power BI or Tableau
- Automated model retraining

---

## Project Type

**Domain:** Logistics & Supply Chain Analytics  
**Category:** Data Science / Predictive Analytics  
**Task:** Predictive Modeling and Optimization  
**Target:** Delivery Time Prediction  
**Dataset:** Simulated Logistics Dataset
