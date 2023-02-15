from bs4 import BeautifulSoup
from bs4.element import Tag


def opening():
    try:
        file = open("webscraper/webscrap.txt", "r")
    except:
        print("Opening the file has failed")
    return file


def reading(file):
    with open("template.html", "r") as f:
        f = f.read()
        lines_to_read = [1, 2, 3]
        lines_to_read1 = [6, 7, 8]
        lines_to_read2 = [12, 13, 14]
        lines_to_read3 = [17, 18, 19]
        test = []
        test1 = []
        test2 = []
        test3 = []
        for position, line in enumerate(file):

            if position in lines_to_read:
                test.append(line)

            elif position in lines_to_read1:
                test1.append(line)

            elif position in lines_to_read2:
                test2.append(line)

            elif position in lines_to_read3:
                test3.append(line)
            else:
                print()
        f = f.replace("test0", str(test))
        f = f.replace("test1", str(test1))
        f = f.replace("test2", str(test2))
        f = f.replace("test3", str(test3))
        f = f.replace("\\n", " ")
        f = f.replace("[", " ")
        f = f.replace("]", " ")
        f = f.replace("'", " ")
        f = f.replace(",", " ")
        f = f.replace("�", "")
    with open("index.html", "w") as fl:
        fl.write(f)

    with open("template_m.html", "r") as f:
        f = f.read()

        f = f.replace("test0", str(test))
        f = f.replace("test1", str(test1))
        f = f.replace("test2", str(test2))
        f = f.replace("test3", str(test3))
        f = f.replace("\\n", " ")
        f = f.replace("[", " ")
        f = f.replace("]", " ")
        f = f.replace("'", " ")
    with open("m_index.html", "w") as fll:
        fll.write(f)


def closing(file):
    try:
        file.close()
    except:
        print("Closing or exiting the file has failed")


file = opening()
reading(file)
closing(file)
