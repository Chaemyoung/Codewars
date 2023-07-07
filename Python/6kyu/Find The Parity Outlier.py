def find_outlier(arr):
    even_count = 0
    odd_count = 0
    last_even = None
    last_odd = None

    for num in arr:
        if num % 2 == 0:
            even_count += 1
            last_even = num
        else:
            odd_count += 1
            last_odd = num

        # Check if we have identified both even and odd elements
        if even_count > 0 and odd_count > 0:
            break

    return last_even if even_count == 1 else last_odd
