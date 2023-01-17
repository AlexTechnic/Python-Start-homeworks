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
    homework_intro = (f'\nHomework #{str(HOMEWORK_NUM)} ({HOMEWORK_DATE}) by {STUDENT_NAME} \n\n{20 * "*"}')
    return homework_intro


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

from math import log

def search_sequence_pattern_1(seq):
    """ sequence '+x' """
    temp = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i - 1] == temp and i == len(seq) - 1:
            return seq_plus(seq)
        elif seq[i] - seq[i - 1] == temp:
            continue
        else:
            return search_sequence_pattern_2(seq)


def search_sequence_pattern_2(seq):
    """ sequence '*x' """
    if seq[0]:
        temp = seq[1] / seq[0]
        for i in range(2, len(seq)):
            if seq[i] / seq[i - 1] == temp and i == len(seq) - 1:
                return seq_multiply(seq)
            elif seq[i] / seq[i - 1] == temp:
                continue
            else:
                return search_sequence_pattern_3(seq)
    else:
        return None


def search_sequence_pattern_3(seq):
    """ sequence '**x' """
    temp = log(seq[1]) / log(2)
    if len(seq) > 4 and 1 not in seq[1:]:
        for i in range(2, len(seq)):
            if log(seq[i - 1]) / log(i) == temp and i == len(seq) - 1:
                return seq_exponentiate(seq)
            elif log(seq[i - 1]) / log(i) == temp:
                continue
            else:
                return None
    else:
        return None


def seq_plus(seq):
    return seq[-1] + seq[1] - seq[0]


def seq_multiply(seq):
    return seq[-1] * int(seq[1] / seq[0])


def seq_exponentiate(seq):
    return (len(seq) + 1) ** int(log(seq[1]) / log(2))


seq = list(map(int, ((input('Please enter list of numbers with some progression rule (at least three or more nums\n'
                            'separated by coma, for example 1, 3, 5, or 2, 4, 16 etc): ')).split(","))))
print(f'Next number in list must be: {search_sequence_pattern_1(seq)}.')


# END OF TASK 1

task_next()

# TASK 2
# calculating the biggest palindrome from two three-digit numbers


# variant 1:
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

# # variant 2
# def palindrome_func():
#     """
#     Function calculates the biggest existing palindrome of two three-digits numbers.
#     @return: int(palindrome number)
#     """
#     first_num = 1000
#     second_num = 1000
#     max_pal = 0
#     a = 0
#     b = 0
#     for i in range(first_num, second_num, -1):
#         for j in range(first_num, second_num, -1):
#             temp = i * j
#             if str(temp) == str(temp)[::-1] and max_pal < temp:
#                 max_pal = i * j
#                 a = i
#                 b = j
#     return(max_pal)


# print(f'The biggest palindrome of two three-digits nums is:{palindrome_func()}.')



# END OF TASK 2

print(tasks_end())

# END
