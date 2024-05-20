window.setTimeout(function () {
  const alert = document.querySelector(".alert");
  if (alert) {
    alert.classList.remove("show");
    alert.classList.add("fade");
    alert.addEventListener("transitionend", () => alert.remove());
  }
}, 5000); // 5 seconds
