"""
Assignment: Function Keyword Arguements Assignment
Program: main.py
Author: Colby Boell
Last date modified: 02/26/2022

The purpose of this program is to use arbitrary argument lists and keyword arguments to return a
string that returns student first name and last name, the current gpa, and the course they are in.
Should only return the specified keywords.
"""


# function to figure out average score(gpa)
def average_scores(*args, **kwargs):
    # Use *args for average calculation
    # variables
    total = 0
    count = 0
    # for loop to add up all the numbers to figure out total and count of them
    for i in args:
        total = total + i
        count = count + 1
    # variable to calculate gpa
    current_gpa = total/count

    f_name = ''  # variables
    l_name = ''
    the_c = ''
    # searches kwargs for key and values
    for key, value in kwargs.items():
        # if statement to assign variables if we find matching key values
        if key == "first_name":
            f_name = value
        if key == "last_name":
            l_name = value
        if key == "course":
            the_c = value
    # return the statement
    return f'Result: name= {f_name} {l_name} gpa= {current_gpa: 5.2f} course= {the_c}'


# main for calling the function and printing out the results
if __name__ == '__main__':
    # this one has all the necessary variables for final result
    print(average_scores(4, 3, 2, 4, first_name='Colby', last_name='Boell', course='Python'))
    # this one has extra keywords that we shouldn't see print out in final result
    print(average_scores(4, 3, 4, 4, 4, first_name='Lisa', middle_name='Marie', last_name='Kellihan', course='Economics'))
    # this one has course missing so shouldn't print out the course since we are missing the keyword in this one
    print(average_scores(4, 4, 3, 3, first_name='Margot', middle_name='Taco', last_name='Nala', major='Biology', school='DMACC'))
    # this one also has extras we shouldn't see print out
    print(average_scores(2, 4, 3, first_name='Anthon', middle_name='James', course='Biology', school='DMACC'))

"""
Test Results:
Result: name= Colby Boell gpa=  3.25 course= Python
Result: name= Lisa Kellihan gpa=  3.80 course= Economics
Result: name= Margot Nala gpa=  3.50 course= 
Result: name= Anthon  gpa=  3.00 course= Biology

"""
