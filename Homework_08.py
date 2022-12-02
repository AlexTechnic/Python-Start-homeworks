# Homework_07.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

homework_num = 8
student_name = 'Alex Lavrenchuk'
homework_date = '12.11.2022'  # in format dd.mm.yyyy

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
# printing day of the week using dict

week_day = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday'
}

day = int(input('Please input day number: '))
res = (week_day.get(day, 'Invalid day number'))
print(f'Day {day} is: {res}.')

# END OF TASK 1

task_counter += 1  # increment of task counter

task_divider()

# TASK 2
# describe cat with dict

cat = {
    'class': 'mammals',
    'warm blooded': True,
    'name': 'Snezjok',
    'color': 'black',
    'weight': 4.5,
    'speed': 15,
    'body': {
        'paws': 4,
        'eyes': 2,
        'tail': True
        },
    }

if {cat.get('warm blooded')}:
    print(f'Yes, {cat.get("name")} is a warm blooded animal.')

# else:
#     print(f'{cat.get("name")} is a reptile.')  # value never reached :)

# END OF TASK 2

task_counter += 1  # increment of task counter

task_divider()

# TASK 3
# calculating used letters in text

# user_text = input('Please input text: ')
#
# res = {}
#
# for item in set(user_text):
#     res[item] = user_text.count(item)
#
# print(f'Used letters: {res}')

user_text = input('Please input text: ')

res = {item: user_text.count(item) for item in set(user_text) if item.isalpha()}

res = '\n'.join(map(lambda item: f'{item[0]}: {item[1]}', res.items()))

print(f'Used letters:\n{res}')

# END OF TASK 3

task_counter += 1  # increment of task counter

task_divider()

# TASK 4
# finding same letters in two texts

text_1 = input('Please input first text: ')
text_2 = input('Please input second text: ')

res = {item for item in set(text_1) & set(text_2) if item.isalpha() }
print(f'The both texts have same letters: {res}')

# END OF TASK 4

task_counter += 1  # increment of task counter

task_divider()

# TASK 5
# two lists multiple of 3 and 5

list_1 = list(range(3, 100, 3))
list_2 = list(range(5, 100, 5))

print(f'\nFirst list 0-100 multiple of 3:\n{list_1}'
      f'\n\nSecond list 0-100 multiple of 5:\n{list_2}')

# finding common numbers shared to both two lists
res = list(set(list_1) & set(list_2))
print(f'\nCommon numbers shared to both two lists:\n{res}')

# END OF TASK 5

print('\n*** End of tasks list ***')

# END