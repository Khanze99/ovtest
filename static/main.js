

let response = fetch("ovision/get_last_images")
    .then((result) => {return result.json();})
    .then((data) => {
        let htmlData = '';
        for (let i = 0; i < data.images.length; i++){
            htmlData += "<img src='"+data.images[i].image+"' style='white-space: pre-line'>"+"<img src='"+data.images[i].negative_image+"' style='white-space: pre-line'>"
        }
        return document.getElementById("images").innerHTML = htmlData;
    });


const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
    reader.onerror = error => reject(error);
});


function postImage() {
    let fd = new FormData();
    let name = $("#name").val();
    let image = $("#image")[0].files[0];
    const reader = new FileReader();
    reader.onloadend = () => {
        // console.log(reader.result);                   ---------------------- 1
    };
    reader.readAsDataURL(image)
    // console.log(reader.result)                         ---------------------- 2
    fd.append("name", name);
    fd.append("image", reader.result);
    fetch("ovision/negative_image/", {method: "POST", body: fd})
        .then(res => res.json())
        .then(data => {console.log(data);});
}