# Homework_02.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8
import math

homework_num = 2
student_name = 'Alex Lavrenchuk'
homework_date = '22.10.2022'  # in format dd.mm.yyyy

# information about homework
print(f'\nHomework #{str(homework_num)} ({homework_date}) by {student_name} \n\n{20 * "*"}\n')

# list of tasks
task_1 = 'Construct an integer from the string "123"'

task_2 = 'Construct a float from the integer 123'

task_3 = 'Construct an integer from the float 12.345'

task_4 = 'Write a Python-script that detects the last 4 digits of a credit card'

task_5 = 'Write a Python-script that calculates the sum of the digits of a three-digit number'

task_6 = 'Write a program that calculates and displays the area of a triangle if its sides are known'

task_7 = '* Write a Python-script that calculates the sum of the digits of a number'

task_8 = '*Determine the number of digits in a number'

task_9 = '*Print the digits in reverse order'

task_list = (task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9)

task_counter = 0


def task_brief():  # function to print task brief text
    print('Task ' + str(task_counter + 1) + '. ' + str(task_list[0 + task_counter])
          + '\n\nResult:\n')


def task_divider():  # function of divider between tasks
    input('\n*** Press Enter key to execute next task ***\n')


# start of task #1
task_brief()  # call brief func

x = int('123')  # solution
print(x)

task_counter += 1  # increment of task counter

task_divider()

# start of task #2
task_brief()  # call brief func

x = float(124)  # solution
print(x)

task_counter += 1  # increment of task counter

task_divider()

# start of task #3
task_brief()  # call brief func

x = int(12.345)  # solution
print(x)

task_counter += 1  # increment of task counter

task_divider()

# start of task #4
task_brief()  # call brief func

card_num = int(input('Enter 16 digits of a card number without spaces: '))
card_last_dig = (card_num % 10000)
print(f'Last four digits of the card is: {card_last_dig}')

task_counter += 1  # increment of task counter

task_divider()

# start of task #5
task_brief()  # call brief func

x_num = int(input('Enter a three-digit number: '))
num_digits_sum = (x_num % 10 + x_num // 10 % 10 + x_num // 100)
print(f'Sum of the number digits is : {num_digits_sum}')

task_counter += 1  # increment of task counter

task_divider()

# start of task #6
task_brief()  # call brief func

triangle_side_1 = float(input('Enter a length of the triangle first side in cm: '))
triangle_side_2 = float(input('Enter a length of the triangle second side in cm: '))

# function to calculate third side of the triangle
triangle_side_3 = float(math.sqrt((triangle_side_1 ** 2) + (triangle_side_2 ** 2)))
print(f'Length of the triangle third side is: {int(triangle_side_3)} cm')

# formula to find a semi-perimetr of the triangle
triangle_semi_p = float((triangle_side_1 + triangle_side_2 + triangle_side_3) / 2)

# formula to find an area of the triangle
triangle_area = float(math.sqrt(triangle_semi_p * ((triangle_semi_p - triangle_side_1)
                                                   * (triangle_semi_p - triangle_side_2)
                                                   * (triangle_semi_p - triangle_side_3))))
print(f'The triangle area is: {triangle_area} cm^2')

# end of tasks
print('\n*** End of tasks list ***')

# END
