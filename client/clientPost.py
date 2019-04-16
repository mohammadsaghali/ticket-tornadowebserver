
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
    print("To Create New Account Enter The Authentication")
    print("USERNAME : ")
    USERNAME = sys.stdin.readline()[:-1]
    print("PASSWORD : ")
    PASSWORD = sys.stdin.readline()[:-1]
    CMD = "signup"
    clear()
    PARAMS = {'username': USERNAME, 'password': PASSWORD, 'rool': "user1"}
    r = requests.post(__postcr__(), PARAMS)
    print(r.text)
    if r.status_code == 200:
        print("Your Acount Is Created\n" + "Your Username :" + USERNAME + "\nYour API : ")
        input("Press Any Key To Continue ...")
        break
    else:
        print(r['status'] + "\n" + "Try Again")
        input("Press Any Key To Continue ...")
        clear()
