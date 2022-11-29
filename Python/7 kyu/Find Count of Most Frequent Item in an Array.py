def most_frequent_item_count(collection):
    count = 0
    numbers = collection
    
    for n in numbers:
        frequency = numbers.count(n)
        if frequency > count:
            count = frequency
        else:
            pass
        
    return count
  
  ### https://www.w3schools.com/python/ref_list_count.asp
  ### https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
