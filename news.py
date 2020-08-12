import webbrowser
from pymongo import MongoClient


client = MongoClient(
    "mongodb://admin:admin123@192.168.18.92:27017/news-aggregator-v1?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")

# Database Name
db = client["news-aggregator-v1"]

# Collection Name
news_article = db["news-article"]
news_project = db["news-project"]
news_source = db["news-source"]


articles = news_article.find({'author': 'Mohammad Yaqoob'})
projects = news_project.find({'name': 'Techavenue'})
sources = news_source.find({'sourcename': 'pakistan-today'})

# articlesPage = open("articles.html", "a", encoding="utf-8")

# colour = ["red", "red", "green", "yellow"]

# with open('articles.html', 'w') as myFile:
#     myFile.write('<html>')
#     myFile.write('<body>')
#     myFile.write('<table>')

#     s = '1234567890'
#     for i in range(0, len(s), 60):
#         myFile.write('<tr><td>%04d</td>' % (i+1))
#     for j, k in enumerate(s[i:i+60]):
#         myFile.write('<td><font style="background-color:%s;">%s<font></td>' % (colour[j %len(colour)], k));


#     myFile.write('</tr>')
#     myFile.write('</table>')
#     myFile.write('</body>')
#     myFile.write('</html>')
     

# articlesPage.close()

projectsPage = open("projects.html", "a", encoding="utf-8")

for project in projects:
    print(project)
#      projectsPage.write(str(project)+'<br>')

# projectsPage.close()

sourcesPage = open("sources.html", "a", encoding="utf-8")

for source in sources:
    sourcesPage.write(str(source)+'<br>')

sourcesPage.close()

new = 2
url1 = "file://C:/Users/sheheryar.ahmad/Desktop/News Aggregator/articles.html"
webbrowser.open(url1, new=new)
url2 = "file://C:/Users/sheheryar.ahmad/Desktop/News Aggregator/projects.html"
'webbrowser.open(url2, new=new)'
url3 = "file://C:/Users/sheheryar.ahmad/Desktop/News Aggregator/sources.html"
'webbrowser.open(url3, new=new)'
