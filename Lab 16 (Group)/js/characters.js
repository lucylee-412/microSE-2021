var img = [{
   src: "https://pbs.twimg.com/media/ELsWmr0XYAAfegy?format=jpg&name=large"
}, {
   src: "https://i.pinimg.com/736x/ef/af/f0/efaff033659ec8769a5b5b680bc7dba2.jpg"
}];

function myFunction()
  randomChar = Math.floor(Math.random()*img.length);
  document.getElementById("imgDisplay").innerHTML = img[randomChar];
};
