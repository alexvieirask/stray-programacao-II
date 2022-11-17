function handleUserIP () {
  const URL = document.URL
  const PROTOCOL = 'http://'

  var ENDERECO_IP = URL.substring(PROTOCOL.length)

  const COLON_POSITION = ENDERECO_IP.indexOf(':')

  ENDERECO_IP = ENDERECO_IP.substring(0, COLON_POSITION)

  sessionStorage.setItem('ENDERECO_IP', handleUserIP())
}