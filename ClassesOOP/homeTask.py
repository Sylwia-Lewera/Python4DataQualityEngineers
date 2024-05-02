import self
from datetime import date
from datetime import datetime
from stringObject.homeTask import normalize_text

class NewsFeed(object):
    def __init__(self):
        self.feedDB = []

    def saveToFile(self):
        self.sortFeed()
        with open("output .md", "a") as file:
            for item in self.feedDB:
                file.write(f"<b>{item.title}</b><br>")
                file.write(f"{item.text}<br>")
                if item.type == 'News':
                    file.write(f"{item.city}, <b>{item.pubDate.day}/{item.pubDate.month}/{item.pubDate.year} {item.pubDate.hour}.{item.pubDate.minute}</b><br>")
                elif item.type == 'PrivateAdd':
                    file.write(f"<b>Actual until:</b> {item.expirationDate.day}/{item.expirationDate.month}/{item.expirationDate.year} <b>{item.daysLeft} days left</b><br>")
                elif item.type == 'Weather':
                    file.write(f"{item.city}, <b>{item.date.day}/{item.pubDate.month}/{item.pubDate.year}</b><br>")

    def addToFeed(self, feedItem):
        self.feedDB.append(feedItem)

    def sortFeed(self):
        self.feedDB.sort(key=lambda x: x.type, reverse=False)


class News(object):
    def __init__(self, text, city):
        self.title = "News--------------------"
        self.text = text
        self.type = 'News'
        self.city = city
        self.pubDate = datetime.now()
class Weather(News):
    def __init__(self, text, city, date):
        super().__init__(text, city)
        self.date = date
        self.type = 'Weather'
        self.title = "Weather--------------------"

class PrivateAdd(object):
    def __init__(self, text, expirationDate):
        self.text = text
        self.title = "Private Add------------------"
        self.type = 'PrivateAdd'
        self.expirationDate = expirationDate
        self.daysLeft = (expirationDate - datetime.now()).days

"""
testAdd = PrivateAdd('addvert', datetime(2024, 6, 4))

sellAdd = PrivateAdd(normalize_text('Sprzedam Opla za 3000 PLN'), datetime(2024, 12, 31))
testNews = News('test', 'Cracow')
testNews2 = News('test2', 'Warsaw')
testWeather = Weather('Sunny','Cracow', datetime(2024, 8, 15))
sampleFeed.addToFeed(testAdd)
sampleFeed.addToFeed(sellAdd)
sampleFeed.addToFeed(testNews)
sampleFeed.addToFeed(testNews2)
sampleFeed.addToFeed(testWeather)"""

sampleFeed = NewsFeed()
menuLoop = True
while menuLoop:
    print(""""Select action you wish to perform
    1. Add News record
    2. Add Private Add record
    3. Save current weather condition.
    4. Save Current Feed to the file
    5. Exit the program
    """)
    action = int(input())
    match action:
        case 1:
            print("""Provide news text:
            """)
            newsText = str(input())
            print("""Provide city name:
                        """)
            newsCity = str(input())
            newsRecord = News(normalize_text(newsText), newsCity)
            sampleFeed.addToFeed(newsRecord)
        case 2:
            print("""Provide private add text:
                        """)
            addText = str(input())
            print("""Provide year of expiration date:
                                    """)
            expYear = int(input())
            print("""Provide month of expiration date:
                                                """)
            expMonth = int(input())
            print("""Provide day of expiration date:
                                                """)
            expDay = int(input())
            addvRecord = PrivateAdd(normalize_text(addText), datetime(expYear, expMonth, expDay))
            sampleFeed.addToFeed(addvRecord)

        case 3:
            print("""Provide current weather description:
                                    """)
            weatherText = str(input())
            print("""Provide city name:
                                    """)
            weatherCity = str(input())
            print("""Provide current year:
                                                """)
            wYear = int(input())
            print("""Providecurrent month:
                                                            """)
            wMonth = int(input())
            print("""Provide current day:
                                                            """)
            wDay = int(input())
            weatherRecord = Weather(weatherText, weatherCity, datetime(wYear, wMonth, wDay))
            sampleFeed.addToFeed(weatherRecord)
        case 4:
            sampleFeed.saveToFile()
        case 5:
            menuLoop = False
            break


