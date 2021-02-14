import tkinter as tk
# import Tkinter
top = tk.Tk()
from flask import Flask, render_template

from tkinter import  *
# root= top.Tk()
# top.title("Password Generator")
#
# canvas1 = tk.Canvas(top, width = 400, height = 300)
# canvas1.pack()
#
# label1=tk.Label(top, text="Username")
# canvas1.create_window(200, 40,window=label1)
# entry1 = tk.Entry (top)
# canvas1.create_window(200, 60, window=entry1)
# label2=tk.Label(top, text="password")
# canvas1.create_window(200, 90,window=label2)
# entry2 = tk.Entry (top)
# canvas1.create_window(200, 110, window=entry2)
# button1 = tk.Button(text='Login', command='main()')
# canvas1.create_window(200, 150, window=button1)
# # register
#
# button2 = tk.Button(text='Register', command='main()')
# canvas1.create_window(200, 200, window=button2)
#
# top.mainloop()
# entry1 = top.Entry ()

app = Flask(__name__)

# @app.route('/')
# def home():
#     print("welcome to password locker")
#     return render_template('index.html')


# import pyperclip
from user_credentials import User, Credential


def create_user(fname, lname, password):
    '''
    Function to create a new user account
    '''
    new_user = User(fname, lname, password)
    return new_user


def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)


def verify_user(first_name, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = Credential.check_user(first_name, password)
    return checking_user


def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass


def create_credential(user_name, site_name, account_name, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(user_name, site_name, account_name, password)
    return new_credential


def save_credential(credential):
    '''
    Function to save a newly created credential
    '''
    Credential.save_credentials(credential)


def display_credentials(user_name):
    '''
    Function to display credentials saved by a user
    '''
    return Credential.display_credentials(user_name)


def copy_credential(site_name):
    '''
    Function to copy a credentials details to the clipboard
    '''
    return Credential.copy_credential(site_name)


def main():
    print(' ')
    print('PASSWORD LOCKER.')
    while True:
        # print(' ')
        print("~" * 120)
        print('Enter an action to continue, sign-up to create account, login, or exit to quit')
        short_code = input('Enter a choice: ').lower().strip()
        if short_code == 'exit':
            break

        elif short_code == 'sign-up':
            print("~" * 120)
            # print(' ')
            print('To create a new account:')
            first_name = input('Enter your first name - ').strip()
            last_name = input('Enter your last name - ').strip()
            password = input('Enter your password - ').strip()
            save_user(create_user(first_name, last_name, password))
            print(" ")
            print(f'Account Created for: {first_name} {last_name} with password: {password}')
        elif short_code == 'login':
            print("~" * 120)
            # print(' ')
            print('To login, enter your account details:')
            user_name = input('Enter your first name - ').strip()
            password = str(input('Enter your password - '))
            user_exists = verify_user(user_name, password)
            if user_exists == user_name:
                print(" ")
                print(f'Welcome {user_name}. Please choose an action to continue.')
                print(' ')
                while True:
                    print("-" * 60)
                    print(
                        'Input the following keywords to navigate: \n create-Create a Credential \n display-Display Credentials \n copy-Copy Password \n exit-Exit')
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-" * 60)
                    if short_code == 'exit':
                        print(" ")
                        print(f'Goodbye {user_name}')
                        break
                    elif short_code == 'create':
                        print(' ')
                        print('Enter your credential details:')
                        site_name = input('Enter the site\'s name- ').strip()
                        account_name = input('Enter your account\'s name - ').strip()
                        while True:
                            print(' ')
                            print("-" * 60)
                            print(
                                'Please choose an option for entering a password: \n existing-enter existing password \n generate-generate a password \n exit-exit')
                            psw_choice = input('Enter an option: ').lower().strip()
                            print("-" * 60)
                            if psw_choice == 'existing':
                                print(" ")
                                password = input('Enter your password: ').strip()
                                break
                            elif psw_choice == 'generate':
                                password = generate_password()
                                break
                            elif psw_choice == 'exit':
                                break
                            else:
                                print('Invalid option, Try again.')
                        save_credential(create_credential(user_name, site_name, account_name, password))
                        print(' ')
                        print(
                            f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
                        print(' ')
                    elif short_code == 'display':
                        print(' ')
                        if display_credentials(user_name):
                            print('My saved credentials')
                            # print(' ')
                            for credential in display_credentials(user_name):
                                print(
                                    f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                            print(' ')
                        else:
                            # print(' ')
                            print("No saved credentials found")
                            print(' ')
                    elif short_code == 'copy':
                        print(' ')
                        chosen_site = input('Enter the site name for the credential password to copy: ')
                        copy_credential(chosen_site)
                        print('')
                    else:
                        print('Invalid option, Try again.')

            else:
                print(' ')
                print('Wrong details entered, try again with correct details or Create an Account.')

        else:
            print("-" * 60)
            print(' ')
            print('Incorrect password entered, Retry with correct password.')


if __name__ == '__main__':
    main()

