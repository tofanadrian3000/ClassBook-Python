'''
Created on Nov 12, 2017

@author: ad
'''
from Repository.Repository import Repository, RepositoryExceptions
from Service.Student_Service import StudentService
from Domain.Clasa_student import Student

class TesteStudentService:
    '''
    Contine testele functiilor din StudentService
    '''    
    
    def run(self):
        '''
        Ruleaza toate testele functiilor pentru StudentService
        '''
        self.TestInit()
        self.TestAdaugaStudent()
        self.TestRemoveStudent()
        self.TestUpdateStudent()
    
    def TestInit(self):
        '''
        Testeaza functia de initializare a unui StudentService
        '''
        repo = Repository ()
        StudCtrl = StudentService (repo)
        assert StudCtrl.getStudenti() == []
        
    def TestAdaugaStudent(self):
        '''
        Testeaza functia de adaugare a unui student
        '''
        repo = Repository ()
        StudCtrl = StudentService (repo)
        stud = Student (1, 'Claudiu')
        StudCtrl.adaugaStudent (stud)
        assert StudCtrl.getStudenti() == [stud]
        stud2 = Student (2, 'Marin')
        StudCtrl.adaugaStudent(stud2)
        assert StudCtrl.getStudenti() == [stud, stud2]
        stud3 = Student (1,'Andrei')
        try:
            StudCtrl.adaugaStudent(stud3)
            assert False
        except RepositoryExceptions:
            assert True
        
    def TestUpdateStudent(self):
        '''
        Testeaza functia de actualizare a unui student
        '''
        repo = Repository ()
        StCtrl = StudentService (repo)
        StCtrl.adaugaStudent(Student (1,'Vlad'))
        StCtrl.updateStudent(Student (1,'Vlad'), Student (1, 'Gheorghe'))
        assert StCtrl.getStudenti() == [Student (1, 'Gheorghe')]
        try:
            StCtrl.updateStudent(Student(2,'Marin'), Student (2, 'Ciprian'))
            assert False
        except RepositoryExceptions:
            assert True
            
    def TestRemoveStudent(self):
        '''
        Testeaza functia de stergere a unui student
        '''
        repo = Repository ()
        StudCtrl = StudentService (repo)
        stud = Student (1, 'Marin')
        StudCtrl.adaugaStudent (stud)
        StudCtrl.removeStudent (stud)
        assert StudCtrl.getStudenti() == []
        try:
            StudCtrl.removeStudent(Student (2, 'Cristian'))
            assert False
        except RepositoryExceptions:
            assert True
            

        