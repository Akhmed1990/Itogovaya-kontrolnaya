def filter_strings(arr):
    new_string = []
    for string in arr:
        if len(string) <= 3:
            new_string.append(string)
    return new_string
input_arr = input("Введите массив строк через запятую: ").split(",")
result_arr = filter_strings(input_arr)
print("Результат:", result_arr)