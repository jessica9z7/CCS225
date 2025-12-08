# Jessica Kusmierz
# 11/6/2025
# Problem 3

def multiply_list(numbers):
    """
       Multiply all the numbers in a list and return the product.

       Args:
           numbers (list of int/float): The numbers to multiply.

       Returns:
           int/float: The product of all numbers in the list.
       """
    product = 1
    for number in numbers:
        product *= number
    return product
