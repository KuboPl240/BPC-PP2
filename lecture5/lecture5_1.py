
def hex_calculator(first_operand, operation, second_operand):
    try:
        if len(first_operand) != 2 or not all(c in "0123456789ABCDEFabcdef" for c in first_operand):
            raise ValueError("Invalid hexadecimal number for the first operand. Please enter a two-digit hex number.")

        if len(second_operand) != 2 or not all(c in "0123456789ABCDEFabcdef" for c in second_operand):
            raise ValueError("Invalid hexadecimal number for the second operand. Please enter a two-digit hex number.")

        if operation not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operation. Please use one of +, -, *, /.")

        first_operand_decimal = int(first_operand, 16)
        second_operand_decimal = int(second_operand, 16)

        if operation == '/' and second_operand_decimal == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        if operation == '+':
            result = first_operand_decimal + second_operand_decimal
        elif operation == '-':
            result = first_operand_decimal - second_operand_decimal
        elif operation == '*':
            result = first_operand_decimal * second_operand_decimal
        elif operation == '/':
            result = first_operand_decimal / second_operand_decimal

        result_hex = hex(int(result))[2:].upper()
        return f"The result is: {result_hex}"

    except ValueError as ve:
        return f"Error: {ve}"
    except ZeroDivisionError as zde:
        return f"Error: {zde}"

print(hex_calculator("00", "/", "00"))  
