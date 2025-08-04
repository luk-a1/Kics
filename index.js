/*
const uploadButton = document.getElementById("uploadButton");
const ErrorMsgP = document.getElementById("ErrorP");
const fileInput = document.getElementById("fileInput");
const Form = document.getElementById("UploadForm");

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];

    ErrorMsgP.textContent = '';

    //const fileExtension = fileName.split('.').pop().toLowerCase();

    if (file) {
        const fileName = file.name.toLowerCase();
        if (!fileName.endsWith('.tgz') || !fileName.endsWith('.tf')) {
            ErrorMsgP.textContent = 'Error: Please upload a .tgz file.';
            ErrorMsgP.style.color = 'red';
            fileInput.value = '';
        }
      }
});
*/