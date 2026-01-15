"""
<Name>, <Grade> <Course>
Assignment: Job Title
This assignment will print a combination of job titles based on
user input and conditional logic.
"""

# do not change this code
import sys

def die(*args, **kwargs):
    '''print an error message and exit the program'''
    print(*args, file=sys.stderr, **kwargs)
    sys.exit(1)

# main section (your code goes below here)

# example to help get started (replace this)
have_job = input('Do you have a job (Y/N)? ').strip().lower()
if have_job in ('y', 'yes'):
    print("Yes, I have a job.")
elif have_job in ('n', 'no'):
    print("No, I don't have a job.")
else:
    # print error message and exit
    die(f"invalid input: {have_job}")