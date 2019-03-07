'''
Created on Nov 7, 2017

@author: ad
'''
from Utils.Validare_Student import ValidatorStudent, ValidationStudentException
from Domain.Clasa_student import Student

class TesteValidareStudent():
    
    def __init__(self):
        '''
        Initializeaza ValidatorStudent folosit in teste
        '''
        self.__ValidatorStudent = ValidatorStudent ()
        
    def run(self):
        '''
        Ruleaza toate testele de validare
        '''
        self.TestValidareStudent ()
        
    def TestValidareStudent(self):
        '''
        Testeaza functia de validare a unui student
        '''
        st1 = Student (1,'Stefan Marian')
        try:
            self.__ValidatorStudent.ValidareStudent(st1)
            assert True
        except ValidationStudentException:
            assert False
        st2 = Student (1,'123')
        try:
            self.__ValidatorStudent.ValidareStudent(st2)
            assert False
        except ValidationStudentException:
            assert True
        st3 = Student (-15,'123')
        try:
            self.__ValidatorStudent.ValidareStudent(st3)
            assert False
        except ValidationStudentException:
            assert True
    