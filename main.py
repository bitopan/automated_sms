import pandas
import requests
import datetime
import random
import datetime as dt
from datetime import datetime

import config as cfg

def send_msg(user, dob, mobile):
    with open("data.txt", "a+") as myfile:
        user = str(user)
        message = cfg.SMS_MSG.format(user, "\n", "\n")

        payload = {
            'uname': cfg.SMS_UNAME,
            'pass': cfg.SMS_PASS,
            'send': cfg.SMS_SEND,
            'dest': str(mobile),
            'msg': message,
            'priority': cfg.SMS_PRIORITY
        }

        try:
            r = requests.get(cfg.SMS_URL, params=payload)
            r.raise_for_status()
            myfile.write(r.url + " at " + str(datetime.now()) + "\n")
        except requests.exceptions.HTTPError as e:
            print("Something went wrong! " + e.response.text)


def get_employees():
    df = pandas.read_csv(cfg.EMPLOYEE_FILE)

    df[['MOBILE']] = df[['MOBILE']].astype(str)

    is_active = (
        ((df['STATUS'] == 'yes') | (df['STATUS'] == 'Yes')) &
        (df['DOB'] != '') &
        (df['MOBILE'] != 'nan')
        )

    df = df[is_active]

    users = []
    for i, j in df.iterrows():
        dob = j[1]
        try:
            dob = dt.datetime.strptime(str(dob), '%d/%m/%Y')
            today = dt.date.today()
            if (isinstance(dob, dt.datetime)):
                if dob.day == today.day and dob.month == today.month:
                    user, dob, mobile = j[0], j[1], j[2]
                    users.append([user, dob, mobile])
        except:
            pass
    return users
    