from urllib.request import urlopen
from requests_html import HTMLSession

session = HTMLSession()
page = session.get('https://www.nytimes.com/section/technology')
page.html.render()


def opening():
    file = open("webscraper/webscrap.txt", "w")
    return file


def searching(file):
    try:
        html = page.html.find(
            ".css-xta2bx", first=True)
        html = html.text
        html = html.replace("Photo", " ")
        html = html.replace("Credit", " ")
        file.write(html)
    except:
        print("Searching or opening the file has failed")
    return html


def closing(html, file):
    try:
        file.close()
        session.close()
        print(html)
    except:
        print("Closing or exiting the file has failed")


file = opening()
html = searching(file)
closing(html, file)
