$(function () { 
    $.ajax({
        url: "http://localhost:5000/game/return_all",
        method: 'GET',
        dataType: 'json',
        success: listGames, 
        error: () => { alert("Error reading data, verify backend") }
    });
    
    function listGames(data) {
        const GAMELIST  = data.details

        for (var index in GAMELIST) { 
            const GAME = {
                ID: GAMELIST[index].id,
                TITLE: GAMELIST[index].title,
                COVER: GAMELIST[index].cover,
                PRICE: GAMELIST[index].price,
                TITLE_LINK: GAMELIST[index].title.replace(/\s/g, '')
            }

            const GAMEBOX__HTML =
                `  
                    <li>
                        <a href="game/${GAME.ID}/${GAME.TITLE_LINK}">
                            <img src=${GAME.COVER} alt="${GAME.COVER}-cover">
                            <div>
                                <h2>${GAME.TITLE}</h2>
                                <p class="games-price">${GAME.PRICE == 0 ? "Free": `R$ ${GAME.PRICE}`}</p>
                            </div>
                        </a>
                    </li>
                `
            $('#gamelist').append(GAMEBOX__HTML);
        }
    }
});