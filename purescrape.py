from lxml import html
from datetime import datetime
import requests
import sqlite3
import config

LOGIN_URL = "https://www.puregym.com/login/"
LOGIN_API_URL = "https://www.puregym.com/api/members/login/"
DASH_URL = "https://www.puregym.com/members/"

# Connect to sqlite
db_conn = sqlite3.connect(config.sqlite_path)
db_cur = db_conn.cursor()

def main():
    # Persistent login session
    session_requests = requests.session()

    # Get login auth token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='__RequestVerificationToken']/@value")))[0]

    # Create payload
    payload = {
            "associateAccount": "false",
            "email": config.EMAIL,
            "pin": config.PIN
    }

    headerPayload = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Host': 'www.puregym.com',
            'Origin': 'https://www.puregym.com',
            'Referer': LOGIN_URL,
            '__RequestVerificationToken': authenticity_token
    }

    # Perform login
    result = session_requests.post(
            LOGIN_API_URL,
            data = payload,
            headers = headerPayload
    )

    print("Login succeeded: ", result.ok)
    print("Status code:", result.status_code)

    # Scrape dashboard

    url = 'https://www.puregym.com/members/'
    result = session_requests.get(
            url,
            headers = dict(referer = url)
    )

    tree = html.fromstring(result.content)

    # People
    people = tree.xpath('//*[@id="main-content"]/div[2]/div/div/div[1]/div/div/div/div[1]/div/p[1]/span/text()')
    print(people[0])
    print("Time now: ", datetime.today())
    #print (result.content)

    createdb()



    closedb()

def closedb():
    db_conn.close()

def createdb():
    try:
        db_cur.execute('''
            CREATE TABLE IF NOT EXISTS visitors(datetime TEXT PRIMARY KEY, people INTEGER)
        ''')
        db_conn.commit()
    except Exception as e:
        print(e)

# Entry point
if __name__ == '__main__':
    main()
