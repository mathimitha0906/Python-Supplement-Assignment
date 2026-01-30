# Problem 77: Check if number is perfect square
# Find and fix the error

def is_perfect_square(n):
    if n < 0:
        return False  # negative numbers cannot be perfect squares
    sqrt = int(n ** 0.5)  # integer square root
    return sqrt * sqrt == n  # check by squaring back

# Test cases
print(f"Is 16 perfect square? {is_perfect_square(16)}")  # True
print(f"Is 15 perfect square? {is_perfect_square(15)}")  # False
print(f"Is 100000000 perfect square? {is_perfect_square(100000000)}")  # True
print(f"Is 100000001 perfect square? {is_perfect_square(100000001)}")  # False

