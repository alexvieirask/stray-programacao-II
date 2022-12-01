from services.config import *

'''  Funções relacionadas á database '''

def db_query_all(schema:object) -> list:
    ''' Retorna uma lista com todos 
    os objetos de um determinado schema.
    '''
    return schema.query.all()

def db_query_by_id(schema:object,id:int) -> object:
    ''' Retorna um objeto através de uma 
    query que utiliza o schema e id. 
    '''
    return schema.query.get(id)

def db_query_by_username(schema, username:str) -> object:
    ''' Retorna um objeto através de uma 
    query que utiliza o username. 
    '''
    return schema.query.filter_by(username = username).first()

def db_query_by_email(schema, email:str) -> object:
    ''' Retorna um objeto através de uma 
    query que utiliza o username. 
    '''
    return schema.query.filter_by(email = email).first()

def db_drop_database() -> None:
    ''' Destrói todas as tabelas.'''
    db.drop_all()

def db_add_many_objects(list:list):
    ''' Adiciona diversos itens na database através de uma lista '''
    for item in list:
        db.session.add(item)
    db.session.commit()

def db_delete_many_objects(list:list):
    ''' Remove diversos itens da database através de uma lista '''
    for item in list:
        db.session.delete(item)
    db.session.commit()

def db_check_if_username_exists(schema,username):
    ''' Verifica se um username já existe '''
    user = db_query_by_username(schema,username)
    if user:
        return True
    return False

def PATH_FROM_MAIN_FOLDER(others_folders:list):
    ''' Função dinâmica para acessar as pastas da aplicação '''
    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
    CURRENT_PATH_LIST = CURRENT_PATH.split('\\')
    STRING_PATH = "" 
    SO = platform.system()

    SEPARATOR ="\\"

    if SO != "Windows":
        SEPARATOR = "/"

    index_app_folder = CURRENT_PATH_LIST.index("app") + 1
    path_app_folder_in_list = CURRENT_PATH_LIST[0: index_app_folder]

    
    path_complete = path_app_folder_in_list + others_folders


    for folder in path_complete:
        STRING_PATH+= folder + SEPARATOR
    
    return STRING_PATH