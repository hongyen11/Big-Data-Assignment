import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader)  # skip header

for row in reader:
    try:
        manufacturer = row[1].strip().lower()
        price = float(row[0].strip())

        if manufacturer and price > 0:
            print(f"{manufacturer}\t{price}")
    except (IndexError, ValueError):
        continue  # skip malformed rows
