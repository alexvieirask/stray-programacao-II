from schemas.game import Game
from schemas.user import User

'''
Default gamelist

Games: Celeste, Undertale, Rocket League, Deltarune, Doom Eternal, Cities Skyline,
       The Stanley Parable Ultra Deluxe, Roblox, Euro Truck Simulator 2, FIFA 23, The Sims 4,
       Slime Rancher 2 e Genshin Impact.
'''

CELESTE = Game(
    title='''Celeste''',
    description=''' Ajude Madeline a enfrentar seus demônios internos em sua jornada até o topo da Montanha Celeste, 
    nesse jogo de plataforma super afiado dos criadores de TowerFall. Desbrave centenas de desafios meticulosos, 
    descubra segredos complicados e desvende o mistério da montanha.''',
    categorie='''Ação, Aventura, Indie''', 
    price='''36,99''',
    required_age=10,
    launch_date='''25/jan./2018''',
    screenshot='''celeste.png''',
    developer='''TESTE1'''
) 

UNDERTALE = Game(
    title='''UNDERTALE''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros. 
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price='''19,99''',
    required_age=10,
    launch_date='''15/set./2015''',
    screenshot='''undertale.png''',
    developer='''TESTE1'''
)

ROCKET_LEAGUE = Game(
    title='''Rocket League''',
    description=''' Futebol e pilotagem se encontram mais uma vez na aguardada sequência do jogo clássico de arena baseado 
    em física tão amado pelos fãs, o Supersonic Acrobatic Rocket-Powered Battle-Cars! ''',
    categorie='''Esportes, Corrida''',
    price='''0''',
    required_age=0,
    launch_date='''7/jul./2015''',
    screenshot='''rocket_league.png''',
    developer='''TESTE'''
)

GAMES = [ CELESTE, UNDERTALE, ROCKET_LEAGUE ]


'''
Default userlist

users: Alex Vieira Dias, Emanoela Rodrigues Erthal, Igor Gramkow, Gabriel Molon Zanella, Yara Rahn, Alana Cristina Andreazza,
Amadeus Vitor Poletti e Beatriz Miranda.
'''

ALEX = User(
    name = '''Alex Vieira Dias''',
    username = '''alex.vieira''',
    email = '''alexvieiradias2019@gmail.com''',
    password = '''my-password''',
    age = '''24/01/2005''',
    description = '''This profile...''',
    profile_picture = '''alex.png'''
    )

EMANOELA = User(
    name = '''Emanoela Rodrigues Erthal''',
    username = '''emanoela.erthal''',
    email = '''emanoelaerthal@gmail.com''',
    password = '''my-password2''',
    age = '''12/12/2012''',
    description = '''This profile...''',
    profile_picture = '''emanoela.png'''
)

USERS = [ ALEX, EMANOELA ]