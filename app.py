import streamlit as st
import pandas as pd
import plotly.express as px

from src.preprocessing import preprocess_data
from src.clustering import run_kmeans
from src.business_logic import assign_segments
from src.recommendation import customer_recommendation

st.set_page_config(
    page_title="AI Customer Segmentation",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Artificial Intelligence-Driven Customer Segmentation")
st.subheader("Personalized Marketing for Handmade Small Businesses")

uploaded_file = st.file_uploader(
    "Upload Customer Dataset (.csv)",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.dataframe(df)

    if st.button("Run AI Segmentation"):

        df = preprocess_data(df)
        df = run_kmeans(df, "models/kmeans_model.pkl")
        df = assign_segments(df)

        df["Recommendation"] = df["Customer_Segment"].apply(customer_recommendation)

        st.success("AI Analysis Completed")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Customers", len(df))
        col2.metric("High Value", (df["Customer_Segment"]=="High Value").sum())
        col3.metric("Moderate", (df["Customer_Segment"]=="Moderate").sum())
        col4.metric("Risk", (df["Customer_Segment"]=="Risk").sum())

        st.divider()

        chart1 = px.pie(
            df,
            names="Customer_Segment",
            title="Customer Segments"
        )

        st.plotly_chart(chart1, use_container_width=True)

        chart2 = px.bar(
            df,
            x="Customer_ID",
            y="Purchase_Volume",
            color="Customer_Segment",
            title="Purchase Volume"
        )

        st.plotly_chart(chart2, use_container_width=True)

        chart3 = px.bar(
            df,
            x="Region",
            color="Customer_Segment",
            title="Regional Distribution"
        )

        st.plotly_chart(chart3, use_container_width=True)

        st.subheader("Final AI Output")

        st.dataframe(df)

        csv = df.to_csv(index=False).encode()

        st.download_button(
            "📥 Download Customer Segments",
            csv,
            "customer_segments.csv",
            "text/csv"
        )