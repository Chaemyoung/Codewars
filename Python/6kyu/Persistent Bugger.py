def persistence(num):
    if num < 10:
        return 0

    product = 1
    while num > 0:
        product *= num % 10
        num //= 10

    return 1 + persistence(product)
