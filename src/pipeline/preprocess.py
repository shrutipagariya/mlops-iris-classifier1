
"""
Stage 2: Data Preprocessing.
Removes duplicate rows and handles missing values.
"""

import argparse
import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("preprocess")


def preprocess_data(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    initial_rows = len(df)

    df = df.drop_duplicates()
    df = df.dropna()

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    logger.info("Rows before cleaning: %d", initial_rows)
    logger.info("Rows after cleaning: %d", len(df))
    logger.info("Saved cleaned data to %s", output_path)

    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="data/processed/iris_clean.csv")

    args = parser.parse_args()
    preprocess_data(args.input, args.output)
