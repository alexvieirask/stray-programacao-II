$(function(){
    var ENDERECO_IP;
    var URL = document.URL;  
    var protocolo = "http://"; 
    var http = protocolo.length; 
    var comeco = URL.substring(http); 
    var partes = comeco.split("/"); 
    var primeiro = partes[0]; 

    posicao_doispontos = primeiro.indexOf(":");
    
    if (posicao_doispontos >= 0) { 
        ENDERECO_IP = primeiro.substring(0, posicao_doispontos);
    } else {
        ENDERECO_IP = primeiro;
    }
  
    sessionStorage.setItem("IP", ENDERECO_IP)


})

