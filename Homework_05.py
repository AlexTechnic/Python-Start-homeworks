# Homework_05.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

homework_num = 5
student_name = 'Alex Lavrenchuk'
homework_date = '30.10.2022'  # in format dd.mm.yyyy

# information about homework
print(f'\nHomework #{str(homework_num)} ({homework_date}) by {student_name} \n\n{20 * "*"}\n')

# list of tasks
task_1 = 'Given a number (four digits). Check if it is a "lucky ticket". \n' \
         'Note: a lucky ticket is a number in which, with an even number of digits, \n' \
         'the sum of the digits of its left half is equal to the sum of the digits of its right half. \n' \
         'For example, 1322 is a lucky ticket because 1 + 3 = 2 + 2.'

task_2 = 'A number (six digits) is entered from the keyboard. Check if it is a palindrome. \n' \
         'Note: A palindrome is a number, word, or text that reads the same \n' \
         'from left to right and from right to left. \n' \
         'For example, these numbers are 143341, 5555, 7117, etc.'

task_3 = 'Given a circle with the center at the origin of the coordinates and radius 4. \n' \
         'The user enters the coordinates of the point x and y from the keyboard. \n' \
         'Write a program that will determine whether this point lies inside the circle or not.'

task_list = (task_1, task_2, task_3)

task_counter = 0


def task_brief():  # function to print task brief text
    print('Task ' + str(task_counter + 1) + '. ' + str(task_list[0 + task_counter])
          + '\n\nResult:\n')


def task_divider():  # function of divider between tasks
    input('\n*** Press Enter key to execute next task ***\n')


# TASK 1
task_brief()  # print of task brief

user_ticket = input('Please enter your ticket number: ')

if len(user_ticket) % 2:
    print('Input error')
else:
    user_ticket = list(map(int, user_ticket))
    mid = len(user_ticket) // 2
    res = 'Congrats! Your ticket is lucky!' if sum(user_ticket[:mid]) == sum(user_ticket[mid:]) \
        else 'Sorry, your ticket is not lucky.'
    print(res)

# END OF TASK 1

task_counter += 1  # increment of task counter

task_divider()

# TASK 2
task_brief()  # call brief func

user_text = input('Please enter the text: ')

res = user_text == user_text[::-1]

res = res == 1 and 'Entered text is a palindrome' or 'Entered text is not a palindrome'

print(res)

# END OF TASK 2

task_counter += 1  # increment of task counter

task_divider()

# TASK 3
task_brief()  # call brief func

circle_rad = int(input('Please enter radius of the circle in cm: '))

x, y = int (input('Please enter position of the X point: ')), int (input('Please enter position of the Y point: '))

circle_dia = (x ** 2) + (y ** 2)

if circle_dia == circle_rad:
    print('Position is on the circle.')
elif circle_dia < circle_rad:
    print('Position is in the circle area.')
else:
    print('Position is out the circle area.')

# END OF TASK 3

print('\n*** End of tasks list ***')

# END
