var a, b, c, y, x1, x2;
a = 1; b = 2; c = 2;

x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);

document.getElementById("quadForm").innerHTML = "The discriminant found by the quadratic formula is " + x1 + " or " + x2 + ".";
