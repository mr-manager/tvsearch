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
    return shows


def displayShow(show):
    return json.loads(getJsonFromFile(show))


def displayEpisode(showid, episodeid):
    show_data = json.loads(getJsonFromFile(showid))
    for episode in show_data['_embedded']['episodes']:
        if episode['id'] == int(episodeid):
            return episode


def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


def getEpisodes():
    # episodes = []
    shows = getShows()
    for show in shows:
        # foor loop prints a list of dictionaries of episodes
        print("in for loop")
        print((show['_embedded']['episodes']))
    #     get shows function prints only one list of dictionaries ((black mirror only)) -
    #     here I actually need to print each one in the for loop into a list - issue then
    # is how to access the keys in the dictionaries in the list.
    print('getshowsfunction:')
    print(show['_embedded']['episodes'])
    # print(type(episodes))
    return show['_embedded']['episodes']


# this get names function literally doe sthe same as the query function except prints directly into a list
def getNames():
    names = []
    episodes = getEpisodes()
    for episode in episodes:
        names.append(episode['name'])
    # print(type(names))
    print('names:')
    print(names)
    return names


def searchResults(query):
    episodes = getNames()
    for name in episodes:
        # if statement is incorrect
        if name is query:
            print(query)
        #query prints single episodes for each (loops)
        print('query:')
        print(query)
        print(name)
    #     episodes: prints list of black mirror episodes
    print('episodes:')
    print(episodes)
    print(type(episodes))
    return episodes



