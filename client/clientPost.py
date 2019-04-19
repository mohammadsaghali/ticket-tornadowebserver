
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
    2. get ticket
    3. change status
    4. change status (admin)
    5. response to tickets(admin)
    6. logout
    7. Exit
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

                if str(r.json()['status']) == 'OK':
                    clear()
                    print("API IS CORRECT\nLogging You in ...")
                    USERNAME = str(r.json()['username'])
                    print('Press Any Key To Continue ...')
                    x = sys.stdin.readline()[:-1]
                    break
                else:
                    clear()
                    print("API IS INCORRECT\nTRY AGAIN ...")
                    print('Press Any Key To Continue ...')
                    x = sys.stdin.readline()[:-1]


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
                        print("message ID : " + str(r.json()['id']))
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]

                    else:
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
                            print("status : " + str(r.json()[block]['type']))
                            print("subject : " + str(r.json()[block]['subject']))
                            print("message : " + str(r.json()[block]['body']))
                            print("response : " + str(r.json()[block]['response']) + "\n")
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]
                    else:
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]

                #change status
                if func_type[:-1] == '3':
                    clear()
                    CMD = "ticketStatus"
                    print("enter ticket ID : ")
                    id = sys.stdin.readline()[:-1]
                    PARAMS = {"apiToken": API, 'id': id}
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]
                    else:
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]



                #change status admin mode
                if func_type[:-1] == '4':
                    clear()
                    CMD = "ticketStatusAdmin"
                    print("enter ticket ID : ")
                    id = sys.stdin.readline()[:-1]

                    while True:
                        print("change status to this options:\n1.open\n2.close\n3.in progress\n")
                        state = sys.stdin.readline()[:-1]
                        if state == '1':
                            state = 'open'
                            break
                        elif state == '2':
                            state = 'close'
                            break
                        elif state == '3':
                            state = 'in progress'
                            break
                        else:
                            print("incorrect number try again")
                    PARAMS = {"apiToken": API, 'id': id, 'status': state}
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]
                    else:
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]

                #responsing
                if func_type[:-1] == '5':
                    clear()
                    CMD = "response"
                    print("enter ticket ID : ")
                    id = sys.stdin.readline()[:-1]
                    print("enter your response for this ticket : ")
                    body = sys.stdin.readline()[:-1]
                    PARAMS = {"apiToken": API, 'id': id, 'body': body}
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print(str(r.json()['message']))
                        print("message : " + str(r.json()['ticket']))
                        print("response : " + body)
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]
                    else:
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]


                if func_type[:-1] == '6':
                    break
                if func_type[:-1] == '7':
                    sys.exit()


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

                if str(r.json()['status']) == 'OK':
                    clear()
                    print("USERNAME AND PASSWORD IS CORRECT\nLogging You in ...")
                    API = str(r.json()['api'])
                    print('Press Any Key To Continue ...')
                    x = sys.stdin.readline()[:-1]
                    break
                else:
                    clear()
                    print("USERNAME AND PASSWORD IS INCORRECT\nTRY AGAIN ...")
                    print('Press Any Key To Continue ...')
                    x = sys.stdin.readline()[:-1]

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

                    else:
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
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]
                    else:
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]

                # change status
                if func_type[:-1] == '3':
                    clear()
                    CMD = "ticketStatus"
                    print("enter ticket ID : ")
                    id = sys.stdin.readline()[:-1]
                    PARAMS = {"apiToken": API, 'id': id}
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]
                    else:
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]

                # change status admin mode
                if func_type[:-1] == '4':
                    clear()
                    CMD = "ticketStatusAdmin"
                    print("enter ticket ID : ")
                    id = sys.stdin.readline()[:-1]

                    while True:
                        print("change status to this options:\n1.open\n2.close\n3.in progress\n")
                        state = sys.stdin.readline()[:-1]
                        if state == '1':
                            state = 'open'
                            break
                        elif state == '2':
                            state = 'close'
                            break
                        elif state == '3':
                            state = 'in progress'
                            break
                        else:
                            print("incorrect number try again")
                    PARAMS = {"apiToken": API, 'id': id, 'status': state}
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]
                    else:
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]

                # responsing
                if func_type[:-1] == '5':
                    clear()
                    CMD = "response"
                    print("enter ticket ID : ")
                    id = sys.stdin.readline()[:-1]
                    print("enter your response for this ticket : ")
                    body = sys.stdin.readline()[:-1]
                    PARAMS = {"apiToken": API, 'id': id, 'body': body}
                    r = requests.post(__postcr__(), PARAMS)

                    if str(r.json()['status']) == "OK":
                        print(str(r.json()['message']))
                        print("message : " + str(r.json()['ticket']))
                        print("response : " + body)
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]
                    else:
                        print(str(r.json()['message']))
                        print('Press Any Key To Continue ...')
                        x = sys.stdin.readline()[:-1]

                if func_type[:-1] == '6':
                    break
                if func_type[:-1] == '7':
                    sys.exit()

        #signup
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
                print("ROLE : " + "\n1.admin\n2.user")
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
                print(str(r.json()['message']))
                print("Your Acount Is Created\n" + "Your Username :" + USERNAME + "\nYour API : " + str(r.json()['apitoken']))
                print('Press Any Key To Continue ...')
                x = sys.stdin.readline()[:-1]
                break
            else:
                print(str(r.json()['message']) + "\n" + "Try Again")
                print('Press Any Key To Continue ...')
                x = sys.stdin.readline()[:-1]
                clear()

    # exit
    elif status[:-1] == '3':
        sys.exit()


    # wrong answer
    else:
        print("Wrong Choose Try Again")

