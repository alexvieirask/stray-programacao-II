$(function () {
  const JWT = sessionStorage.getItem("JWT");
  const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");

  function redirectToLogin() {
    window.location = "/login";
  }

  if (JWT) {
    $(".main").show();
    $(".column-giftcard").on("click", giftcardBuyed);

    $(".column-giftcard").hover(giftcardHover);
    $(".column-giftcard").mouseleave(giftcardMouseLeave);

    $("#code-submit").on("click", useGiftcard);

    function availableGiftcardsShow() {
      var ulAllGames = $(".giftcards-available");
      ulAllGames.stop().slideToggle();
    }

    function setDataGiftcards() {
      $.ajax({
        url: `http://${ENDERECO_IP}:5000/user/giftcards`,
        method: "GET",
        dataType: "json",
        contentType: "application/json",
        success: handleGiftcardsInfo,
        headers: { Authorization: "Bearer " + JWT },
        error: () => {
          alert("Error reading data, verify backend");
        },
      });
    }

    function handleGiftcardsInfo(data) {
      var ulGiftcardAvailables = $("<ul>").addClass("giftcards-available");

      const GIFTCARD = {
        all: data.details,
        available: data.details.filter(
          (giftcard) => giftcard.available == true
        ),
      };

      $("#giftcards-availables").text(GIFTCARD.available.length);
      $("#giftcards-buyed").text(GIFTCARD.all.length);

      if (GIFTCARD.available.length > 0) {
        var divAll = $(".all-giftcards");
        var divEnd = $("<div>").addClass("end-container");
        var inputGiftcardsAvailable = $("<input>")
          .addClass("my-giftcards-submit")
          .val("Giftcards Available")
          .attr("type", "submit");

        divEnd.append(inputGiftcardsAvailable);
        divAll.append(divEnd);

        inputGiftcardsAvailable.on("click", availableGiftcardsShow);
      }

      $(".all-giftcards").append(ulGiftcardAvailables);

      for (let giftcard in GIFTCARD.available) {
        const currentGiftcard = GIFTCARD.available[giftcard];

        var liGiftcardAvailables = $("<li>").addClass(
          "giftcards-available-item"
        );

        var spanCode = $("<span>").text(`${currentGiftcard.giftcard_code}`);
        var spanValue = $("<span>").text(`R$ ${currentGiftcard.value / 100}`);

        liGiftcardAvailables.append(spanCode);
        liGiftcardAvailables.append(spanValue);

        ulGiftcardAvailables.append(liGiftcardAvailables);
      }
    }

    function useGiftcard() {
      var inputGiftcard = $("#code-input").val() || "empty";

      if (inputGiftcard != "empty") {
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
      } else {
        $("#span-message")
          .text("This field is empty")
          .removeClass()
          .addClass("span-warning");
      }
    }

    function handleValidationGiftcard(data) {
      if (data.result == "error") {
        $("#span-message")
          .text(data.details)
          .removeClass()
          .addClass("span-error");
      } else {
        $("#span-message")
          .text("Giftcard successfully used")
          .removeClass()
          .addClass("span-success");

        const TIMER = 1000;

        clearTimeout(TIMER);

        setTimeout(() => {
          window.location.reload();
        }, TIMER);
      }
    }

    function giftcardMouseLeave() {
      const TIMER = 200;
      var columnGiftcard = $(this);
      var imgGold = $(this.children[0]);

      const GIFTCARD_VALUE = this.children[0].alt.split("-")[0];
      imgGold.fadeIn(TIMER);

      setTimeout(() => {
        imgGold.attr("src", `/static/img/fixed/${GIFTCARD_VALUE}.jpg`);
        columnGiftcard.removeClass().addClass("column-giftcard");
      }, TIMER);
    }

    function giftcardHover() {
      const TIMER = 200;
      var columnGiftcard = $(this);
      var imgGold = $(this.children[0]);

      var GIFTCARD_VALUE = this.children[0].alt.split("-")[0];
      imgGold.stop().fadeOut(TIMER).fadeIn(TIMER);

      setTimeout(() => {
        imgGold.attr("src", `/static/img/fixed/dourado${GIFTCARD_VALUE}.jpg`);
        columnGiftcard.removeClass().addClass("column-giftcard-gold");
      }, TIMER);
    }

    function giftcardBuyed() {
      const gitfcardValue = this.children[0].alt.split("-")[0];

      $.ajax({
        url: `http://${ENDERECO_IP}:5000/giftcard/${gitfcardValue}`,
        method: "GET",
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
          alert(data.details.giftcard_code);
          window.location.reload();
        },
        headers: { Authorization: "Bearer " + JWT },
        error: () => {
          alert("Error reading data, verify backend");
        },
      });
    }

    setDataGiftcards();
  } else {
    redirectToLogin();
  }
});
