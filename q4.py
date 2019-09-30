# ### Problem 4
# Write a program that allows users to compare words by their length. Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer) than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```
userinput1= input("enter first string")
userinput2= input("enter second string")
def chk_strings(str1,str2):
    if len(str1)> len(str2):

        return True
    else:

        return False


chk_strings(userinput1, userinput2)