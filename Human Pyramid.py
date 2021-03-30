###Nick Jones
###DSC 430 Assignment 8 Human Pyramid
####I have not given or received any unauthorized assistance on this assignment
###https://youtu.be/2k2zagJFQ6Y

'''function determining weight on back of person in human pyramid'''
def humanPyramid(row,col,weight):
#base case
    if row == 0:
        return 0
#if the person is first or last in any row then he is holding only one person's weight
    elif col == 0:
        return (humanPyramid(row - 1, col, weight) + weight) / 2
    elif row == col:
        return (humanPyramid(row - 1, col -1, weight) + weight) / 2
#if the person is not first or last then
#he has load from two person above them
    else:
        return weight + (humanPyramid(row - 1, col - 1, weight) / 2) + (humanPyramid(row - 1, col, weight) / 2)

r = int(input("row= "))
c = int(input("col= "))
w = int(input("weight= ")
    print(humanPyramid(r,c,w))

#print(humanPyramid(4,2,128))
#print(humanPyramid(3,3,128))
#print(humanPyramid(4,4,128))
#print(humanPyramid(4,1,128))
#print(humanPyramid(4,3,128))
#print(humanPyramid(4,0,128))