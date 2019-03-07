'''
Created on Nov 8, 2017

@author: ad
'''
from Utils.Validare_id_nume_calificativ import Validator

class ValidationDisciplinaException(Exception):
    pass

class ValidatorDisciplina:
    
    def __init__(self):
        self.__validator = Validator ()
        
    def ValidareDisciplina (self, disc):
        '''
        Valideaza o disciplina
        '''
        erori = ''
        if self.__validator.ValidareId (disc.GetIdDisciplina ()) == False:
            erori += 'Id-ul introdus nu este valid.'
        if self.__validator.ValidareNume (disc.GetNumeDisciplina ()) == False:
            erori += 'Numele introdus nu este valid.'
        if self.__validator.ValidareNume (disc.GetProfesorDisciplina ()) == False:
            erori += 'Numele profesorului introdus nu este valid.'
        if len (erori) > 0:
            raise ValidationDisciplinaException(erori)
        
            