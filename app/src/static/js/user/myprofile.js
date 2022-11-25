$(function () {
  const JWT = sessionStorage.getItem("JWT");
  const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");

  function redirectToLogin() {
    window.location = "/login";
  }

  if (JWT) {
    $.ajax({
      url: `http://${ENDERECO_IP}:5000/user/info`,
      method: "GET",
      dataType: "json",
      contentType: "application/json",
      success: setUserInfo,
      headers: { Authorization: "Bearer " + JWT },
      error: () => {
        alert("Error reading data, verify backend");
      },
    });

    $.ajax({
      url: `http://${ENDERECO_IP}:5000/user/library`,
      method: "GET",
      dataType: "json",
      contentType: "application/json",
      success: setGamesInfo,
      headers: { Authorization: "Bearer " + JWT },
      error: () => {
        alert("Error reading data, verify backend");
      },
    });

    function setUserInfo(data) {
      const USER = data.details;

      $("#username").text(USER.username);
      $("#name").text(USER.name);
      $("#description").text(USER.description);
      $("#my-picture").attr("src", USER.profile_picture);
    }

    function setGamesInfo(data) {
      const allGames = data.details.games;
      const purchases = data.details.purchases;
      const allGamesLength = allGames.length;

      const lastGames = allGames.length > 3 ? allGames.slice(allGamesLength - 3, allGamesLength) : allGames;

      const gamesInfo = {
        lastBuyed: lastGames,
        totalQuantity: allGames.length,
        purchases: purchases,
        all: allGames,
      };

      $("#quantity-games").text(gamesInfo.totalQuantity);

      if (gamesInfo.totalQuantity > 0) {
        HTML__GAMES(gamesInfo);
      }
    }

    function HTML__GAMES(GAMES) {
      HTML__lastGamesBuyed(GAMES.lastBuyed);
      HTML__allGamesBuyed(GAMES.all, GAMES.purchases);
    }

    function HTML__lastGamesBuyed(GAMES) {
      var divGamesInfoSecond = $("#games-info-second");

      var divGamesLastContainer = $("<div>").attr("id", "games-last-container");
      var h2TitleLastGames = $("<h2>").text("Last Games Buyed");

      var ulHeader = $("<ul>").attr("id", "list-games-last");

      for (let game in GAMES) {
        var liItemGame = $("<li>");
        var imgCoverGame = $("<img>").attr("src", GAMES[game].cover);
        var spanTitleGame = $("<span>").addClass("game-title").text(GAMES[game].title);

        ulHeader.append(liItemGame);
        liItemGame.append(imgCoverGame);
        liItemGame.append(spanTitleGame);
      }

      divGamesLastContainer.append(h2TitleLastGames);
      divGamesLastContainer.append(ulHeader);
      divGamesInfoSecond.append(divGamesLastContainer);
    }

    function HTML__allGamesBuyed(GAMES, purchases) {
      var divGamesInfoSecond = $("#games-info-second");
      var ulHeader = $("<ul>").attr("id", "all-games");
      var buttonAllGames = $("<button>").text("All Games").attr("id", "button-all-games");

      for (let game in GAMES) {
        var liItemGame = $("<li>").addClass("row-item");
        var spanTitleGame = $("<span>").text(GAMES[game].title);
        var spanDatePurchase = $("<span>").text(purchases[game].realized_date).addClass("date-buyed");

        ulHeader.append(liItemGame);
        liItemGame.append(spanTitleGame);
        liItemGame.append(spanDatePurchase);
      }

      divGamesInfoSecond.append(buttonAllGames);
      divGamesInfoSecond.append(ulHeader);

      buttonAllGames.on("click", showAllGames);
    }

    function showAllGames() {
      var ulAllGames = $("#all-games");
      ulAllGames.slideToggle()
    }
  } else {
    redirectToLogin();
  }
});
