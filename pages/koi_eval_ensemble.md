# KOI Ensemble Model Evaluation Report

## Accuracy: 0.7700

## ROC AUC (macro, OVR): 0.9029

## Classification Report
![Classification Report](./figures/classification_report_ensemble.png)

## Confusion Matrix
![Confusion Matrix](./figures/confusion_matrix_ensemble.png)

## Compact Metrics Table (Slide Ready)
|                |   precision |   recall |   f1-score |   support |
|:---------------|------------:|---------:|-----------:|----------:|
| CANDIDATE      |        0.56 |     0.58 |       0.57 |       396 |
| CONFIRMED      |        0.78 |     0.82 |       0.8  |       549 |
| FALSE POSITIVE |        0.86 |     0.82 |       0.84 |       968 |

## Feature Importances
![Feature Importance](./figures/feature_importance_ensemble.png)

## Error Analysis (first 5 errors per class)
|     | True           | Predicted      |   koi_period |   koi_prad |   koi_steff |   koi_slogg |   koi_srad |
|----:|:---------------|:---------------|-------------:|-----------:|------------:|------------:|-----------:|
|   6 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
|  15 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
|  20 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
|  36 | CANDIDATE      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
|  47 | CANDIDATE      | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
|  13 | CONFIRMED      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
|  63 | CONFIRMED      | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
|  66 | CONFIRMED      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
|  73 | CONFIRMED      | FALSE POSITIVE |          nan |        nan |         nan |         nan |        nan |
| 107 | CONFIRMED      | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
|   5 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
|  22 | FALSE POSITIVE | CONFIRMED      |          nan |        nan |         nan |         nan |        nan |
|  23 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
|  26 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
|  37 | FALSE POSITIVE | CANDIDATE      |          nan |        nan |         nan |         nan |        nan |
