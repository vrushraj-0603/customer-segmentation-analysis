import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

st.title("Customer Segmentation Analysis")

uploaded_file = st.file_uploader("Upload Mall_Customers.csv", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    df = df.drop("CustomerID", axis=1)

    scaler = MinMaxScaler()

    features = df[['Age',
                   'Annual Income (k$)',
                   'Spending Score (1-100)']]

    scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=5, random_state=42)

    df["Cluster"] = kmeans.fit_predict(scaled)

    st.subheader("Clustered Data")
    st.dataframe(df.head())

    fig, ax = plt.subplots(figsize=(8,6))

    scatter = ax.scatter(
        df["Annual Income (k$)"],
        df["Spending Score (1-100)"],
        c=df["Cluster"],
        cmap="viridis"
    )

    ax.set_xlabel("Annual Income")
    ax.set_ylabel("Spending Score")

    st.pyplot(fig)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Clustered CSV",
        csv,
        "Mall_Customer_Clustered.csv",
        "text/csv"
    )