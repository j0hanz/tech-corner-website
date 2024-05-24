// Set a timeout to execute the alert messages
window.setTimeout(function () {
  const alert = document.querySelector(".alert");
  if (alert) {
    // Remove the 'show' class from the alert element
    alert.classList.remove("show");
    // Add the 'fade' class to the alert element to start the fade-out effect
    alert.classList.add("fade");
    alert.addEventListener("transitionend", () => {
      // Remove the alert element from the DOM after the fade-out transition ends
      alert.remove();
    });
  }
}, 7000); // 7000 milliseconds = 7 seconds
