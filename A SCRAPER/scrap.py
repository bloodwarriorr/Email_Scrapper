from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests.exceptions
import urllib.parse
from collections import deque
import re


def email_scrapper():
    sent_url = user_url.get()
    if 'https://' not in sent_url:
        sent_url = 'https://' + user_url.get()
    urls = deque([sent_url])
    scraped_urls = set()
    emails = set()
    count = 0
    try:
        while len(urls):
            count += 1
            if count == 20:
                break
            url = urls.popleft()
            scraped_urls.add(url)
            parts = urllib.parse.urlsplit(url)
            base_url = '{0.scheme}://{0.netloc}'.format(parts)
            path = url[:url.rfind('/') + 1] if '/' in parts.path else url
            print('[%d] Processing %s' % (count, url))
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                continue

            new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, features="html.parser")

            for anchor in soup.find_all("a"):
                link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                if not link in urls and not link in scraped_urls:
                    urls.append(link)
    except KeyboardInterrupt:
        print('[-] Closing!')

    export_scan_to_file(list(emails))


def export_scan_to_file(emails):
    """
    This function exports the emails into a text file
    :return: None
    """
    with open('Emails.txt', 'w+') as fh:
        for mail in range(0, len(emails)):
            fh.write(f"{mail + 1}){emails[mail]}\n")


main_window = Tk()
main_window.title("Email Scrapper")
main_window.geometry('500x300')
main_window.config(bg='azure')
user_url = StringVar(main_window)
Label(main_window, text='The Email Scrapper', bg='azure', fg='black', font=('Times', 20, 'bold')).place(x=100, y=10)
Label(main_window, text='Enter Url With https://', bg='azure2', anchor="e", justify=LEFT).place(x=225, y=90)
Entry(main_window, textvariable=user_url, width=35, font=('calibre', 10, 'normal')).place(x=150, y=140)
Button(main_window, text="Start", bg='ivory3', font=('calibre', 13), command=email_scrapper).place(x=225, y=180)
main_window.mainloop()



