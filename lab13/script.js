var birthYear, future;

function validateForm() {
  var x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Fields for birth year and current age must be filled out.");
    return false;
  }
}
