from urllib.request import urlopen
from requests_html import HTMLSession

session = HTMLSession()
page = session.get('http://127.0.0.1:5500/')
page.html.render()


def opening():
    file = open("webscraper/webscrap.txt", "w")
    return file


def searching(file):
    try:
        html = page.html.search(
            "My Years {} Assabet")[0]
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