from urllib.request import urlopen
from requests_html import HTMLSession

session = HTMLSession()
page = session.get('https://www.nytimes.com/section/technology')
page.html.render(timeout=20)


def opening():
    file = open("webscraper/webscrap.txt", "w")
    return file


def searching(file):
    try:
        html = page.html.find(
            ".css-xta2bx")[range(1,3)]
        html = html.text
        html = html.replace("Photo", " ")
        html = html.replace("Credit", "Photo credit: ")
        file.write(html+"\n")
    except:
        print("Searching or opening the file has failed")
    return html


def closing(file):
    try:
        file.close()
        session.close()
    except:
        print("Closing or exiting the file has failed")


file = opening()
x = 0
while x in range(0, 4):
    html = searching(file)
    print(html)
    x = x+1
closing(file)
