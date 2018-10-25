# The interpreter figures out what site is being visited (either youtube or amazon), and will run
# the appropriate comment parser.  The interpreter will then feed the return of the parser to the
# filter, which will filter the comment based on the specified parameters.

import requests
from bs4 import BeautifulSoup
from AmazonScraper import *
from YouTubeScraper import *

# This is a list of swear words.  Let it be known that my
# knowledge of swear words is fairly limited as I never
# really learned to swear, so if I miss something, I'm
# terribly sorry :(
#
# The main purpose of this is to keep you from writing these
# words yourself in the extension window and suddenly have
# your mother storm in the room, which might not end well,
# depending on your mother :D
sw_list = ["fuck", "shit", "cunt", "nigger", "nigga", "prick",
           "dick", "dickhead", "shithead", "cock", "socksucker"]


class Interpreter:
    pass


def getRequest(url):
    page = requests.get(url)
    html_soup = BeautifulSoup(page.text, 'html.parser')
    type(html_soup)
    return html_soup


def filterComments(url, words_raw, swearwords, negativity):
    host = url.split('/')[2]
    words = words_raw.split(', ')
    print(host)
    if "amazon" in host:
        comments = AmazonScraper.scrape(url)
        print(type(comments))
        print(len(comments))
        print(comments)
    elif "youtube" in host:
        comments = YouTubeScraper.scrape(url)
    else:
        raise NotImplementedError
    if swearwords:
        words += sw_list
    print(words)
    comments_text = []
    for i in comments:
        try:
            comments_text.append(i.span.text)
        except UnicodeEncodeError:
            comments_text.append("----Comment contains emoji----")
    index = 0
    for i in comments_text:
        for j in words:
            if j in i:
                comments_text[index] = "----filtered----"
        index = index + 1
    commentfile = open("Comments.html", "w")
    commentfile.write("<!--DOCTYPE HTML-->\n")
    commentfile.write("<html>\n<body>\n" + "<h1>Comments for ya!</h1>\n<hr>\n")
    for i in comments_text:
        try:
            commentfile.write("<br>" + "<p>" + i + "</p>\n")
        except UnicodeEncodeError:
            commentfile.write("<br><p>--comment contains an emoji :(--</p>\n")
    commentfile.write("</body>\n" + "</html>\n")
    commentfile.close()
    return 0
