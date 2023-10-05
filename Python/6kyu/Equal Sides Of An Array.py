def find_even_index(arr):
    left_sum = 0
    right_sum = sum(arr)
    for i in range(len(arr)):
        right_sum -= arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1
