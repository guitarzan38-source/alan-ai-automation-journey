import csv
from pathlib import Path

# CSV CLEANER – Day 2/84
# Drop any messy CSV here → gets cleaned in 2 seconds
input_file = "messy.csv"
output_file = "clean.csv"

rows = []
with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # Remove blank rows + strip whitespace
        clean_row = [cell.strip() for cell in row if cell.strip()]
        if clean_row:  # skip completely empty rows
            rows.append(clean_row)

# Remove duplicates while preserving order
seen = set()
unique_rows = []
for row in rows:
    row_tuple = tuple(row)
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_rows.append(row)

# Write clean version
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(unique_rows)

print(f"✅ Cleaned! {len(rows)} → {len(unique_rows)} rows. Saved to {output_file}")
Day 2: CSV cleaner (dedupes + strips junk)
