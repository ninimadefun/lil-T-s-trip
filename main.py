# This is a sample Python script.
import sys
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
number=1

def print_Hello(name,My_number):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}{My_number}')  # Press Ctrl+F8 to toggle the breakpoint.

def ask_user(question):
    print(f'{question} ',end='')
    sys.stdout.flush()
    answer=sys.stdin.readline().strip()
    return answer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number=number+3
    print_Hello('Niboy',number)
    number=int(number/2)
    print_Hello('Nini',number+1)
    m=ask_user('who are you?')
    niboy=ask_user('who is your pet?')
    age=ask_user(f'how old is {niboy}?')
    age=int(age)
    # nini love mama, mama love nini
    print(f'{niboy} love {m}, {m} love {niboy} !')
    print(f'{niboy} is {age} years old.')
    if age > 6:
        if age == 8:
            print(f'{niboy} is awesome!')
        print(f'{niboy} is old')
    else:
        if age <= 3:
            print(f'{niboy} is young')
        else:
            print(f'{niboy} is cute')
    while True:
        niboy_number = ask_user('give me a number between 0 and 10:')
        niboy_number=int(niboy_number)
        if niboy_number >= 0 and niboy_number <= 10:
            break
    print(niboy_number)
    for niboy3 in range(1,5):
        print(niboy3)
    for a in range(1, 10):
        print(f'3 X {a} = {3*a}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
