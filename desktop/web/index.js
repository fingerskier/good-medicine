async function greet() {
  const name = document.getElementById("nameInput").value;
  const greeting = await eel.greet(name)();
  document.getElementById("output").innerText = greeting;
}