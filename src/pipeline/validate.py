
"""
Stage 4: Data Validation.
Checks the quality of the engineered Iris dataset.
"""

import argparse
import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("validate")


def validate_data(input_path: str) -> None:
    df = pd.read_csv(input_path)

    required_columns = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "species",
        "petal_area",
        "sepal_area",
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("Dataset is empty.")

    if df[required_columns].isnull().any().any():
        raise ValueError("Dataset contains missing values.")

    measurement_columns = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "petal_area",
        "sepal_area",
    ]

    if (df[measurement_columns] < 0).any().any():
        raise ValueError("Negative measurements found.")

    logger.info("Validation successful!")
    logger.info("Rows: %d", len(df))
    logger.info("Columns: %d", len(df.columns))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="data/processed/iris_features.csv"
    )

    args = parser.parse_args()
    validate_data(args.input)
