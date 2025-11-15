# Jessica Kusmierz
# 11/14/2025
# Problem 2
def check_sum():

    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    
     total = x + y
    
     if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")
    
    check_sum()