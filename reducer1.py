import sys

current_state = None
count = 0

for line in sys.stdin:
    try:
        state, val = line.strip().split('\t')
        val = int(val)
    except:
        continue

    if state == current_state:
        count += val
    else:
        if current_state:
            print(f"{current_state}\t{count}")
        current_state = state
        count = val

# Final state
if current_state:
    print(f"{current_state}\t{count}")
