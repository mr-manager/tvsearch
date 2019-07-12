from bottle import template
import json


JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871","2993", "305"]


def getVersion():
    return "0.0.1"


def getShows():
    shows = []
    for show in AVAILABE_SHOWS:
        shows.append(json.loads(getJsonFromFile(show)))
    return shows


def displayShow(show):
    return json.loads(getJsonFromFile(show))


def displayEp(showname, episodenum):
    show_data = json.loads(getJsonFromFile(showname))
    for episode in show_data['_embedded']['episodes']:
        if episode['id'] == int(episodenum):
            return episode


def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


def searchResults(query):
    search_result = []
    shows = getShows()
    for show in shows:
        episodes = show['_embedded']['episodes']
        for episode in episodes:
            if query in episode['name']:
                result_info = {
                    'showid': show['id'],
                    'episodeid': episode['id'],
                    'text': show['name'] + ": " + episode['name']
                }
                search_result.append(result_info)
            elif query in str(episode['summary']):
                search_result.append(result_info)
    print(search_result)
    return search_result

