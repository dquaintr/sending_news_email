import yagmail
import pandas
from news import NewsFeed
import datetime
import time



def send_email():
    email = yagmail.SMTP(user, password)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    today = now
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    user = USERADDRESS
    password = PASSWORDUSER
    news_feed = NewsFeed(interest=row['interest'],
                         from_date='2024-3-26',
                         to_date=today,
                         language='en')
    receiver = row["email"]
    subject = f"Your {row['interest']} news for today"
    contents = f"Hi {row['name']}, " \
               f"see what is new in the world of {row['interest']} " \
               f"\n {news_feed.get()} \n Daniel"
    attachments = path_to_file
    email.send(to=receiver,
               subject=subject,
               contents=contents,
               attachments=attachments)


while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 23:

        df = pandas.read_excel(list_of_addresses)

        for index, row in df.interrows():
            send_email()

    time.sleep(60)



