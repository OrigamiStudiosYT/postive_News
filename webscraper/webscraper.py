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
        html = page.html.find(".css-xta2bx")
        for allcontainers in html:
            html = allcontainers.find("div", {"class": "css-gjijuv"})
            html = allcontainers.text
            html = allcontainers.replace("Photo", " ")
            html = allcontainers.replace("Credit", "Photo credit: ")
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
html = searching(file)
print(html)
closing(file)
