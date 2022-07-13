from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests.exceptions
import urllib.parse
from collections import deque
import re
import threading
import os


def email_scrapper(main_window, user_url):
    """
    This functions recive url address,scrapping through 20 hyperlinks inside the root url and extracting them into a list
    :param main_window: tkinter
    :param user_url: string
    :return: None
    """
    sent_url = "https://" + user_url.get()
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
    handle_results(main_window)


def handle_results(main_window):
    """
    This function handle the result after url scrapping, decide to watch the list of scrapped emails or exit
    :param main_window: tkinter
    :return: None
    """
    response = messagebox.askokcancel("Finished Successfully!", "Open the text file to watch results!")
    label = Label(main_window, text=response)
    label.pack()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if response == 1:
        os.startfile(dir_path + "/Emails.txt")
        main_window.quit()
    else:
        exit_response = messagebox.showwarning("Exit", "Bye Bye!")
        Label(main_window, text=exit_response).pack()
        main_window.quit()


def export_scan_to_file(emails):
    """
    This function exports the emails into a text file
    :return: None
    """
    with open('Emails.txt', 'w+') as fh:
        for mail in range(0, len(emails)):
            fh.write(f"{mail + 1}){emails[mail]}\n")


def main():
    # init the tkinter window, add the scrapping functionality to the start button
    main_window = Tk()
    main_window.title("Email Scrapper")
    main_window.geometry('500x300')
    main_window.config(bg='azure')
    user_url = StringVar(main_window)
    Label(main_window, text='The Email Scrapper', bg='azure', fg='black', font=('Times', 20, 'bold')).place(x=100, y=10)
    Label(main_window, text='Enter Url', bg='azure2', anchor="e", justify=LEFT).place(x=225, y=90)
    Entry(main_window, textvariable=user_url, width=35, font=('calibre', 10, 'normal')).place(x=150, y=140)
    Button(main_window, text="Start", bg='ivory3', font=('calibre', 13),
           command=threading.Thread(target=email_scrapper, args=(main_window, user_url)).start).place(x=225, y=180)
    main_window.mainloop()


if __name__ == '__main__':
    main()
