# Practical 4: Data Collection, Preprocessing, Feature Engineering, Validation, and Pipeline Automation

## 1. Aim
To build an automated data pipeline using Python and DVC for data collection, preprocessing, feature engineering, and data validation.

## 2. Software Required
- Python
- Visual Studio Code
- Git
- DVC
- Pandas
- Scikit-learn

## 3. Pipeline Stages

### Stage 1: Data Collection
The `collect.py` script collects the Iris dataset, converts target values into species names, adds collection-time information, and saves the raw data to `data/raw/iris_raw.csv`.

### Stage 2: Data Preprocessing
The `preprocess.py` script removes duplicate rows and rows containing missing values. The cleaned dataset is saved to `data/processed/iris_clean.csv`.

### Stage 3: Feature Engineering
The `features.py` script creates two additional features:
- `petal_area` = petal length × petal width
- `sepal_area` = sepal length × sepal width

The engineered dataset is saved to `data/processed/iris_features.csv`.

### Stage 4: Data Validation
The `validate.py` script checks required columns, empty datasets, missing values, and negative measurements.

## 4. DVC Pipeline Configuration
The `dvc.yaml` file defines the four stages and their dependencies and outputs. DVC records pipeline information in `dvc.lock`.

## 5. Commands Used

Run the pipeline:

```bash
dvc repro
```

Display the pipeline dependency graph:

```bash
dvc dag
```

Check pipeline status:

```bash
dvc status
```

## 6. Results
- Raw dataset collected: 150 rows.
- Rows after preprocessing: 149.
- Engineered dataset: 149 rows and 8 columns.
- Data validation: Successful.
- DVC status: Data and pipelines are up to date.

## 7. Conclusion
The data pipeline was implemented successfully using Python and DVC. Data collection, preprocessing, feature engineering, and validation were executed as separate stages. DVC was used to track pipeline dependencies and outputs.