# Jessica Kusmierz
# 11/6/2025
# Problem 2

def check_range(num):
    """
    Check if a number is within the range 1 to 9 (inclusive of 1, exclusive of 10).

    Args:
        num (int): The number to check.
    """
    if num in range(1, 10):
        print(num, "is in the range")
    else:
        print(num, "is out of range")   
        
