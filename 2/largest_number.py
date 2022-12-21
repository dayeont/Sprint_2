def largest_number(n: int, numbers: str) -> str:
    numbers = numbers.split()
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            s1 = numbers[j] + numbers[j + 1]
            s2 = numbers[j + 1] + numbers[j]
            if s1 < s2:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return "".join(numbers)


print(largest_number(int(input()), input()))
