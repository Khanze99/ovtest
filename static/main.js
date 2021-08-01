

let response = fetch("ovision/get_last_images")
    .then((result) => {return result.json();})
    .then((data) => {
        console.log(data);
        let htmlData = '';
        for (let i = 0; i < data.images.length; i++){
            htmlData += "<img src='"+data.images[i].image+"' style='white-space: pre-line'>"+"<img src='"+data.images[i].negative_image+"' style='white-space: pre-line'>"
        }
        return document.getElementById("images").innerHTML = htmlData;
    });
