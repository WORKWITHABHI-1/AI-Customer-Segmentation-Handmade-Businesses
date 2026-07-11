import pandas as pd

def generate_summary(df):

    summary = df.groupby("Customer_Segment").agg(

        Total_Customers=("Customer_ID","count"),

        Average_Purchase=("Purchase_Volume","mean"),

        Average_Overdue=("Overdue_Days","mean"),

        Maximum_Purchase=("Purchase_Volume","max"),

        Minimum_Purchase=("Purchase_Volume","min")

    )

    summary.to_csv("output/business_summary.csv")

    return summary