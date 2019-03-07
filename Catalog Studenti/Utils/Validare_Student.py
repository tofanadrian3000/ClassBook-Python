'''
Created on Nov 8, 2017

@author: ad
'''
from Domain.Clasa_student import Student
from Utils.Validare_id_nume_calificativ import Validator

class ValidationStudentException(Exception):
    pass

class ValidatorStudent:
    
    def __init__(self):
        self.__validator = Validator ()
    
        
    def ValidareStudent (self, stud):
        '''
        Valideaza un student
        '''
        erori = ''
        if self.__validator.ValidareId (Student.GetIdStudent(stud)) == False:
            erori += 'Id-ul introdus nu este valid.'
        if self.__validator.ValidareNume (Student.GetNumeStudent(stud)) == False:
            erori += 'Numele introdus nu este valid.'
        if len (erori) > 0:
            raise ValidationStudentException(erori)
        