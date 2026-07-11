import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_FOLDER = "output"


def payment_analysis(df):
    payment = df["Payment_Method"].value_counts()

    print("\n===== PAYMENT ANALYSIS =====")
    print(payment)

    plt.figure(figsize=(6,4))
    payment.plot(kind="bar")
    plt.title("Online vs Offline Payment")
    plt.xlabel("Payment Method")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FOLDER}/payment_analysis.png")
    plt.close()


def region_analysis(df):
    region = df["Region"].value_counts()

    print("\n===== REGION ANALYSIS =====")
    print(region)

    plt.figure(figsize=(6,4))
    region.plot(kind="bar")
    plt.title("Regional Customer Distribution")
    plt.xlabel("Region")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FOLDER}/region_analysis.png")
    plt.close()


def overdue_analysis(df):

    print("\n===== OVERDUE ANALYSIS =====")

    plt.figure(figsize=(6,4))

    plt.hist(df["Overdue_Days"], bins=5)

    plt.title("Overdue Days Distribution")

    plt.xlabel("Days")

    plt.ylabel("Customers")

    plt.tight_layout()

    plt.savefig(f"{OUTPUT_FOLDER}/overdue_analysis.png")

    plt.close()


def purchase_analysis(df):

    plt.figure(figsize=(6,4))

    plt.bar(df["Customer_ID"], df["Purchase_Volume"])

    plt.xticks(rotation=90)

    plt.title("Purchase Volume by Customer")

    plt.tight_layout()

    plt.savefig(f"{OUTPUT_FOLDER}/purchase_volume.png")

    plt.close()