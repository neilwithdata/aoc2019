total_fuel = 0

with open('day01_input.txt') as file:
    for line in file:
        mass = int(line.strip())
        total_fuel += (mass // 3) - 2

print(total_fuel)
