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

## Example Usage & Output

```
```