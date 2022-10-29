import schedule
import requests
import time
from mobile import number_

def send_message():

    resp = requests.post('https://textbelt.com', {
        'phone': number_,
        'message': 'ON DAY SON',
        'key': 'textbelt'
    })


    print(resp.json())


# schedule.every().day.at('05:00').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:

    schedule.run_pending()
    time.sleep(1)