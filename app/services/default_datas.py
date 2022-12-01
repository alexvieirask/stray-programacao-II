''' Importação das configurações e serviços '''
from services.config import *

'''
Default gamelist
'''
game01 = Game(
    title='''God of War Ragnarök''',
    description=''' Ajude Madeline a enfrentar seus demônios internos em sua jornada até o topo da Montanha Celeste,
    nesse jogo de plataforma super afiado dos criadores de TowerFall. Desbrave centenas de desafios meticulosos,
    descubra segredos complicados e desvende o mistério da montanha.''',
    categorie='''Ação, Aventura, Indie''',
    price=34900,
    required_age=18,
    launch_date='''25/jan./2018''',
    developer=''' Extremely OK Games, Ltd. ''',
    cover= "../static/img/uploads/games/game1cover.jpeg"
)

game02 = Game(
    title='''Ori and the will of the wisps''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game2cover.jpeg"
)

game03 = Game(
    title='''Dying Light''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game3cover.jpeg"
)

game04 = Game(
    title='''Spider-Man''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game4cover.jpeg"
)

game05 = Game(
    title='''Spider-Man: Miles Morales''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game5cover.jpeg"
)

game06 = Game(
    title='''Life is Strange''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game6cover.jpeg"
)

game07 = Game(
    title='''Cyberpunk 2077''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game7cover.jpeg"
)

game08 = Game(
    title='''Genshin Impact''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game8cover.jpeg"
)

game09 = Game(
    title='''Dragon Ball Z Kakarot''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game9cover.jpeg"
)

game10 = Game(
    title='''Grand Theft Auto V''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game10cover.jpeg"
)

game11 = Game(
    title='''Grand Theft Auto San Andreas''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
    cover= "../static/img/uploads/games/game11cover.jpeg"
)

game12 = Game(
    title='''Call Of Duty Modern Warfare II''',
    description='''Bem-vindo ao UNDERTALE. Neste RPG, você controla um humano que cai no subsolo no mundo dos monstros.
    Agora você deve encontrar a saída... ou ficará preso para sempre.''',
    categorie='''Indie, RPG''',
    price=2500,
    required_age=10,
    launch_date='''15/set./2015''',
    developer='''tobyfox''',
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