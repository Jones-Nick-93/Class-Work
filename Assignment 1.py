###Nick Jones April 12th 2020
###DSC 430: Assignment 1
###I have not given or received any unauthorized assistance on this assignment
### https://youtu.be/NdzX8swoYiw

'''these are the helper functions for CreateGrade for the bullet points'''
###I used an additional if statement for the response, so there 
### is an output for each user input.
###Yes continues the function and No tells the user 
###their grade is 0 for failing assignment prereqs
'Function asking if it is compressed .Py file'
def dotPy():
    resp = input('Is the file an uncompressed .py file Yes or No: ')
    if (resp == "Yes"):
       return True
    if (resp == "No"):
        print ("grade is 0")
'Function verifying name and date on assignment'
def nameDate():
    resp = input('Is there a labelled name and date Yes or No: ')
    if (resp == "Yes"):
        return True
    if (resp == "No"):
        print ("grade is 0")
'Function verifying there is the honor statement'
def honorState():
    resp = input('Does assignment contain an honor statement Yes or No: ')
    if (resp == "Yes"):
        return True  
    if (resp == "No"):
        print ("grade is 0")
'Function veryfing a unlisted youtube link'
def ytDiscuss():
    resp = input('Does assignment have 3min YouTube video Yes or No: ')
    if (resp == "Yes"):
        return True
    if (resp == "No"):
        print ("grade is 0")
'''User defined helper functions to compute the grade'''
###Here are the helper functions used to generate 
# the ComputeGrade() function
'Grading correctness of code'
def correctness():
    resp = input('From 1 to 10 grade the code for correctness: ')
    return int(resp)
'grading elegance of code'    
def elegance():
    resp = input('From 1 to 10 grade the code for elegance: ')
    return int(resp)
'grading the hygiene of the code'
def hygiene():
    resp = input('From 1 to 10 grade the code for hygiene: ')
    return int(resp)
'grading the quality of the discussion'    
def ytQuality():
    resp = input('From 1 to 10 grade the YouTube discussion: ')
    return int(resp)
'calculating the late penalty if turned in after 11:59 on Sunday'
def latepenalty():
    resp = input('How many hours late was the assignment: ')
    return ((int(resp)/100)*40)
'''Total score function summing each of the 4 grades along with subtracting the late penalty'''
###Summation of all the /10 grading categories minus the late penalty###
'Grade on the assignment: sum of all helpers above'
def totalScore():
    resp = input(correctness() + elegance() + hygiene() + ytQuality() - latepenalty() )
    return int(resp)
     ###After generating all helper functions the below function makes sure we have done all mandatory steps to get hw graded###
'''function that creates a grade off of parameters listed'''
###Here we have the create grade fcn that allows us to determine grade###
def computeGrade():
    if not ( dotPy() ):
       return 0
    if not ( nameDate() ):
        return 0
    if not ( honorState() ):
        return 0
    if not ( ytDiscuss() ):
        return 0
    else:
        return totalScore()
###Run function get assignment grade
computeGrade()


