import bottle
import translator

from bottle import route, run, static_file, request


@route("/")
def index():
    return static_file("index.html", root="")


@route("/main.js")
def main():
    return static_file("main.js", root="")


@route("/grid")
def grid():
    return translator.csvtoarray()


@route("/getcode")
def code1():
    print("asked for code")
    hex = request.query["hex"]
    return translator.txttocode(hex)
    print("code given")


@route("/givecode")
def code2():
    hex = request.query["hex"]
    fam = request.query["fam"]
    return translator.writecode(hex, fam)


@route("/update")
def update():
    hex = request.query["hex"]
    x = request.query["x"]
    y = request.query["y"]
    return translator.updategrid(hex, x, y)


@route("/javascriptexclusive")
def code3():
    fam = request.query["fam"]
    return translator.getcolorforjavascript(fam)


"""
@route("/process2")
def processing2():
    sq = request.query["sq"]
    return process2.dotheneedful(sq)

@route("/process3")
def processing3():
    q = request.query["gamename"]
    return process3.gib(q)
"""

run(host='0.0.0.0', port=8080, debug=True)