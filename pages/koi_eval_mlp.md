# KOI Neural Network Evaluation Report

## Accuracy: 0.7554

## Classification Report
![Classification Report](./figures/classification_report_mlp.png)

## Confusion Matrix
![Confusion Matrix](./figures/confusion_matrix_mlp.png)

## Compact Metrics Table (Slide Ready)
|                |   precision |   recall |   f1-score |   support |
|:---------------|------------:|---------:|-----------:|----------:|
| CANDIDATE      |        0.53 |     0.54 |       0.54 |       396 |
| CONFIRMED      |        0.79 |     0.79 |       0.79 |       549 |
| FALSE POSITIVE |        0.83 |     0.82 |       0.83 |       968 |

## Feature Importances
![Feature Importance](./figures/feature_importance_mlp.png)

## Error Analysis (first 5 errors per class)
|    | True           | Predicted      |   koi_period |   koi_prad |   koi_steff |   koi_slogg |   koi_srad |
|---:|:---------------|:---------------|-------------:|-----------:|------------:|------------:|-----------:|
|  6 | CANDIDATE      | FALSE POSITIVE |     nan      |     nan    |         nan |     nan     |    nan     |
| 20 | CANDIDATE      | FALSE POSITIVE |     nan      |     nan    |         nan |     nan     |    nan     |
| 36 | CANDIDATE      | FALSE POSITIVE |     nan      |     nan    |         nan |     nan     |    nan     |
| 57 | CANDIDATE      | FALSE POSITIVE |     nan      |     nan    |         nan |     nan     |    nan     |
| 75 | CANDIDATE      | CONFIRMED      |      14.1798 |       1.88 |        5799 |       4.539 |      0.878 |
|  7 | CONFIRMED      | CANDIDATE      |     nan      |     nan    |         nan |     nan     |    nan     |
| 13 | CONFIRMED      | FALSE POSITIVE |     nan      |     nan    |         nan |     nan     |    nan     |
| 63 | CONFIRMED      | CANDIDATE      |     nan      |     nan    |         nan |     nan     |    nan     |
| 66 | CONFIRMED      | FALSE POSITIVE |     nan      |     nan    |         nan |     nan     |    nan     |
| 73 | CONFIRMED      | FALSE POSITIVE |     nan      |     nan    |         nan |     nan     |    nan     |
|  5 | FALSE POSITIVE | CANDIDATE      |     nan      |     nan    |         nan |     nan     |    nan     |
| 22 | FALSE POSITIVE | CONFIRMED      |     nan      |     nan    |         nan |     nan     |    nan     |
| 23 | FALSE POSITIVE | CANDIDATE      |     nan      |     nan    |         nan |     nan     |    nan     |
| 37 | FALSE POSITIVE | CANDIDATE      |     nan      |     nan    |         nan |     nan     |    nan     |
| 39 | FALSE POSITIVE | CANDIDATE      |     nan      |     nan    |         nan |     nan     |    nan     |
