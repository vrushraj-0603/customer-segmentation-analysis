# Customer Segmentation Analysis using K-Means Clustering

## Objective
Analyze customer data and divide customers into different groups based on their annual income and spending behavior using the K-Means Clustering algorithm.

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- Scikit-learn
- Power BI

## Dataset
**Mall_Customers.csv**

### Columns
- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

## Workflow

### 1. Load Dataset
Import the dataset using Pandas.

### 2. Data Cleaning & Preprocessing
- Remove the CustomerID column.
- Normalize numerical features using MinMaxScaler.

### 3. Exploratory Data Analysis (EDA)
Create the following visualizations:
- Age Distribution by Gender
- Annual Income vs Spending Score

### 4. Apply K-Means Clustering
- Select:
  - Annual Income (k$)
  - Spending Score (1-100)
- Create 5 customer clusters using the K-Means algorithm.

### 5. Visualize Clusters
Generate a scatter plot showing customer segments based on Annual Income and Spending Score.

### 6. Save Results
Output files:
- Mall_Customer_Preprocessed.csv
- Mall_Customer_Clustered.csv

### 7. Power BI Dashboard
Create an interactive dashboard with:
- Total Customers
- Total Clusters
- Average Annual Income
- Average Spending Score
- Customer Segmentation Scatter Plot
- Customer Distribution by Cluster
- Customers by Cluster
- Customer Details Table
- Gender and Cluster Slicers

## Business Insights
- Cluster 0: High Income – High Spending (Premium Customers)
- Cluster 1: High Income – Low Spending (Potential Customers)
- Cluster 2: Low Income – High Spending (Frequent Buyers)
- Cluster 3: Low Income – Low Spending (Low Value Customers)
- Cluster 4: Medium Income – Medium Spending (Average Customers)

## Project Outcome
This project demonstrates how businesses can use K-Means Clustering to segment customers based on income and spending behavior. The Power BI dashboard provides interactive insights to support data-driven marketing decisions.

## Author
Vrushraj