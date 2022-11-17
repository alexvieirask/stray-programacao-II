$(function () {
  let ENDERECO_IP = sessionStorage.getItem("IP")
  /* Validação de Formulário através do Jquery validate */
  $("#form-new-user").validate({
    rules: {
      name: {
        required: true,
        minlength: 4,
      },
      username: {
        required: true,
        rangelength: [4, 30],
      },
      email: {
        required: true,
        email: true,
      },
      password: {
        required: true,
        minlength: 8,
      },
      passwordconfirm: {
        required: true,
        equalTo: "#input_password",
      },
    },
    submitHandler: onSubmit,
  });

  function onSubmit() {
    var IP = sessionStorage.getItem("ip") 
    formData = JSON.stringify({
      name: $("#input_name").val(),
      username: $("#input_username").val(),
      email: $("#input_username").val(),
      password: $("#input_password").val(),
    });

    $.ajax({
<<<<<<< HEAD
      url: `http://${ENDERECO_IP}:5000/join/auth`,
=======
      url: `http://${IP}:5000/join/auth`,
>>>>>>> 4f7a116a59740adc2432efc999b5d8e2aac9bcf1
      type: "POST",
      dataType: "json",
      contentType: "application/json",
      data: formData,
      success: onSuccess,
      error: onError,
    });

    function onSuccess(response) {
      $("#form-new-user").each(function () {
        this.reset();
      });
    }

    function onError(response) {
      console.log("Error, verify backend", response);
    }
  }
});
