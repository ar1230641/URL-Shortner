import pyshorteners

link = input('Enter the url: ')


def shorturl(link):
    s = pyshorteners.Shortener()
    print("short url :")
    print(s.tinyurl.short(link))

shorturl(link)