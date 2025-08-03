import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader)  # skip header row

for row in reader:
    try:
        # Adjust this index if needed
        state = row[2].strip().lower()

        if state:
            print(f"{state}\t1")
    except IndexError:
        continue  # skip malformed rows
