import os
from bottle import (get, post, request, route, run, static_file, error, template)
import utils


@error(404)
def error(error):
    error_template = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=error_template, sectionData={})


@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")


@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    sectionData = utils.getShows()
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


@route('/ajax/show/<showname>')
def display_show(showname):
    sectionData = utils.displayShow(showname)
    return template("./templates/show.tpl", result=sectionData)


@route('/show/<showname>')
def display_show(showname):
    sectionTemplate = "./templates/show.tpl"
    sectionData = utils.displayShow(showname)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@post('/search')
def search_shows():
    q = request.POST.get("q")
    search_results = utils.searchResults(q)
    sectionTemplate = "./templates/search_result.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={}, results=search_results, query=q)


@route('/show/<showname>/episode/<episodenum>')
def display_episode(showname, episodenum):
    sectionTemplate = "./templates/episode.tpl"
    sectionData = utils.displayEp(showname, episodenum)
    if sectionData == 'error':
        return error(error)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={sectionData})


@route('/ajax/show/<showname>/episode/<episodenum>')
def display_episode(showname, episodenum):
    sectionData = utils.displayEp(showname, episodenum)
    if sectionData == 'error':
        return error(error)
    return template("./templates/episode.tpl", result=sectionData)


if __name__ == "__main__":
    run(host='localhost', port=os.environ.get('PORT', 5000), reloader=True)



