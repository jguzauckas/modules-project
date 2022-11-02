# Import our three modules.
import math
import random as rdm
from datetime import datetime as dtm

# Make a blank list called grades.  Use the random module to
# add 1,000 random scores (1 to 100) to the list for us to
# work with.
grades = []
for x in range(1000):
    grades.append(rdm.randint(1, 100))

# Use the math module to find a quick average of all of the
# grades and print the result out nicely.  (Because this was
# random, we expect it to be close to 50)
average = math.fsum(grades) / len(grades)
print(f"The average grade was {average:.2f}")

# Print out the highest grade and the number of people who
# achieved it.  Repeat with the lowest grade
max = 0
min = 100
for grade in grades:
    if grade > max:
        max = grade
    if grade < min:
        min = grade
max_count = 0
min_count = 0
for grade in grades:
    if grade == max:
        max_count += 1
    if grade == min:
        min_count += 1
print(f"The maximum grade was {max}, and was achieved by {max_count} students.")
print(f"The minimum grade was {min}, and was achieved by {min_count} students.")

# Make a blank list called dates.  Use the datetime and random
# modules to add 1000 random dates to the list.  The random
# dates should all have the year 2022, with a randomized month
# and day (from 1 to 28)
dates = []
for x in range(1000):
    date = dtm(2022, rdm.randint(1, 12), rdm.randint(1, 28))
    dates.append(date)

# Count the number of times your birthday from this year occurs
# in the list and report the result.
count = 0
birth_day = dtm(2022, 8, 5)
for date in dates:
    if date == birth_day:
        count += 1
print(f"{count} people have the same birthday as me.")

# Determine the percentage of the dates that occurred before
# right now (in time) and report the result.
count = 0
now = dtm.now()
for date in dates:
    if date < now:
        count += 1
percentage = count / len(dates)
print(f"{percentage:.2%} of the dates occurred before {now}")

# Create a Student class that contains the following properties:
#   - gender - string, male, female, etc. (you pick
#       number of options)
#   - group - string: A, B, C, D, or E
#   - completed test prep course - bool
#   - math score - int 0 - 100
#   - reading score - int 0 - 100
#   - writing score - int 0 - 100
# You should have getter and setter methods for all of the above
# properties.  Make sure to guarantee the values are acceptable
# (i.e. scores between 0 and 100, group between A and E)
# You should also have __init__ and __str__ methods
class Student:
    def __init__(self, gender:str, group:str, test_prep:bool, math:int, read:int, write:int) -> None:
        self._gender = gender
        self._group = group
        self._completed_test_prep_course = test_prep
        self._math_score = math
        self._reading_score = read
        self._writing_score = write

    def __str__(self) -> str:
        return f"This student got {self._math_score} in math, {self._reading_score} in reading, and {self._writing_score} in writing."

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, gender:str) -> None:
        if gender == "Female" or gender == "Male" or gender == "Other":
            self._gender = gender
        else:
            print("Gender not compatible with list")

    @property
    def group(self) -> str:
        return self._group
    
    @group.setter
    def group(self, grp:str) -> None:
        if grp == "A" or grp == "B" or grp == "C" or grp == "D" or grp == "E":
            self._group = grp
        else:
            print("Group not compatible with list")

    @property
    def completed_test_prep_course(self) -> bool:
        return self._completed_test_prep_course

    @completed_test_prep_course.setter
    def completed_test_prep_course(self, c:bool) -> None:
        self._completed_test_prep_course = c
    
    @property
    def math_score(self) -> int:
        return self._math_score

    @math_score.setter
    def math_score(self, score:int) -> None:
        if 1 <= score <= 100:
            self._math_score = score
        else:
            print("Score not compatible")
    
    @property
    def reading_score(self) -> int:
        return self._reading_score

    @reading_score.setter
    def reading_score(self, score:int) -> None:
        if 1 <= score <= 100:
            self._reading_score = score
        else:
            print("Score not compatible")

    @property
    def writing_score(self) -> int:
        return self._writing_score

    @writing_score.setter
    def writing_score(self, score:int) -> None:
        if 1 <= score <= 100:
            self._writing_score = score
        else:
            print("Score not compatible")


# Create a blank list called students.  Generate 100 random students
# by doing the following each time:
#   - Use a random number to assign a gender (i.e. 1 is female,
#       2 is male, etc.)
#   - Use a random number to assign a group (i.e. 1 is A, 2 is B,
#       etc.)
#   - Use a random number to assign a test prep (i.e. 1 is True,
#       2 is False)
#   - Assign random scores for math, reading, and writing
students = []
for x in range(100):
    g = rdm.randint(1, 3)
    if g == 1:
        gender = "Female"
    elif g == 2:
        gender = "Male"
    else:
        gender = "Other"
    g = rdm.randint(1, 5)
    if g == 1:
        group = "A"
    elif g == 2:
        group = "B"
    elif g == 3:
        group = "C"
    elif g == 4:
        group = "D"
    else:
        group = "E"
    test_prep = bool(rdm.randint(0, 1))
    maths = rdm.randint(1, 100)
    read = rdm.randint(1, 100)
    write = rdm.randint(1, 100)
    student = Student(gender, group, test_prep, maths, read, write)
    students.append(student)

# Please note for the following sections, we expect no appreciable
# difference between groups because the data is completely random.
# Determine which group of students performed the best in math
# by calculating average scores based on the groups students were in
# and comparing them.  To do this, you will want to:
#   - Create a function that averages all the scores given a particular
#       group as an input.
#   - Create a dictionary where you store the average grades for each
#       of the groups.
#   - Print out the dictionary.
def average_group(group:str) -> float:
    count = 0
    sum = 0
    for stu in students:
        if stu.group == group:
            count += 1
            sum += stu.math_score
    return sum / count

group_average_scores = {"A":0, "B":0, "C":0, "D":0, "E":0}

for key in group_average_scores.keys():
    group_average_scores[key] = average_group(key)

print(group_average_scores)

# Do the same as the above for the gender of students on reading.
def average_gender(gender:str) -> float:
    count = 0
    sum = 0
    for stu in students:
        if stu.gender == gender:
            count += 1
            sum += stu.reading_score
    return sum / count

gender_average_scores = {"Female":0, "Male":0, "Other":0}

for key in gender_average_scores.keys():
    gender_average_scores[key] = average_gender(key)

print(gender_average_scores)

# Finally do the same as the above for students that have completed
# a test preparation course vs. students that have not on writing.
def average_test_prep(test_prep:bool) -> float:
    count = 0
    sum = 0
    for stu in students:
        if stu.completed_test_prep_course == test_prep:
            count += 1
            sum += stu.writing_score
    return sum / count

test_prep_average_scores = {True:0, False:0}

for key in test_prep_average_scores.keys():
    test_prep_average_scores[key] = average_test_prep(key)

print(test_prep_average_scores)