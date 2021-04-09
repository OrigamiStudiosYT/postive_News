file = open("webscraper/webscrap.txt", "r")

try:
    print(file.read())
except:
    print("Gathering has failed")
finally:
    file.close()
