#Jessica Kusmierz
#10/31/2025
#Problem 4

import math
print("pi Approximation")
terms = 1000000
pi_approx = 0
for i in range(terms):
    pi_approx += ((-1)**i) / (2 * i + 1)
pi_approx *= 4
print(f"Approximated pi: {pi_approx}")
print(f"math module pi: {math.pi}")
print(f"Difference: {abs(math.pi - pi_approx)}")