def input_array():
    while True:
        try:
            input_str = input("Привіт, введіть 10 чисел в одну строку через пробіл: ")
            numbers = input_str.split()

            if len(numbers) != 10:
                print(f"Помилка! Потрібно ввести рівно 10 чисел. Ви ввели {len(numbers)} чисел.")
                continue
            
            arr = []
            for num in numbers:
                arr.append(float(num))
            return arr
            
        except ValueError:
            print("Помилка! Введіть дійсні числа через пробіл.")
            continue

def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def main():
    array = input_array()
    
    print("\nПочатковий масив:", array)
    
    sorted_array = selection_sort_desc(array)
    
    print("Відсортований масив за спаданням:", sorted_array)

if __name__ == "__main__":
    main()
