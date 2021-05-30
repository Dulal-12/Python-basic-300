def add_number (a , b):
    
    if not((isinstance(a , int)) and isinstance(b , int)):
        raise TypeError("Value must be integer")
    return a+b

print(add_number(2,4.6))