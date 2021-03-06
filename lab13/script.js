var birthYear, future;


x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);

function validateForm() {
  var x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Fields for birth year and current age must be filled out.");
    return false;
  }
}

document.getElementById("quadForm").innerHTML = "The discriminant found by the quadratic formula is " + x1 + " or " + x2 + ".";
