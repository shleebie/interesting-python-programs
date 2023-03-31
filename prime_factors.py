import math

# initiate

factor = 2

n = int(input(f"Enter a number: "))

# if number is greater than 2, calculate prime factors

if n >= 2:
    print(f"The prime factors of {n} are: ")
    while factor <= n:
      
        # if remainder is zero, count as factor
        
        if n % factor == 0:
            print(factor)
            n //= factor
        else:
          
            # increase by one
            
            factor = factor + 1
else:
    print("No prime factors")
