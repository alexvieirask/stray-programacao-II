''' Importação das configurações e serviços '''
from services.config import *

'''
Default gamelist
'''
game01 = Game(
    title='''God of War Ragnarök''',
    description='''O Fimbulwinter já começou. Kratos e Atreus devem viajar pelos Nove Reinos em busca de respostas enquanto as forças asgardianas se preparam para uma batalha profetizada que causará o fim do mundo. Nessa jornada, eles explorarão paisagens míticas impressionantes e enfrentarão inimigos aterradores: deuses nórdicos e monstros. A ameaça do Ragnarök se aproxima. Kratos e Atreus terão de escolher entre a segurança deles próprios e a dos reinos.''',
    categorie='''ADVENTURE''',
    price=34990,
    required_age=18,
    launch_date='''09/nov./2022''',
    developer='''Santa Monica Studio''',
    cover= "../static/img/uploads/games/game1cover.jpeg"
)

game02 = Game(
    title='''Ori and the will of the wisps''',
    description='''Embarque em uma nova jornada em um mundo vasto e exótico, onde você encontrará inimigos gigantescos e quebra-cabeças desafiadores na sua missão para descobrir o destino de Ori.''',
    categorie='''PLATAFORM''',
    price=12900,
    required_age=0,
    launch_date='''11/mar./2020''',
    developer='''Moon Studios GmbH''',
    cover= "../static/img/uploads/games/game2cover.jpeg"
)

game03 = Game(
    title='''Dying Light''',
    description='''Um jogo de ação e sobrevivência em primeira pessoa em um mundo aberto pós-apocalíptico tomado por zumbis comedores de carne humana. Atravesse uma cidade devastada por um vírus misterioso. Procure por suprimentos, crie armas e enfrente os infectados.''',
    categorie='''RPG''',
    price=7499,
    required_age=16,
    launch_date='''26/jan./2015''',
    developer='''Techland''',
    cover= "../static/img/uploads/games/game3cover.jpeg"
)

game04 = Game(
    title='''Marvel's Spider-Man''',
    description='''Quando vilões icônicos ameaçam a Nova York, os mundos de Peter Parker e Spider-Man entram em conflito. Para salvar a cidade e as pessoas que ama, ele precisa se superar.''',
    categorie='''ADVENTURE''',
    price=24990,
    required_age=12,
    launch_date='''07/set./2018''',
    developer='''Insomniac Games, Nixxes Software''',
    cover= "../static/img/uploads/games/game4cover.jpeg"
)

game05 = Game(
    title='''Marvel's Spider-Man: Miles Morales''',
    description='''Após os eventos de Marvel's Spider-Man Remasterizado, o adolescente Miles Morales está se adaptando à sua nova casa enquanto segue os passos do seu mentor, Peter Parker, para se tornar um novo Spider-Man. Mas uma violenta disputa de forças ameaça destruir seu novo lar e faz o aspirante a herói perceber que com grandes poderes também vêm grandes responsabilidades. Para salvar a Nova York da Marvel, Miles precisa reconhecer e assumir o título de Spider-Man.''',
    categorie='''ADVENTURE''',
    price=19990,
    required_age=12,
    launch_date='''18/nov./2022''',
    developer='''Insomniac Games, Nixxes Software''',
    cover= "../static/img/uploads/games/game5cover.jpeg"
)

game06 = Game(
    title='''Life is Strange''',
    description='''Jogue como Max Caulfield, estudante de fotografia que, ao salvar sua melhor amiga Chloe Price de uma briga violenta, descobre que pode voltar no tempo. Logo depois, a dupla se vê investigando o misterioso desaparecimento de Rachel Amber, revelando um lado sombrio da vida em Arcadia Bay. Enquanto isso, Max precisa aprender o quanto antes que mudar o passado, às vezes, pode levar a um futuro devastador.''',
    categorie='''ADVENTURE''',
    price=19900,
    required_age=16,
    launch_date='''29/jan./2015''',
    developer='''Deck Nine''',
    cover= "../static/img/uploads/games/game6cover.jpeg"
)

game07 = Game(
    title='''Cyberpunk 2077''',
    description='''Cyberpunk 2077 é um RPG de ação e aventura em mundo aberto que se passa em Night City, uma megalópole perigosa onde todos são obcecados por poder, glamour e alterações corporais.''',
    categorie='''RPG''',
    price=19990,
    required_age=18,
    launch_date='''09/dez./2020''',
    developer='''CD PROJEKT RED''',
    cover= "../static/img/uploads/games/game7cover.jpeg"
)

game08 = Game(
    title='''Genshin Impact''',
    description='''Você irá explorar um mundo de fantasia chamado "Teyvat" no jogo, onde você pode viajar por sete nações, encontrar companheiros com diferentes personalidades e habilidades únicas, lutar contra inimigos e embarcar na estrada para reencontrar seu parente de sangue.''',
    categorie='''RPG''',
    price=00,
    required_age=0,
    launch_date='''28/set./2020''',
    developer='''HoYoverse''',
    cover= "../static/img/uploads/games/game8cover.jpeg"
)

game09 = Game(
    title='''Dragon Ball Z: Kakarot''',
    description='''Viva novamente a história de Goku e outros Guerreiros Z em DRAGON BALL Z: KAKAROT! Além das batalhas épicas, sinta como é a vida no mundo de DRAGON BALL Z lutando, pescando, comendo e treinando com Goku, Gohan, Vegeta e outros.''',
    categorie='''RPG''',
    price=15990,
    required_age=12,
    launch_date='''16/jan./2020''',
    developer='''CyberConnect2 Co. Ltd.''',
    cover= "../static/img/uploads/games/game9cover.jpeg"
)

game10 = Game(
    title='''Grand Theft Auto V''',
    description='''Quando um malandro de rua, um ladrão de bancos aposentado e um psicopata aterrorizante se envolvem com alguns dos criminosos mais assustadores e loucos do submundo, o governo dos EUA e a indústria do entretenimento, eles devem realizar golpes ousados para sobreviver nessa cidade implacável onde não podem confiar em ninguém, nem mesmo um no outro.''',
    categorie='''ADVENTURE''',
    price=10790,
    required_age=18,
    launch_date='''17/set./2013''',
    developer='''Rockstar North''',
    cover= "../static/img/uploads/games/game10cover.jpeg"
)

game11 = Game(
    title='''Grand Theft Auto San Andreas''',
    description='''Há 5 anos, Carl Johnson fugiu das pressões da vida em Los Santos, San Andreas... uma cidade que se destruía com gangues, drogas e corrupção, onde estrelas de cinema e milionários fazem o melhor que podem para evitar traficantes e bandidos. É o começo dos anos 90. Carl volta para casa. A sua mãe foi assassinada, a sua família ruiu e seus amigos de infância estão todos indo em direção ao desastre. Para piorar tudo, dois policiais corruptos armaram para que ele fosse acusado de homicídio. CJ é forçado a embarcar numa jornada que o levará por todo o estado de San Andreas para salvar sua família e assumir o controle das ruas.''',
    categorie='''ADVENTURE''',
    price=31990,
    required_age=18,
    launch_date='''26/out./2004''',
    developer='''Rockstar North''',
    cover= "../static/img/uploads/games/game11cover.jpeg"
)

game12 = Game(
    title='''Call Of Duty: Modern Warfare II''',
    description='''O Call of Duty: Modern Warfare II coloca os jogadores dentro de um conflito global sem precedentes que conta com o retorno dos Operadores icônicos da Força-Tarefa 141.''',
    categorie='''FPS''',
    price=29990,
    required_age=18,
    launch_date='''28/out./2022''',
    developer='''Infinity Ward, Raven Software, Beenox, Treyarch, High Moon Studios, Sledgehammer Games, Activision Shanghai, Demonware, Toys for Bob''',
    cover= "../static/img/uploads/games/game12cover.jpeg"
)

default_games = [ game01, game02, game03, game04, game05, game06, game07, game08, game09, game10, game11, game12 ]



'''
Default userlist
'''
user01 = User(
    name = '''Alex Vieira Dias''',
    username = '''alex.vieira''',
    email = '''alexvieiradias2019@gmail.com''',
    password = generate_password_hash('''my-password''').decode("utf-8"),
    description = '''This profile...''',
    profile_picture = '''/static/img/uploads/users/user1.jpeg''',
    wallet = 0,
    is_admin = True
)

user02 = User(
    name = '''Emanoela Rodrigues Erthal''',
    username = '''emanoela.erthal''',
    email = '''emanoelaerthal@gmail.com''',
    password = generate_password_hash('''my-password2''').decode("utf-8"),
    description = '''This profile...''',
    profile_picture = '''/static/img/uploads/users/user2.jpeg''',
    is_admin = True
)

user03 = User(
    name = '''Neymar''',
    username = '''neymar''',
    email = '''neymar@gmail.com''',
    password = generate_password_hash('''my-password3''').decode("utf-8"),
    description = '''This profile...''',
    profile_picture = '''/static/img/uploads/users/user3.jpeg'''
)

default_users = [ user01, user02, user03 ]

screenshot01 = Screenshot(url="https://viciados.net/wp-content/uploads/2022/04/God-of-War-Ragnarok-1000x600.webp", alt="GOW-Screenshot01",game_id=1)
screenshot02 = Screenshot(url="https://dropsdejogos.uai.com.br/wp-content/uploads/sites/10/2022/10/divulgacao-god-of-war-ragnarok-reproducao-1-scaled.jpg", alt="GOW-Screenshot01",game_id=1)
screenshot03 = Screenshot(url="https://viciados.net/wp-content/uploads/2022/04/God-of-War-Ragnarok-1000x600.webp", alt="GOW-Screenshot01",game_id=1)

default_screenshots = [screenshot01,screenshot02,screenshot03]