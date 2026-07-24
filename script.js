fetch("tournament.json")
.then(res => res.json())
.then(data => {

document.getElementById("tname").innerHTML = data.name;
document.getElementById("entry").innerHTML = "Entry Fee: ₹" + data.entry;
document.getElementById("kill").innerHTML = "Per Kill: ₹" + data.kill;
document.getElementById("prize").innerHTML = "Prize Pool: ₹" + data.prize;
document.getElementById("slots").innerHTML = "Slots: " + data.slots;

});
