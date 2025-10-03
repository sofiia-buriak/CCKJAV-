from __future__ import annotations
import json
import math
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
from joblib import load


RAW_FEATURES = [
    "koi_period", "koi_duration", "koi_depth", "koi_prad",
    "koi_steff", "koi_slogg", "koi_srad", "koi_kepmag",
]

class ExoPredictor:
    def __init__(self, artifacts_dir: str = "./artifacts"):
        a = Path(artifacts_dir)
        self.model = load(a / "model.joblib")
        self.le = load(a / "label_encoder.joblib")
        with open(a / "features.json", "r", encoding="utf-8") as f:
            self.model_features = json.load(f)["features"]

    @staticmethod
    def _ln1p(x: float) -> float:
        return float(math.log1p(float(x)))

    def _build_feature_row_from_raw(self, raw: Dict[str, float]) -> pd.DataFrame:
        # Ініціалізуємо всі потрібні полями для моделі нулями, потім заповнюємо
        feat = {c: 0.0 for c in self.model_features}

        if "koi_period_log" in feat:
            feat["koi_period_log"] = self._ln1p(raw.get("koi_period", 0.0))
        if "koi_depth_log" in feat:
            feat["koi_depth_log"] = self._ln1p(raw.get("koi_depth", 0.0))
        if "koi_prad_log" in feat:
            feat["koi_prad_log"] = self._ln1p(raw.get("koi_prad", 0.0))
        if "koi_srad_log" in feat:
            feat["koi_srad_log"] = self._ln1p(raw.get("koi_srad", 0.0))

        # 2) Сирі зоряні та інші параметри (якщо модель їх використовує напряму)
        for k in ["koi_duration", "koi_steff", "koi_slogg", "koi_kepmag"]:
            if k in feat:
                feat[k] = float(raw.get(k, 0.0))

        # 3) Missing‑індикатори (для ручного вводу завжди 0, але залишаємо гнучкість)
        for mflag in [
            "koi_depth_missing", "koi_prad_missing", "koi_srad_missing",
            "koi_steff_missing", "koi_slogg_missing",
        ]:
            if mflag in feat:
                # якщо у raw немає поля або воно None → 1, інакше 0
                base = mflag.split("_missing")[0]
                val = raw.get(base, None)
                feat[mflag] = 1.0 if (val is None) else 0.0

        # 4) Якщо модель очікує ще якісь поля (інша конфігурація) — вони залишаться 0.0
        # Побудова DataFrame у правильному порядку
        row = [feat[c] for c in self.model_features]
        return pd.DataFrame([row], columns=self.model_features)

    def predict_one_raw(self, raw: Dict[str, float]) -> Tuple[np.ndarray, str]:
        X = self._build_feature_row_from_raw(raw)
        probs = self.model.predict_proba(X)[0]
        idx = int(np.argmax(probs))
        return probs, self.le.classes_[idx]
