
def validate_hex_input(hex_str):
    if len(hex_str) != 2 or not all(c in '0123456789ABCDEFabcdef' for c in hex_str):
        raise ValueError(f"Invalid hexadecimal number: {hex_str}")
    return int(hex_str, 16)

def hex_calculator():
    try:
        first_operand = input("Enter the first operand (two hexa-digits): ").strip()
        first_value = validate_hex_input(first_operand)
        
        operation = input("Enter the operation (+, -, *, /): ").strip()
        if operation not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operation. Use one of +, -, *, /.")
        
        second_operand = input("Enter the second operand (two hexa-digits): ").strip()
        second_value = validate_hex_input(second_operand)
        
        if operation == '/' and second_value == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        
        if operation == '+':
            result = first_value + second_value
        elif operation == '-':
            result = first_value - second_value
        elif operation == '*':
            result = first_value * second_value
        elif operation == '/':
            result = first_value // second_value
        
        print(f"The result in hexadecimal is: {hex(result)[2:].upper()}")
    
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)

hex_calculator()
