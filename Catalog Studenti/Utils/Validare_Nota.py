'''
Created on Nov 8, 2017

@author: ad
'''

from Utils.Validare_id_nume_calificativ import Validator

class ValidationNotaException(Exception):
    pass

class ValidatorNota:
    
    def __init__(self):
        self.__validator = Validator ()
        
    def ValidareNota (self, nota):
        '''
        Valideaza un student
        '''
        erori = ''
        if self.__validator.ValidareId (nota.GetIdsNota()) == False:
            erori += 'Id-ul studentului introdus nu este valid.'
        if self.__validator.ValidareId (nota.GetIddNota()) == False:
            erori += 'Id-ul disciplinei introduse nu este valid.'
        if self.__validator.ValidareCalificativ (nota.GetNota()) == False:
            erori += 'Calificativul introdus nu este valid.'
        if len (erori) > 0:
            raise ValidationNotaException(erori)
        
            