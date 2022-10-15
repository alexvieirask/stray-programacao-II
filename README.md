# Stray
Stray é um sistema desenvolvido por Alex Vieira Dias e Emanoela Rodrigues Erthal para a disciplina de
programação II. Este projeto tem como finalidade a criação de uma biblioteca de jogos inspirada na Steam.


---
## Diagrama UML de classes
<img src="https://i.ibb.co/PrxhzFr/diagrama-uml-classes.jpg" width="800px">

## Testes de Rotas
### Delete:
```
Deletar algum dado cadastrado na database.

    1. curl localhost:5000/user/delete/1
    2. curl localhost:5000/game/delete/1
    3. curl localhost:5000/giftcard/delete/1
    4. curl localhost:5000/medal/delete/1
    5. curl localhost:5000/screenshot/delete/1
    6. curl localhost:5000/purchase/delete/1
```
### Include:
``` 
Incluir um novo usuário na database.
   
    Windows: 
    1. curl -H \Content-Type:application/json\ -X POST --data "{\"name\":\"Alex Vieira Dias\",\"username\":\"alexvieirasdias\",\"email\":\"alexvieirasdias@gmail.com\",\"password\":\"teste\"}" http://localhost:5000/user/include
    2. curl -H \Content-Type:application/json\ -X POST --data "{\"name\":\"Emanoela Rodrigues Erthal\",\"username\":\"manu_erthal\",\"email\":\"manu@gmail.com\",\"password\":\"manu\"}" http://localhost:5000/user/include

    Linux:
    1. curl -d '{"name":"Alex Vieira Dias","username":"alexvieiradiasSK","email":"alexvieiradias2019@gmail.com","password":"teste"}' -X  POST -H "Content-Type:application/json" localhost:5000/user/include
    2. curl -d '{"name":"Emanoela Rodrigues Erthal","username":"manu.erthal","email":"emanoela@gmail.com","password":"teste"}' -X  POST -H "Content-Type:application/json" localhost:5000/user/include
```
```
Incluir um novo jogo na database.

    Windows: 
    1. curl -H \Content-Type:application/json\ -X POST --data "{\"title\":\"The test\",\"description\":\"this game...\",\"categorie\":\"aventura\",\"price\":\"2\",\"required_age\":\"0\",\"launch_date\":\"24/01/2005\",\"developer\":\"The Tester\"}" http://localhost:5000/game/include

    Linux: 
    2. curl -d '{"title":"The Game of Year","description":"This game...","categorie":"aventura","price":"50.99","required_age":"0","launch_date":"24/01/2005","developer":"God"}' -X  POST -H "Content-Type:application/json" localhost:5000/user/include
```

### Return:

```
Listar todos os dados cadastrados em uma determinada tabela da database.

    1. curl localhost:5000/user/return_all 
    2. curl localhost:5000/game/return_all
    3. curl localhost:5000/giftcard/return_all
    4. curl localhost:5000/medal/return_all 
    5. curl localhost:5000/screenshot/return_all
    6. curl localhost:5000/purchase/return_all
```

```
Listar um determinado objeto cadastrado na database a partir de sua tabela e id.

    1. curl localhost:5000/user/return/1
    2. curl localhost:5000/game/return/1
    3. curl localhost:5000/giftcard/return/1
    4. curl localhost:5000/medal/return/1
    5. curl localhost:5000/screenshot/return/1
    6. curl localhost:5000/purchase/return/1
```