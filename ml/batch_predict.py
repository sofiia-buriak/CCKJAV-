import argparse

def _parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--artifacts", default="./artifacts")
    p.add_argument("--csv", required=True)
    p.add_argument("--out", default="./preds.csv")
    return p.parse_args()

if __name__ == "__main__":
    args = _parse_args()
    from inference_core import ExoPredictor, RAW_FEATURES

    import pandas as pd
    from pathlib import Path

    pred = ExoPredictor(args.artifacts)
    df = pd.read_csv(args.csv)

    # Перевірка мінімальних колонок
    miss = [c for c in RAW_FEATURES if c not in df.columns]
    if miss:
        raise ValueError(f"Input CSV must contain raw features {RAW_FEATURES}; missing: {miss}")

    rows = []
    for _, r in df.iterrows():
        raw = {f: float(r[f]) if pd.notna(r[f]) else None for f in RAW_FEATURES}
        probs, cls = pred.predict_one_raw(raw)
        rec = dict(r)
        rec["pred_class"] = cls
        for i, cname in enumerate(pred.le.classes_):
            rec[f"prob_{cname}"] = float(probs[i])
        rows.append(rec)

    out = pd.DataFrame(rows)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False)
    print(f"[DONE] Wrote predictions → {Path(args.out).resolve()}")
