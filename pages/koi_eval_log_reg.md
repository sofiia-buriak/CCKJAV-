# KOI Evaluation Report

## Classification Report
![Classification Report](./figures/classification_report.png)

## Confusion Matrix
![Confusion Matrix](./figures/confusion_matrix.png)

## Compact Metrics Table (Slide Ready)
|                |   precision |   recall |   f1-score |   support |
|:---------------|------------:|---------:|-----------:|----------:|
| CANDIDATE      |        0.38 |     0.48 |       0.43 |       396 |
| CONFIRMED      |        0.55 |     0.78 |       0.64 |       549 |
| FALSE POSITIVE |        0.84 |     0.55 |       0.66 |       968 |

## Feature Importances
![Feature Importance](./figures/feature_importance.png)

## Error Analysis (first 5 errors per class)
|    | True           | Predicted      |   koi_period |   koi_prad |   koi_steff |   koi_slogg |   koi_srad |
|---:|:---------------|:---------------|-------------:|-----------:|------------:|------------:|-----------:|
|  6 | CANDIDATE      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
| 15 | CANDIDATE      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
| 20 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 36 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 47 | CANDIDATE      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
| 16 | CONFIRMED      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 18 | CONFIRMED      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 32 | CONFIRMED      | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
| 86 | CONFIRMED      | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
| 95 | CONFIRMED      | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
|  5 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
|  9 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
| 10 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
| 22 | FALSE POSITIVE | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
| 23 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
