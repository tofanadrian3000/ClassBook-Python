'''
Created on Nov 7, 2017

@author: ad
'''

from Domain.Clasa_student import Student
    
class TesteStudent:
    '''
    Contine testele functiilor asociate clasei Student  
    '''
    
    def run (self):
        '''
        Ruleaza toate testele ale functiilor asociate clasei Student
        '''
        self.TestInit()
        self.TestGetIdStudent()
        self.TestGetNumeStudent()
        self.TestSetNumeStudent()
        self.TestSetIdStudent()
        self.TestEq()
    
    def TestInit (self):
        '''
        Testeaza functia de initializare a unui student
        '''
        studNou = Student (1,'Tofan Paul-Adrian')
        assert studNou.GetIdStudent() == 1
        assert studNou.GetNumeStudent() == 'Tofan Paul-Adrian'
            
    def TestGetNumeStudent (self):
        '''
        Testeaza functia de obtinere a unui nume a unui student
        '''
        assert (Student.GetNumeStudent (Student (5, 'Tofan Paul-Adrian')) == 'Tofan Paul-Adrian')
        assert (Student.GetNumeStudent (Student (5, 'Trifescu Stefan')) == 'Trifescu Stefan')
          
    def TestGetIdStudent (self):
        '''
        Testeaza functia de obtinere a unui id a unui student 
        '''
        assert (Student.GetIdStudent(Student (10, 'Tofan')) == 10)
        assert (Student.GetIdStudent(Student (312, 'Tofan')) == 312)
        
    def TestSetNumeStudent (self):
        '''
        Testeaza functia de setare a unui nume a unui student 
        '''
        stud = Student (12, 'Asd')
        Student.SetNumeStudent(stud, 'Adi')
        assert Student.GetNumeStudent(stud) == 'Adi'
    
    def TestSetIdStudent (self):
        '''
        Testeaza functia de setare a unui id a unui student
        '''
        stud = Student (12, 'ASD')
        Student.SetIdStudent (stud, 1)
        assert Student.GetIdStudent(stud) == 1    
        
    def TestEq (self):
        '''
        Testeaza functia de egalitate dintre noi studenti
        '''
        stud1 = Student (12, 'asd')
        stud2 = Student (25, 'asd')
        stud3 = Student (12, 'nsa')
        if stud1 == stud2:
            assert False
        if stud2 == stud3:
            assert False
        if stud1 == stud3:
            assert True