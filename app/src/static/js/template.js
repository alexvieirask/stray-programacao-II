$(function () { 
    let jwt = sessionStorage.getItem("JWT")
    let username = sessionStorage.getItem("username")

    if (jwt){
        var ulHeader = $("#ul-header")
        var liLogin = $("#ul-header").find("li")
        liLogin.remove()

        var liUsername = $("<li>")
        var liLogout = $("<li>")
        
        var aUsername = $("<a>").text(`@${username}`).attr("id","username-header")
        var aLogout = $("<a>").text(`Logout`).attr("id","logout-header")

        liLogout.on("click", onLogout)
        
        ulHeader.append(liUsername)
        ulHeader.append(liLogout)
        
        liUsername.append(aUsername)
        liLogout.append(aLogout)

    }


    function onLogout(){
        sessionStorage.removeItem("JWT")
        sessionStorage.removeItem("username")
        window.location = '/'
    }


});