$(function () {
  let jwt = sessionStorage.getItem("JWT");
<<<<<<< HEAD
  let ENDERECO_IP = sessionStorage.getItem("IP")

  if (jwt) {
    $.ajax({
      url: `http://${ENDERECO_IP}:5000/user/info`,
=======
  var IP = sessionStorage.getItem("ip") 

  if (jwt) {
    $.ajax({
      url: `http://${IP}:5000/user/info`,
>>>>>>> 4f7a116a59740adc2432efc999b5d8e2aac9bcf1
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

      if (user.is_admin){
        var liAddGameIcon = $("<li>")
        var addGameIcon = $("<img>")
        .attr("src", "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAY1BMVEX///8BAAIAAADz8/M/P0AdHR3w8PC4uLgJCQq8u7zKycpVVVY1NTWSkpLb29vFxcV6enqgoKAVFRbT09M6OjpwcHGqqqpfX19NTU0lJSWGhoZra2zh4eHn5+cuLi6CgoIvLzC0CGJtAAACwklEQVR4nO3d3VbiQBBFYUkAxR+igo6ozMz7P+XczQXSpKs7fSqle98n9LcWmFRa5eqKiIjU7e6X4vYvUuDQ6btTAl+7bqFOKnxwAEqFjx5ApfCXC1An7N98gDLh+uDjkwk/F15AkfDW6R0qE147AiXCJ0+gQvjuChQIX3yB7YV3o8Cp77S1wn4/DvzYTNr7yQu2FX4+j79Fu4dpX3NQCnc5H8GphRuhcMj6GRNYmDnuxhXmjrthhdnjblRh/rgbU5hxGYwtPP423KhFFG5XljvRgELjuBtPaB13wwnN42404R/zNBhM+GEfd0MJ+/FxN7ZwvSx5YBFIeLwpeiATR5g17kYWbkofqUURlu/uBhFW7O7GENbs7oYQVu3uBhD2RZfBQMJj5e7u7IXbsut8IOFz7c7S7IXVW2ezF9YCEZpDaA4hQoTmEJpDiBChOYTmvizYXDBh190bOzxNAvtfe+Eky6yovbCfZJ3lXZ9+Ct4qTzg74Xo4aVd5wtkJJw9h/BDGD2H8EMYPYfwQxg9h/BDGD2H8EMYPoa7hMP6AfV+wuvkIvzwKPldw4WKs7gbhmRDqQogwFUJdCBGmQqgLIcJUCHUhRJgKoS6ECFMh1IUQYSqEuhAiTIVQF0KEqRDqQogwFUJdCBGmQqjr+wtP/0z9rLDgvK2EW/s/Z8j5yhd7cxKOA0uIDYU5CxaEECFC/xAiROgfQoQI/UOIEKF/CBEi9A8hQoT+IUSI0D+EFcIWu2v2k7bcXVsZy/j2sM580tWq3S732lj/mrPLfbSedj2jffzv/5sKCBGmQqgLIcJUCHUhRJgKoS6ECFMh1IUQYSqEuhAiTIVQF0KEqX6gcPqlZyYTNu/RVyggegubh/DisQgRSkJ48ViECCUhvHgswnO1vw/1vi/VC1+SwowKhLfytomVDH+XY+2XbvM5EdGP7h8VIHEKYd4PKQAAAABJRU5ErkJggg==")
        .addClass("form-add-game"); 

        ulHeader.append(liAddGameIcon)
        liAddGameIcon.append(addGameIcon)

      }

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
