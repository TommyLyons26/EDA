"""
eda_datetime_check.py

Checks whether the origination_date column is stored as a datetime type.
If it is stored as text (object type), converts it to datetime and
prints a confirmation message, showing the column's type before and after.

Run with:
    python scripts/eda_datetime_check.py
"""

import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "02_Data" / "Raw" / "wildcat_loans_clean.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    before_type = df["origination_date"].dtype
    print(f"origination_date type before: {before_type}")

    if pd.api.types.is_datetime64_any_dtype(df["origination_date"]):
        print("origination_date is already a datetime type. No conversion needed.")
    else:
        df["origination_date"] = pd.to_datetime(df["origination_date"])
        after_type = df["origination_date"].dtype
        print(f"origination_date type after: {after_type}")
        print("Converted origination_date from text (object) to datetime.")


if __name__ == "__main__":
    main()
