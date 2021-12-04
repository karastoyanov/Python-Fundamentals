def smallest_number():
    a = int(input())
    b = int(input())
    c = int(input())
    
    
    for i in range(a, b, c):
        if a < b and a < c:
            return a
        elif b < a and b < c:
            return b
        else:
            return c
 
print(smallest_number())
  