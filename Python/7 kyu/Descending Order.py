def descending_order(num):
    list = []
    for x in str(num):
        list.append(x)
        
    answer = list.sort(reverse=True)

    num_seperates = ''.join(list)
    return int(num_seperates)
