def get_sum(a,b):
    A, B = sorted([a, b])
    if a != b:
        return sum(i for i in range(A, B + 1))
    elif a == b:
        return a
