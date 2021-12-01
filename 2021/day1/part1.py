with open("input.txt") as file:
    input = file.read().strip()

measurements = input.split()
measurements = list(map(int, measurements))

count = 0
for i, measurement in enumerate(measurements):
    if i == 0:
        continue
    if measurement > measurements[i-1]:
        count += 1

print(f"count how often the measurement increased: {count}", )
