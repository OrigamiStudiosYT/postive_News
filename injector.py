from bs4 import BeautifulSoup
from bs4.element import Tag


def opening():
    try:
        file = open("webscraper/webscrap.txt", "r")
    except:
        print("Opening the file has failed")
    return file


def reading(file):
    f = open("index.html", "r")
    line_offset = []
    offset = 0
    for line in f:
        line_offset.append(offset)
        offset += len(line)
    f.seek(0)
    lines_to_read = [1, 2, 3]
    lines_to_read1 = [6, 7, 8]
    lines_to_read2 = [12, 13, 14]
    lines_to_read3 = [17, 18, 19]
    f = open("index.html", "a")
    for position, line in enumerate(file):

        if position in lines_to_read:
            f.seek(line_offset[71])
            f.writelines(line)
        elif position in lines_to_read1:
            f.seek(line_offset[77])
            f.writelines(line)
        elif position in lines_to_read2:
            f.seek(line_offset[83])
            f.writelines(line)
        elif position in lines_to_read3:
            f.seek(line_offset[89])
            f.writelines(line)
        else:
            print(None)
    f.close()


def closing(file):
    try:
        file.close()
    except:
        print("Closing or exiting the file has failed")


file = opening()
reading(file)
closing(file)
