function Hallo(P1){

    document.getElementById("First").innerHTML+=1   
}
var ctx = document.getElementById("con").getContext("2d");

ctx.beginPath();
ctx.arc(95, 50, 40, 0, 2 * Math.PI);
ctx.stroke();
