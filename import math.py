#Jessica Kusmierz
#10/31/2025
#Problem 6

import math
print("Factorial Calculation")
n=int(input("Enter a non-negative integer: "))

if n<0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial_manual=1
    for i in range(1,n+1):
        factorial_manual *=i
    factorial_math=math.factorial(n)
    print(f"Factorial calculated manually: {factorial_manual}")
    print(f"Factorial using math module: {factorial_math}")
    print(f"match: {factorial_manual == factorial_math}")
except ValueError:
       print("Invalid input. Please enter a non-negative integer.")