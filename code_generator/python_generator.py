def generate_python_code(operation, variables):
    if operation == "palindrome":
        if not variables:
            return "print('Error: No number provided for palindrome check')"
        num = variables[0]
        return f"""
num = {num}
num_str = str(num)
if num_str == num_str[::-1]:
    print(f"Yes, {{num}} is a palindrome")
else:
    print(f"No, {{num}} is not a palindrome")
"""
    
    elif operation == "odd_even":
        if not variables:
            return "print('Error: No number provided for odd/even check')"
        num = variables[0]
        return f"""
num = {num}
if int(num) % 2 == 0:
    print(f"{{num}} is an even number")
else:
    print(f"{{num}} is an odd number")
"""
    
    elif operation == "armstrong":
        if not variables:
            return "print('Error: No number provided for Armstrong check')"
        num = variables[0]
        return f"""
num = {num}
num_str = str(num)
num_digits = len(num_str)
sum = 0

for digit in num_str:
    sum += int(digit) ** num_digits

if int(num) == sum:
    print(f"Yes, {{num}} is an Armstrong number")
else:
    print(f"No, {{num}} is not an Armstrong number")
"""
    
    if len(variables) != 2:
        return "print('Error: Invalid number of operands')"
    
    var1, var2 = variables

    operation_map = {
        "add": f"print({var1} + {var2})",
        "subtract": f"print({var1} - {var2})",
        "multiply": f"print({var1} * {var2})",  # ✅ Add multiplication support
        "divide": f"print({var1} / {var2}) if {var2} != 0 else print('Error: Division by zero')"
    }

    return operation_map.get(operation, "print('Error: Unsupported operation')")  # ✅ Ensure "multiply" is mapped
