
"""
Stage 3: Feature Engineering.
Creates additional features from Iris measurements.
"""

import argparse
import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("features")


def create_features(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    df["petal_area"] = (
        df["petal length (cm)"] * df["petal width (cm)"]
    )

    df["sepal_area"] = (
        df["sepal length (cm)"] * df["sepal width (cm)"]
    )

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    logger.info("Created features for %d rows", len(df))
    logger.info("Saved features to %s", output_path)

    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument(
        "--output",
        default="data/processed/iris_features.csv"
    )

    args = parser.parse_args()
    create_features(args.input, args.output)
