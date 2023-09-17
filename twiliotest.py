from twilio.rest import Client
from dotenv import load_dotenv
import os
import re


def msg_sender(body_part):

    load_dotenv()
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    contacts = os.getenv("CONTACTS")
    contacts = re.split("\s", contacts)
    sender = os.getenv("FROM")
    client = Client(account_sid, auth_token)

    for i in contacts:
        receiver = 'whatsapp:+91' + str(i)
        message = client.messages.create(
        from_=sender,
        body=body_part,
        to=receiver
        )   

