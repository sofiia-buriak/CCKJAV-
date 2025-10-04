# KOI Evaluation Report

## Classification Report XGB
![Classification Report](./figures/classification_report_xgb.png)

## Confusion Matrix
![Confusion Matrix](./figures/confusion_matrix.xgb)

## Compact Metrics Table (Slide Ready)
|                |   precision |   recall |   f1-score |   support |
|:---------------|------------:|---------:|-----------:|----------:|
| CANDIDATE      |        0.57 |     0.48 |       0.52 |       396 |
| CONFIRMED      |        0.76 |     0.82 |       0.79 |       549 |
| FALSE POSITIVE |        0.83 |     0.85 |       0.84 |       968 |

## Feature Importances
![Feature Importance](./figures/feature_importance.png)

## Error Analysis (first 5 errors per class)
|    | True           | Predicted      |   koi_period |   koi_prad |   koi_steff |   koi_slogg |   koi_srad |
|---:|:---------------|:---------------|-------------:|-----------:|------------:|------------:|-----------:|
|  6 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 15 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 20 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 36 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 47 | CANDIDATE      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
| 16 | CONFIRMED      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
| 18 | CONFIRMED      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
| 32 | CONFIRMED      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
| 86 | CONFIRMED      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
| 95 | CONFIRMED      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
|  5 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
|  9 | FALSE POSITIVE | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 10 | FALSE POSITIVE | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 22 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
| 23 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
