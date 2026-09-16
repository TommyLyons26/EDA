"""
eda_inspect.py

Step 1 of EDA: Load wildcat_loans_clean.csv and perform an initial inspection.

Prints:
    - Shape of the DataFrame (rows, columns)
    - All column names with their data types
    - Count of missing values for every column

Run with:
    python scripts/eda_inspect.py
"""

import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "02_Data" / "Raw" / "wildcat_loans_clean.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    print(f"Shape (rows, columns): {df.shape}\n")

    print("Column names and data types:")
    print(df.dtypes)
    print()

    print("Missing values per column:")
    print(df.isnull().sum())


if __name__ == "__main__":
    main()
