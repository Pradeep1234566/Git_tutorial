def sum_of_n_numbers(n):
    print("Version 4")
    return sum(range(1, n + 1))

# Example usage
n = int(input())
result = sum_of_n_numbers(n)
print(f"The sum of numbers from 1 to {n} is: {result}")