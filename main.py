import pandas
import requests
import datetime
import random
import datetime as dt
from datetime import datetime

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
sms_url = config.get('sms_gateway', 'url')
sms_uname = config.get('sms_gateway', 'uname')
sms_pass = config.get('sms_gateway', 'pass')
sms_send = config.get('sms_gateway', 'send')
sms_priority = config.get('sms_gateway', 'priority')

def send_msg(user, dob, mobile):
    with open("data.txt", "a+") as myfile:

        msg = "Hi " + str(user) + "!\nWish you a very Happy Birthday.\nRegards, down town hospital"

        payload = {
            'uname': sms_uname,
            'pass': sms_pass,
            'send': sms_send,
            'dest': str(mobile),
            'msg': msg,
            'priority': sms_priority
        }


        try:
            r = requests.get(sms_url, params=payload)
            r.raise_for_status()
            myfile.write(r.url + " at " + str(datetime.now()) + "\n")
            #myfile.write(str(user) + " at " + str(datetime.now()) + "\n")
        except requests.exceptions.HTTPError as e:
            print("Something went wrong! " + e.response.text)
            #myfile.write(e.response.text + " at " + str(datetime.now()))


def get_employees():
    dateparse = lambda x: pandas.datetime.strptime(x, '%d/%m/%Y')
    df = pandas.read_csv('employees.csv',
                         parse_dates=['DOB'],
                         date_parser=dateparse)

    users = []
    for i, j in df.iterrows():
        dob = j[1]

        # date_of_birth = datetime.datetime.strptime(dob, "%Y-%m-%d")
        today = dt.date.today()

        if dob.day == today.day and dob.month == today.month:
            user, dob, mobile = j[0], j[1], j[2]
            users.append([user, dob, mobile])

    return users
