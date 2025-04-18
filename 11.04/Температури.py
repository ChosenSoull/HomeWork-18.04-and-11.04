import random

def generate_temperatures():
    temps = [random.randint(-10, 10) for _ in range(31)]
    return temps

def count_positive_days(temps):
    return sum(temp > 0 for temp in temps)

def count_temperature_jumps(temps):
    jumps = 0
    for i in range(len(temps) - 1):
        if (temps[i] > 0 and temps[i + 1] < 0) or (temps[i] < 0 and temps[i + 1] > 0):
            jumps += 1
    return jumps

def find_lowest_temp_date(temps):
    lowest_temp = min(temps)
    day = temps.index(lowest_temp) + 1 
    return lowest_temp, day

def calc_temp_difference(temps):
    max_temp = max(temps)
    min_temp = min(temps)
    return max_temp, min_temp, max_temp - min_temp

def main():
    temperatures = generate_temperatures()
    print("Температури за березень:", temperatures)
    
    positive_days = count_positive_days(temperatures)
    print(f"Днів із температурою вище 0: {positive_days}")
    
    jumps = count_temperature_jumps(temperatures)
    print(f"Кількість стрибків температур: {jumps}")
    
    lowest_temp, lowest_day = find_lowest_temp_date(temperatures)
    print(f"Найнижча температура {lowest_temp}°C була {lowest_day} березня")
    
    max_temp, min_temp, difference = calc_temp_difference(temperatures)
    print(f"Різниця між найвищою ({max_temp}°C) і найнижчою ({min_temp}°C) температурами: {difference}°C")

if __name__ == "__main__":
    main()
