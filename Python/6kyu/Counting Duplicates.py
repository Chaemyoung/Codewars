def duplicate_count(input_string):
    char_count = {}
    for char in input_string.lower():
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) + 1
            
    count = 0
    for value in char_count.values():
            if value > 1:
                count += 1
                
    return count
