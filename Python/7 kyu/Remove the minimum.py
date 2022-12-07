def remove_smallest(numbers): 
    if len(numbers) < 2:
        return []
    else:
        new = numbers[:]
        new.remove(min(numbers))
    return new
