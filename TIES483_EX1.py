# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:30:24 2019

@author: Anette Karhu

TIES483 Exercise 1 and 2
"""
import numpy as np

# =============================================================================
#  Ex. 1: Way 1 to make a grade calculator
#  A grade is calculated by dividing scores 
#  gotten with maximum scores of the course.
#  The grade is then given by this percentage 
#  of this course grading system.
# =============================================================================
def grade_calculator(score, max_score):
    percentage = score / max_score
    if percentage <= 0.5 :
        grade = 0
        return grade
    elif percentage >= 0.5 and percentage < 0.6:
        grade = 1
        return grade
    elif percentage >= 0.6 and percentage < 0.7:
        grade = 2
        return grade
    elif percentage >= 0.6 and percentage < 0.8:
        grade = 3
        return grade
    elif percentage >= 0.7 and percentage < 0.9:
        grade = 4
        return grade
    elif percentage >= 0.9:
        grade = 5
        return grade
   
# Function calls and printing
grade = grade_calculator(27, 30)
#print('You got grade', grade)

# =============================================================================
# Ex 1 : Way 2 to make a grade calculator. The grades lie between [0,5]
#  In this function the grade is calculated linearly and
#  a floor function is used to return the floor-rounding of the input
# =============================================================================
def grade_calculator2(score, max_score):
    percentage = score/max_score
    # y = kx + b - a linear function for the grading     
    y = 10 * percentage -4
#    print(y)
    grade = np.floor(y)
    if grade > 5:
        grade = 5
        return grade
    elif grade < 0:
        grade = 0
        return grade
    else:
        return grade

# Function calls and printing 
grade = grade_calculator2(27, 30)
#print('You got grade', grade)


# =============================================================================
#  Ex 2, a script that returns the minimum number of points for a wanted grade.
#  grades lie between [1,5]. Script calls the
#  grade_calculator2 -function.
# =============================================================================

max_score = 30
grade_wanted = 5

# timeit minpoint(4,100) tällä saadaan kellotettua kaun menee suorittamiseen aikaa.
# vois myös tehdä for points in range(1, max_score+1)
# tai konstruktorilla!  se on nopeempi
# [points for poinst in range(1, max_score+1) if grade ]
def grade_minimum_score(max_score, grade_wanted):    
    score_gotten = 0
    grade = grade_calculator2(score_gotten, max_score)
    while grade < grade_wanted:
        score_gotten += 1
        grade = grade_calculator2(score_gotten, max_score)
        if grade == grade_wanted:
            return score_gotten
            break
        if grade_wanted > 5:            
            break
        if grade_wanted < 0:            
            break

# Runs the script and print minimum value of scores needed for a certain grade 
min_score = grade_minimum_score(max_score ,grade_wanted)        
print('The minimum score for the grade', grade_wanted, 'is', min_score)