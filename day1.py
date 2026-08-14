# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num - 1)

# print(factorial(4))

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent - 1)

# print(power(2, 0))
# print(power(2, 2))
# print(power(2, 4))

# def capitalizeFirst(arr):
#     result = []
    
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])
    
#     return result + capitalizeFirst(arr[1:])


# print(capitalizeFirst(['car', 'taco', 'banana']))
 
def isPalindrome(strng):
    if len(strng) == 0:
        return True

    if strng[0] != strng[len(strng) - 1]:
        return False

    return isPalindrome(strng[1:-1])


print(isPalindrome('awesome'))