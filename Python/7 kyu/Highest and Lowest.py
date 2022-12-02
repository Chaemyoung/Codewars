def high_and_low(numbers): 
    numbs = [int(num) for num in numbers.split()]
    return f'{max(numbs)} {min(numbs)}'
