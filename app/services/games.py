from schemas.game import Game

'''
Default gamelist

Games: Celeste, Undertale, Rocket League, Deltarune, Doom Eternal, Cities Skyline,
       The Stanley Parable Ultra Deluxe, Roblox, Euro Truck Simulator 2, FIFA 23, The Sims 4,
       Slime Rancher 2, Genshin Impact,   
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

LUCAS = Game(
    title='''LUCAS O ATIRADOR2''', 
    description='''LUCAS MATA TODOS OS SOLDADOS AMERICANOS NA INVASÃO A CAMARA DA PRESIDENCIA EM MARTE''', 
    categorie='''TERROR''', 
    price='''26.30''', 
    required_age=80,
    launch_date='''18-02-2005''',
    screenshot='''SCREENSHOT.PNG''',
    developer='''DMOLES'''
)

GAMES = [CELESTE, UNDERTALE, ROCKET_LEAGUE, LUCAS]