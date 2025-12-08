# Jessica Kusmierz
# 11/6/2025
# Problem 4

def get_unique_elements(numbers):
    """
    Return a list of unique elements from the input list, preserving order.
    """
    seen = set()
    unique_list = []
    for number in numbers:
        if number not in seen:
            unique_list.append(number)
            seen.add(number)
    return unique_list   
