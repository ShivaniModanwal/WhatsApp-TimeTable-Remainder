
import requests
import twiliotest
import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()

def morning_qoutes():
    r = requests.get('http://api.quotable.io/random')
    data = r.json()
    # print(data)
    msg=data['content'] + ' . . . by ' + data['author']
    # print(msg)
    twiliotest.msg_sender("Quote for today")
    twiliotest.msg_sender(msg)

def monday_tfcs():
    load_env()
    tfcs_link = os.getenv("TFCS_LINK")
    twiliotest.msg_sender("TFCS Class Will Commence At 11:00 AM To 01:00 PM")
    twiliotest.msg_sender(tfcs_link)

def monday_coa():
    load_env()
    coa_link = os.getenv("COA_LINK")
    twiliotest.msg_sender("COA Class Will Commence At 02:00 PM To 03:00 PM")
    twiliotest.msg_sender(coa_link)

def tuesday_pm():
    load_env()
    pm_link = os.getenv("PM_LINK")
    twiliotest.msg_sender("PM Class Will Commence At 09:00 AM To 11:00 AM")
    twiliotest.msg_sender(pm_link)

def tuesday_pm_lab():
    load_env()
    pm_link = os.getenv("PM_LINK")
    twiliotest.msg_sender("PM Lab Class Will Commence At 02:00 PM To 05:00 PM")
    twiliotest.msg_sender(pm_link)

def wednesday_tfcs():
    load_env()
    tfcs_link = os.getenv("TFCS_LINK")
    twiliotest.msg_sender("TFCS Class Will Commence At 09:00 AM To 11:00 AM")
    twiliotest.msg_sender(tfcs_link)

def wednesday_cbot():
    twiliotest.msg_sender("CBOT Class Will Commence At 11:00 AM To 01:00 PM")
    twiliotest.msg_sender("Link Will Be Send To Mail")

def wednesday_coa():
    load_env()
    coa_link = os.getenv("COA_LINK")
    twiliotest.msg_sender("COA Class Will Commence At 02:00 PM To 04:00 PM")
    twiliotest.msg_sender(coa_link)

def thursday_pm():
    load_env()
    pm_link = os.getenv("PM_LINK")
    twiliotest.msg_sender("PM Lab Class Will Commence At 09:00 AM To 11:00 AM")
    twiliotest.msg_sender(pm_link)

def friday_tfcs():
    load_env()
    tfcs_link = os.getenv("TFCS_LINK")
    twiliotest.msg_sender("TFCS Class Will Commence At 10:00 AM To 11:00 AM")
    twiliotest.msg_sender(tfcs_link)

def friday_cbot():
    twiliotest.msg_sender("CBOT Class Will Commence At 11:00 AM To 01:00 PM")
    twiliotest.msg_sender("Link Will Be Send To Mail")

def friday_coa():
    load_env()
    coa_link = os.getenv("COA_LINK")
    twiliotest.msg_sender("COA Class Will Commence At 02:00 PM To 04:00 PM")
    twiliotest.msg_sender(coa_link)

def lunch_break():
    twiliotest.msg_sender("Lunch Break At 01:00 PM To 02:00 PM")

