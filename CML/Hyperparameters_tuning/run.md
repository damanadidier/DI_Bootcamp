
## GitHub Actions workflow for Hyperparameter tuning
```dvc repro -f hp_tune```

Training pipeline is run by running ```dvc repro train```.
Force running Hyperparameter tuning pipeline is done by running ```dvc repro -f hp_tune```.
Comparing metrics against the main branch is done by running ```dvc metrics diff main```.