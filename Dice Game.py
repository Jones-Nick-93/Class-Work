# Nick Jones
# DSC 430 Dice and Cups A9
# I have not given or received unauthorized assistance on this assignment
# https://youtu.be/dcEo7SUPS4g
import random
# class to represent SixSidedDie
class SixSidedDie():
# init method
    def __init__(self):
        self.faces = 6
        self.number = 0
# a method to roll the dice it generated the random number between
# 1 and number of faces
    def roll(self):
        self.number = random.randint(1, self.faces)
  
# A funtion to return the dice face number
    def getFaceValue(self):
        return self.number
  
# a funtion to print object in SixSidedDie(number) format
    def __repr__(self):
        return "SixSidedDie(%a)" % (self.number)
'''extensions of six sided die'''
# we inherit two classes TenSidedDie and TwentySidedDie from SixSidedDie
# In these classes all methods will remain same but the number of faces will change
class TenSidedDie(SixSidedDie):
    def __init__(self):
        self.faces = 10
        self.number = 0
class TwentySidedDie(SixSidedDie):
    def __init__(self):
        self.faces = 20
        self.number = 0
  
# before rolling a dice its face number is set to 0

# create a cup class
class Cup():
# this class holds several dices of each type
# for init method parameters are:
# x = number of SixSidedDie objects
# y = number of TenSidedDieobjects
# z = number of TwentySidedDieobjects
    def __init__(self, x, y, z):
# create a list for each type type of dices
        self.sixSided = [SixSidedDie() for i in range(0,x)]
        self.tenSided = [TenSidedDie() for i in range(0,y)]
        self.twentySided =[TwentySidedDie() for i in range(0,z)]
# This method is used to roll all the dices in cup class object
    def roll(self):
# create a empty list to store the dice face numbers
        self.sixSidedNumbers = []
# roll each dice of six faces
        for i in self.sixSided:
            i.roll()
            self.sixSidedNumbers.append(i.getFaceValue())
  
        self.tenSidedNumbers = []
# roll each dice of ten faces
        for i in self.tenSided:
            i.roll()
            self.tenSidedNumbers.append(i.getFaceValue())
  
        self.twentySidedNumbers = []
# roll each dice of 20 faces
        for i in self.twentySided:
            i.roll()
        self.twentySidedNumbers.append(i.getFaceValue())
# this method is used to get sum of all face numbers on each dice of cup object
    def getSum(self):
# return sum of all list of face numbers in eacg type of dice list
        return sum(self.sixSidedNumbers)+sum(self.tenSidedNumbers)+sum(self.twentySidedNumbers)
# a funtion to print object in Cup(x,y,z) format
    def __repr__(self):
        return "Cup(% s,% s,% s)" % (len(self.sixSided),len(self.tenSided),len(self.twentySided))
  

d= SixSidedDie()
d.roll()
print(d)

d= TenSidedDie()
d.roll()
print(d)

cup = Cup(1,1,1)
print(cup)
cup.roll()
print(cup.getSum())