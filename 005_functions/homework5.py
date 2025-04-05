# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number
def square_list(numbers):
    # squares = []
    # for num in numbers:
    #     squares.append(num ** 2)
    # return squares
    return [num ** 2 for num in numbers]

print(square_list([1,2,3,4,5,6]))


# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens
def odds_and_evens(numbers):
    odds = 0
    evens = 0
    for num in numbers:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    return odds, evens

print(odds_and_evens([1, 1, 2, 2, 2, 3, 4, 5, 6, 7]))


# Write a function that accepts a list of numbers
# and returns largest number
def largest_from_list(numbers):
    return max(numbers)

# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)
def fizz_buzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(num, 'FIZZBUZZ')
        elif num % 3 == 0:
            print(num, 'FIZZ')
        elif num % 5 == 0:
            print(num, 'BUZZ')
        else:
            print(num)

fizz_buzz(500, 600)