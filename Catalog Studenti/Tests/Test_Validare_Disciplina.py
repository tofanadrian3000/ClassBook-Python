'''
Created on Nov 15, 2017

@author: ad
'''
'''
Created on Nov 7, 2017

@author: ad
'''
from Utils.Validare_Disciplina import ValidatorDisciplina, ValidationDisciplinaException
from Domain.Clasa_disciplina import Disciplina

class TesteValidareDisciplina():
    
    def __init__(self):
        '''
        Initializeaza validatorulul folosit in teste
        '''
        self.__validator = ValidatorDisciplina ()
        
    def run(self):
        '''
        Ruleaza toate testele de validare
        '''
        self.TestValidareDisciplina ()
        
    def TestValidareDisciplina(self):
        '''
        Testeaza functia de validare a unei discipline
        '''
        disc1 = Disciplina (1, 'Analiza matematica', 'Berinde Stefan')
        try:
            self.__validator.ValidareDisciplina(disc1)
            assert True
        except ValidationDisciplinaException:
            assert False
        disc2 = Disciplina (-2, 'FP', 'Czibula Istvan')
        try:
            self.__validator.ValidareDisciplina(disc2)
            assert False
        except ValidationDisciplinaException:
            assert True
        disc3 = Disciplina (2, 'asd', ' ')
        try:
            self.__validator.ValidareDisciplina(disc3)
            assert False
        except ValidationDisciplinaException:
            assert True
        disc4 = Disciplina (2, 'as0d', ' ')
        try:
            self.__validator.ValidareDisciplina(disc4)
            assert False
        except ValidationDisciplinaException:
            assert True
    