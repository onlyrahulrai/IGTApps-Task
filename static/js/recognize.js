const video = document.getElementById("video");
const form = document.getElementById("form");
const canvas = document.getElementById("canvas");
const imageField = document.getElementById("self_image")
const captureAnotherImage = document.getElementById("capture-btn");

document.addEventListener("DOMContentLoaded", async () => {
  await navigator.mediaDevices
    .getUserMedia({ video: true, audio: false })
    .then((stream) => {
      video.srcObject = stream;
    })
    .catch((error) => console.log(" --- Error --- "));
});

video.addEventListener("play",async () => {
    canvas
        .getContext("2d")
        .drawImage(video, 0, 0, canvas.width, canvas.height);
    let image = canvas.toDataURL("image/jpeg");

    const response = await fetch(image);
  // here image is url/location of image
    const blob = await response.blob();

    const file = new File([blob], 'image.jpg', {type: blob.type});
    let container = new DataTransfer(); 
    container.items.add(file);

    imageField.files = container.files;
})

