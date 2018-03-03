import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox***.mailgun.org/messages",
        auth=("api", "key-****"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox******.mailgun.org>",
              "to": "UserAdi <user mail adresi>",
              "subject": "Hello useradi",
              "text": "Lütfen değerleriniz sınır değerine ulaştı!"})
