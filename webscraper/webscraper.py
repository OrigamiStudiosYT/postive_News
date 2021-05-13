from urllib.request import urlopen
from requests_html import HTMLSession

session = HTMLSession()
page = session.get('https://www.nytimes.com/section/technology')
page.html.render(timeout=20)


def opening():
    try:
        file = open("webscraper/webscrap.txt", "w")
    except:
        print("Opening the file has failed")
    return file


def searching(file):
    try:
        bol = False
        html = page.html.find(".css-xta2bx")
        for allcontainers in html:
            html = allcontainers.text
            html = html.replace("Photo", "")
            html = html.replace("Credit", "Photo credit: ")
            html = html.replace("agoBy", "ago By")
            if bol == False:
                file.writelines(html[1:]+"\n")
                bol = True
            else:
                file.writelines(html+"\n")
    except:
        print("Searching the file has failed")
    return html


def closing(file):
    try:
        file.close()
        session.close()
    except:
        print("Closing or exiting the file has failed")


file = opening()
html = searching(file)
#print(html)
closing(file)
