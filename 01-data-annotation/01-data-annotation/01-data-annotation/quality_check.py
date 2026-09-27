import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "annotation_sample.csv"

REVIEW_THRESHOLD = 0.75


def load_records(file_path):
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}\n"
            "Make sure annotation_sample.csv is in the same folder as this script."
        )

    records = load_records(DATA_FILE)

    total_records = len(records)

    approved = sum(
        1 for row in records
        if row["review_status"].strip().lower() == "approved"
    )

    review = sum(
        1 for row in records
        if row["review_status"].strip().lower() == "review"
    )

    low_confidence = sum(
        1 for row in records
        if float(row["confidence"]) < REVIEW_THRESHOLD
    )

    label_inconsistencies = sum(
        1 for row in records
        if row["issue_flag"].strip().lower() == "label inconsistency"
    )

    corrections = sum(
        1 for row in records
        if row["assigned_label"].strip().lower()
        != row["corrected_label"].strip().lower()
    )

    approval_rate = (approved / total_records) * 100 if total_records else 0
    review_rate = (review / total_records) * 100 if total_records else 0

    print("\nANNOTATION QUALITY REPORT")
    print("=" * 30)

    print(f"Total records: {total_records}")
    print(f"Approved records: {approved}")
    print(f"Records requiring review: {review}")
    print(f"Approval rate: {approval_rate:.1f}%")
    print(f"Review rate: {review_rate:.1f}%")
    print(f"Low-confidence cases: {low_confidence}")
    print(f"Label inconsistencies: {label_inconsistencies}")
    print(f"Label corrections: {corrections}")

    print("\nQUALITY CHECK COMPLETE")


if __name__ == "__main__":
    main()
