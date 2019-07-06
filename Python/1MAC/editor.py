import urllib
import sys
from termcolor import colored, cprint
def read():
    quotes = open("test.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    chk_word(content_of_file)

def chk_word(text_to_chk):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_chk)
    output = connection.read()
    connection.close()

    if ("true" in output):
        cprint(" Yes found in this file, please check your text.file have word curse ")
    elif ("false" in output):
        cprint("No found in this file, this file is clean from curse words")
    else:
        print("could not scan the doc properly")
read()