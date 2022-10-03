from schemas.game import Game
from schemas.user import User
from services.encrypt import encrypt_password

'''
Default gamelist

Games: Celeste, Undertale, Rocket League, Deltarune, Doom Eternal, Cities Skyline,
       The Stanley Parable Ultra Deluxe, Roblox, Euro Truck Simulator 2, FIFA 23, The Sims 4,
       Slime Rancher 2 e Genshin Impact.
'''

game01 = Game(
    title='''Celeste''',
    description=''' Ajude Madeline a enfrentar seus demônios internos em sua jornada até o topo da Montanha Celeste, 
    nesse jogo de plataforma super afiado dos criadores de TowerFall. Desbrave centenas de desafios meticulosos, 
    descubra segredos complicados e desvende o mistério da montanha.''',
    categorie='''Ação, Aventura, Indie''', 
    price='''36,99''',
    required_age=10,
    launch_date='''25/jan./2018''',
    developer='''TESTE1'''
) 

game02 = Game(
    title='''UNDERTALE''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros. 
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price='''19,99''',
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''TESTE1'''
)

game03 = Game(
    title='''Rocket League''',
    description=''' Futebol e pilotagem se encontram mais uma vez na aguardada sequência do jogo clássico de arena baseado 
    em física tão amado pelos fãs, o Supersonic Acrobatic Rocket-Powered Battle-Cars! ''',
    categorie='''Esportes, Corrida''',
    price='''0''',
    required_age=0,
    launch_date='''7/jul./2015''',
    developer='''TESTE'''
)

default_games = [ game01, game02, game03 ]


'''
Default userlist

users: Alex Vieira Dias, Emanoela Rodrigues Erthal, Igor Gramkow, Gabriel Molon Zanella, Yara Rahn, Alana Cristina Andreazza,
Amadeus Vitor Poletti, Lucas Gabriel Sievert e Beatriz Miranda.
'''

user01 = User(
    name = '''Alex Vieira Dias''',
    username = '''alex.vieira''',
    email = '''alexvieiradias2019@gmail.com''',
    password = encrypt_password('''my-password'''),
    description = '''This profile...''',
    profile_picture = '''alex.png'''
)

user02 = User(
    name = '''Emanoela Rodrigues Erthal''',
    username = '''emanoela.erthal''',
    email = '''emanoelaerthal@gmail.com''',
    password = encrypt_password('''my-password2'''),
    description = '''This profile...''',
    profile_picture = '''emanoela.png'''
)

user03 = User(
    name = '''Igor Gramkow''',
    username = '''igor.gramkow''',
    email = '''igorgramkow@gmail.com''',
    password = encrypt_password('''my-password3'''),
    description = '''This profile...''',
    profile_picture = '''igor.png'''
)

user04 = User(
    name = '''Gabriel Molon Zanella''',
    username = '''gabriel.zanella''',
    email = '''grabrielzanella@gmail.com''',
    password = encrypt_password('''my-password4'''),
    description = '''This profile...''',
    profile_picture = '''zanella.png'''
)

default_users = [ user01, user02, user03, user04 ]