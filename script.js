let tournament = {
    game: "Free Fire",
    entry: "10",
    kill: "5"
};

function showTournament(){

document.getElementById("game").innerHTML =
tournament.game;

document.getElementById("entry").innerHTML =
"Entry Fee: ₹" + tournament.entry;

document.getElementById("kill").innerHTML =
"Per Kill: ₹" + tournament.kill;

}
