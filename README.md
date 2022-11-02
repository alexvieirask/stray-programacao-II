# Stray
Stray é um sistema desenvolvido por Alex Vieira Dias e Emanoela Rodrigues Erthal para a disciplina de
programação II. Este projeto tem como finalidade a criação de uma biblioteca de jogos inspirada na Steam

## Diagrama UML de classes
<img src="https://i.ibb.co/PrxhzFr/diagrama-uml-classes.jpg" width="1200px">

## Como utilizar?
**Dependências:** pip install -r requirements.txt <br/><br/>
**Inicializador: app/app.py** <br/><br/>
Executando o arquivo acima o backend será acionado permitindo assim o funcionamento da aplicação.


### Testes

Existem diversos testes de rotas POST/GET nos arquivos dentro da pasta routes, estes testes se encontram como comentários em suas respectivas rotas
Abaixo se encontra o teste da rota que retorna todos os jogos cadastrados no sistema.

```
curl localhost:5000/game/return_all
```

**Login para testes**
```
username: alex.vieira
password: my-password
```

## Screenshots
**Tela de Login** 
<img src="https://i.ibb.co/PwLDnVH/login.png" width="1200px">
