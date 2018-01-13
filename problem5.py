class ExitLoop(Exception):
    pass

# define module for checking uppercase using ASCII Values
def check_uppercase(letter):
    if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
        return True
    else:
        return False

def check_lowercase(letter):
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        return True
    else:
        return False

def check_number(letter):
    if ord(letter) >= ord('0') and ord(letter) <= ord('9'):
        return True
    else:
        return False

if __name__=='__main__':
    try:
        while True:
            password_one = str(input("Enter a password: "))
            pass_list = list(password_one)
            uppercase = False
            lowercase = False
            number = False
            for letter in pass_list:
                if check_uppercase(letter):
                    uppercase = True 
                if check_lowercase(letter):
                    lowercase = True
                if check_number(letter):
                    number = True
            if uppercase and lowercase and number:
                while True:
                    password_two = str(input("Enter password again: "))
                    if password_two == password_one:
                        print("Success!")
                        raise ExitLoop
                    else:
                        print("Password does not match!")
            else:
                print("Condition not met, try again. ")
    except ExitLoop:
        print("Successfully made password")