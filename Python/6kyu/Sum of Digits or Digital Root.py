def digital_root(n):
    while n > 9:
        digits = [int(d) for d in str(n)]
        n = sum(digits)
    return n
