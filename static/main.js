
function postImage() {
    var fd = new FormData();
    var name = $('#name').val();
    var images = $('#image')[0].files;

    if (images.length > 0){
        fd.append("name", name);
        fd.append("image", images[0]);
        $.ajax(
            {
                url: "/ovision/negative_image/",
                type: "POST",
                data: fd,
                processData: false,
                contentData: false,
                success: function(response) {
                    if(response != 0){
                        console.log(response);
                    }
                    else {
                        console.log("file not upload")
                    }
                }
            }
        );
    }else{console.log("select file");}
}
