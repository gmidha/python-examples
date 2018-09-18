#!/usr/bin/env python3

def get_gpa():
    print('Welcome to GPA Calculator')
    print('Please enter all your letter grades, one per line')
    print('Submit a blank line to mark the end')
    points = { 'A+':4.0, 'A':3.9, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67, 'C+':2.50,
               'C': 2.36, 'C-':2.30, 'D+':1.33,'D':1.26, 'D-':1.0 }
    num_courses = 0
    total_points = 0
    done = False
    while not done:
        grade = input()
        if grade == '':
            done = True
        elif grade not in points:
            print(f"{grade} not in the list")
        else:
            num_courses += 1
            total_points += points[grade]
    if num_courses > 0:
         print(f"Your GPA is { total_points / num_courses }")

if __name__ == '__main__':
    get_gpa()
