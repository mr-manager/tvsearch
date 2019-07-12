from bottle import template, request
import json


JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871","2993", "305"]


def getVersion():
    return "0.0.1"


def getShows():
    shows = []
    for show in AVAILABE_SHOWS:
        shows.append(json.loads(getJsonFromFile(show)))
    # print(type(shows))
    return shows


def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


def searchResults(query):
    episodes = getNames()
    for name in episodes:
        if name is query:
            print(query)
        print('query:')
        print(query)
        print(name)
    print('episodes:')
    print(episodes)
    print(type(episodes))
    return episodes


def getEpisodes():
    # episodes = []
    shows = getShows()
    for show in shows:
        print((show['_embedded']['episodes']))
    print('getshowsfunction:')
    print(show['_embedded']['episodes'])
    # print(type(episodes))
    return show['_embedded']['episodes']


def getNames():
    names = []
    episodes = getEpisodes()
    for episode in episodes:
        names.append(episode['name'])
    # print(type(names))
    return names


searchResults("White Bear")

