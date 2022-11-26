$(function () {
  const JWT = sessionStorage.getItem("JWT");
  const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");
  const GAMEID = document.URL.split("/")[4];

  $(".icon-giftcard").attr("src", "teste");

  function redirectToLogin() {
    window.location = "/login";
  }

  function setDataGame() {
    $.ajax({
      url: `http://${ENDERECO_IP}:5000/game/${GAMEID}`,
      type: "GET",
      dataType: "json",
      contentType: "application/json",
      success: handleSetData,
    });
  }

  function handleSetData(data) {
    const GAME = data.details;

    const main = $(".main");

    var divTitleRow = $("<div>").addClass("title-row");

    var spanValue = $("<span>").text("R$ " + GAME.price / 100);

    var title = $("<h1>").text(GAME.title);

    var hr1 = $("<hr>");
    var hr2 = $("<hr>");

    var divDescription = $("<div>");
    var description = $("<p>").attr("id", "description").text(GAME.description);

    var divScreenshots = $("<div>");
    var ulScreenshots = $("<ul>").addClass("screenshots-container");

    var divContainerInfo = $("<div>").addClass("container-info");
    var spanCategorie = $("<span>").text(`Categorie: ${GAME.categorie}`);
    var spanlaunchDate = $("<span>").text(`Launch Date: ${GAME.launch_date}`);
    var spanDeveloper = $("<span>").text(`Developer: ${GAME.developer}`);

    divTitleRow.append(title);
    divTitleRow.append(spanValue);

    main.append(divTitleRow);
    main.append(hr1);
    divDescription.append(description);
    main.append(divDescription);

    for (let screenshot in data.screenshots) {
      var liScreenshot = $("<li>");
      var imgScreenshot = $("<img>").attr(
        "src",
        data.screenshots[screenshot].url
      );

      liScreenshot.append(imgScreenshot);
      ulScreenshots.append(liScreenshot);
    }

    divScreenshots.append(ulScreenshots);
    main.append(divScreenshots);

    divContainerInfo.append(spanCategorie);
    divContainerInfo.append(spanlaunchDate);
    divContainerInfo.append(spanDeveloper);

    main.append(divContainerInfo);
    main.append(hr2);

    if (JWT) {
      $.ajax({
        url: `http://${ENDERECO_IP}:5000/user/library`,
        type: "GET",
        dataType: "json",
        contentType: "application/json",
        headers: { Authorization: "Bearer " + JWT },
        success: handleValidateThisGame,
      });
    } else {
      var divContainerPrice = $("<div>").addClass("container-price");
      var inputBuy = $("<input>")
        .addClass("default-button")
        .attr("type", "submit")
        .val("Buy")
        .attr("id", "game-buy");
      inputBuy.on("click", redirectToLogin);

      divContainerPrice.append(inputBuy);
      main.append(divContainerPrice);
    }
  }

  function handleValidateThisGame(data) {
    const GAMES_BUYED = data.details.purchases;
    const result = GAMES_BUYED.find(
      (element) => element.game_buyed_id == GAMEID
    );

    var divContainerPrice = $("<div>").addClass("container-price");
    var inputBuy = $("<input>")
      .addClass("default-button")
      .attr("type", "submit")
      .val("Buy")
      .attr("id", "game-buy");
    inputBuy.on("click", handleBuyThisGame);

    if (result) {
      inputBuy
        .val("Game already purchased")
        .removeClass()
        .addClass("golden-button");
      inputBuy.off();
    }

    divContainerPrice.append(inputBuy);

    $(".main").append(divContainerPrice);
  }

  function handleBuyThisGame() {
    if (JWT) {
      $.ajax({
        url: `http://${ENDERECO_IP}:5000/game/purchase/${GAMEID}`,
        type: "GET",
        dataType: "json",
        contentType: "application/json",
        headers: { Authorization: "Bearer " + JWT },
        success: tryPurchaseThisGame,
        error: failedPurchase,
      });

      function tryPurchaseThisGame(data) {
        if (data.result == "error") {
          var spanError = $("<span>")
            .addClass("span-warning")
            .text(data.details)
            .attr("id", "span-buy");

          if ($("#span-buy").attr("id") == undefined) {
            $(".main").append(spanError);
          }
        } else {
          alert("successful purchase");
          window.location.reload();
        }
      }

      function failedPurchase(data) {
        alert("error, try again.");
      }
    } else {
      redirectToLogin();
    }
  }

  setDataGame();
});
