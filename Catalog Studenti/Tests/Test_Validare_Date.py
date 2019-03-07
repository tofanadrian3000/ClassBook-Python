'''
Created on Nov 15, 2017

@author: ad
'''
from Utils.Validare_id_nume_calificativ import Validator

class TesteValidareDate:
    def __init__ (self):
        self.__validator = Validator()
        
    def run(self):
        self.TestValidareCalificativ()
        self.TestValidareId()
        self.TestValidareNume()
        
    def TestValidareNume(self):
        '''
        Testeaza functia de validare a unui nume
        '''
        assert self.__validator.ValidareNume ('Marius Calin-Adrei') == True
        assert self.__validator.ValidareNume ('Marius Cal123in-Adrei') == False
        assert self.__validator.ValidareNume ('  ') == False   
        
    def TestValidareId(self):
        '''
        Testeaza functia de validare a unui id
        '''
        assert self.__validator.ValidareId (12) == True
        assert self.__validator.ValidareId (-1) == False    
    
    def TestValidareCalificativ(self):
        '''
        Testeaza functia de validare a unui calificativ 
        '''
        assert self.__validator.ValidareCalificativ(10) == True
        assert self.__validator.ValidareCalificativ(5) == True
        assert self.__validator.ValidareCalificativ(-1) == False
        assert self.__validator.ValidareCalificativ(12) == False