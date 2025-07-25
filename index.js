console.log(document.getElementById("uB"));
console.log(document.getElementById("er"));

const uploadButton =document.getElementById("uB");
const ErrorMsgP = document.getElementById("er");

uploadButton.addEventListener("onclick", upload);

function upload(){
    const file = document.getElementById("fileInputs");
    const file_type = file.value.substring(file.lastIndexOf('.')+1, file.length) || file;

    if(file_type != "tgz"){
        ErrorMsgP.innerHTML = "You can only upload .tgz file";
    }
}