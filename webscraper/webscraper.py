from urllib.request import urlopen

URL = 'https://origamistudiosyt.github.io/'
page = urlopen(URL)
try:
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    file = open("webscraper/webscrap.txt", "w")
    file.write(html)
except:
    print("Something has failed and this is not epic")
finally:
    file.close()
    print(html)
