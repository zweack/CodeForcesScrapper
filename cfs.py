from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import time
import sys
import webbrowser


def userDetails(userHandle, userTitle, userRating, maxRating):

    table = []
    for i in range(len(userHandle)):

        entry = []
        entry.append(i+1)
        entry.append(userHandle[i])
        entry.append(userTitle[i])
        entry.append(userRating[i])
        entry.append(maxRating[i])
        table.append(entry)

    print(tabulate(table, headers=["S. No.", "Handle", "Title", "Rating", "Max Rating"]))


def getResponse(url):
    try:
        source = requests.get(url, verify=False, timeout=240)
    except:
        time.sleep(5)
        source = requests.get(url, verify=False, timeout=240)
    textDetail = source.text
    soup = BeautifulSoup(textDetail, "html.parser")
    return soup


def readFile():
    fr = open('friends.txt', 'r')
    text = fr.readlines()
    fr.close()
    return text


def calculate():

    handles = readFile()
    userHandle = []
    userTitle = []
    userRating = []
    maxRating = []
    i = 0

    while i < len(handles):

        url = "http://codeforces.com/profile/" + handles[i]
        soup = getResponse(url)

        link = soup.findAll('div', {'class': 'info'})
        for div in link:
            span = div.find_all('span')

        userHandle.append(handles[i])
        userTitle.append(span[0].string)
        userRating.append(span[1].string)
        maxRating.append(span[4].string)
        i += 1

    return userHandle, userTitle, userRating, maxRating


def main():

    userHandle, userTitle, userRating, maxRating = calculate()
    userDetails(userHandle, userTitle, userRating, maxRating)
    num = int(input("Choose option: 1-"+str(len(userHandle)) +" To view profile OR Press "+str(len(userHandle)+1)+" to exit : "))

    if num >= 1 and num <= len(userHandle):
        webbrowser.open("http://codeforces.com/profile/" +userHandle[num-1])
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
