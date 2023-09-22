def positive_sum(arr):
    # Your code here
    final_ans = 0
    
    for num in arr:
        if num > 0:
            final_ans += num
        elif num == 0:
            final_ans += 0
        else:
            pass
    
    return final_ans
