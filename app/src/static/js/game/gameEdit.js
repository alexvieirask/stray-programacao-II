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
        $(".form-container-game").show();
        if (USER.is_admin) {
          $(".form-container-game").show();
          
          const URL = document.URL.split("/")
          const GAME_ID =  URL[URL.length - 1]  

          $.ajax({
            url: `http://${ENDERECO_IP}:5000/game/${GAME_ID}`,
            type: "GET",
            dataType: "json",
            contentType: "application/json",
            success: handleSetData,
          });
        

        function handleSetData(data){
            const GAME = data.details
            console.log(GAME)

            $("#input_title").val(GAME.title)
            $("#input_description").val(GAME.description)
            $("#input_categorie").val(GAME.categorie)
            $("#input_price").val(GAME.price)
            $("#input_requiredAge").val(GAME.required_age)
            $("#input_developer").val(GAME.developer)
        }



     
       







        }
      }
    }
  }
});
