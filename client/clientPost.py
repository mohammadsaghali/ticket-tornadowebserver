
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

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def show_func():
    print("USERNAME : "+USERNAME+"\n"+"API : " + API)
    print("""What Do You Prefer To Do :
    1. send ticket
    2. get ticeket
    """)


#start project
while True:
    clear()
    print("""WELCOME TO Ticketing to users
    Please Choose What You Want To Do :
    1. sign in
    2. sign up
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

        #login with API
        if login_type[:-1] == '1':
            clear()

            while True:
                print("API : ")
                API = sys.stdin.readline()[:-1]
                CMD = "apicheck"
                PARAMS = {'api':API}
                r = requests.post(__postcr__(), params=PARAMS)
                if str(r.json()['status']) == 'TRUE':
                    clear()
                    print("API IS CORRECT\nLogging You in ...")
                    USERNAME = str(r.json()['username'])
                    time.sleep(2)
                    break
                else:
                    clear()
                    print("API IS INCORRECT\nTRY AGAIN ...")
                    time.sleep(2)

            # functions
            while True:
                clear()
                show_func()
                func_type = sys.stdin.readline()

                # sendticket
                if func_type[:-1] == '1':
                    clear()
                    print("subject : ")
                    subject = sys.stdin.readline()[:-1]
                    print("body : ")
                    body = sys.stdin.readline()[:-1]
                    CMD = "sendTicket"
                    PARAMS = {'apiToken': API, 'subject': subject, 'body': body}
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print("message ID : " + str(r.json()['id']))
                        print(str(r.json()['message']))

                    print('Press Any Key To Continue ...')
                    x = sys.stdin.readline()[:-1]

                # get ticket
                if func_type[:-1] == '2':
                    clear()
                    CMD = "getTicket"
                    PARAMS = {"apiToken": API}
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print(str(r.json()['tickets']))
                        index = int(r.json()['index'])
                        for i in range(0, index):
                            block = 'block ' + str(i)
                            print("message id : " + str(r.json()[block]['id']))
                            print("status : " + str(r.json()[block]['type']))
                            print("subject : " + str(r.json()[block]['subject']))
                            print("message : " + str(r.json()[block]['body']))
                            print("response : " + str(r.json()[block]['response']) + "\n")

                    # if dont have message
                    else:
                        print(str(r.json()['tickets']))


        #login with user & pass
        elif login_type[:-1] == '2':
            clear()
            while True:
                print("USERNAME : ")
                USERNAME = sys.stdin.readline()[:-1]
                print("PASSWORD : ")
                PASSWORD = sys.stdin.readline()[:-1]
                CMD = "authcheck"
                PARAMS = {'username': USERNAME, 'password': PASSWORD}
                r = requests.post(__postcr__(), PARAMS)
                if str(r.json()['status']) == 'TRUE':
                    clear()
                    print("USERNAME AND PASSWORD IS CORRECT\nLogging You in ...")
                    API = str(r.json()['api'])
                    time.sleep(2)
                    break
                else:
                    clear()
                    print("USERNAME AND PASSWORD IS INCORRECT\nTRY AGAIN ...")
                    time.sleep(2)

            #functions
            while True:
                clear()
                show_func()
                func_type = sys.stdin.readline()

                #sendticket
                if func_type[:-1] == '1':
                    clear()
                    print("subject : ")
                    subject = sys.stdin.readline()[:-1]
                    print("body : ")
                    body = sys.stdin.readline()[:-1]
                    CMD = "sendTicket"
                    PARAMS = {'apiToken': API, 'subject': subject, 'body': body }
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print("message ID : " + str(r.json()['id']) )
                        print(str(r.json()['message']))

                    print('Press Any Key To Continue ...')
                    x = sys.stdin.readline()[:-1]

                #get ticket
                if func_type[:-1] == '2':
                    clear()
                    CMD = "getTicket"
                    PARAMS = {"apiToken": API}
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print(str(r.json()['tickets']))
                        index = int(r.json()['index'])
                        for i in range(0, index):
                            block = 'block ' + str(i)
                            print("message id : " + str(r.json()[block]['id']))
                            print("status : "+ str(r.json()[block]['type']))
                            print("subject : " + str(r.json()[block]['subject']))
                            print("message : " + str(r.json()[block]['body']))
                            print("response : " + str(r.json()[block]['response']) + "\n")

                    #if dont have message
                    else:
                        print(str(r.json()['tickets']))

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
                print("Your Acount Is Created\n" + "Your Username :" + USERNAME + "\nYour API : " + str(r.json()['api']))

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

