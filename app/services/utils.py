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

def db_query_by_username(username:str):
    ''' Retorna um objeto através de uma 
    query que utiliza o username. 
    '''
    return User.query.filter_by(username = username).first()

def db_insert(item:object):
    ''' Realiza a inserção de um objeto
    em uma determinada tabela da database
    de acordo com sua classe.
    '''
    db.session.add(item)
    db.session.commit()

def db_delete(item:object):
    ''' Realiza a remoção de um objeto
    da database.
    '''
    db.session.delete(item)
    db.session.commit()

def db_drop_database():
    ''' Destrói todas as tabelas.'''
    db.drop_all()