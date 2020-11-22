import secrets
import string

def passwd_gen(password_length):
    characters = (string.ascii_letters + string.digits + string.punctuation)
    secure_password = ''.join(secrets.choice(characters) for i in range(password_length))
    return secure_password

def main():
    user_password_length = int(input("Input number of digits for password: "))
    if(user_password_length < 8):
        print("Password Should Be Atleast 8 Characters Long")
        exit(1) 
    print("Password Generated: ", passwd_gen(user_password_length))

main()
