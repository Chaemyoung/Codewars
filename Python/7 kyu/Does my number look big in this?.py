def narcissistic( value ):

    # Convert the value to a string to count its digits
    value_str = str(value)
    
    # Get the number of digits in the value
    num_digits = len(value_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in value_str)
    
    # Check if the sum is equal to the original value
    return sum_of_powers == value

