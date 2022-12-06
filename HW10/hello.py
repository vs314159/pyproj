from faker import Faker

fake = Faker()


def is_valid_pwd(password):
    set_pw = set(password)
    conditions = ((len(password) >= 8,
                  'Not valid: must contain at least 8 characters.'),

                  (sum(c.isalpha() for c in password) >= 4,
                  'Not valid: must contain at least four alphabetic characters.'),

                  (any(not c.isalpha() for c in set_pw),
                  'Not valid: must contain at least one non-alphabetic character.'),

                  (all(not (c*3 in password) for c in set_pw),
                  'Not valid: contains more than two repeated characters.'))
    for con, mess in conditions:
        if not con:
            print(mess)
            return False
    return True


def is_valid_name(name):
    spaces = name.count(' ')
    return sum(c.isalpha() for c in name) == len(name) - spaces and spaces >= 1


def hello():
    name = input("Hello! My name is Password Checker. And what is your name?\n\
Please, enter your first name and last name: ")
    if not (name and is_valid_name(name)):
        name = fake.name()
        print(f"Did you enter your first name AND last name?\n\
I'm afraid you didn't, then I'll call you {name}")
    print(f'Hello, {name}! How are you?')
    check_pw = input('Do you want to check your password for strength? Type "yes" if you do: ')
    if check_pw.lower() == 'yes':
        password = input('Enter your password: ')
        pw_valid = is_valid_pwd(password)
        fed_up = 12
        tries = 1
        while not pw_valid:
            password = input('Try again or type "stop": ')
            if password.lower() == "stop":
                print('Okay, bye! Have a nice day!')
                break
            if tries == fed_up:
                print("I'm sorry, but I have other things to do. Bye!")
                break
            pw_valid = is_valid_pwd(password)
            tries += 1
        if pw_valid:
            print(f"Password {password} seems to be a good password. My work is done, bye!")
    else:
        print('Okay, bye! Have a nice day!')
