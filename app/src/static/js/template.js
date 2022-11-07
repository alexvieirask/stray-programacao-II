$(function () {
  let jwt = sessionStorage.getItem("JWT");
  var IP = sessionStorage.getItem("ip") 

  if (jwt) {
    $.ajax({
      url: `http://${IP}:5000/user/info`,
      method: "GET",
      dataType: "json",
      contentType: "application/json",
      success: headerWithUser,
      headers: { Authorization: "Bearer " + jwt },
      error: () => {
        alert("Error reading data, verify backend");
      },
    });

    function headerWithUser(data) {
      const user = data.details;
      const walletInReal = user.wallet / 100

      var ulHeader = $("#ul-header");
      var liLogin = ulHeader.find("li");

      liLogin.remove();

      var liUsername = $("<li>").attr("id", "username-header");

      var profilePicture = $("<img>")
        .attr("src", user.profile_picture)
        .addClass("username-img-header");
      var exitButton = $("<img>")
        .attr("src", "../static/img/others/exit.jpg")
        .addClass("username-img-header");
      exitButton.attr("id", "username-exit-header");

      var spanWallet = $("<span>")
        .text(`R$${walletInReal.toFixed(2)}`)
        .addClass("username-wallet-header");
      var spanUsername = $("<span>")
        .text(`@${user.username}`)
        .addClass("username-text-header");

      ulHeader.append(liUsername);
      liUsername.append(profilePicture);
      liUsername.append(spanUsername);
      liUsername.append(spanWallet);
      liUsername.append(exitButton);

      exitButton.on("click", onLogout);

      function onLogout() {
        sessionStorage.removeItem("JWT");
        sessionStorage.removeItem("username");
        window.location = "/";
      }
    }
  }
});
