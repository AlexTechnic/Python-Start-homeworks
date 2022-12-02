# Homework_07.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

homework_num = 7
student_name = 'Alex Lavrenchuk'
homework_date = '06.11.2022'  # in format dd.mm.yyyy

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

task_list = (task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10)

task_counter = 0


def task_brief():  # function to print task brief text
    print('Task ' + str(task_counter + 1) + '. ' + str(task_list[0 + task_counter])
          + '\n\nResult:\n')


def task_divider():  # function of divider between tasks
    input('\n*** Press Enter key to execute next task ***\n')


# TASK 1
# finding qty of symbol 'b' in text
task_brief()  # call brief func

# using inbuilt method '.count':
user_text = input('Please input your text including "b" symbols: ')
res = user_text.count('b')
print(f'There are {res} "b" symbols in entered text.')

# END OF TASK 1

task_counter += 1  # increment of task counter

task_divider()

# TASK 2
# checking symbols validity of entered name
task_brief()  # call brief func

# using methods .isalpha and .istitle:
user_name = input('Please input name: ')
if user_name.isalpha() and user_name.istitle():
    print('Ok.')
else:
    print(f'Error: name "{user_name}" has invalid input.')

# END OF TASK 2

task_counter += 1  # increment of task counter

task_divider()

# TASK 3
# finding sum of entered symbol codes
task_brief()  # call brief func

# using inbuilt function 'ord':
user_text = input('Please enter any symbols: ')
res = 0

for item in user_text:
    res += ord(item)

print(f'Sum of entered symbols codes are: {res}.')

# END OF TASK 3

task_counter += 1  # increment of task counter

task_divider()

# TASK 4
# printing 10 rows of Pi number with increasing length
task_brief()  # call brief func

import math

row_count = 0

for i in range(2, 12):
    row_count += 1
    print(f'Row {row_count} output:'
          f' {math.pi:.{i}f}')
print('End of list.')

# END OF TASK 4

task_counter += 1  # increment of task counter

task_divider()

# TASK 5
# finding the longest entered word
task_brief()  # call brief func

# using inbuilt function 'max()' with 'key = ' parameter
# (not supporting multiple result):

user_text = input('Please enter any text: ')

user_text = user_text.split()
res = (max(user_text, key = len))
print(f'The biggest entered word by value is: {res}.')

# to print multiple values must be used some other algorythm

# END OF TASK 5

task_counter += 1  # increment of task counter

task_divider()

# TASK 6
# detecting repeated pattern of entered text
task_brief()  # call brief func


# using cycle for:

user_text = input('Please enter text with repeated word: ')
len_str = len(user_text)

for i in range(1, len(user_text) // 2 + 1):
    text_pattern = user_text[:i]
    if len(text_pattern) * user_text.count(text_pattern) == len_str:
        print(f'Repeated word written by Vovochka is: {text_pattern}.')
        break

# # tip: benchmark of code execution speed can be done by 'timeit' lib, for example:
#
# stp = """
# user_text = input('Please enter text with repeated word: ')
# """
#
# import timeit
#
# s = """
# len_str = len(user_text)
# for i in range(1, len(user_text) // 2 + 1):
#     text_pattern = user_text[:i]
#     if len(text_pattern) * user_text.count(text_pattern) == len_str:
#         print(f'Repeated word by Vovochka is: {text_pattern}.')
#         break
# """
#
# print(timeit.timeit(s, setup=stp, number=100000))

# END OF TASK 6

task_counter += 1  # increment of task counter

task_divider()

# TASK 7
# clearing HTML text from '< >' tags
task_brief()  # call brief func

# # using regex (may not work correctly in some cases!):
#
# import re
#
#
# def striphtml(data):
#     p = re.compile(r'<.*?>')
#     return p.sub('', data)
#
#
# html_text = """<html>
#   <head>
#     <title>Div Align Attribbute</title>
#   </head>
#   <body>
#     <div align="left">
#       Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
#       labore et dolore magna aliqua.
#     </div>
#     <div align="right">
#       Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
#       labore et dolore magna aliqua.
#     </div>
#     <div align="center">
#       Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
#       labore et dolore magna aliqua.
#     </div>
#     <div align="justify">
#       Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
#       labore et dolore magna aliqua.
#     </div>
#   </body>
# </html>"""
#
# res = striphtml(html_text)
#
# print(f'Text below are cleared from < > tags using regex:\n{res}')
#
# # better to use 'Beautiful Soup' lib to work with HTML


# using while cycle:

html_text = """<html>
  <head>
    <title>Div Align Attribbute</title>
  </head>
  <body>
    <div align="left">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
      labore et dolore magna aliqua.
    </div>
    <div align="right">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
      labore et dolore magna aliqua.
    </div>
    <div align="center">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
      labore et dolore magna aliqua.
    </div>
    <div align="justify">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
      labore et dolore magna aliqua.
    </div>
  </body>
</html>"""

while '<' in html_text:
    start = html_text.find('<')
    stop = html_text.find('>')
    res = html_text = html_text.replace(html_text[start: stop +1], '')

print(f'Text below are cleared from "< >" tags using "while" cycle:\n{res}')
# may be improved to delete /n from output

# END OF TASK 7

print('\n*** End of tasks list ***')

# END