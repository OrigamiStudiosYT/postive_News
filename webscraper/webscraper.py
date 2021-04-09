from urllib.request import urlopen
from requests_html import HTMLSession
session = HTMLSession()

URL = session.get('https://www.nytimes.com/section/technology')
page = URL.html.render()
try:
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    file = open("webscraper/webscrap.txt", "w")
    file.write(html)
except:
    print("Something has failed and this is not epic")
finally:
    file.close()
    session.close()
    URL.close()
    print(html)
    
