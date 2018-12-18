# --- Directions
# Print out the n-th entry in the fibonacci series.
# The fibonacci series is an ordering of numbers where
# each number is the sum of the preceeding two.
# For example, the sequence
#  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# forms the first ten entries of the fibonacci series.
# Example:
#   fib(4) === 3
# iterative and recursive
# https://www.geeksforgeeks.org/memoization-using-decorators-in-python/


# memoization
def memoize_factorial(f):
    """Memoize function to save and run factorial."""
    memo = {}

    def inner(num):
        if num not in memo:
            memo[num] = f(num)
        return memo[num]
    return inner


@memoize_factorial
def facto(num):
    """Factorial function."""
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


print(facto(3))
