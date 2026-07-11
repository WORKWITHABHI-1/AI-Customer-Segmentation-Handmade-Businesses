def assign_segments(df):

    avg = (
        df.groupby("Cluster")
        ["Purchase_Volume"]
        .mean()
        .sort_values(ascending=False)
    )

    clusters = avg.index.tolist()

    mapping = {
        clusters[0]: "High Value",
        clusters[1]: "Moderate",
        clusters[2]: "Risk"
    }

    df["Customer_Segment"] = (
        df["Cluster"]
        .map(mapping)
    )

    return df