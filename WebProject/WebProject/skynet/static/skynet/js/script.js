//var abc = 123;
//
//if (abc>0) {alert(321);}
var hidden = false;
var time = 0;



var t = 0;
var st = 1;
var imgb = document.createElement('img');

imgb.alt = 'лиса с сигарой';
imgb.addEventListener("click", add_img);
imgb.src = '/static/skynet/images/123.jpg';
imgb.height = 120;
imgb.width = 120;


function add_img() {
    footer = document.getElementById('abc');
    console.log(footer);
    footer.appendChild(imgb);

    imgb.src = '/static/skynet/images/skynet.jpg';
};

function testt() {

    if (hidden) {
        document.getElementById("image_test").style.visibility="visible";
        hidden = false;
    }
    else{
        document.getElementById("image_test").style.visibility="hidden";
        hidden = true;
    }
    //alert(document.getElementById("image_test").style.visibility);
    console.log(document.getElementById("image_test").style.visibility)
};

function timer() {
    document.getElementById("image_test").style.visibility="hidden";
//    setTimeOut(document.getElementById("inp").value*1000);
    setTimeout(() => {
        console.log("time out");
        document.getElementById("image_test").style.visibility="visible";
    }, document.getElementById("inp").value*1000);



};

function theme() {
    if (cur_theme == "red") {
        cur_theme = "green";
        document.body.style.background = "#00FA9A";


    } else {
        cur_theme = "red";
        document.body.style.background = "#F08080";
    }
};