import argparse
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
from joblib import dump
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# -----------------------------
# Аргументи CLI
# -----------------------------

def parse_args():
    p = argparse.ArgumentParser(description="Train baseline RandomForest on KOI")

    # Якщо --csv не задано — шукати відносно цього файлу: ../data/cleaned/KOI_clean_for_learning.csv
    p.add_argument(
        "--csv",
        type=str,
        default=None,
        help="Path to KOI CSV (default: ../data/cleaned/KOI_clean_for_learning.csv relative to this file)",
    )
    p.add_argument("--outdir", type=str, default="./artifacts", help="Where to save artifacts")

    default_features = [
        # лог-фічі, які ти маєш у CSV
        "koi_period_log", "koi_duration", "koi_depth_log", "koi_prad_log",
        # зоряні параметри (raw)
        "koi_steff", "koi_slogg", "koi_srad_log", "koi_kepmag",
        # індикатори пропусків
        "koi_depth_missing", "koi_prad_missing", "koi_srad_missing", "koi_steff_missing", "koi_slogg_missing",
    ]
    p.add_argument("--features", nargs="*", default=default_features, help="Feature columns to use")

    p.add_argument("--label", type=str, default="koi_disposition", help="Label column")
    p.add_argument("--test_size", type=float, default=0.2, help="Test split size")
    p.add_argument("--seed", type=int, default=42, help="Random seed")

    return p.parse_args()


# -----------------------------
# Допоміжні функції
# -----------------------------

def resolve_default_csv() -> Path:
    """Визначити CSV відносно місця, де лежить цей файл.
    ../data/cleaned/KOI_clean_for_learning.csv
    """
    base_dir = Path(__file__).resolve().parent
    relative_path = Path("..") / "data" / "cleaned" / "KOI_clean_for_learning.csv"
    return (base_dir / relative_path).resolve()


def load_koi(csv_path: Path, features: list[str], label: str) -> tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv(csv_path)

    # Перевірити наявність необхідних колонок
    missing_cols = [c for c in features + [label] if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in CSV: {missing_cols}")

    # Мінімальна чистка: дропнути рядки з NA у використовуваних колонках
    df = df.dropna(subset=features + [label])

    return df[features].copy(), df[label].copy()


def train_baseline_rf(X: pd.DataFrame, y: pd.Series, seed: int = 42, test_size: float = 0.2):
    # Енкодер міток (CONFIRMED/CANDIDATE/FALSE POSITIVE)
    le = LabelEncoder()
    y_enc = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X.values, y_enc, test_size=test_size, stratify=y_enc, random_state=seed
    )

    model = RandomForestClassifier(
        n_estimators=300,
        n_jobs=-1,
        class_weight="balanced",
        random_state=seed,
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)

    report = classification_report(y_test, y_pred, target_names=list(le.classes_), output_dict=True)
    roc_auc = roc_auc_score(y_test, y_proba, multi_class="ovr")

    metrics = {
        "macro_f1": report["macro avg"]["f1-score"],
        "weighted_f1": report["weighted avg"]["f1-score"],
        "roc_auc_ovr": float(roc_auc),
        "per_class": {k: v for k, v in report.items() if k in le.classes_},
    }

    return model, le, metrics


def save_artifacts(outdir: Path, model, label_encoder, features: list[str], metrics: dict):
    outdir.mkdir(parents=True, exist_ok=True)
    dump(model, outdir / "model.joblib")
    dump(label_encoder, outdir / "label_encoder.joblib")
    with open(outdir / "features.json", "w", encoding="utf-8") as f:
        json.dump({"features": features}, f, indent=2)
    with open(outdir / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)


# -----------------------------
# Точка входу
# -----------------------------
if __name__ == "__main__":
    args = parse_args()

    csv_path = Path(args.csv).resolve() if args.csv else resolve_default_csv()
    print(f"[INFO] CSV: {csv_path}")

    features = args.features
    print(f"[INFO] Using {len(features)} features: {features}")

    print("[INFO] Loading data…")
    X, y = load_koi(csv_path, features, args.label)
    print(f"[INFO] Data shape: {X.shape}; classes: {sorted(y.unique().tolist())}")

    print("[INFO] Training RandomForest baseline…")
    model, le, metrics = train_baseline_rf(X, y, seed=args.seed, test_size=args.test_size)

    print("[INFO] Metrics summary:")
    print(json.dumps(metrics, indent=2))

    outdir = Path(args.outdir)
    print(f"[INFO] Saving artifacts to {outdir.resolve()} …")
    save_artifacts(outdir, model, le, features, metrics)

    print("[DONE] Baseline training complete.")
