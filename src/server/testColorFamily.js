function testColorFam(fam){
    var xhttp = new XMLHttpRequest()
    xhttp.open("GET", "/javascriptexclusive?fam=" + fam)
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            hexcode = "#" + this.response
            console.log("hexcode = " + hexcode)
            return hexcode
        }
    }
    xhttp.send()
}

function test() {
    if (testColorFam("monochrome") == "#0f0f0f") {
        return true
    }
    else if(testColorFam("purple") in ['#b98bd3', '#ac5ed1', '#a786d6']){
        return true
    }
    return false
}
console.log(test())