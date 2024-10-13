import os
from bs4 import BeautifulSoup


def fixSpacing():
    """uses bs4 to make html somewhat pleasant to look at"""
    directory = os.curdir
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".html"):
            print(filename)
            opened = open(file, 'r', encoding='utf-8')
            soup = BeautifulSoup(opened, 'html.parser').prettify()
            opened.close()

            opened = open(file, 'w', encoding='utf-8')
            opened.write(soup)
            opened.close()
        else:
            continue


fixSpacing()
