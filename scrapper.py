from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import os
from random import choices
import string
import webbrowser

def getText(url, selector):
    try:
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urlopen(request_site)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        text = bs.find('div', {'class' : selector[1:]})
    except AttributeError as e:
        print(e)
        return None
    return str(text)

def getFileName():
    '''returns an html file name with 10 random alphanumeric characters'''
    seq = string.ascii_letters + string.digits
    return ''.join(choices(seq, k = 10)) + '.html'

domainListSelector = {
'textbookplus.in': '.entry-content',
'englishshyamsir.com' : '.entry-content', 
'edutricks.in' : '.entry-content',
}
    

if __name__ == '__main__':
    # input a URL
    url = input('Enter a URL: ')

    # extract domain
    domainMatch = re.search(r'^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)', url)
    if domainMatch != None:
        domain = domainMatch.group(1)
    else:
        domain = ''

    # check whether domain is in our list
    if domain in domainListSelector:
        selector = domainListSelector[domain]
    else:
        # input for custom selector
        selector = input('Enter custom selector: ')
        
        # if input is blank then use most common selector
        if selector == '':
            selector = '.entry-content'

    # scrap the element 
    text = getText(url, selector)
    if text == None:
        print('Text could not be found')
    else:
        # write the text to a file with extension html
        # get a unique file name
        fileName = 'data/'+ getFileName()
        while os.path.isfile(fileName):
            fileName = getFileName()

        # create a file 
        file = open(fileName, 'w', encoding='utf-8')
        file.write(text)
        file.close()

        # open the file in browser
        currentDir = os.getcwd()
        filePath = os.path.join(currentDir, fileName)
        webbrowser.open(filePath)

        print('Text is scrapped successfully')