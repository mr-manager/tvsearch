import os
from bottle import (get, post, redirect, request, route, run, static_file, error,
                    template)
import utils

# Static Routes

# @error(404)
# def page_not_found(error):
#     return static_file('404.tpl', root='./templates')

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
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

if __name__ == "__main__":
    run(host='0.0.0.0', port=os.environ.get('PORT', 5000))


