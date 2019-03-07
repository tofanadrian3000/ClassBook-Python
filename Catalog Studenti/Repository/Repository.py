'''
Created on Nov 8, 2017
@author: Adi
'''
class RepositoryExceptions (Exception):
    pass

class Repository:
    def __init__ (self):
        '''
        Initializeaza o lista de elemente ca fiind goala
        '''
        self.__elemente = []
    
    def add (self, element):
        '''
        Adauga un element la lista
        element - elementul ce va fi adaugat la lista
        '''
        if element in self.__elemente:
            raise RepositoryExceptions('Element existent!')
        self.__elemente.append (element)
        
    def removeEl (self, element):
        '''
        Sterge un element din lista
        element - elementul ce va fi sters din lista
        '''
        if element in self.__elemente:
            self.__elemente.remove (element)
        else:
            raise RepositoryExceptions('Element inexistent!')
        
    def update (self, elementVechi, elementNou):
        '''
        Modifica un element existent din lista in cazul in care exista
        elementVechi - elementul ce urmeaza sa fie actualizat
        elementNou - elementul la care va fi actualizat elementul vechi
        '''
        if elementVechi not in self.__elemente:
            raise RepositoryExceptions('Element inexistent!')
        else:
            index = self.__elemente.index (elementVechi) 
            self.__elemente[index] = elementNou
    
    def find(self,element):
        '''
        Verifica daca un element se regaseste in lista de elemente
        element - elementul ce urmeaza sa fie cautat
        '''
        if element in self.__elemente:
            return self.__elemente [self.__elemente.index(element)] 
        else:
            raise RepositoryExceptions("Element inexistent!")
    
    def __len__(self):
        '''
        Returneaza lungimea listei de elemente
        '''
        return len(self.__elemente)
    
    def getAll(self):
        '''
        Returneaza lista intreaga
        '''
        return self.__elemente[:]