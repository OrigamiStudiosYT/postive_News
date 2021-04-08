from urllib.request import urlopen

URL = 'https://www.indeed.com/jobs?q=software+developer&l=Concord%2C+MA'
page = urlopen(URL)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("se","<title>")
print(html)