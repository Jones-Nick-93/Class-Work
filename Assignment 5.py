#Nick Jones
#DSC 430 Assignment 5 Goldbach Loop
####I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/nWeOTnH_f54


###Import math to sqrt
from math import *
'''generating list of primes''' #helper functions to set up the main function looping through the list of evens
def primeList(number):          # and then breaking them into a pair of primes summing to the even numbers
    prime_list = [2]
    for x in range(2, number + 1):
            if is_prime(x):
                prime_list.append(x)
    return prime_list
'''determining if the number is prime'''
def is_prime(number):
    if number % 2:
        for num in range(3, int(sqrt(number)) + 1, 2):
            if number % num == 0:
                return False
        return True
    else:
        return False
''' function for running goldbach conjecture'''
def goldbach(number, prime_list):
    x, y = 0, 0
    result = 0
    if not number % 2:
        for i in range(len(prime_list)):
            x = prime_list[i]
            if result == number: break
            for j in range(len(prime_list)):
                y = prime_list[j]
                result = x + y

                if result == number:
                    return x, y
'''main function listing all goldbach conjectures from 4 to 100'''
def main():
    while True:
        userInput = int(input("Please enter a positive number greater than 1: "))          
        if userInput > 1:
            break
        else:
            print("Not in range")
    allprimes = primeList(userInput)
    list_all = []
    for i in range(4,101,2):
        list_all.append([i,goldbach(i, allprimes)])
    print(list_all)
main()

