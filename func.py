from cli import get_arguments
import string
import random

def generate_password(length, list_s_alpha, list_c_alpha, list_num, list_special):
    list_pass = list_c_alpha + list_s_alpha + list_num
    rand_pass = random.choices(list_pass, k=length)
    for i in list_special:
        rand_idx = random.randint(0, length - 1)
        rand_pass[rand_idx] = i
    return "".join(rand_pass)

def check_password_strength(password, list_special, list_c_alpha, list_num):
    conditions = {
        'length': False,
        'special': False,
        'capital': False,
        'number': False
    }
    strength_grade = 0
    if len(password) >= 10:
        conditions['length'] = True
        strength_grade += 2
    if any(c in password for c in list_special):
        conditions['special'] = True
        strength_grade += 2
    if any(c in password for c in list_c_alpha):
        conditions['capital'] = True
        strength_grade += 2
    if any(c in password for c in list_num):
        conditions['number'] = True
        strength_grade += 2
    return strength_grade, conditions

def print_strength_report(conditions, strength_grade):
    print("Security conditions:")
    print(f"Length >= 10 ===> {'pass' if conditions['length'] else 'fail'}")
    print(f"Special characters ===> {'pass' if conditions['special'] else 'fail'}")
    print(f"Capital alphabet characters ===> {'pass' if conditions['capital'] else 'fail'}")
    print(f"Numbers ===> {'pass' if conditions['number'] else 'fail'}")
    print(f"Password strength is {strength_grade}/8")

def pass_generator(arguments):
    specials = ["@", "#", "$", "%", "!", "&", "+"]
    list_s_alpha = list(string.ascii_lowercase)
    list_c_alpha = list(string.ascii_uppercase)
    list_num = list(string.digits)
    if arguments.special_chr is not None:
        list_special = list(arguments.special_chr)
    else:
        list_special = ['@']
    try:
        if(arguments.length):
            length = int(arguments.length)
        else:
            length = 10
    except Exception:
        print("Please enter number")
        return
    
    if arguments.generate:
        flag = True
        if length > 32 or length < 10:
            flag = False
        if flag:
            real_pass = generate_password(length, list_s_alpha, list_c_alpha, list_num, list_special)
            print(f"Your password is: {real_pass}")
            if arguments.strength:
                strength_grade, conditions = check_password_strength(real_pass, list_special, list_c_alpha, list_num)
                print_strength_report(conditions, strength_grade)
        else:
            print("Can't generate password more than 32 or less than 10 charachters")
    elif arguments.strength and arguments.password:
        user_password = arguments.password
        strength_grade, conditions = check_password_strength(user_password, specials, list_c_alpha, list_num)
        print_strength_report(conditions, strength_grade)
    else:
        print("Error while grading security of your password")