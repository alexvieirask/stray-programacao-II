$(function () {
    var URL = document.URL;
    var PROTOCOL = "http://"; 
    
    var IP = URL.substring(PROTOCOL.length);
    var COLON_POSITION = IP.indexOf(":");
    IP = IP.substring(0, COLON_POSITION)

    sessionStorage.setItem("ip",IP); 

});