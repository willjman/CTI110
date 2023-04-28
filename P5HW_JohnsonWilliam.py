#math quiz
#4/27/2023
#CTI-110 P5HW-Math Quiz
#William Johnson
import random

def print_menu():
    print('Welcome to Math Quiz')
    print()
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()

print_menu()
user_num = int(input('Please choose one of the menu options:'))


def add():
    num_1 = random.randint(0, 1000)
    num_2 = random.randint(0, 450)
    tries = 1
    print(f' {num_1} + {num_2}')
    aw = int(input('Enter answer.'))
    while aw != num_1 + num_2:
        if aw > num_1 + num_2:
            print('Sorry, guess is too hight')
        else:
            print('Sorry, guess is to low')
        aw = int(input('Enter answer.'))
        tries += 1
      
    print('Congratulations!!! Your answer is correct')
    print('Number of guesses:',tries)
    print()
    return add

def sub():
    num_1 = random.randint(0, 1000)
    num_2 = random.randint(0, 450)
    tries = 1
    print(f' {num_1} - {num_2}')
    aw = int(input('Enter answer.'))
    while aw != num_1 - num_2:
      if aw > num_1 - num_2:
          print('Sorry, guess is too hight')
      else:
          print('Sorry, guess is to low')
      aw = int(input('Enter answer.'))
      tries += 1
      
    print('Congratulations!!! Your answer is correct')
    print('Number of guesses:',tries)
    print()
    return sub


while user_num == 1:
    add()
    print_menu()
    user_num = int(input('Please choose one of the menu options:'))

while user_num == 2:
    sub()
    print_menu()
    user_num = int(input('Please choose one of the menu options:'))

if user_num == 3:
    print('Thank you for playing...')
    print('Bye!!')

while user_num > 3:
    print('Try agian, use number 1 - 3')
    print_menu()
    user_num = int(input('Please choose one of the menu options:'))
    while user_num == 1:
        add()
        print_menu()
        user_num = int(input('Please choose one of the menu options:'))

    while user_num == 2:
        sub()
        print_menu()
        user_num = int(input('Please choose one of the menu options:'))

    if user_num == 3:
        print('Thank you for playing...')
        print('Bye!!')
