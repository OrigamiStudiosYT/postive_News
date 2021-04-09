from urllib.request import urlopen

URL = 'https://origamistudiosyt.github.io/'
page = urlopen(URL)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("se", "<title>")
file = open("webscrap.txt", "w")
file.write(html)
file.close()
print(html)
