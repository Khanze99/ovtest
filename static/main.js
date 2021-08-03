const imageObjects = [];

const clearFileList = () => {
    const elt = document.getElementById('images');
    elt.innerHTML = '';
    imageObjects.length = 0;
};

const postImage = () => {
    const elt = document.getElementById('image');
    const format = elt.value.split('.')[1];
    const prefix = `data:image/${format};base64,`
    const name = document.getElementById('name').value;
    if (elt.files.length === 0) {
        alert('No file selected!');
        return;
    }

    const reader = new FileReader();
    reader.onloadend = async () => {
        const array = new Uint8Array(reader.result);
        const data = await Base64.fromUint8Array(array);
        elt.files[0];
        const resp = await fetch('/ovision/negative_image', {
            method: 'POST',
            headers: {
                'content-type': 'application/json',
            },
            body: JSON.stringify({
                name: name,
                image: prefix + data
            }),
        });
        const json = resp.json();
    }
    reader.readAsArrayBuffer(elt.files[0]);
}

const addFileToList = (obj, prepend) => {
    if (imageObjects.find(x => x.id === obj.id)){
        return;
    }
    const elt = document.getElementById('images');

    const tr = document.createElement('tr');
    const origData = obj.image;
    const negData = obj.negative_image;
    const name = obj.name

    tr.innerHTML = `
        <td>${name}</td>
        <td><img src="${origData}"</td>
        <td><img src="${negData}"</td>`;

    if (prepend) {
        imageObjects.unshift(obj);
    }else {
        elt.appendChild(tr);
        imageObjects.push(obj);
    }
};

const loadLastImages = async () => {
    const response = await fetch("ovision/get_last_images");
    const json = await response.json();
    if (response.status !== 200){
        return;
    }
    clearFileList();
    for (const image  of json.images) {
        addFileToList(image);
    }
};

window.onload = () => {
    loadLastImages();
}
