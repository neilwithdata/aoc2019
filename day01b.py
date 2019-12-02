def calculate_fuel(mass):
    fuel = max(0, (mass // 3) - 2)
    if fuel > 0:
        fuel += calculate_fuel(fuel)
    return fuel


total_fuel = 0
with open('day01_input.txt') as file:
    for line in file:
        mass = int(line.strip())
        total_fuel += calculate_fuel(mass)

print(total_fuel)
