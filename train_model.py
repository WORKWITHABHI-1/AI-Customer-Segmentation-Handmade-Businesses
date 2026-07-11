from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.clustering import run_kmeans
from src.business_logic import assign_segments
from src.recommendation import customer_recommendation

from src.visualization import plot_clusters
from src.statistics import generate_summary

from src.eda import *

from config.config import *


def main():

    print("="*60)
    print("AI CUSTOMER SEGMENTATION")
    print("="*60)

    df = load_data(DATA_PATH)

    df = preprocess_data(df)

    df = run_kmeans(df, MODEL_PATH)

    df = assign_segments(df)

    df["Recommendation"] = (
        df["Customer_Segment"]
        .apply(customer_recommendation)
    )

    df.to_csv(
        "output/customer_segments.csv",
        index=False
    )

    summary = generate_summary(df)

    payment_analysis(df)

    region_analysis(df)

    overdue_analysis(df)

    purchase_analysis(df)

    plot_clusters(df)

    print(summary)

    print("\nCompleted Successfully")


if __name__ == "__main__":

    main()