import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Segmentation", layout="wide")

st.title("Customer Segmentation Analysis using K-Means")

st.sidebar.header("Project Information")
st.sidebar.write("Upload the Mall_Customers.csv dataset to perform customer segmentation.")

uploaded_file = st.file_uploader("Upload Mall_Customers.csv", type=["csv"])

if uploaded_file is not None:

    # Load Dataset
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Remove CustomerID if present
    if "CustomerID" in df.columns:
        df = df.drop("CustomerID", axis=1)

    # Select Features
    features = df[[
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]]

    # Scale Data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)

    # K-Means Clustering
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(scaled_data)

    # KPIs
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Customers", len(df))

    with col2:
        st.metric("Total Clusters", df["Cluster"].nunique())

    st.subheader("Clustered Data")
    st.dataframe(df.head())

    st.subheader("Customers per Cluster")
    st.write(df["Cluster"].value_counts().sort_index())

    # Scatter Plot
    st.subheader("Customer Segmentation")

    fig, ax = plt.subplots(figsize=(8,6))

    scatter = ax.scatter(
        df["Annual Income (k$)"],
        df["Spending Score (1-100)"],
        c=df["Cluster"],
        cmap="viridis",
        s=60
    )

    ax.set_xlabel("Annual Income (k$)")
    ax.set_ylabel("Spending Score (1-100)")
    ax.set_title("Customer Segmentation")

    plt.colorbar(scatter, label="Cluster")

    st.pyplot(fig)

    # Download CSV
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Clustered CSV",
        data=csv,
        file_name="Mall_Customer_Clustered.csv",
        mime="text/csv"
    )
