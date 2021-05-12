from bs4 import BeautifulSoup




def opening():
    try:
        file = open("webscraper/webscrap.txt", "r")
    except:
        print("Opening the file has failed")
    return file


def injecting():
    for x in range(4):
        htmla = reading(file)
        print(htmla)


def reading(file):
    with open("index.html", encoding="utf-8", mode="r+") as fp:
        soup = BeautifulSoup(fp, "html.parser")
    #lines = file.readlines()
    #htmla = []
    pclassses1 = soup.find("p", class_="Text1")
    pclassses2 = soup.find("p", class_="Text2")
    pclassses3 = soup.find("p", class_="Text3")
    pclassses4 = soup.find("p", class_="Text4")

    pclassses1 = pclassses1.replaceWith("<p class='Text1'> line2 </p>")
    pclassses2 = pclassses2.replaceWith("<p class='Text2'> line2 </p>")
    pclassses3 = pclassses3.replaceWith("<p class='Text3'> line3 </p>")
    pclassses4 = pclassses4.replaceWith("<p class='Text4'> line4 </p>")

    fp.write(str(pclassses1))
    fp.write(str(pclassses2))
    fp.write(str(pclassses3))
    fp.write(str(pclassses4))

    # for line in lines:
    #    if line == " \n":
    #        print("Empty Line")
    #    else:
    #        htmla.append(line.strip())
    # return htmla


def closing(file):
    try:
        file.close()
    except:
        print("Closing or exiting the file has failed")


file = opening()
reading(file)
#readed = injecting()
closing(file)
