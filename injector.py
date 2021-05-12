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
    lines = file.readlines()
    htmla = []
    for line in lines:
        if line == " \n":
            print("Empty Line")
        else:
            htmla.append(line.strip())
    return htmla


def closing(file):
    try:
        file.close()
    except:
        print("Closing or exiting the file has failed")


file = opening()
readed = injecting()
closing(file)
