import math

def is_square(n):   
    if n < 0:
        return False
    else:
        squared = math.sqrt(n)
        
    if n == squared**2:
        return True
    else:
        return False
