# Jessica Kusmierz
# 11/14/2025
# Problem 3
def check_for_five(my_list):
    if 5 in my_list:
        print("5 is in the list.")
    else:
        print("5 is not in the list.")
test_list1 = [1, 2, 3, 4, 6]
test_list2 = [2, 4, 6, 8, 10]
test_list3 = [5, 5, 5, 5]

print("Test List 1:", test_list1)
check_for_five(test_list1)

print("Test List 2:", test_list2)
check_for_five(test_list2)

print("Test List 3:", test_list3)
check_for_five(test_list3)



