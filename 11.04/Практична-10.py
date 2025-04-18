def input_results():
    while True:
        try:
            input_str = input("Введіть результати учасників у форматі 'номер:час' через пробіл (наприклад, 1:30 2:33): ")
            entries = input_str.split()
            
            if len(entries) == 0:
                print("Помилка! Введіть хоча б один результат.")
                continue
            
            results = []
            participant_numbers = []
            for entry in entries:
                if ':' not in entry:
                    print(f"Помилка! Неправильний формат у '{entry}'. Використовуйте 'номер:час'.")
                    break
                num, time = entry.split(':')
                
                participant_num = int(num)
                participant_time = float(time)
                if participant_num <= 0 or participant_time <= 0:
                    print(f"Помилка! Номер учасника і час мають бути більше 0 у '{entry}'.")
                    break
                if participant_num in participant_numbers:
                    print(f"Помилка! Номер учасника {participant_num} повторюється.")
                    break
                
                participant_numbers.append(participant_num)
                results.append(participant_time)
            else:
                return participant_numbers, results
            
        except ValueError:
            print("Помилка! Перевірте, що номери учасників — цілі числа, а час — дійсні числа.")
        continue

def analyze_results(participant_numbers, results, record):
    max_time = max(results)
    min_time = min(results)
    max_time_idx = results.index(max_time)
    min_time_idx = results.index(min_time)
    worst_participant = participant_numbers[max_time_idx]
    best_participant = participant_numbers[min_time_idx]
    
    better_than_record_count = sum(1 for time in results if time < record)
    
    record_updated = min_time < record
    new_record = min_time if record_updated else record
    
    return max_time, min_time, worst_participant, best_participant, better_than_record_count, record_updated, new_record

def main():
    while True:
        try:
            record = float(input("Введіть поточний рекорд закладу (у секундах): "))
            if record <= 0:
                print("Помилка! Рекорд має бути більше 0.")
                continue
            break
        except ValueError:
            print("Помилка! Введіть дійсне число.")
    
    participant_numbers, results = input_results()
    
    max_time, min_time, worst_participant, best_participant, better_than_record_count, record_updated, new_record = analyze_results(participant_numbers, results, record)
    
   
    print("\nРезультати змагань:")
    print(f"Найгірший результат: учасник {worst_participant}, час {max_time} секунд")
    print(f"Найкращий результат: учасник {best_participant}, час {min_time} секунд")
    print(f"Кількість спортсменів, які пробігли швидше за старий рекорд ({record} секунд): {better_than_record_count}")
    if record_updated:
        print(f"Рекорд закладу оновлено! Новий рекорд: {new_record} секунд")
    else:
        print("Рекорд закладу не оновлено.")

if __name__ == "__main__":
    main()
