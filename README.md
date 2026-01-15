# Job Title

Print a combination of job titles based on user input and conditional logic.

Write your program in `job_title.py`. See the starter code and usage examples
to help get started.

## Input

This program will prompt for input of an employee's

* First Name
* Last Name
* Gender Code (M/F)
* Age in Years
* Whether or not they are an Engineer (Yes/No)
* Whether or not they are a Manager (Yes/No)

## Output Format

It will then print the employee's Job Title in the form:

```python
"{gender_title} {first_name} {last_name}, {seniority} {role}"
```

## Conditional Logic

Following these rules:

* `gender_title` will start with
  + "Mrs." if Female
  + "Mr." if Male
* `seniority` will be
  + "Jr." if they are less than 25 years old
  + "Sr." if they are greater than or equal to 35 years old
  + blank if not "Jr." or "Sr." with no extra space
* `role` will be
  + "Engineering Manager" if they are both an *Engineer* and a *Manager*
  + "Manager" if they are a *Manager* and *not an Engineer*
  + "Engineer" if they are an *Engineer* and *not a Manager*
  + "Employee" if they are *neither an Engineer nor a Manager*

## Starter Code Test Usage

Test the starter code and understand the input and conditional logic.

```
$ py job_title.py
Do you have a job (Y/N)? Y
Yes, I have a job.

$ py job_title.py no
Do you have a job (Y/N)? no
No, I don't have a job.

$ py job_title.py
Do you have a job (Y/N)? why
invalid input: why
```

## Finished Progam Example Usage & Output

```
$ py job_title.py
First Name: John
Last Name: Handy
Gender (M/F): M
Age: 18
Is Engineer? (Y/N): n
Is Manager? (Y/N): n
Mr. John Handy, Jr. Employee

$ py job_title.py
First Name: Suzy
Last Name: Karmon
Gender (M/F): F
Age: 26
Is Engineer? (Y/N): y
Is Manager? (Y/N): n
Ms. Suzy Karmon, Engineer

$ py job_title.py
First Name: Philip
Last Name: Farkuat
Gender (M/F): m
Age: 36
Is Engineer? (Y/N): Yes
Is Manager? (Y/N): N
Mr. Philip Farkuat, Sr. Engineer

$ py job_title.py
First Name: Janice
Last Name: Dearborne
Gender (M/F): F
Age: 41
Is Engineer? (Y/N): Y
Is Manager? (Y/N): Y
Ms. Janice Dearborne, Sr. Engineering Manager
```
