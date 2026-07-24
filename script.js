function showTournament(){

fetch("tournament.json")
.then(response => response.json())
.then(data => {

document.getElementById("game").innerHTML =
"🎮 Game: " + data.game;

document.getElementById("entry").innerHTML =
"💰 Entry Fee: ₹" + data.entry;

document.getElementById("kill").innerHTML =
"🎯 Per Kill: ₹" + data.kill;

});

}}
