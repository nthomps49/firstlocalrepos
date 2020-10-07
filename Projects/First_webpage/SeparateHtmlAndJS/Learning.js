// JavaScript source code
function runMe() {
    var un = document.getElementById("name").value;
    var pw = document.getElementById("pass").value;
    alert("Username: " + un + " Password: " + pw + "\nHAHA I GOT YOUR PASSWORD NOW!!");
}

name = prompt("Please enter your name");
alert("Welcome to Chip Diesel's website, " + name + "!");

let output = confirm("Confirmation message: \nReady to move to the next demo?");

if (output) {
    console.log("You pressed OK");
}
else {
    console.log("You pressed cancel");
}


//Enter your Gmail ID: <input id="name" type="text" />
//Enter your password: <input id="pass" type="password" />
//<input type="button" value="Submit" onclick="runMe(this)"/>