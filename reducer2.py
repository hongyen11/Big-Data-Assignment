import sys

current_manufacturer = None
total_price = 0.0
count = 0

for line in sys.stdin:
    try:
        manufacturer, price = line.strip().split('\t')
        price = float(price)
    except:
        continue

    if manufacturer == current_manufacturer:
        total_price += price
        count += 1
    else:
        if current_manufacturer and count > 0:
            avg_price = total_price / count
            print(f"{current_manufacturer}\t{round(avg_price, 2)}")
        current_manufacturer = manufacturer
        total_price = price
        count = 1

# final output
if current_manufacturer and count > 0:
    avg_price = total_price / count
    print(f"{current_manufacturer}\t{round(avg_price, 2)}")
