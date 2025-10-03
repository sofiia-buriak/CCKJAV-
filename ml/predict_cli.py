import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from joblib import load


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--artifacts", default="./artifacts", help="Folder with model.joblib, label_encoder.joblib, features.json")
    p.add_argument("--csv", required=True, help="Path to input CSV containing required features")
    p.add_argument("--out", default="./preds.csv", help="Where to write predictions CSV")
    return p.parse_args()


def main():
    args = parse_args()
    a = Path(args.artifacts)

    model = load(a / "model.joblib")
    le = load(a / "label_encoder.joblib")
    with open(a / "features.json", "r", encoding="utf-8") as f:
        feat = json.load(f)["features"]

    df = pd.read_csv(args.csv)
    missing = [c for c in feat if c not in df.columns]
    if missing:
        raise ValueError(f"Input CSV is missing required features: {missing}")

    X = df[feat].values
    probs = model.predict_proba(X)
    yhat_idx = probs.argmax(1)
    yhat = le.inverse_transform(yhat_idx)

    # Build output
    out = df.copy()
    out["pred_class"] = yhat
    for i, cls in enumerate(le.classes_):
        out[f"prob_{cls}"] = probs[:, i]

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False)
    print(f"[DONE] Wrote predictions → {Path(args.out).resolve()}")


if __name__ == "__main__":
    main()