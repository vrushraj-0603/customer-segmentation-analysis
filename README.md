# Customer Segmentation Analysis using K-Means Clustering

## Overview

The **Customer Segmentation Analysis** project uses the **K-Means Clustering** algorithm to group customers based on their **Annual Income** and **Spending Score**. The project includes data preprocessing, exploratory data analysis (EDA), customer segmentation, visualization, an interactive Power BI dashboard, and a live Streamlit application.

---

## Objectives

- Analyze customer purchasing behavior.
- Segment customers using K-Means Clustering.
- Identify high-value and low-value customer groups.
- Visualize customer segments using scatter plots.
- Build an interactive Power BI dashboard.
- Deploy the project using Streamlit.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Power BI
- Streamlit

---

## Dataset

**Mall_Customers.csv**

The dataset contains the following attributes:

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1–100)

---

## Project Workflow

1. Load the dataset using Pandas.
2. Clean and preprocess the data.
3. Normalize numerical features using MinMaxScaler.
4. Perform Exploratory Data Analysis (EDA).
5. Apply the K-Means Clustering algorithm.
6. Visualize customer clusters.
7. Build an interactive Power BI dashboard.
8. Deploy the project using Streamlit.
9. Generate business insights.

---

## Live Demo

**Streamlit Application**

https://customer-segmentation-analysis-mnr4ejkkpfuukmxurdh79f.streamlit.app/

---

## Project Files

```text
README.md
Mall_Customers.csv
Mall_Customer_Preprocessed.csv
Mall_Customer_Clustered.csv
customer_segmentation.py
Mall_Customer_Segmentation.pbix
Mall_Customer_Segmentation.pdf
Figure_1.png
app.py
requirements.txt
```

---

## Dashboard Features

- Total Customers
- Total Clusters
- Average Annual Income
- Average Spending Score
- Customer Segmentation Scatter Plot
- Customer Distribution by Cluster
- Customers by Cluster
- Customer Details Table
- Gender Filter
- Cluster Filter

---

## Business Insights

- Cluster 0: High Income – High Spending (Premium Customers)
- Cluster 1: High Income – Low Spending (Potential Customers)
- Cluster 2: Low Income – High Spending (Frequent Buyers)
- Cluster 3: Low Income – Low Spending (Low Value Customers)
- Cluster 4: Medium Income – Medium Spending (Average Customers)

---

## Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Project Outcome

This project demonstrates how businesses can use K-Means Clustering to segment customers based on income and spending behavior. The Power BI dashboard and Streamlit application provide interactive insights that support data-driven marketing and customer engagement strategies.

---

## Author

**Vrushraj**
