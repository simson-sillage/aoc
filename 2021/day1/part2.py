with open("input.txt") as file:
    input = file.read().strip()

measurements = input.split()
measurements = list(map(int, measurements))

count = 0
i = 3
while i < len(measurements):
    previous_window = measurements[i-3] + measurements[i-2] + measurements[i-1]
    current_window = measurements[i-2] + measurements[i-1] + measurements[i]
    if current_window > previous_window:
        count += 1
    i = i+1

print(f"count how often the measurement increased: {count}", )
