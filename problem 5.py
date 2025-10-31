#Jessica Kusmierz
#10/31/2025
#Problem 5

import math
print("Radians to degree conversion")
radians = float(input("Enter a value in radians: "))
degrees_manual = radians * (180 / math.pi)
degrees_math = math.degrees(radians)
print(f"Manual conversion: {degrees_manual} degrees")
print(f"math.degrees(): {degrees_math} degrees")
print(f"Difference: {abs(degrees_manual - degrees_math)} degrees")
except ValueError
    print("Invalid input. Please enter a numeric value for radians.")