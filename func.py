from cli import get_arguments
import string
import random
import os
from cryptography.fernet import Fernet

def generate_password_key():
    key = Fernet.generate_key()
    with open("./The_Key.key", "wb") as f:
        f.write(key)

def load_key():
    if(not os.path.isfile("./The_key.key")):
        generate_password_key()
    with open("./The_key.key", "rb") as f:
        return f.read()

key = load_key()
fernet = Fernet(key)

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
    
    if arguments.view:
        with open("./Passwords.txt", "r") as f:
            for idx, item in enumerate(f, 1):
                encrypted_real_pass, description  = item.split(';')
                password = fernet.decrypt(encrypted_real_pass).decode()
                print(f"{idx}. password: {password} | description: {description}".strip())
        return
    
    if arguments.remove:
        with open("./Passwords.txt", "r") as f:
            lines = f.readlines()
        try:
            n = int(arguments.remove)
            if 1 <= n <= len(lines):
                del lines[n - 1]
                with open("./Passwords.txt", "w") as f:
                    f.writelines(lines)
                print("Password removed successfully.")
            else:
                print("Invalid number.")
        except Exception:
            print("Invalid input.")
        return
            
    if arguments.generate:
        flag = True
        if length > 32 or length < 10:
            flag = False
        if flag:
            real_pass = generate_password(length, list_s_alpha, list_c_alpha, list_num, list_special)
            print(f"Your password is: {real_pass}")
            
            if arguments.describe:
                description = arguments.describe
                
            with open("./Passwords.txt", "a") as f:
                encrypted_real_pass = fernet.encrypt(real_pass.encode()).decode()
                f.write(f"{encrypted_real_pass};{description}\n")
                
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
    