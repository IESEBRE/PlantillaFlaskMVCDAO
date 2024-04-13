import persistent
from model.dao import BaseDAO

#La classe els objectes de la qual volem guardar --> canvieu el nom a un de més concret
class Pojo(persistent.Persistent):
    def __init__(self): #Afegir camps
        #Inicialitzar camps
        pass

#Classe que implementa la classe abstracta BaseDAO per fer CRUD d'objectes de la classe Pojo
class Implementation(BaseDAO[Pojo]):
    def __init__(self): #Afegir propietats necessàries per connectar en la BD
        #Inicialitzar propietats
        pass

    #Implementar els mètodes abstractes de la forma correcta per la BD a utilitzar
    def get_all(self):
        pass

    def get_all_ordered(self, key):
        pass

    def get_by_id(self, id):
        pass

    def add(self):  #afegir props del Pojo als param
        pass

    def update(self):  #afegir props del Pojo als param
        pass

    def delete(self, id):
        pass


    def save(self):
        #tancar la connexió
        pass

