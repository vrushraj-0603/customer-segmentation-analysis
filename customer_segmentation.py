# Customer Segmentation Analysis using K-Means Clustering
import os
os.environ["OMP_NUM_THREADS"] = "1"

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# ==========================
# 1. Load Dataset
# ==========================
df = pd.read_csv("Mall_Customers.csv")

print("Original Dataset:")
print(df.head())

# ==========================
# 2. Clean & Preprocess Data
# ==========================

# Remove unnecessary column
df.drop(columns=['CustomerID'], inplace=True)

# Normalize numerical columns
scaler = MinMaxScaler()

df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']] = scaler.fit_transform(
    df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
)

print("\nPreprocessed Dataset:")
print(df.head())

# Save preprocessed dataset
df.to_csv("Mall_Customer_Preprocessed.csv", index=False, sep=",",
    encoding="utf-8-sig")



# ==========================
# 3. Explore the Data
# ==========================
# Age Distribution by Gender
plt.figure(figsize=(8,5))

for gender in df['Gender'].unique():
    plt.hist(
        df[df['Gender'] == gender]['Age'],
        bins=10,
        alpha=0.6,
        label=gender
    )

plt.title("Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.legend()
plt.show()
plt.close()

# Distribution of Annual Income and Spending Score
plt.figure(figsize=(8,5))

plt.scatter(
    df['Annual Income (k$)'],
    df['Spending Score (1-100)'],
    alpha=0.7
)

plt.title("Annual Income vs Spending Score")
plt.xlabel("Annual Income (Normalized)")
plt.ylabel("Spending Score (Normalized)")
plt.show()
plt.close()
# ==========================
# 4. Apply K-Means Clustering
# ==========================

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

kmeans = KMeans(n_clusters=5, random_state=42)

df['Cluster'] = kmeans.fit_predict(X)

print("\nCluster Result:")
print(df.head())

# ==========================
# 5. Visualize Clusters
# ==========================

plt.figure(figsize=(8,6))

plt.scatter(
    df['Annual Income (k$)'],
    df['Spending Score (1-100)'],
    c=df['Cluster'],
    s=60
)

plt.title("Customer Segmentation (Annual Income vs Spending Score)")
plt.xlabel("Annual Income (Normalized)")
plt.ylabel("Spending Score (Normalized)")
plt.show()
plt.close()
# ==========================
# 6. Save Clustered Dataset
# ==========================

df.to_csv("Mall_Customer_Clustered.csv", index=False, sep=",",
    encoding="utf-8-sig")

print("\nClustered dataset saved successfully!")
