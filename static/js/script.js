// Set a timeout to execute the alert messages
window.setTimeout(function () {
  const alert = document.querySelector('.alert');
  if (alert) {
    alert.classList.remove('show');
    // Add the 'fade' class to the alert element to start the fade-out effect
    alert.classList.add('fade');
    alert.addEventListener('transitionend', () => {
      alert.remove();
    });
  }
}, 7000); // 7000 milliseconds = 7 seconds

// Function to preview the image selected by the user
function previewImage(event) {
  const output = document.getElementById('preview-image');
  const placeholderText = document.querySelector('.placeholder-text');
  if (event.target.files && event.target.files[0]) {
    output.src = URL.createObjectURL(event.target.files[0]);
    output.classList.remove('upload-icon');
    placeholderText.style.display = 'none';
  }
}
