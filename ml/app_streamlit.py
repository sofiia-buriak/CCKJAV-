import json
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from joblib import load

st.set_page_config(page_title="Exoplanet KOI→TOI Baseline", layout="centered")

@st.cache_resource
def load_artifacts(art_dir: str):
    a = Path(art_dir)
    model = load(a / "model.joblib")
    le = load(a / "label_encoder.joblib")
    with open(a / "features.json", "r", encoding="utf-8") as f:
        features = json.load(f)["features"]
    return model, le, features

st.title("Exoplanet Baseline (KOI-trained)")
artifacts_dir = st.sidebar.text_input("Artifacts folder", value="./artifacts")
try:
    model, le, FEATURES = load_artifacts(artifacts_dir)
    st.sidebar.success("Artifacts loaded")
except Exception as e:
    st.sidebar.error(f"Failed to load artifacts: {e}")
    st.stop()

mode = st.radio("Select input mode", ["CSV upload", "Manual input"], horizontal=True)

if mode == "CSV upload":
    st.write("Upload a CSV that contains the required features:")
    st.code(", ".join(FEATURES))
    file = st.file_uploader("CSV file", type=["csv"]) 
    if file is not None:
        df = pd.read_csv(file)
        miss = [c for c in FEATURES if c not in df.columns]
        if miss:
            st.error(f"Missing columns: {miss}")
        else:
            X = df[FEATURES].values
            probs = model.predict_proba(X)
            yhat_idx = probs.argmax(1)
            yhat = le.inverse_transform(yhat_idx)
            out = df.copy()
            out["pred_class"] = yhat
            for i, cls in enumerate(le.classes_):
                out[f"prob_{cls}"] = probs[:, i]
            st.success("Predictions ready")
            st.dataframe(out.head(50))
            st.download_button("Download predictions CSV", out.to_csv(index=False).encode("utf-8"), file_name="preds.csv")
else:
    st.write("Enter feature values and get an instant prediction.")
    vals = {}
    for f in FEATURES:
        if f.endswith("_missing"):
            # For manual entry we default missing flags to 0, but let user toggle
            vals[f] = st.checkbox(f, value=False)
        else:
            vals[f] = st.number_input(f, value=0.0, step=0.1, format="%.6f")
    X = np.array([[vals[f] if not isinstance(vals[f], bool) else float(vals[f]) for f in FEATURES]])
    if st.button("Predict"):
        probs = model.predict_proba(X)
        idx = np.argmax(probs, axis=1)[0]
        st.metric("Predicted class", le.classes_[idx])
        st.write("Probabilities:")
        prob_tbl = pd.DataFrame({"class": le.classes_, "prob": probs[0]}).sort_values("prob", ascending=False)
        st.dataframe(prob_tbl, hide_index=True)