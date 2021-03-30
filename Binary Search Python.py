#Nick Jones
#DSC 430 Assignment 7 Time Complexity/Binary Search
#I have not given or received any unauthorized assistance on this assignment
#YouTube Link

import random
'''function to do a binary search to see if 2 #s from a given list sum to n'''
def binary_search(array, to_search, left, right):
    # terminating condition
    if right < left:
        return -1
    # compute mid
    mid = (left+right)//2
    # element found
    if array[mid] == to_search:
        return mid
    # current element is greater than element to search
    elif array[mid] > to_search:
        # move left
        return binary_search(array, to_search, left, mid-1)
    # current element is less than element to search
    else:
        # move right
        return binary_search(array, to_search, mid + 1, right)
# ask user for i
i = int(input("Enter i: "))
# ask user for n
n = int(input("Enter n: "))
# generate a random list of i items
numbers = []

for j in range(i):
    numbers.append(random.randint(0, 100))

# for every element in numbers
for number in numbers:
    # if there is a element in list which is n-number
    if binary_search(numbers, n-number, 0, len(numbers)) != -1:
        print("Found:", number, n-number)
        exit(0)
print("Not found")