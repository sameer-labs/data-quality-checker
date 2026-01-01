import csv
import numpy as np

input_file = "used_cars.csv"
output_file = "used_cars_cleaned.csv"

# Track errors per column
error_count = {}

def clean_and_validate(value, column_name):
    
   # Detect missing / dirty data and clean numeric fields.

    # Initialize counter
    if column_name not in error_count:
        error_count[column_name] = 0

    # Handle missing values
    if value is None or value.strip() == "" or value.lower().strip() == "null":
        error_count[column_name] += 1
        return np.nan

    value = value.strip()

    # Remove common units
    cleaned = (
        value.replace(" kmpl", "")
             .replace(" km/kg", "")
             .replace(" CC", "")
             .replace(" bhp", "")
             .replace(" Lakh", "")
    )

    # Try converting to number
    try:
        return float(cleaned)
    except ValueError:
        return value  # keep text fields unchanged


with open(input_file, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

cleaned_rows = []

for row in rows:
    cleaned_row = {}
    for column in fieldnames:
        value = row.get(column, "")
        cleaned_row[column] = clean_and_validate(value, column)
    cleaned_rows.append(cleaned_row)

# Write cleaned CSV
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows)

# ===== ERROR SUMMARY (Client-Facing) =====
print("\nDATA QUALITY SUMMARY")
print("-" * 30)
for col, count in error_count.items():
    print(f"{col}: {count} issues detected")

print("\nCleaned file saved as:", output_file)
