numbers_1 = [8, 19, 148, 4]
numbers_2 = [9, 1, 33, 83]
numbers_result = []

for number in numbers_1:
    for number2 in numbers_2:
        x = number * number2
        numbers_result.append(x)
print(numbers_result)

