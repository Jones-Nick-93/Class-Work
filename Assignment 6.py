#Nick Jones
#DSC 430 Assignment 6 Happy Prime Numbers
#I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/6sopo3Eo2o4



# Utility method to return  
# sum of square of digit of n 
'''Function determing if our number is a happy number'''
def isHappyNumber(n): 
    digit = sum = 0
    while(n > 0):
        digit = n % 10
        sum = sum + (digit * digit)
        n = n // 10
    return sum
num = int(input("Enter a number: "))
result = num
while(result != 1 and result != 4):
    result = isHappyNumber(result)
if(result == 1):
    print(num, " is a happy prime number!")
    resp = input("Do you wish to continue Yes or No: ")
    if (resp == "Yes"):
        num = int(input("Enter a number: "))
        result = num
    else:
        print("Thanks")
else:
    print(num, "is sad non prime number!")
