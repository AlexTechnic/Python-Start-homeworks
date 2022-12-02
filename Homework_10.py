# Homework_10.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

# homework template v0.1

# IMPORTS

# CONSTS
HOMEWORK_NUM = 10
STUDENT_NAME = 'Alex Lavrenchuk'
HOMEWORK_DATE = '13.11.2022'  # in format dd.mm.yyyy


# FUNCS
# information about homework
def homework_intro():
    res = (f'\nHomework #{str(HOMEWORK_NUM)} ({HOMEWORK_DATE}) by {STUDENT_NAME} \n\n{20 * "*"}')
    return res


# next task
def task_next():
    global task_counter
    task_next = input(f'\n*** Press Enter key to execute task {task_counter} ***\n')
    task_counter += 1
    return task_next


# end of tasks
def tasks_end():
    task_end = ('\n*** End of homework ***\n')
    return task_end


task_counter = 1

print(homework_intro())

task_next()

# TASK 1


# END OF TASK 1

task_next()

# TASK 2
# calculating the biggest palindrome from two three-digit numbers

def three_digs_nums_pal(c):
    return int(str(c)[::-1]) == c


maxpal = 0

for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        prod = a * b
        if three_digs_nums_pal(prod) and prod > maxpal:
            maxpal = prod
            a_num = a
            b_num = b

print(f'The biggest palindrome of two three-digits nums {a_num} and {b_num} is: {maxpal}.')

# END OF TASK 2

print(tasks_end())

# END
