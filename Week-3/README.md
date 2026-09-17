# Week 3 – Advanced Data Analysis and Visualization in Logistics

## Project Overview

This Week 3 project focuses on **Advanced Data Analysis and Visualization in Logistics** using Python.

The project demonstrates how logistics data can be analyzed to understand shipment performance, delivery times, transportation costs, delays, shipment volumes, transport modes, and customer experience.

A **hypothetical logistics dataset containing 500 shipment records** was created for this project. Python was then used to perform Exploratory Data Analysis (EDA), statistical analysis, correlation analysis, and data visualization.

> **Note:** The dataset used in this project is simulated for educational and analytical practice. It does not represent the actual operational data of any logistics company.

---

## Objectives

The main objectives of this project are:

- Create a structured hypothetical logistics dataset.
- Perform Exploratory Data Analysis (EDA).
- Analyze logistics performance using descriptive statistics.
- Identify missing values and understand data quality.
- Analyze delivery-time and transportation-cost distributions.
- Study the relationship between distance and transportation cost.
- Study the relationship between distance and delivery time.
- Compare Road, Rail, and Air transportation modes.
- Analyze delivery delays and delivery status.
- Examine the relationship between delays and customer ratings.
- Visualize shipment trends over time.
- Identify potential logistics bottlenecks and cost drivers.
- Provide data-driven recommendations for logistics operations.

---

## Dataset Description

The dataset contains **500 simulated shipment records** covering the period from **January 2026 to June 2026**.

### Dataset Variables

| Variable | Description |
|---|---|
| `Shipment_ID` | Unique identification number for each shipment |
| `Date` | Shipment date |
| `Origin` | Shipment origin city |
| `Destination` | Shipment destination city |
| `Transport_Mode` | Transportation method: Road, Rail, or Air |
| `Distance_km` | Shipment distance in kilometres |
| `Shipment_Volume_kg` | Shipment volume/weight in kilograms |
| `Delivery_Time_hr` | Total delivery time in hours |
| `Transportation_Cost_INR` | Estimated transportation cost |
| `Fuel_Cost_INR` | Estimated fuel-related cost |
| `Delay_Hours` | Number of hours a shipment was delayed |
| `Delivery_Status` | Shipment status: On Time or Delayed |
| `Customer_Rating` | Customer rating from 1 to 5 |

---

## Technologies Used

### Python

Used as the primary programming language for data analysis and visualization.

### Pandas

Used for:

- Data manipulation
- Data cleaning
- Grouping and aggregation
- Descriptive statistics
- Missing-value analysis

### NumPy

Used for:

- Numerical calculations
- Dataset simulation
- Generating realistic hypothetical values

### Matplotlib

Used for:

- Histograms
- Bar charts
- Scatter plots
- Line charts
- Correlation matrix visualization

### python-docx

Used to generate the detailed project report in Microsoft Word format.

---

## Exploratory Data Analysis

The following EDA techniques were performed:

### 1. Dataset Inspection

The dataset was inspected using:

```python
df.head()
df.shape
df.info()
```

These commands help understand:

- First few records
- Number of rows and columns
- Data types
- Available values

---

### 2. Descriptive Statistics

Descriptive statistics were calculated using:

```python
df.describe()
```

The analysis includes:

- Mean
- Median
- Standard deviation
- Minimum
- Maximum
- Quartiles

These statistics help understand the typical behavior and spread of logistics metrics.

---

### 3. Missing-Value Analysis

Missing values were identified using:

```python
df.isnull().sum()
```

This step is important because incomplete data can affect statistical calculations and visualizations.

---

### 4. Correlation Analysis

Correlation was calculated between important numerical variables:

```python
df[numeric_cols].corr()
```

The analysis focuses on relationships such as:

- Distance vs Transportation Cost
- Distance vs Delivery Time
- Delay Hours vs Customer Rating

> Correlation indicates an association between variables. It does not by itself prove causation.

---

# Visualizations

The project contains **8 major visualizations**.

## 1. Delivery Time Distribution

**Chart Type:** Histogram

The histogram shows how delivery times are distributed across shipments.

### Purpose

It helps identify:

- Typical delivery-time ranges
- Spread of delivery times
- Unusually slow shipments
- Possible long-tail behavior

---

## 2. Average Transportation Cost by Transport Mode

**Chart Type:** Bar Chart

This visualization compares the average transportation cost of:

- Road
- Rail
- Air

### Purpose

It helps understand how transportation costs differ between modes.

---

## 3. Transportation Cost vs Distance

**Chart Type:** Scatter Plot

This visualization examines the relationship between shipment distance and transportation cost.

### Purpose

It helps identify whether longer routes tend to have higher transportation costs and whether other factors may influence cost.

---

## 4. Delivery Time vs Distance

**Chart Type:** Scatter Plot

This visualization examines the relationship between distance and delivery time.

### Purpose

It helps determine whether longer-distance shipments generally require more time.

---

## 5. Monthly Shipment Volume Trend

**Chart Type:** Line Chart

This visualization shows how shipment activity changes over time.

### Purpose

It can support:

- Capacity planning
- Workforce planning
- Fleet allocation
- Warehouse planning
- Demand analysis

---

## 6. Delivery Status Distribution

**Chart Type:** Bar Chart

This visualization compares:

- On Time shipments
- Delayed shipments

### Purpose

It provides a simple view of delivery reliability and helps monitor the on-time delivery KPI.

---

## 7. Average Delay by Transport Mode

**Chart Type:** Bar Chart

This visualization compares the average delay associated with different transportation modes.

### Purpose

It helps identify differences in delay patterns between Road, Rail, and Air.

---

## 8. Correlation Matrix

**Chart Type:** Correlation Matrix

The correlation matrix displays relationships between numerical logistics variables.

### Purpose

It helps identify variables that may have meaningful relationships and deserve further investigation.

---

# Key Logistics KPIs

The project analyzes several important logistics performance indicators.

| KPI | Purpose |
|---|---|
| Average Delivery Time | Measures typical shipment delivery duration |
| Median Delivery Time | Shows the middle delivery-time value |
| Average Transportation Cost | Measures typical transportation spending |
| On-Time Delivery Rate | Measures delivery reliability |
| Average Delay | Measures typical delay duration |
| Average Shipment Volume | Helps understand shipment capacity requirements |

---

# Key Analytical Insights

The analysis demonstrates several important logistics patterns.

### 1. Distance and Transportation Cost

The simulated dataset shows a positive relationship between distance and transportation cost.

This means longer shipments generally require greater transportation expenditure.

However, distance is not the only cost driver. Other factors can include:

- Shipment volume
- Transportation mode
- Fuel cost
- Route conditions
- Operational expenses

---

### 2. Distance and Delivery Time

Longer-distance shipments generally require more delivery time in the simulated dataset.

This makes route distance an important variable when estimating expected delivery time.

---

### 3. Transportation Mode

Road, Rail, and Air have different cost and delivery characteristics.

For example:

- Road may provide flexibility.
- Rail can be useful for suitable longer-distance movements.
- Air can support faster transportation but may have higher costs.

Therefore, transportation mode should be selected according to:

- Delivery urgency
- Cost requirements
- Shipment characteristics
- Route distance
- Service-level requirements

---

### 4. Delivery Delays

The analysis separates shipments into:

- On Time
- Delayed

Monitoring this metric helps logistics teams identify changes in service reliability.

---

### 5. Customer Experience

The project also examines the relationship between delay hours and customer ratings.

In the simulated data, higher delays tend to be associated with lower customer ratings.

This indicates why delivery reliability can be an important component of customer-service analysis.

---

### 6. Shipment Volume

Monthly shipment trends help identify periods of higher and lower activity.

This information can support:

- Vehicle planning
- Warehouse capacity planning
- Workforce scheduling
- Resource allocation

---

# Potential Logistics Bottlenecks

The analysis highlights several areas that could be investigated in a real logistics environment:

- Long-distance routes with high delivery times
- Routes with repeated delays
- High transportation-cost routes
- High fuel-cost shipments
- Periods of high shipment volume
- Transportation modes with unfavorable cost/service combinations
- Shipments associated with poor customer ratings

---

# Recommendations

### 1. Route Optimization

Analyze route-level performance to identify routes with consistently high delivery times or transportation costs.

### 2. Transportation Mode Optimization

Compare transportation modes based on both cost and delivery requirements instead of considering cost alone.

### 3. Delay Monitoring

Create a dashboard that tracks:

- Delay hours
- Delay rate
- Origin
- Destination
- Transport mode
- Shipment volume

### 4. Cost Management

Separate transportation
