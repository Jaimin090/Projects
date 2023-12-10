const helloButton = document.getElementById("hello-button");
helloButton.addEventListener("click", changeMessage)
// Add an event listener to call changeMessage() when button isclicked
function changeMessage() {
    const NewButton = document.getElementById("message");
    NewButton.innerHTML = "I am a SAIT Student";
    NewButton.style.backgroundColor = "red"
    NewButton.style.color = "green"
// Add code to get the element with id = "message" and change its
// innerHTML attribute value to "Hello, JavaScript!"
}