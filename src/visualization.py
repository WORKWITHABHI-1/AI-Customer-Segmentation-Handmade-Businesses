import matplotlib.pyplot as plt

def plot_clusters(df):

    plt.figure(figsize=(8,6))

    colors = ["red", "green", "blue"]

    for cluster in sorted(df["Cluster"].unique()):
        subset = df[df["Cluster"] == cluster]

        plt.scatter(
            subset["Purchase_Volume"],
            subset["Overdue_Days"],
            label=f"Cluster {cluster}"
        )

    plt.xlabel("Purchase Volume")
    plt.ylabel("Overdue Days")
    plt.title("AI Customer Segmentation")

    plt.legend()

    plt.grid(True)

    plt.savefig("output/customer_segmentation.png")

    plt.show()