# Calculate the sum of three numbers if the values is equl and return thrice
def sum_thrice(x , y , z):
    sum  = x + y + z
    if x == y == z:
        sum *= 3
        return sum
    
print(sum_thrice(3,3,3))