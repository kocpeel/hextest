def decimal_to_hex(decimal_number):
    if not isinstance(decimal_number, int) or decimal_number < 0:
        raise ValueError("Invalid input. Please provide a positive integer.")

    if decimal_number == 0:
        return "0"

    hex_representation = ""
    hex_digits = "0123456789ABCDEF"

    while decimal_number > 0:
        remainder = decimal_number % 16
        hex_representation = hex_digits[remainder] + hex_representation
        decimal_number //= 16

    # print(hex_representation)
    return hex_representation

# decimal_to_hex(12345)