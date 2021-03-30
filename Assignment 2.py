###Nick Jones April 12th 2020
###DSC 430: Assignment 2
###I have not given or received any unauthorized assistance on this assignment
### 

###Helper function to do act as greatest common demoninator.
'''Helper function that's user defined to determine gcd for coprime'''
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
'''Coprime function that returns if numbers 
input are coprime or not'''
def coprime(a, b):
    if ( gcd(a, b) == 1): 
        print("Co-Prime") 
    else: 
        print("Not Co-Prime")
'''While loop that while true will repeatedly give us if
 our two input #s are coprime or not'''
def coprimeTestLoop():
    while True:
        f = eval(input("Please enter a number: "))
        d = eval(input("Please enter a number: "))
       
        coprimeAB = coprime(f,d)
        resp = input("Do you wish to continue Yes or No: ")
        if (resp == "Yes"):
            return coprimeTestLoop()
        else:
            break
    print("Thanks for your time!")
coprimeTestLoop()
###As you can see we have added a user input way 
# to exit the loop upon user input of 'No'###