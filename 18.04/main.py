import random

def generate_array():
    size = random.randint(7, 12)
    array = [random.randint(-50, 50) for _ in range(size)]
    return array

def sort_array(array):
    return sorted(array)

def print_arrays(original, sorted_array):
    print("Несортований масив:", original)
    print("Відсортований масив:", sorted_array)

def main():
    original_array = generate_array()
    
    sorted_array = sort_array(original_array)
    
    print_arrays(original_array, sorted_array)

if __name__ == "__main__":
    main()