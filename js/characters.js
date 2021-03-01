randomChar = Math.floor(Math.random()*2+1);

function myFunction() {
  if (randomChar == 1) {
    document.getElementById("Nama").style.display = "inline";
    document.getElementById("All Might").style.display = "none";
  }
  else {
    document.getElementById("Nama").style.display = "none";
    document.getElementById("All Might").style.display = "inline";
  }
}
