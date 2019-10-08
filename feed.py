import feedparser
from bs4 import BeautifulSoup as bs
from pprint import pprint
from hashlib import md5
import os
import re
from disc import post

def write(feed):
    counter = 0
    arr = []
    for i in range(len(feed['items'])):
        soup = bs(feed['items'][i]['summary'], 'html.parser')
        text = soup.get_text()
        enc = md5(text.encode())
        if not os.path.isfile('sub.dat'):
            f = open('sub.dat', 'w')
            f.close()
        val = check(enc.hexdigest(), 'sub.dat')
        with open('sub.dat', 'a+') as f:
            if val:
                print('Already present...')
            else:
                with open('sub.dat', 'a') as f:
                    print('Successfully encoded as ' + enc.hexdigest() + ' !')
                    f.write(enc.hexdigest() + '\n')
                    counter += 1
                    arr.append(text)
    return arr

def check(y, f):
    with open(f, 'r') as file:
        for line in file:
            if re.match(y, line):
                return True
    return False

def respond(a):
    if len(a) == 0:
        print('[!]No new RSS received...')
    else:
        print('[+]Received new Feed! Processing...')
        post(MESSAGE = a,CHANNEL = 398538798994161664)

if __name__ == '__main__':
    url = 'https://www.helionet.org/index/rss/forums/1-heliohost-news/'
    feed = feedparser.parse(url)
    messages = write(feed)
    try:
        respond(messages[0])
    except exception as e:
        print(str(e))
