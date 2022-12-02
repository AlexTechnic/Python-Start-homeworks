# Homework_04.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

homework_num = 4
student_name = 'Alex Lavrenchuk'
homework_date = '29.10.2022'  # in format dd.mm.yyyy

# information about homework
print(f'\nHomework #{str(homework_num)} ({homework_date}) by {student_name} \n\n{20 * "*"}\n')

# list of tasks
task_1 = 'There is a nine-story building with 4 entrances. The entrance number starts with one. \n' \
         'There are 4 apartments on one floor. Write a program that receives the apartment number from the user \n' \
         'and outputs the entrance, floor and number for the given apartment. \n' \
         'If there is no such apartment in this building, it is necessary to inform the user about it. \n' \
         '( dont use "if" )'

task_2 = 'Write a program that will return the number of days for a given year. \n' \
         'A year is a leap year if it is a multiple of 4 but not a multiple of 100, \n' \
         'and also if it is a multiple of 400'

task_3 = 'A triangle exists only when the sum of any two sides is greater than the third. \n' \
         'Given: A, B, C - sides of a triangle. \n' \
         'Write a program that indicates whether such a triangle exists.'

task_list = (task_1, task_2, task_3)

task_counter = 0


def task_brief():  # function to print task brief text
    print('Task ' + str(task_counter + 1) + '. ' + str(task_list[0 + task_counter])
          + '\n\nResult:\n')


def task_divider():  # function of divider between tasks
    input('\n*** Press Enter key to execute next task ***\n')


# TASK 1
task_brief()  # print of task brief

#  parameters of the house
ENTRANCES = 4

FLOORS = 9

FLOOR_FLATS = 4

TOTAL_FLATS = (ENTRANCES * FLOORS * FLOOR_FLATS)

ENTRANCE_FLATS = (FLOORS * FLOOR_FLATS)

#  calculations
user_flat = int(input('Please enter flat number: '))

entrance_num = (((user_flat-1) // ENTRANCE_FLATS) + 1)

floor_num = int(((user_flat - 1) - ((entrance_num - 1) * ENTRANCE_FLATS)) / FLOOR_FLATS) + 1

flat_num = int(user_flat % FLOOR_FLATS) or 4

#  entrance and flat pos. to verbal form
entrance_literal = entrance_num == 1 and 'first' \
    or entrance_num == 2 and 'second' \
    or entrance_num == 3 and 'third' \
    or entrance_num == 4 and 'fourth'

flat_verbal = flat_num == 1 and 'first' \
    or flat_num == 2 and 'second' \
    or flat_num == 3 and 'third' \
    or flat_num == 4 and 'fourth'

#  result
res = 1 <= user_flat <= TOTAL_FLATS and f'\nEntered flat location is: \n' \
      f' - {entrance_literal} entrance, floor #{floor_num}, {flat_verbal} flat.' \
      or 'Error #404: flat is not exist.'
print(res)

# END OF TASK 1

task_counter += 1  # increment of task counter

task_divider()

# TASK 2
task_brief()  # call brief func

user_year = int(input('Please enter a year: '))

if not user_year % 4 and (user_year % 100 or not user_year % 400):
    print(f'Year {user_year} have 366 days.')
else:
    print(f'Year {user_year} have 365 days.')

# END OF TASK 2

task_counter += 1  # increment of task counter

task_divider()

# TASK 3
task_brief()  # call brief func

# triangle parameters
triangle_side_a, triangle_side_b, triangle_side_c = \
    int(input('Please enter length of A side of triangle in cm: ')), \
    int(input('Please enter length of B side of triangle in cm: ')), \
    int(input('Please enter length of C side of triangle in cm: '))

# calculations
if triangle_side_a + triangle_side_b > triangle_side_c \
        and triangle_side_a + triangle_side_c > triangle_side_b \
        and triangle_side_c + triangle_side_b > triangle_side_a:
    print('Triangle exist.')
else:
    print('Triangle dont exist.')

# END OF TASK 3

print('\n*** End of tasks list ***')

# END
