var x = 0
function btn_click() {
    if (x == 0) {
        document.getElementById("image_test").style.visibility="hidden";
//        document.getElementById("image_test").style.display="none";
        x = 1;
    } else {
        document.getElementById("image_test").style.visibility="visible";
//        document.getElementById("image_test").style.display="";
        x = 0;
    }
}


//адаптивное меню
function myFunction() {
    var x = document.getElementById("myMenu");
    if (x.className === "mainmenu") {
        x.className += " responsive";
    } else {
        x.className = "mainmenu";
    }
}