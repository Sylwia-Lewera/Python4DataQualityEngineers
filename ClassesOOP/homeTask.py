import self
from datetime import date
from datetime import datetime

class NewsFeed(object):
    def __init__(self):
        self.feedDB = []
    def saveToFile(self):
        test = 'teste.rtf'
        out_file = open(test, 'w')
        for item in self.feedDB:
            out_file.write(("{\\rtf1\n"
                            "            This is \\b %s \\b0 line \n"
                            "            }").format(item.title))
        out_file.close()
    def addToFeed(self, feedItem):
        self.feedDB.append(feedItem)

class News(object):
    def __init__(self, text, city):
        self.title = '\033[1m{:10s}\033[0m'.format('News-----')
        self.text = text
        self.city = city
        self.pubDate = datetime.now()



class PrivateAdd(object):
    def __init__(self, text, expirationDate):
        self.title = 'Private Add-----'
        self. daysLeft = (expirationDate - datetime.now()).days

testAdd = PrivateAdd('addvert', datetime(2024,6,4))
sampleFeed = NewsFeed()

testNews = News('test', 'Cracow')

sampleFeed.addToFeed(testAdd)
sampleFeed.addToFeed(testNews)

sampleFeed.saveToFile()
