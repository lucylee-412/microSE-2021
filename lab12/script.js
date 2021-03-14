// Quadratic Formula
var x1, x2, discriminant;

let a = prompt("Enter the first number: ");
let b = prompt("Enter the second number: ");
let c = prompt("Enter the third number: ");

discriminant = b ** 2 - 4 * a * c;

if (discriminant > 0) {
  x1 = (-b + Math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);
  x2 = (-b - Math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);

  console.log("Roots: " + x1 + ", " + x2);
}
else if (discriminant == 0) {
  x1 = x2 = -b / (2 * a);

  console.log("Root: " + x1 + ", " + x2);
}
else {
  console.log("Roots are imaginary.");
}

document.getElementById("quadForm").innerHTML = "The roots found by the quadratic formula are " + x1 + " or " + x2 + ".";
