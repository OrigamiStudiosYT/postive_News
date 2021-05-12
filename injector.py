def opening():
    try:
        file = open("webscraper/webscrap.txt", "r")
    except:
        print("Opening the file has failed")
    return file


def reading(file):
    lines = file.readlines()
    for line in lines:
        if line == " \n":
            print("Empty Line")
        else:
            html = line.strip()
    return html


def injecting(html):
    for x in range(4):
        html = reading(file)
        print("Something")


def closing(file):
    try:
        file.close()
    except:
        print("Closing or exiting the file has failed")


file = opening()
readed = injecting(html)
print(html)
closing(file)
