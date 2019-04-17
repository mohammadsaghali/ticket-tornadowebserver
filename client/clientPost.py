
import requests
import os
import time
import platform
import sys

PARAMS = CMD = USERNAME = PASSWORD = API = ""
HOST = "localhost"
PORT = "1104"


def __postcr__():
    return "http://"+HOST+":"+PORT+"/"+CMD+"?"


def print_bal(r):
    print("YOUR BALANCE IS : " + str(r['Balance']))


def print_depwith(r):
    print("YOUR OLD BALANCE IS : " + str(r['Old Balance'])
          +"\n"+"YOUR NEW BALANCE IS : "+str(r['New Balance']))

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


while True:
    clear()
    print("""WELCOME TO Ticketing to users
    Please Choose What You Want To Do :
    1. signin
    2. signup
    3. exit
    """)
    status = sys.stdin.readline()

    # login
    if status[:-1] == '1':

        clear()
        print("""What Kind Of Login Do You Prefer :
            1. API
            2. USERNAME | PASSWORD
            """)
        login_type = sys.stdin.readline()


        # signup
    elif status[:-1] == '2':

        clear()
        while True:
            print("To Create New Account Enter The Authentication")
            print("USERNAME : ")
            USERNAME = sys.stdin.readline()[:-1]
            print("PASSWORD : ")
            PASSWORD = sys.stdin.readline()[:-1]
            print("FIRSTNAME : ")
            FIRSTNAME = sys.stdin.readline()[:-1]
            print("LASTNAME : ")
            LASTNAME = sys.stdin.readline()[:-1]
            while True:
                print("ROLE : "+ "\n1.admin\n2.user")
                temp = sys.stdin.readline()[:-1]
                if temp == '1':
                    ROLE = 'admin'
                    break
                elif temp == '2':
                    ROLE = 'user'
                    break
                else:
                    print("choose correct number")
            CMD = "signup"
            clear()
            PARAMS = {'username': USERNAME, 'password': PASSWORD, 'role': ROLE, 'firstname': FIRSTNAME, 'lastname': LASTNAME}
            r = requests.post(__postcr__(), PARAMS)
            if str(r.json()['status']) == "OK":
                print("Your Acount Is Created\n" + "Your Username :" + USERNAME + "\nYour API : " + str(r.json()['apitoken']))

                print('Press Any Key To Continue ...')
                x = sys.stdin.readline()[:-1]
                break
            else:

                print(str(r.json()['status']) + "\n" + "Try Again")
                print('Press Any Key To Continue ...')
                x = sys.stdin.readline()[:-1]
                clear()

    # exit
    elif status[:-1] == '3':
        sys.exit()


    # wrong answer
    else:
        print("Wrong Choose Try Again")

