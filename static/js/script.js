// Set a timeout to execute the alert messages
window.setTimeout(function () {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach((alert) => {
    alert.classList.remove('show');
    alert.classList.add('fade');

    // Remove the alert after the fade transition ends
    alert.addEventListener('transitionend', () => {
      if (alert.classList.contains('fade')) {
        alert.remove();
      }
    });
  });
}, 7000);

// Function to preview the image selected by the user
function previewImage(event) {
  const file = event.target.files[0];

  if (file && file.type.startsWith('image/')) {
    const reader = new FileReader();

    reader.onload = function (e) {
      const imageWrapper = document.querySelector('.image-wrapper');
      let output = imageWrapper.querySelector('img');

      // Create an img element if not already present
      if (!output) {
        output = document.createElement('img');
        output.classList.add('img-fluid');
        imageWrapper.appendChild(output);
      }

      // Set the src of the img element to the uploaded image's data URL
      output.src = e.target.result;
    };

    reader.readAsDataURL(file);
  } else {
    console.error('The selected file is not a valid image.');
  }
}
