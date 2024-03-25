function validate(){
  var fname = document.getElementById("fname").value;
  var email = document.getElementById("email").value;
  var address = document.getElementById("feedback").value;
  var error_message = document.getElementById("error_message");
  
  error_message.style.padding = "10px";
  
  var text;
  if(fname.length < 7){
    text = "Please Enter valid Full Name";
    error_message.innerHTML = text;
    return false;
  }
  if(email.indexOf("@") == -1 || email.length < 6){
    text = "Please Enter valid Email";
    error_message.innerHTML = text;
    return false;
  }
  if(address.length <= 10){
    text = "Please Enter More Than 10 Characters";
    error_message.innerHTML = text;
    return false;
  }
  alert("Thank you for your feedback");
  return true;
}