from entities.entidades import Lector
from connection.lectorDB import LectorDB

class ModelLector:

    @staticmethod
    def listarLectores():        
        return LectorDB.getAll()
    
    @staticmethod
    def buscarLectorPorId(id):
        return LectorDB.getById(id)
    
    @staticmethod
    def buscarLectorPorNombre(nombre):
        return LectorDB.getByName(nombre)

    @staticmethod
    def registrarLector(nombre):        
        return LectorDB.insert(Lector(None, nombre))