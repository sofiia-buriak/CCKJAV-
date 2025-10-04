# TOI Evaluation Report

## Multi-class Ensemble
                precision    recall  f1-score   support

     CANDIDATE       0.79      0.84      0.82      1028
     CONFIRMED       0.56      0.54      0.55       253
FALSE POSITIVE       0.59      0.46      0.52       259

      accuracy                           0.73      1540
     macro avg       0.65      0.61      0.63      1540
  weighted avg       0.72      0.73      0.72      1540


Confusion matrix saved as `multi_class_cm.png`

## Binary Ensemble
              precision    recall  f1-score   support

   CANDIDATE       0.35      0.27      0.30        92
       FALSE       0.57      0.46      0.51       259
      PLANET       0.87      0.92      0.89      1189

    accuracy                           0.80      1540
   macro avg       0.59      0.55      0.57      1540
weighted avg       0.79      0.80      0.79      1540


Confusion matrix saved as `binary_cm.png`

## Top-N TOI by CONFIRMED probability
|      |   prob_CONFIRMED |
|-----:|-----------------:|
| 4446 |        0.0503584 |
| 5073 |        0.0775141 |
| 6550 |        0.0825785 |
| 4406 |        0.112184  |
| 7296 |        0.100437  |
| 2755 |        0.0194206 |
| 7577 |        0.018377  |
| 3993 |        0.133595  |
| 2120 |        0.236434  |
| 1062 |        0.314577  |