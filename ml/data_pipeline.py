import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from pathlib import Path


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def preprocess_data(df: pd.DataFrame):
    df = df.copy()

    # Тринарна класифікація
    df["label"] = df["koi_disposition"].map({
        "FALSE POSITIVE": 0,
        "CANDIDATE": 1,
        "CONFIRMED": 2
    })

    features = [
        "koi_period",
        "koi_duration",
        "koi_depth",
        "koi_prad",
        "koi_steff",
        "koi_slogg",
        "koi_srad",
        "koi_kepmag"
    ]

    X = df[features]
    y = df["label"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y


def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent

    relative_path = Path("..") / "data" / "cleaned" / "KOI_clean_for_learning.csv"
    final_path = base_dir / relative_path

    df = load_data(final_path)
    print("Завантажено:", df.shape)

    X, y = preprocess_data(df)
    print("Фічі:", X.shape, "Мітки:", y.shape)
    print("Класи:", y.value_counts().to_dict())

    X_train, X_test, y_train, y_test = split_data(X, y)
    print("Train:", X_train.shape, "Test:", X_test.shape)
