# # Solving using loop but array given in advance



# def Missing_Num():
#     not_empty_array = [1,2,3,4,5,6,7,8,9]
#     print(not_empty_array)
#     for i in range (1,11):
#         if i not in not_empty_array:
#             print(f"This missing number is: {i}")
        
    
# Missing_Num()



# # Solving using loop but array given at runtime




# print("Input numbers are: ")
# weird_array = input()

# parts = weird_array.split()

# nums = list(map(int, parts))



# def Missing_Number():
#     for i in range (1, 11):
#         if i not in nums:
#             print(f"Missing number is: {i}")
    
# Missing_Number()



# # Solving it by comparing to an array



# comparison_array = [1,2,3,4,5,6,7,8,9,10]

# print("Enter your array: ")
# creation = input()
# splitting = creation.split()
# final_array = list(map(int,splitting))
# print(f"Entered array by the user: {final_array}")

# main_set = set(comparison_array)
# user_set = set(final_array)

# def missing_num():
#     another_array = main_set - user_set
#     print(f"Missing Numbers are: {another_array}")
    

# missing_num()
    