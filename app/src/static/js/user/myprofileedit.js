$(function () {
    const JWT = sessionStorage.getItem("JWT");
    const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");

    function redirectToLogin() {
        window.location = "/login";
    }

    if (JWT) {
        $(".form-container").show()


        $.ajax({
            url: `http://${ENDERECO_IP}:5000/user/info`,
            method: "GET",
            dataType: "json",
            contentType: "application/json",
            headers: { Authorization: "Bearer " + JWT },
            error: () => { alert("Error reading data, verify backend"); },
            success: function (data) {
                const USER = data.details

                const NAME = USER.name
                const USERNAME = USER.username
                const EMAIL = USER.email
                const DESCRIPTION = USER.description
                const PROFILE_SRC = USER.profile_picture

                $("#input_name").val(NAME)
                $("#input_username").val(USERNAME)
                $("#input_email").val(EMAIL)
                $("#input_description").val(DESCRIPTION)
                $(".img-preview").attr("src", PROFILE_SRC)


                $("#input-picture-profile").on("change", function (event) {
                    $("#span-warning-profile-picture").remove()
                    var file = event.target.files[0]

                    if (file) {
                        const reader = new FileReader()

                        reader.addEventListener("load", (event) => {
                            const readerTarget = event.target
                            const img = readerTarget.result

                            $(".img-preview").attr("src", img)
                        })

                        reader.readAsDataURL(file)
                    }
                })

                $("#button-submit").on("click", function (event) {
                    event.preventDefault()

                    const formData = JSON.stringify({
                        name: $("#input_name").val().trim(),
                        username: $("#input_username").val().trim(),
                        email: $("#input_email").val().trim(),
                        description: $("#input_description").val().trim(),
                    });

                    $.ajax({
                        url: `http://${ENDERECO_IP}:5000/user/update`,
                        type: "POST",
                        dataType: "json",
                        headers: { Authorization: "Bearer " + JWT },
                        contentType: "application/json",
                        data: formData,
                        error: function (data) { console.log(data) },
                        success: function (data) {
                            var response = data
                            $(".span-error").remove()

                            if (response.result == "error"){

                                let EXCEPTIONS = response.details
                                
            
                                for (index in EXCEPTIONS){
                                    if(EXCEPTIONS[index].type == "input_field"){
                                        var errorInput = EXCEPTIONS[index].details.split(" ")[1]
                                        var spanError = $("<span>").addClass("span-error").text(EXCEPTIONS[index].details.replace(errorInput, "Field"))  
                                        var insert_message = $(errorInput).parent()
                                        insert_message.append(spanError)
                                    }

                                    
                                    if (EXCEPTIONS[index].type == "username_exists"){
                                        var spanError = $("<span>").addClass("span-error").text(EXCEPTIONS[index].description)
                                        var insert_message = $("#input_username").parent()
                                        insert_message.append(spanError)
                                    }


                               

        
                                   
                                }


                            }
                            else{
                                alert("user editado")
                            }
    
                                var archive_photo = new FormData($("#form-new-user")[0])

                                $.ajax({
                                    url: `http://${ENDERECO_IP}:5000/save_image_profile_user`,
                                    method: 'POST',
                                    headers: { Authorization: "Bearer " + JWT },
                                    data: archive_photo,
                                    contentType: false,
                                    cache: false,
                                    processData: false,
                                    success: function (data) { console.log(data) },
                                    error: function (data) { console.log(data) }
                                })
                            
                           
                        },

                    });
                
                    if (USER.username != $("#input_username").val()) {
                        alert("Username changed! Login again!")
                        sessionStorage.removeItem("JWT")
                        redirectToLogin()
                    }
                    
                
                })
            }
        })



    } else {
        redirectToLogin()
    }


})