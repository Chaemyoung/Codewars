def dominator(arr):
    n = len(arr)
    if n == 0:
        return -1
    candidate = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = arr[i]
                count = 1
    count = 0
    for i in range(n):
        if arr[i] == candidate:
            count += 1
    if count > n // 2:
        return candidate
    else:
        return -1
