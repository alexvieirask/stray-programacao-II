$(function () {
  let ENDERECO_IP = sessionStorage.getItem("IP")

  $("#input_username").val("alex.vieira"),
    $("#input_password").val("my-password"),
    /* Validação de Formulário através do Jquery validate */
    $("#form-login").validate({
      rules: {
        username: {
          required: true,
          rangelength: [4, 30],
        },
        password: {
          required: true,
          minlength: 8,
        },
      },
      submitHandler: onSubmit,
    });

  function onSubmit() {
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
        window.location = "/";
      } else {
        alert(`Invalid login ${response.details}`);
      }
    }

    function onError(response) {
      console.log("Error, verify backend", response);
    }
  }
});
