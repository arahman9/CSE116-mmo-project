var hexcode = ""
var family = "none"
var arrayofhexes = null
var arrayofmaps = []
var gridchanged = false
var x = null
var y = null

function startgridprocess(){
    getgrid()
    setuplistener()
    setInterval(checkforchange, 100)
    setInterval(getgrid, 100)
}

function getgrid(){
    var xhttp = new XMLHttpRequest()
    xhttp.open("GET", "/grid")
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            arrayofhexes = JSON.parse(this.response)
            rendergrid()
        }
    }
    xhttp.send()
}

/*
arrayofhexs = hch.watchoutforthatgridonthefloor()
gridx = 0
gridy = 0
for row in arrayofhexs:
    for element in row:
        box = pygame.Rect(gridx * 20, gridy * 20, 20, 20)
        pygame.draw.rect(screen, pygame.Color(element), box, 0)
        gridx += 1
        gridofboxes.append(box)
    gridx = 0
    gridy += 1
    */

/*
for (var rowcount = 0; rowcount < arrayofhexes.length; rowcount++){
        var row = arrayofhexes[rowcount]
        for (var colcount = 0; colcount < row.length; colcount++){
            var canvas = document.getElementById("canvas")
            var c = canvas.getContext("2d")
            c.fillStyle = arrayofhexes[rowcount][colcount]
            c.fillRect(colcount * 20, rowcount * 20, 20, 20)
        }
    }
 */

function rendergrid(){
    for (var rowcount = 0; rowcount < arrayofhexes.length; rowcount++){
        var row = arrayofhexes[rowcount]
        for (var colcount = 0; colcount < row.length; colcount++){
            var tempboi = {
                color: arrayofhexes[rowcount][colcount],
                left: colcount * 20,
                top: rowcount * 20,
                thisx: colcount,
                thisy: rowcount
            }
            arrayofmaps.push(tempboi)
        }
    }
    var canvas = document.getElementById("canvas")
    var c = canvas.getContext("2d")
    arrayofmaps.forEach(function(boi) {
        c.fillStyle = boi.color
        c.fillRect(boi.left, boi.top, 20, 20)
    })
}

function setuplistener(){
    var canvas = document.getElementById("canvas")
    var cleft = canvas.offsetLeft
    var ctop = canvas.offsetTop
    canvas.addEventListener("click", function(event) {
        var eventx = event.pageX - cleft
        var eventy = event.pageY - ctop
        arrayofmaps.forEach(function(pixel){
            if (eventy > pixel.top && eventy < pixel.top + 20
                && eventx > pixel.left && eventx < pixel.left + 20) {
                x = pixel.thisx
                console.log(x)
                y = pixel.thisy
                console.log(y)
                gridchanged = true
            }
        })
    })
}

function checkforchange(){
    if (gridchanged) {
        sendgrid()
        gridchanged = false
    }
}

function sendgrid(){
    var xhttp = new XMLHttpRequest()
    var EGGSFORBART = hexcode.replace("#", "")
    var url = "/update?hex=" + EGGSFORBART + "&x=" + x.toString() + "&y=" + y.toString()
    console.log(url)
    xhttp.open("GET", url)
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            console.log(x + " and " + y + " just sent")
        }
        else{
            console.log("EGGS FOR BART")
        }
    }
    xhttp.send()
}

/*
def editgrid(hexcode, xy):
    notborked = hexcode.strip("#")
    x = xy[0]
    y = xy[1]
    index = math.floor(x / 20)
    indey = math.floor(y / 20)
    url = urlbase + "/update?hex=" + notborked + "&x=" + str(index) + "&y=" + str(indey)
    result = requests.get(url)
    print(result.text + " updated in grid")
 */

function hexcodebutton(){
    //get hexcode entered
    hexcode = document.getElementById("hexcode").value
    console.log(hexcode)
    //strip of #s
    var stripped = hexcode.replace("#","")
    console.log(stripped)
    //ask the server for the thing
    var xhttp = new XMLHttpRequest()
    xhttp.open("GET", "/getcode?hex=" + stripped)
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            family = this.response
            console.log("family = " + family)
            hexcodebuttoncontinued()
        }
    }
    xhttp.send()
}

function hexcodebuttoncontinued(){
    //to make sure errors can be cleaned up
    var errors = document.getElementById("errors")
    //error first, don't ask
    var error = document.createTextNode("Hexcode not found. Please try again. ")
    errors.appendChild(error)
    //check family
    if (family !== "none"){
        console.log("family !== none tripped")
        cleanupbeforegrid()
        startgridprocess()
    }
}

function colorfamily(){
    //get family entered
    family = document.getElementById("colorfamily").value
    console.log(family)
    //ask the server for the thing
    var xhttp = new XMLHttpRequest()
    xhttp.open("GET", "/javascriptexclusive?fam=" + family)
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            hexcode = "#" + this.response
            console.log("hexcode = " + hexcode)
            colorfamilycontinued()
        }
    }
    xhttp.send()
}

function colorfamilycontinued(){
    var TDA = document.getElementById("givecode")
    var instructions = document.createTextNode("Congrats, your new hex code is: " + hexcode + " . Please save this for future reference. Click the button below to continue.")
    TDA.appendChild(instructions)
    var newbutton = document.createElement("input")
    newbutton.type = "button"
    newbutton.value = "Continue"
    newbutton.id = "remove"
    newbutton.onclick = donewithnewcode
    TDA.appendChild(newbutton)

}

function donewithnewcode(){
    cleanupbeforegrid()
    cleanupbeforegrid2electricboogaloo()
    startgridprocess()
}

function cleanupbeforegrid(){
    var errors = document.getElementById("errors")
    errors.remove()
    var one = document.getElementById("1")
    var two = document.getElementById("2")
    var three = document.getElementById("3")
    var four = document.getElementById("4")
    var five = document.getElementById("5")
    var noonereadsthese = document.getElementById("6")
    one.remove()
    two.remove()
    three.remove()
    four.remove()
    five.remove()
    noonereadsthese.remove()
    var six = document.getElementById("hexcode")
    six.remove()
    six = document.getElementById("hexcodebutton")
    six.remove()
    six = document.getElementById("colorfamily")
    six.remove()
    console.log(hexcode, family)
}

function cleanupbeforegrid2electricboogaloo(){
    var temp = document.getElementById("givecode")
    temp.remove()
}

/*
function translatebar(input){
    var raw = JSON.parse(input)
    var result = {
        x: raw.names,
        y: raw.ratings,
        marker: {
            color: ['rgba(139,0,0,1)', 'rgba(139,0,0,1)', 'rgba(139,0,0,1)', 'rgba(139,0,0,1)', 'rgba(139,0,0,1)',
                'rgba(139,0,0,1)', 'rgba(139,0,0,1)', 'rgba(139,0,0,1)', 'rgba(139,0,0,1)', 'rgba(139,0,0,1)',
                'rgba(0,100,0,1)', 'rgba(0,100,0,1)', 'rgba(0,100,0,1)', 'rgba(0,100,0,1)', 'rgba(0,100,0,1)',
                'rgba(0,100,0,1)', 'rgba(0,100,0,1)', 'rgba(0,100,0,1)', 'rgba(0,100,0,1)', 'rgba(0,100,0,1)']
        },
        type: "bar"
    }
    return [result]
}

function searchforgame(){
    var sq = document.getElementById("sq").value
    var xhttp = new XMLHttpRequest()
    xhttp.open("GET", "/process2?sq=" + sq)
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            var raw = JSON.parse(this.response)
            selectgame(raw)
        }
    }
    xhttp.send()
}

function selectgame(arrayofarrays){
    var instructions = document.getElementById("bd")
    instructions.innerHTML = "Please select the game you wanted. If it's not on the list, it may not have a rating, or your query may not have been understood."
    var para = document.createElement("p")
    instructions.appendChild(para)
    for (var i = 0; i < arrayofarrays.length; i++){
        var array = arrayofarrays[i]
        var gamename = array[0]
        var gamerating = array[1]
        var element = document.createElement("input")
        element.type = "button"
        element.value = gamename
        element.id = gamerating
        element.onclick = function(){
            var name = this.value
            var rating = this.id
            makepiechart(name, rating)
            displayvideo(name)
        }
        para.appendChild(element)
        var para = document.createElement("p")
        instructions.appendChild(para)
    }
}

function displayvideo(gamename){
    var xhttp = new XMLHttpRequest()
    xhttp.open("GET", "/process3?gamename=" + gamename)
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            var raw = JSON.parse(this.response)
            actuallydisplay(raw)
        }
    }
    xhttp.send()
    var instructions = document.getElementById("plzreload")
    instructions.innerHTML = "Youtube video should appear soon..."
}

function actuallydisplay(array){
    var instructions = document.getElementById("youtuber")
    var embedurl = array[0]
    var youtuber = array[1]
    var youtubething = document.getElementsByTagName("iframe")[0]
    youtubething.src = "https://www.youtube.com/embed/" + embedurl
    instructions.innerHTML = "FEATURED YOUTUBER: " + youtuber
}

function makepiechart(name, rating){
    rating = parseFloat(rating)
    restofpie = 100 - rating
    var data = [{
        values: [rating, restofpie],
        labels: [name, ""],
        hoverinfo: 'none',
        textinfo: 'none',
        hole: .9,
        type: "pie",
        marker: {colors: ["rgb(0,0,0)", "rgb(255,255,255)"]}
    }]
    var layout = {
        height: 400,
        width: 500,
        title: "Game Rating: " + rating,
        showlegend: false
    }
    Plotly.newPlot("piechart", data, layout)
}

function onload(){
    var layout = {
        margin: {
            b: 200
        }
    }
    var xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            var data = translatebar(this.response)
            Plotly.newPlot("bargraph", data, layout)
        }
    }
    xhttp.open("GET", "/process")
    xhttp.send()
}
 */