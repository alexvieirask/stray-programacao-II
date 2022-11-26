$(function () {
  const ENDERECO_IP = sessionStorage.getItem("ENDERECO_IP");

  $.ajax({
    url: `http://${ENDERECO_IP}:5000/game/return_all`,
    method: "GET",
    dataType: "json",
    success: listGames,
    error: () => {
      alert("Error reading data, verify backend");
    },
  });

  function listGames(data) {
    const GAMELIST = data.details;

    for (var index in GAMELIST) {
      const GAME = {
        ID: GAMELIST[index].id,
        TITLE: GAMELIST[index].title,
        COVER: GAMELIST[index].cover,
        PRICE: GAMELIST[index].price / 100,
        TITLE_LINK: GAMELIST[index].title.replace(/\s/g, ""),
      };

      const GAMEBOX__HTML = `  
                    <li>
                        <a href="game/${GAME.ID}/${GAME.TITLE_LINK}">
                            <img src=${GAME.COVER} alt="${GAME.TITLE_LINK}-cover">
                            <div class="game-info-container">
                                <span class="game-title">${GAME.TITLE}</span>
                                <span class="game-price">${
                                  GAME.PRICE == 0 ? "Free" : `R$${GAME.PRICE}`
                                }</span>
                            </div>
                        </a>
                    </li>
                `;
      $(".games").append(GAMEBOX__HTML);
    }
  }
});
