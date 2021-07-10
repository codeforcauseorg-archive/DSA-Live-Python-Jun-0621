# sal < 5000 then bonus is 500
# else bonus is 1000
salary = int(input("Enter Salary = "))

if salary < 5000:
    salary += 500
else:
    salary += 1000

print(salary)


