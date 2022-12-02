# Homework_09.py
# Prog Academy python developer course (22.10.2022)
# part I - python start - imperative programing
# teacher - Oleh Tymchuk

# written on pycharm v.2022.1.3
# tested on python v.3.10.8

homework_num = 9
student_name = 'Alex Lavrenchuk'
homework_date = '13.11.2022'  # in format dd.mm.yyyy

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


# !PRINT() INSIDE FUNC IS A BAD STYLE, IN CODING MUST BE USED "PURE FUNC"!
def task_brief():  # function to print task brief text
    task_brief = ('Task ' + str(task_counter + 1) + '. ' + str(task_list[0 + task_counter])
                  + '\n\nResult:\n')
    return task_brief


def task_divider():  # function of divider between tasks
    task_divider = ('\n*** Press Enter key to execute next task ***\n')
    return task_divider


# TASK 1
# sum and concatenation func

print(task_brief())


# # variant 1 func
# def custom_sum(a, b, c):
#     res = str(a + b) + c
#     return res

# # variant 2 func
# def custom_sum(a, b, c):
#     return f'{a + b}{c}'

# variant 3 func
def custom_sum(a: int, b: int, c: str):
    if isinstance(a, int) and isinstance(b, int):
        return f'{a + b}{c}'
    return -1


first_num = int(input('Please input first num: '))
second_num = int(input('Please input second num: '))
user_text = str(input('Please input some text: '))

print(f'Sum of int nums {first_num} + {second_num} and concatenation with string "{user_text}" '
      f'= "{custom_sum(first_num, second_num, user_text)}"')

# END OF TASK 1

task_counter += 1  # increment of task counter

task_divider()

# TASK 2
#  drawing user rectangle with func

print(task_brief())


def drawing_rectangle(a, b, /):
    res = (f"{'*' * rect_width}\n") + (f"*{' ' * (rect_width - 2)}*\n" * (rect_height - 2)) + (f"{'*' * rect_width}")
    return res


rect_height = int(input('Please enter height of rectangle: '))
rect_width = int(input('Please enter width of rectangle: '))

print(drawing_rectangle(rect_height, rect_width))

# END OF TASK 2

task_counter += 1  # increment of task counter

task_divider()

# TASK 3
# linear search of the number index in the list of int numbers

print(task_brief())


# function
def linear_search(user_nums, search_num):
    for num_index, item in enumerate(user_nums):
        if item == search_num:
            return num_index
    return -1


# user input
user_list = input('Please enter list of int numbers separeted by space: ').split()

user_nums = list(map(int, user_list))

search_num = int(input('Please enter number in list to find it index in list: '))

# result output
if linear_search(user_nums, search_num) != -1:
    res = f'Index of number "{search_num}" in list is: [{linear_search(user_nums, search_num)}].'
else:
    res = -1

print(res)

# END OF TASK 3

task_counter += 1  # increment of task counter

task_divider()

# TASK 4
# func that returns qty of words in text

print(task_brief())

import string


# function
def words_qty(user_text: str):
    for item in string.punctuation:
        user_text = user_text.replace(item, ' ')
    return len(user_text.split())


# result
user_text = input('Please enter some words: ')
print(f'Qty of words in text is: {words_qty(user_text)}.')

# END OF TASK 4

task_counter += 1  # increment of task counter

task_divider()

# TASK 5
# conversion money amount to words
# ("123.34$" -> "one hundred twenty three dollars thirty four cents")

# source code to translate nums to words taken from:
# https://www.codesansar.com/python-programming-examples/number-words-conversion-no-library-used.htm

# Number to Words

# Main Logic
ones = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

twos = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')

tens = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred')

suffixes = ('', 'thousand', 'million', 'billion')


def process(number, index):
    if number == '0':
        return 'zero'

    length = len(number)

    if length > 3:
        return False

    number = number.zfill(3)
    words = ''

    hdigit = int(number[0])
    tdigit = int(number[1])
    odigit = int(number[2])

    words += '' if number[0] == '0' else ones[hdigit]
    words += ' hundred ' if not words == '' else ''

    if tdigit > 1:
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]

    elif tdigit == 1:
        words += twos[(int(tdigit + odigit) % 10) - 1]

    elif tdigit == 0:
        words += ones[odigit]

    if words.endswith('zero'):
        words = words[:-len('zero')]
    else:
        words += ' '

    if not len(words) == 0:
        words += suffixes[index]

    return words


def get_words(number):
    length = len(str(number))

    if length > 12:
        return 'This program supports upto 12 digit numbers.'

    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []

    for i in range(length - 1, -1, -3):
        words.append(process(str(number)[0 if i - 2 < 0 else i - 2: i + 1], copy - count))
        count -= 1

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp

    return final_words


# End Main Logic

# ADDED CURRENCY FUNCS

# Reading number from user // ADDED USER INPUT NUMBER SIZE CHECK

user_input = first_input = str(input('\nPlease enter amount of money in numeral format (max 12 digits): '))

while int(len(user_input)) > 12:
    user_input = first_input = str(input('\nOver 12 digits! Please re-enter amount of money in numeral format: '))

# splitting dollars and cents parts
if ',' in user_input:
    user_input = user_input.split(',')
elif '.' in user_input:
    user_input = user_input.split('.')
else:
    user_input = [int(user_input), 0]

dollars = int(user_input[0])
cents = int(user_input[1])

# working with cents rounding
if cents < 10:
    cents *= 10
elif cents > 100:
    cents = int(str(cents)[0:2])

# final result
res = (f'\nEntered {first_input}$ was transformed to: {get_words(dollars).strip()} dollar(s) '
       f'and {get_words(cents).strip()} cent(s).')

print(res)

# END OF TASK 5

task_counter += 1  # increment of task counter

task_divider()


# TASK 6

# Roman numeral -> decimal numeral convertion


def roman_to_int(roman_input):
    # Roman dict
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(roman_input):
        if i + 1 < len(roman_input) and roman_input[i:i + 2] in roman:
            num += roman[roman_input[i:i + 2]]
            i += 2
        else:
            # print(i)
            num += roman[roman_input[i]]
            i += 1
    return num


# result
roman_input = str(input('Please enter Roman numbers (capitalised): '))

res = roman_to_int(roman_input)

print(f'Roman number "{roman_input}" = {res}.')

# END OF TASK 6

print('\n*** End of tasks list ***')

# END
