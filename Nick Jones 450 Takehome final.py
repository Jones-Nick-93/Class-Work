#Nick Jones DSC 450 Takehome Final
#Problem 1 starts on line 56
import sqlite3, json, time
import urllib.request as urllib
#Creating the Tweet, User, and Geo tables
TweetTable = '''CREATE TABLE Tweet
(
    created_at              VARCHAR2(50),
    id_str                  VARCHAR2(50),
    text                    VARCHAR2(50),
    source                  VARCHAR2(50),
    in_reply_to_user_id     NUMBER(20),
    in_reply_to_screen_name VARCHAR2(30),
    in_reply_to_status_id   NUMBER(20),
    retweet_count           NUMBER(4),
    contributors            VARCHAR2(10),
    user_id                 VARCHAR2(50),
    geo_id                  INTEGER(50),
    CONSTRAINT Tweer_PK PRIMARY KEY(id_str),
    CONSTRAINT Tweet_FK FOREIGN KEY(user_id)
    REFERENCES User(id),
    CONSTRAINT Tweet_FK1 FOREIGN KEY(geo_id)
    REFERENCES Geo(id)
)'''

UserTable = '''CREATE TABLE User
(
    id              VARCHAR2(50),
    name            VARCHAR2(50),
    screen_name     VARCHAR2(50),
    description     VARCHAR2(50),
    friends_count   NUMBER(10),
    CONSTRAINT User_PK PRIMARY KEY(id)
)'''

GeoTable = '''CREATE TABLE Geo
(
    id              INTEGER PRIMARY KEY,
    type            VARCHAR2(50),
    longitude       VARCHAR2(50),
    latitude        VARCHAR2(50)
)
'''

conn = sqlite3.connect('JonesTweet.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Tweet")
c.execute(TweetTable)
c.execute("DROP TABLE IF EXISTS User")
c.execute(UserTable)
c.execute("DROP TABLE IF EXISTS Geo")
c.execute(GeoTable)

#Problem 1a (lines 56-71)
# Write the downloaded file of tweets to a txtfile
import urllib.request as urllib
import time
response = urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt")
tInput = {}
tweet = open('JonesTweetFinal.txt', 'w', encoding = 'utf8')
Start1a = time.time()
for i in range(500000):
    str_response = response.readline()
    tInput[i] = str_response
    tweet.write(str_response.decode("utf8"))
End1a = time.time()
RunTime1a = End1a - Start1a
#Print Runtime 1a
print("The run time is ", RunTime1a, "seconds.")
response.close()
tweet.close()

#Problem 1 part b (75-166)
#Populate 3 Table Schema in SQLite and report loaded row count
response = urllib.urlopen("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt")

Start1b = time.time()
flag = 1

for i in range(500000): 
    str_response = response.readline().decode("utf8")
    try:
        tDict = json.loads(str_response)
        for value in tDict.values():
            if value == "null":
                value == None
#User Table Data
        uData = []
        uID = tDict['user']['id']
        uName = tDict['user']['name']
        uSname = tDict['user']['screen_name']
        uDescription = tDict['user']['description']
        uFcount = tDict['user']['friends_count']
        uData.append(uID)
        uData.append(uName)
        uData.append(uSname)
        uData.append(uDescription)
        uData.append(uFcount)
                      
#Tweet Table Data
        if 'retweeted_status' in tDict.keys():
            retweetcount = tDict['retweeted_status']['retweet_count']
        else:
            retweetcount = tDict['retweet_count']
        tData = []
        tCreatedat = tDict['created_at']
        tIdstr = tDict['id_str']
        tText = tDict['text']
        tSource = tDict['source']
        tInreplyID = tDict['in_reply_to_user_id']
        tInreplyName = tDict['in_reply_to_screen_name']
        tInreplysID = tDict['in_reply_to_status_id']
        tContributors = tDict['contributors']
        tUid = tDict['user']['id']
        tData.append(tCreatedat)
        tData.append(tIdstr)
        tData.append(tText)
        tData.append(tSource)
        tData.append(tInreplyID)
        tData.append(tInreplyName)
        tData.append(tInreplysID)
        tData.append(retweetcount)
        tData.append(tContributors)
        tData.append(tUid)
                       
#Geo Table Data
        if tDict['geo'] != None:
            gData = []
            gID = flag
            gType = tDict['geo']['type']
            gLongitude = tDict['geo']['coordinates'][1]
            gLatitude = tDict['geo']['coordinates'][0]
            gData.append(gID)
            gData.append(gType)
            gData.append(gLongitude)
            gData.append(gLatitude)
            c.execute("INSERT INTO Geo VALUES(?, ?, ?, ?);", gData)
            tData.append(gID)
            flag = flag + 1
        else:
            tData.append(None)
        
        c.execute("INSERT INTO Tweet VALUES(?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?);", tData)
        c.execute("INSERT INTO User VALUES(?, ?, ?, ?, ?);", uData)
    except ValueError:
        print(" ")

tRows = c.execute("SELECT COUNT(*) FROM Tweet;").fetchall()[0]
print("There are", tRows, "rows in Tweet Table.")
uRows = c.execute("SELECT COUNT(*) FROM User;").fetchall()[0]
print("There are", uRows, "rows in User Table.")
gRows = c.execute("SELECT COUNT(*) FROM Geo;").fetchall()[0]
print("There are", gRows, "rows in Geo Table.")

End1b = time.time()
RunTime1b = End1b - Start1b
#Runtime for 1b
print("The run time is ", RunTime1b, "seconds.")

c.close()
conn.commit()
conn.close()

#Problem 1C (168-300)
#Load tweets to database using saved txt file
import json, time, sqlite3
TweetTable = '''CREATE TABLE Tweet
(
    created_at              VARCHAR2(50),
    id_str                  VARCHAR2(50),
    text                    VARCHAR2(50),
    source                  VARCHAR2(50),
    in_reply_to_user_id     NUMBER(20),
    in_reply_to_screen_name VARCHAR2(30),
    in_reply_to_status_id   NUMBER(20),
    retweet_count           NUMBER(4),
    contributors            VARCHAR2(10),
    user_id                 VARCHAR2(50),
    geo_id                  INTEGER(50),
    CONSTRAINT Tweer_PK PRIMARY KEY(id_str),
    CONSTRAINT Tweet_FK FOREIGN KEY(user_id)
    REFERENCES User(id),
    CONSTRAINT Tweet_FK1 FOREIGN KEY(geo_id)
    REFERENCES Geo(id)
)'''

UserTable = '''CREATE TABLE User
(
    id              VARCHAR2(50),
    name            VARCHAR2(50),
    screen_name     VARCHAR2(50),
    description     VARCHAR2(50),
    friends_count   NUMBER(10),
    CONSTRAINT User_PK PRIMARY KEY(id)
)'''

GeoTable = '''CREATE TABLE Geo
(
    id              INTEGER PRIMARY KEY,
    type            VARCHAR2(50),
    longitude       VARCHAR2(50),
    latitude        VARCHAR2(50)
)
'''

conn = sqlite3.connect('JonesTweet.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Tweet")
c.execute(TweetTable)
c.execute("DROP TABLE IF EXISTS User")
c.execute(UserTable)
c.execute("DROP TABLE IF EXISTS Geo")
c.execute(GeoTable)

tweet = open('JonesTweetFinal.txt', 'r', encoding='utf8')

Start1d = time.time()
flag = 1
for i in range(500000):
    str_response = tweet.readline()
    try:
        tDict = json.loads(str_response)
#User Table Data
        uData = []
        uID = tDict['user']['id']
        uName = tDict['user']['name']
        uSname = tDict['user']['screen_name']
        uDescription = tDict['user']['description']
        uFcount = tDict['user']['friends_count']
        uData.append(uID)
        uData.append(uName)
        uData.append(uSname)
        uData.append(uDescription)
        uData.append(uFcount)
                      
#Tweet Table Data
        if 'retweeted_status' in tDict.keys():
            retweetcount = tDict['retweeted_status']['retweet_count']
        else:
            retweetcount = tDict['retweet_count']
        tData = []
        tCreatedat = tDict['created_at']
        tIdstr = tDict['id_str']
        tText = tDict['text']
        tSource = tDict['source']
        tInreplyID = tDict['in_reply_to_user_id']
        tInreplyName = tDict['in_reply_to_screen_name']
        tInreplysID = tDict['in_reply_to_status_id']
        tContributors = tDict['contributors']
        tUid = tDict['user']['id']
        tData.append(tCreatedat)
        tData.append(tIdstr)
        tData.append(tText)
        tData.append(tSource)
        tData.append(tInreplyID)
        tData.append(tInreplyName)
        tData.append(tInreplysID)
        tData.append(retweetcount)
        tData.append(tContributors)
        tData.append(tUid)
                       
#Geo Table Data
        if tDict['geo'] != None:
            gData = []
            gID = flag
            gType = tDict['geo']['type']
            gLongitude = tDict['geo']['coordinates'][1]
            gLatitude = tDict['geo']['coordinates'][0]
            gData.append(gID)
            gData.append(gType)
            gData.append(gLongitude)
            gData.append(gLatitude)
            c.execute("INSERT INTO Geo VALUES(?, ?, ?, ?);", gData)
            tData.append(gID)
            flag = flag + 1
        else:
            tData.append(None)
        
        c.execute("INSERT INTO Tweet VALUES(?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?);", tData)
        c.execute("INSERT INTO User VALUES(?, ?, ?, ?, ?);", uData)
    except ValueError:
        print(" ")

tRows = c.execute("SELECT COUNT(*) FROM Tweet;").fetchall()[0]
print("There are", tRows, "rows in Tweet Table.")
uRows = c.execute("SELECT COUNT(*) FROM User;").fetchall()[0]
print("There are", uRows, "rows in User Table.")
gRows = c.execute("SELECT COUNT(*) FROM Geo;").fetchall()[0]
print("There are", gRows, "rows in Geo Table.")

End1c = time.time()
RunTime1c = End1c - Start1c
#Print runtime 1c.
print("The run time is ", RunTime1c, "seconds.")

c.close()
conn.commit()
conn.close()

#Problem 1D (304-411)
#Run 1c but with batch size of 1000
def loadTweetsBatch(tLines):
    import json
    batchRows = 1000
    gBatchInput = []
    tBatchInput = []
    uBatchInput = []
    flag = 1
    while len(tLines) > 0:
        line = tLines.pop()
        try:
            tDict = json.loads(line)
            for value in tDict.values():
                if value == "null":
                    value = None
#User Table Data
            uData = []
            uID = tDict['user']['id']
            uName = tDict['user']['name']
            uSname = tDict['user']['screen_name']
            uDescription = tDict['user']['description']
            uFcount = tDict['user']['friends_count']
            uData.append(uID)
            uData.append(uName)
            uData.append(uSname)
            uData.append(uDescription)
            uData.append(uFcount)
            
#Tweet Table Data
            if 'retweeted_status' in tDict.keys():
                retweetcount = tDict['retweeted_status']['retweet_count']
            else:
                retweetcount = tDict['retweet_count']
            tData = []
            tCreatedat = tDict['created_at']
            tIdstr = tDict['id_str']
            tText = tDict['text']
            tSource = tDict['source']
            tInreplyID = tDict['in_reply_to_user_id']
            tInreplyName = tDict['in_reply_to_screen_name']
            tInreplysID = tDict['in_reply_to_status_id']
            tContributors = tDict['contributors']
            tUid = tDict['user']['id']
            tData.append(tCreatedat)
            tData.append(tIdstr)
            tData.append(tText)
            tData.append(tSource)
            tData.append(tInreplyID)
            tData.append(tInreplyName)
            tData.append(tInreplysID)
            tData.append(retweetcount)
            tData.append(tContributors)
            tData.append(tUid)
                
#Geo Table Data
            if tDict['geo'] != None:
                gData = []
                gID = flag
                gType = tDict['geo']['type']
                gLongitude = tDict['geo']['coordinates'][1]
                gLatitude = tDict['geo']['coordinates'][0]
                gData.append(gID)
                gData.append(gType)
                gData.append(gLongitude)
                gData.append(gLatitude)
                c.execute("INSERT INTO Geo VALUES(?, ?, ?, ?);", gData)
                tData.append(gID)
                flag = flag + 1
            else:
                tData.append(None)
            tBatchInput.append(tData)
            uBatchInput.append(uData)
            if len(tBatchInput) >= batchRows:
                c.executemany("INSERT INTO Geo VALUES(?, ?, ?, ?);", gBatchInput)
                gBatchInput = []
                c.executemany("INSERT INTO Tweet VALUES(?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?);", tBatchInput)
                tBatchInput = []
            if len(uBatchInput) >= batchRows:
                c.executemany("INSERT INTO User VALUES(?, ?, ?, ?, ?);", uBatchInput)
                uBatchInput = []
            if len(gBatchInput) >= batchRows:
                c.executemany("INSERT INTO Geo VALUES(?, ?, ?, ?);", gBatchInput)
                gBatchInput = []
        except ValueError:
            print(" ")
            
import time, sqlite3

conn = sqlite3.connect('JonesTweet.db')
c = conn.cursor()

response = open('JonesTweetFinal.txt', 'r')
Start1d = time.time()
loadTweetsBatch(response.readlines())

tRows = c.execute("SELECT COUNT(*) FROM Tweet;").fetchall()[0]
print("There are", tRows, "rows in Tweet Table.")
uRows = c.execute("SELECT COUNT(*) FROM User;").fetchall()[0]
print("There are", uRows, "rows in User Table.")
gRows = c.execute("SELECT COUNT(*) FROM Geo;").fetchall()[0]
print("There are", gRows, "rows in Geo Table.")

End1d = time.time()
RunTime1d = End1d - Start1d
#Print runtime for 1D runs faster due batching
print("The run time is ", RunTime1d, "seconds.")
c.close()
conn.commit()
conn.close()

#Part 1E (415-435)
#MATPLOT LIB OF A-C
import matplotlib.pyplot as plt

# Create data
g1 = (RunTime1a)
g2 = (RunTime1b)
g3 = (RunTime1c)

data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("File DL", "SQLite", "NoURLRead")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group in zip(data, colors, groups):
x, y = data
ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
plt.title('Tweets Vs. Run Times')
plt.legend(loc=2)
plt.show()


#Part 2A (440-448)
#SQL Query min long and lat by username
Start2a1 = time.time()
c.execute("SELECT u.name, min(g.longitude), min(latitude) FROM Tweet t, User u, Geo g\
           WHERE t.user_id = u.id AND t.geo_id = g.id GROUP BY u.name;")
End2a1 = time.time()
RunTime2a1 = End2a1 - Start2a1
#Runtime 4.8s
print("The run time is ", RunTime2a1, "seconds.")

#Part 2B (450-466)
#Rexecute 2A 10x and 100x doing it scale linearly?
Start2b = time.time()
for i in range(10):
    c.execute("SELECT u.name, min(g.longitude), min(latitude) FROM Tweet t, User u, Geo g\
           WHERE t.user_id = u.id AND t.geo_id = g.id GROUP BY u.name;")
End2b = time.time()
RunTime2b = End2b - Start2b
#My run time is 48.4 seconds roughly ten times that of 2A.
print("The run time is ", RunTime2b, "seconds.")

Start2b1 = time.time()
for i in range(100):
    c.execute("SELECT u.name, min(g.longitude), min(latitude) FROM Tweet t, User u, Geo g\
           WHERE t.user_id = u.id AND t.geo_id = g.id GROUP BY u.name;")
End2b1 = time.time()
RunTime2b1 = End2b1 - Start2b1
#My run time is 485.24 seconds, this run time is roughly 10x the above and 100x 2A.
print("The run time is ", RunTime2b1, "seconds.")

#2C AND 2D (470-486)
#Write SQL Query above but using Python code
BigTweetFile = open('JonesTweetFinal.txt', 'r', encoding='utf8')
flag = []
for i in range(500000):
    str_response = BigTweetFile.readline()
    tDict = json.loads(str_response)
    #sort 
#10x and 100x of file
start2d = time.time()
for i in range(10):
    #python version of sql query
end2d = time.time()
Runtime2d = end2d - start2d

start2d2 = time.time()
for i in range(100):
    #python version of sql query 100x for runtime
end2d2 = time.time()
Runtime2d2 = end2d2 - start2d2

#Part 3A (491-516)
#Export Tweet Table to a file and deal with duplicated keys
import sqlite3, time

def uniqueID():
    from string import ascii_lowercase
    from itertools import product
    for x in range(1, 6):
        for i in product(ascii_lowercase, repeat = x):
            yield"".join(i)

conn = sqlite3.connect('JonesTweet.db')
c = conn.cursor()
data = c.execute("SELECT * FROM Tweet;")
tFile = open('TweetInsert.txt', 'w', encoding = 'utf8')
for eachRow in data:
    statement = ""
    for value in eachRow:
        for s in uniqueID():
            if value == None:
                value = ""
                statement = statement + s + value
            else:
                statement = statement + s + "'" + str(value) + "'"
            statement = statement + "\n"
        with open('TweetInsert.txt', 'a'):
            tFile.write(statement)
tFile.close()

#Part 3B(520-531-518)
#Export all 3 tables 
export1 = cursor.execute('SELECT * FROM Tweet;').fetchall()
export2 = cursor2.execute('SELECT * FROM User;').fetchall()
export3 = cursor3.execute('SELECT * FROM Geo;').fetchall()
#3B i
#Adding CDM long lat to table
cursor4 = cursor.execute('SELECT *, ABS(lattitude-41.878668) + ABS(longitude-87.625555) AS relative_dist from Geo;')
#3b ii
#Add screen name column
cursor5 = cursor.execute('SELECT Tweet.*, User.name from Tweet LEFT JOIN User ON User.id = Tweet.user_id;')
#3b iii
#User table how many times are tweets in DB
cursor6 = cursor.execute('SELECT User.*, (select count(*) from Tweets where Tweets.user_id = User.id) from User;')