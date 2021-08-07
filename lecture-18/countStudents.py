# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        index = 0

        while True:

            updated = []

            for student in students:

                if student == sandwiches[index]:
                    index += 1
                else:
                    updated.append(student)

            if len(students) == len(updated):
                break

            students = updated

        return len(students)