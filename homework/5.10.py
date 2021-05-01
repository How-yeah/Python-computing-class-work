def sum(numbers: list) -> int:
    sum_number = 0
    for number in numbers:
        sum_number += number
    return sum_number


a = [3, 23, 4, 223, 3]
print(sum(a))

b = sorted(a)
