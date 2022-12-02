# Homework_01.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

homework_num = 1
student_name = 'Alex Lavrenchuk'
homework_date = '22.10.2022'  # in format dd.mm.yyyy

# information about homework
print(f'\nHomework #{str(homework_num)} ({homework_date}) by {student_name} \n\n{20 * "*"}\n')

# list of tasks
task_1 = 'Write a Python-script that displays the message “Hello world”.'

task_2 = 'Rewrite the first script to display three any messages.'

task_3 = 'Write a Python-script to reads values for the length and width of a rectangle and returns the ' \
         'area of the rectangle. '

task_4 = 'Write a program that requests the user to enter two numbers and prints the sum, product, ' \
         'difference and quotient of the two numbers. '

task_5 = 'Write a program that reads in the radius of a circle and prints the circle’s diameter, ' \
         'circumference and area. Use the constant value 3.14159 for π. Do these calculations in output statements. '

task_list = (task_1, task_2, task_3, task_4, task_5)

task_counter = 0


def task_brief():  # function to print task brief text
    print('Task ' + str(task_counter + 1) + '. ' + str(task_list[0 + task_counter])
          + '\n\nResult:\n')


def task_divider():  # function of divider between tasks
    input('\n*** Press Enter key to execute next task ***\n')


# start of task #1
task_brief()  # call brief func

print('Hello Prog.Academy!')  # solution

task_counter += 1  # increment of task counter

task_divider()

# start of task #2
task_brief()  # call brief func

# print('Minerals: 1000')  # solution a)
# print('Gas: 0')
# print('Supply: 16')

print('Minerals: 1000', 'Gas: 0', 'Supply: 16', sep='\n')  # solution b)

task_counter += 1  # increment of task counter

task_divider()

# start of task #3
task_brief()  # call brief func

length = int(input('Enter length of the rectangle in cm: '))  # solution
width = int(input('Enter width of the rectangle in cm: '))
# print('Area of the rectangle is:', length * width, 'cm^2')  # outdated style supported before python 3.7
print(f'Area of the rectangle is: {length * width} cm^2')  # new style supported from python 3.7 using f-string

task_counter += 1  # increment of task counter

task_divider()

# start of task #4
task_brief()  # call brief func

a, b = int(input('Enter first number A:')), int(input('Enter second number B:'))  # solution
print(f'A * B = {a * b}',
      f'A - B = {a - b}',
      f'A + B = {a + b}',
      f'A / B = {a / b}', sep='\n')

task_counter += 1  # increment of task counter

task_divider()

# start of task #5
task_brief()  # call brief func

pi = 3.14159  # solution

circle_rad = int()

# def circle_dia():
#     (2 * circle_rad)
#
#
# def circle_cir():
#     (pi * circle_dia)
#
#
# def circle_area():
#     (pi * (circle_rad ** 2))
#
#
# circle_rad = int(input('Enter radius of the circle in cm:'))
# print(f'Circle DIA is: {circle_dia}',
#       f'Circle CIR is: {circle_cir}',
#       f'Circle area is: {circle_area} ', sep='\n')

circle_rad = int(input('Enter radius of the circle in cm:'))

circle_dia = (2 * circle_rad)

circle_cir = (pi * circle_dia)

circle_area = (pi * (circle_rad ** 2))

print(f'Circle DIA is: {circle_dia}',
      f'Circle CIR is: {circle_cir}',
      f'Circle area is: {circle_area} ', sep='\n')

task_counter += 1  # increment of task counter

# end of tasks
print('\n*** End of tasks list ***')

# END
