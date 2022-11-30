def create_phone_number(n):
    number = n
    digit = ''.join([str(num) for num in number])
    
    return f'({digit[:3]}) {digit[3:6]}-{digit[6:10]}'
  
  
  ###https://github.com/hevalhazalkurt/codewars_python_solutions/blob/master/6kyuKatas/Create_Phone_Number.md
