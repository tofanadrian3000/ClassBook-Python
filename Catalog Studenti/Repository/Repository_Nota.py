'''
Created on Nov 15, 2017

@author: ad
'''

class RepositoryNota:
    
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
        self.__elemente.append (element)
        
    def removeEl (self, element):
        '''
        Sterge un element din lista
        element - elementul ce va fi sters din lista
        '''
        self.__elemente.remove (element)
    
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
    