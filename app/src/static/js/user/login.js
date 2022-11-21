$(function () {
  const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");
  const JWT = sessionStorage.getItem("JWT");

    if (JWT) {
      alert("user is already logged in");
      redirectToHome();
    } 
    else {
      $(".form-container").show();
      $("#input_username").val("alex.vieira")
      $("#input_password").val("my-password")
      
      function onSubmit(event) {
        event.preventDefault()

          formData = JSON.stringify({
            username: $("#input_username").val(),
            password: $("#input_password").val(),
          });

          $.ajax({
            url: `http://${ENDERECO_IP}:5000/login/auth`,
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            data: formData,
            success: onSuccess,
            error: onError,
          });

          function onSuccess(response) {
            if (response.result == "ok") {
              sessionStorage.setItem("JWT", response.details);
              sessionStorage.setItem("username", $("#input_username").val());
              redirectToHome();
            } else {
              alert(`Invalid login ${response.details}`);
            }
          }

          function onError(response) {
            console.log("Error, verify backend", response);
          }
      };
      
      function togglePassword() {
    

        var input = $("#input_password");
        var icon = $("#button-password-show");

        if (input.attr("type") == "password") {
          input.attr("type", "text");
          icon.attr("src", "/static/img/fixed/button-eye-show.png");
        } else {
          input.attr("type", "password");
          icon.attr("src", "/static/img/fixed/button-eye-hide.png");
        }
      }

      $(".default-button-submit").on("click",onSubmit)
      $("#button-password-show").on("click", togglePassword);
    
    }

    function redirectToHome() {
      window.location = "/";
    }
});
