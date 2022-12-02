# Homework_06.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

homework_num = 6
student_name = 'Alex Lavrenchuk'
homework_date = '05.11.2022'  # in format dd.mm.yyyy

# information about homework
print(f'\nHomework #{str(homework_num)} ({homework_date}) by {student_name} \n\n{20 * "*"}\n')

# list of tasks
task_1 = ''

task_2 = ''

task_3 = ''

task_4 = ''

task_5 = ''

task_6 = ''

task_7 = ''

task_8 = ''

task_9 = ''

task_10 = ''

task_11 = ''

task_list = (task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11)

task_counter = 0


def task_brief():  # function to print task brief text
    print('Task ' + str(task_counter + 1) + '. ' + str(task_list[0 + task_counter])
          + '\n\nResult:\n')


def task_divider():  # function of divider between tasks
    input('\n*** Press Enter key to execute next task ***\n')


# TASK 1

task_brief()  # call brief func

# for i in range (1,101):  # for (not optimised!)
#     if not i % 7:
#         print(i)

# for i in range (7, 101, 7):  # for cycle with step
#     print(i)

count = 7  # while cycle
while count <= 100:
    print(count)
    count += 7

# END OF TASK 1

task_counter += 1  # increment of task counter

task_divider()

# TASK 2

task_brief()  # call brief func

x = int(input('Please enter number: '))  # factorial without math lib
p = 1
for i in range(2, x + 1):
    p *= i
print(f'Factorial of {x} is {p}.')

# END OF TASK 2

task_counter += 1  # increment of task counter

task_divider()

# TASK 3
task_brief()  # call brief func

for a in range(1, 11):  # calculation table
    for b in range(1, 11):
        print(f'{a} * {b} = {a * b}')
    print()

# END OF TASK 3

task_counter += 1  # increment of task counter

task_divider()

# TASK 4
task_brief()  # call brief func

#  drawing rectangle task
a, b = int(input('Please enter height of rectangle: ')), \
    int(input('Please enter width of rectangle: '))

res = (f"{'*' * b}\n") + (f"*{' ' * (b - 2)}*\n" * (a - 2)) + (f"{'*' * b}")

print(f'\n{res}')

# END OF TASK 4

task_counter += 1  # increment of task counter

task_divider()

# TASK 5
task_brief()  # call brief func

# x = [0, 5, 2, 4, 7, 1, 3, 19]  # var 1
# count = 0
# for item in x:
#     if item % 2:
#         count += 1
#
# print(f'List [0, 5, 2, 4, 7, 1, 3, 19] have {count} odd numbers.\n')

x = [0, 5, 2, 4, 7, 1, 3, 19]  # var 2
count = 0
for item in x:
    count += item % 2

print(f'List [0, 5, 2, 4, 7, 1, 3, 19] have {count} odd numbers.\n')

# END OF TASK 5

task_counter += 1  # increment of task counter

task_divider()

# TASK 6
task_brief()  # call brief func

import random

x = [random.randint(1, 10) for _ in range(4)]

res = x[:] + [2 * item for item in x]

print(f'{x} -> {res}')

# END OF TASK 6

task_counter += 1  # increment of task counter

task_divider()

# TASK 7
task_brief()  # call brief func

import random

x = [random.randint(10000, 20000) for _ in range(12)]

res = sum(x) / len(x)

print(f'List of 12 month salaries of worker: \n\n{x}\n\n'
      f'Average salary is: {int(res)}.')

# END OF TASK 7

task_counter += 1  # increment of task counter

task_divider()

# TASK 8
task_brief()  # call brief func

matrix = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

summa = 0
for row in matrix:
    summa += sum(row)

for row in matrix:
    print('\t'.join(map(str, row)))

print(f'\nSum of matrix is: {summa}.')

# END OF TASK 8

task_counter += 1  # increment of task counter

task_divider()

# TASK 9
task_brief()  # call brief func

x = [7, 2, 9, 4]

# y = x[::-1]  # to create new list in memory
# print(y)

# x.reverse()  # to change original list
# print(x)

for i in reversed(x):  # to return reversed list and not duplicate in memory
    print(i)

# END OF TASK 9

task_counter += 1  # increment of task counter

task_divider()

# TASK 10
task_brief()  # call brief func

lower_value = int(1)
upper_value = int(100)

print("The prime numbers in the range 1-100 are: ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)

# END OF TASK 10

task_counter += 1  # increment of task counter

task_divider()

# TASK 11
task_brief()  # call brief func

a = int(input('Please input size of sand clock:  '))

res = []

b = 0

for i in range(a, 0, -2):
    res.append(f"{' ' * b}{'*' * i}\n")
    b += 1

res += res[-2::-1]

result = '\n'.join(res)

print(f'\n{result}')


# END OF TASK 11

print('\n*** End of tasks list ***')

# END
