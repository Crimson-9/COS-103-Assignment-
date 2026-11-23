# Create a list of numbers
numbers = [2, 4, 3, 5, 5, 7, 3, 9, 7, 5, 6, 5]

# Print the list
print("Numbers:", numbers)


# 1. Sum of numbers
def sum_numbers(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total


# 2. Average of numbers
def average(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total / len(numbers)


# 3. Median and mode
def median_mode(numbers):
    # Arrange numbers in order
    numbers.sort()

    middle = len(numbers) // 2
    median = numbers[middle]

    # Find the mode
    mode = numbers[0]
    highest = 0

    for num in numbers:
        count = 0

        for other in numbers:
            if num == other:
                count = count + 1

        if count > highest:
            highest = count
            mode = num

    return median, mode


# Print the results
print("Sum:", sum_numbers(numbers))
print("Average:", average(numbers))

median, mode = median_mode(numbers)

print("Median:", median)
print("Mode:", mode)