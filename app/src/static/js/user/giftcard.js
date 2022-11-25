$(function () {
  const JWT = sessionStorage.getItem("JWT");
  const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");

  if (JWT) {    
    $(".column-giftcard").on("click", giftcardBuyed);
    $("#code-submit").on("click", useGiftcard)



    function useGiftcard(){
      var inputGiftcard = $("#code-input").val() || "empty"

      if (inputGiftcard != "empty"){
        $.ajax({
          url: `http://${ENDERECO_IP}:5000/giftcard/use/${inputGiftcard}`,
          method: "GET",
          dataType: "json",
          contentType: "application/json",
          success: handleValidationGiftcard,
          headers: { Authorization: "Bearer " + JWT },
          error: () => {
            alert("Error reading data, verify backend");
          },
        });
      } else{
        $("#span-message").text("This field is empty").removeClass().addClass("span-warning")
      }
    }

    function handleValidationGiftcard(data){
      if (data.result == "error"){
        $("#span-message").text(data.details).removeClass().addClass("span-error")
      }
      else{
        $("#span-message").text("Giftcard successfully used").removeClass().addClass("span-success")
        
        const timer = 2000
        clearTimeout(timer)

        setTimeout(()=>{
          window.location.reload()

        },timer)

      }

    }
  
    function giftcardBuyed(){
      const gitfcardValue = this.children[0].alt.split("-")[0];
      console.log(gitfcardValue)
      

      $.ajax({
        url: `http://${ENDERECO_IP}:5000/giftcard/${gitfcardValue}`,
        method: "GET",
        dataType: "json",
        contentType: "application/json",
        success: function (data){
          alert(data.details.giftcard_code)
        },
        headers: { Authorization: "Bearer " + JWT },
        error: () => {
          alert("Error reading data, verify backend");
        },
      });

    }


  }
});
