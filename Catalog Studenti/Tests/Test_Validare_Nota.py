'''
Created on Nov 15, 2017

@author: ad
'''
from Utils.Validare_Nota import ValidatorNota, ValidationNotaException
from Domain.Clasa_Nota import Nota

class TesteValidareNota:
    
    def __init__(self):
        '''
        Initializeaza validatorul pentru note
        '''
        self.__validator = ValidatorNota ()
        
    def run(self):
        '''
        Ruleaza testul de validare a unei note
        '''
        self.TestValidareNota()
        
        
    def TestValidareNota(self):
        '''
        Testeaza functia de validare a unei discipline
        '''
        nota = Nota (1, 1, 10)
        try:
            self.__validator.ValidareNota(nota)
            assert True
        except ValidationNotaException:
            assert False
        nota = Nota (1, 1, 12)
        try:
            self.__validator.ValidareNota(nota)
            assert False
        except ValidationNotaException:
            assert True
        nota = Nota (1, -5, 10)
        try:
            self.__validator.ValidareNota(nota)
            assert False
        except ValidationNotaException:
            assert True
        nota = Nota (-5, 1, 10)
        try:
            self.__validator.ValidareNota(nota)
            assert False
        except ValidationNotaException:
            assert True

