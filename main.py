import os
from bottle import (get, post, redirect, request, route, run, static_file, error,
                    template)
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
    query = request.forms.get('q')
    sectionTemplate = "./templates/search_result.tpl"
    sectionData = utils.searchResults(query)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)

# something tarek showed me but its not efficient at all.
# @route('/search', method="post")
# def test():
#
#     name_search = request.forms.get("q")
#     string_search=  (str.split(name_search))
#     display_shows = [json.loads(utils.getJsonFromFile(someshows)) for someshows in utils.AVAILABE_SHOWS]
#     m = display_shows[0]
#     y = m["name"]
#     k=m["summary"]
#     x=[m]
#     t=x[0]['_embedded']['episodes'][0]
#     print(t)
#
#     string_search2 = (str.split(y))
#     string_search3 = (str.split(k))
#     for r in string_search:
#
#         for k in string_search2  :
#             if r == k:
#                 print(r)
#                 print(k)
#                 return "hey"


if __name__ == "__main__":
    run(host='localhost', port=os.environ.get('PORT', 5000), reloader=True)



