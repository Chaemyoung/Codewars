def sum_no_duplicates(l):
    list = []
    for x in l:
        if l.count(x) == 1:
            list.append(x)
    return sum(list)

