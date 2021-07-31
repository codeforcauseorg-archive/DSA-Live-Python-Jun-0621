import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    results = []

    for score in grades:

        if score < 38:
            results.append(score)
        elif (score % 5) >= 3:
            results.append(score + (5 - (score % 5)))
        else:
            results.append(score)

    return results


fptr = open(os.environ['OUTPUT_PATH'], 'w')

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

fptr.write('\n'.join(map(str, result)))
fptr.write('\n')

fptr.close()
