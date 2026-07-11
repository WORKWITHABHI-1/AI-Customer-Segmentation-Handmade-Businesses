from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib


def run_kmeans(df, model_path):

    features = df[[
        "Purchase_Volume",
        "Overdue_Days"
    ]]

    scaler = StandardScaler()

    scaled = scaler.fit_transform(features)

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = model.fit_predict(scaled)

    score = silhouette_score(
        scaled,
        df["Cluster"]
    )

    print("\nSilhouette Score :", round(score,3))

    joblib.dump(model, model_path)

    return df