def stray(arr):
    leastCount, leastElement = len(arr), -99
    for i in range(len(arr)):
        currentCount = 0
        for j in range(len(arr)):
            if (arr[i] == arr[j]):
                currentCount += 1
        if (currentCount < leastCount):
            leastCount, leastElement = currentCount, arr[i]
    return leastElement
  
  ###https://iq.opengenus.org/least-frequent-element-in-array/

def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
