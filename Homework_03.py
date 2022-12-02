# Homework_03.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

homework_num = 3
student_name = 'Alex Lavrenchuk'
homework_date = '23.10.2022'  # in format dd.mm.yyyy

# information about homework
print(f'\nHomework #{str(homework_num)} ({homework_date}) by {student_name} \n\n{20 * "*"}\n')

# list of tasks
task_1 = 'Write a Python program to print the number entered by user only if the number entered is negative.'

task_2 = 'Write a Python program to check if the value a is less than 20 or not'

task_3 = 'Write a Python program to check if a given number is Zero or Not.'

task_4 = 'Write a Python program to check if a given number is Even or Odd.'

task_5 = 'Write a Python program to find the largest number among three numbers entered by user.'

task_list = (task_1, task_2, task_3, task_4, task_5)

task_counter: int = 0


def task_brief():  # function to print task brief text
    print('Task ' + str(task_counter + 1) + '. ' + str(task_list[0 + task_counter])
          + '\n\nResult:\n')


def task_divider():  # function of divider between tasks
    input('\n*** Press Enter key to execute next task ***\n')


# Task 1. Write a Python program to print the number entered by user only if the number entered is negative.
task_brief()  # call brief func

x = int(input('Please enter the number: '))
calc = (x < 0) and print(f'The number {x} is negative')

task_counter += 1  # increment of task counter

task_divider()

# Task 2. Write a Python program to check if the value X is less than 20 or not.
task_brief()  # call brief func

x = int(input('Please enter the number: '))
res = x < 20 and f'The number {x} is less than 20' or f'The number {x} is not less than 20'
print(res)

task_counter += 1  # increment of task counter

task_divider()

# Task 3. Write a Python program to check if a given number is Zero or Not.
task_brief()  # call brief func

# x = int(input('Please enter the number: '))  # == is not optimized solution
# res = x == 0 and f'{x} is zero' or f'{x} is not zero'
# print(res)

x = int(input('Please enter the number:'))
res = x and f'{x} is not zero' or f'{x} is zero'
print(res)

task_counter += 1  # increment of task counter

task_divider()

# Task 4. Write a Python program to check if a given number is Even or Odd.
task_brief()  # call brief func

# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

# x = int(input("Please enter a number: "))  # not optimized solution
# res = (x % 2 == 0 and f'{x} is even' or f'{x} is odd')
# print(res)

x = int(input("Please enter a number: "))
res = x % 2 and f'{x} is odd' or f'{x} is even'
print(res)

task_counter += 1  # increment of task counter

task_divider()

# Task 5. Write a Python program to find the largest number among three numbers entered by user.
task_brief()  # call task brief func

# num_1 = int(input("Please enter first number: "))  # solution using only logic operations
# num_2 = int(input("Please enter second number: "))
# num_3 = int(input("Please enter third number: "))
# res = num_1 > num_2 and num_1 > num_3 and f'{num_1} is bigger than {num_2} and {num_3} ' \
#     or num_2 > num_1 and num_2 > num_3 and f'{num_2} number is bigger than {num_1} and {num_3} ' \
#     or num_3 > num_1 and num_3 > num_2 and f'{num_3} is bigger than {num_1} and {num_2} ' \
#     or num_1 == num_2 and num_2 == num_3 and num_3 == num_1 and 'The numbers are equal'
# print(res)

num_1, num_2, num_3 = int(input("Please enter first number: ")), \
                      int(input("Please enter second number: ")), \
                      int(input("Please enter third number: "))
res = (max(num_1, num_2, num_3))
print(f'The largest number is {res} ')

# nums = (input("Please enter the numbers separated by spaces: "))  # solution with one string input
# nums = nums.split()
# nums = list(map(int, nums))
# print(f'The largest number is {max(nums)}')

# end of tasks
print('\n*** End of tasks list ***')

# END
