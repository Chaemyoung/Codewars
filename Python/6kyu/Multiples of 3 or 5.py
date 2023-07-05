def solution(number):
    sum = 0
    for i in range(1,number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

#The range() function generates a sequence of numbers from 1 to number (exclusive), 
#which means that it generates all the numbers between 1 and number, but not including number itself. 
#The loop then iterates over each number in the sequence using the variable i. 
#For each number, it checks if it is a multiple of 3 or 5 using an if statement and the modulo operator %. 
#If it is a multiple of 3 or 5, it adds it to the sum variable using the += operator.
