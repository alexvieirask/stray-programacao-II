$(function () {
  const JWT = sessionStorage.getItem("JWT");
  const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");

  if (JWT) {
    __default_verification__();

    function redirectToLogin() {
      window.location = "/login";
    }

    function __default_verification__() {
      $.ajax({
        url: `http://${ENDERECO_IP}:5000/user/info`,
        method: "GET",
        dataType: "json",
        contentType: "application/json",
        success: userIsAdminOrNot,
        headers: { Authorization: "Bearer " + JWT },
        error: () => {
          alert("Error reading data, verify backend");
        },
      });

      function userIsAdminOrNot(data) {
        const USER = data.details;

        if (USER.is_admin) {
          $(".form-container-game").show();
          $("#button-submit").on("click", onSubmit);

          function onSubmit(event) {
            const date = new Date();
            var form = new FormData($("#form-game")[0]);

            event.preventDefault();
            const formDataObject = {
              title: $("#input_title").val(),
              description: $("#input_description").val(),
              categorie: $("#input_categorie").val(),
              price: $("#input_price").val() * 100 ,
              required_age: $("#input_requiredAge").val(),
              developer: $("#input_developer").val(),
              launch_date: date.getUTCDate(),
            };

            const formData = JSON.stringify(formDataObject);

            $(".span-error").remove();
            for (index in formDataObject) {
              var field = formDataObject[index].toString().trim();
   

              if (!field) {
                var erros = true;
                var span = $("<span>")
                  .addClass("span-error")
                  .text("This field is empty")
                  .attr("id", "span-exception");
                var EXCEPTION = $(`#input_${index}`).parent();

                EXCEPTION.append(span);
              }
            }

            var SCREENSHOTS =
              document.getElementById("input_screenshots").files;
            var QUANTITY_SCREENSHOTS = SCREENSHOTS.length;

            if (QUANTITY_SCREENSHOTS > 3) {
              var erros = true;
              var EXCEPTION = $(`#input_screenshots`).parent();
              var span = $("<span>")
                .addClass("span-error")
                .text("Max screenshots is 3.")
                .attr("id", "span-exception");

              EXCEPTION.append(span);
            }

            var screenshots_name = [];

            for (let index in SCREENSHOTS) {
              screenshots_name.push(SCREENSHOTS[index].name);
            }

            screenshots_name = screenshots_name.slice(
              0,
              screenshots_name.length - 2
            );
            var allExtensions = [];
            screenshots_name.forEach((element) => {
              var nameLength = element.split(".").length;
              allExtensions.push(
                element.split(".")[nameLength - 1].toUpperCase()
              );
            });

            var extension_error = allExtensions.filter(
              (element) =>
                element !== "PNG" && element !== "JPG" && element !== "JPEG"
            );

            if (extension_error.length != 0) {
              $("#span-exception-screenshots").remove();
              var EXCEPTION = $(`#input_screenshots`).parent();
              var span = $("<span>")
                .addClass("span-error")
                .text("Invalid Archives Format.")
                .attr("id", "span-exception-screenshots");

              EXCEPTION.append(span);
            }

            if (!erros && extension_error.length == 0) {
              $.ajax({
                url: `http://${ENDERECO_IP}:5000/game/include`,
                type: "POST",
                dataType: "json",
                headers: { Authorization: "Bearer " + JWT },
                contentType: "application/json",
                data: formData,
                error: function (data) {
                  console.log(data);
                },
                success: function (data) {
                  $.ajax({
                    url: `http://${ENDERECO_IP}:5000/save_image_game/${data.details.id}`,
                    method: "POST",
                    headers: { Authorization: "Bearer " + JWT },
                    data: form,
                    contentType: false,
                    cache: false,
                    processData: false,
                    success: function (data) {
                      console.log(data);
                    },
                    error: function (data) {
                      console.log(data);
                    },
                  });
                },
              });
            }
          }
        } else {
          redirectToLogin();
        }
      }
    }
  }
});
