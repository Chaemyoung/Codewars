def find_outlier(integers):
    odds = [x for x in integers if x%2!=0]
    evens= [x for x in integers if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
