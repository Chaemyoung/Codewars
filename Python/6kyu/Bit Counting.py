def count_bits(n):
    list = []
    binary = bin(n)[2:]
    
    for num in binary:
        list.append(num)
    count = list.count('1')
    return count
