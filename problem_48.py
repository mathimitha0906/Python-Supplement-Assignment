# Problem 48: Create a simple calculator
# Find and fix the error

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:  # Check for division by zero
            return "Error: Division by zero!"
        return a / b
    else:
        return "Error: Unknown operation"

# Test cases
print(f"10 + 5 = {calculator(10, 5, 'add')}")
print(f"10 - 5 = {calculator(10, 5, 'subtract')}")
print(f"10 * 5 = {calculator(10, 5, 'multiply')}")
print(f"10 / 2 = {calculator(10, 2, 'divide')}")
print(f"10 / 0 = {calculator(10, 0, 'divide')}")
