var col = document.getElementById("color")
var element = document.getElementById("el")

function change() {
    console.log(document.getElementById("el").style.background)
    document.getElementById("el").style.background = document.getElementById("color").value
}

function floor() {
    document.getElementById("el").style.top(100)
}