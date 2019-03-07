'''
Created on Nov 12, 2017

@author: ad
'''

from Domain.Clasa_disciplina import Disciplina
    
class TesteDisciplina:
    '''
    Contine testele functiilor asociate clasei Disciplina  
    '''
    
    def run (self):
        '''
        Ruleaza toate testele ale functiilor asociate clasei Disciplina
        '''
        self.TestInit()
        self.TestGetIdDisciplina()
        self.TestGetNumeDisciplina()
        self.TestGetProfesorDisciplina()
        self.TestSetNumeDisciplina()
        self.TestSetIdDisciplina()
        self.TestSetProfesorDisciplina()
        self.TestEq()
       
    def TestInit (self):
        Disc = Disciplina (1, 'Mate', 'Nistor')
        assert (Disc.GetNumeDisciplina() == 'Mate')
        assert (Disc.GetProfesorDisciplina() == 'Nistor')
        assert (Disc.GetIdDisciplina() == 1) 
        
    def TestGetNumeDisciplina (self):
        '''
        Testeaza functia de obtinere a unui nume a unui Disciplina
        '''
        assert (Disciplina.GetNumeDisciplina (Disciplina (5, 'Mate', 'Nistor')) == 'Mate')
        assert (Disciplina.GetNumeDisciplina (Disciplina (5, 'Istorie', 'Lostun')) == 'Istorie')
          
    def TestGetIdDisciplina (self):
        '''
        Testeaza functia de obtinere a unui id a unui Disciplina 
        '''
        assert (Disciplina.GetIdDisciplina(Disciplina (10, 'Mate', 'Nistor')) == 10)
        assert (Disciplina.GetIdDisciplina(Disciplina (312, 'Istorie', 'Lostun')) == 312)
        
    def TestGetProfesorDisciplina (self):
        '''
        Testeaza functia de obtinere a numelui profesorului de la o anumita disciplina
        '''
        assert (Disciplina.GetProfesorDisciplina(Disciplina (10, 'Mate', 'Nistor')) == 'Nistor')
        assert (Disciplina.GetProfesorDisciplina(Disciplina (312, 'Istorie', 'Lostun')) == 'Lostun')
    
    def TestSetNumeDisciplina (self):
        '''
        Testeaza functia de setare a unui nume a unui Disciplina 
        '''
        disc = Disciplina (12, 'Mate', 'Nistor')
        disc.SetNumeDisciplina('Istorie')
        assert disc.GetNumeDisciplina() == 'Istorie'
    
    def TestSetIdDisciplina (self):
        '''
        Testeaza functia de setare a unui id a unui Disciplina
        '''
        disc = Disciplina (12, 'Istorie', 'Marinescu')
        disc.SetIdDisciplina (1)
        assert Disciplina.GetIdDisciplina(disc) == 1    
        
    def TestSetProfesorDisciplina (self):
        '''
        Testeaza functia de setare a unui profesor la o anumita disciplina
        '''
        disc = Disciplina (12,'Mate','Nistor')
        disc.SetProfesorDisciplina('Lostun')
        assert disc.GetProfesorDisciplina() == 'Lostun'
        
    def TestEq (self):
        '''
        Testeaza functia de egalitate dintre noi Disciplinai
        '''
        stud1 = Disciplina (12, 'Mate','Nistor')
        stud2 = Disciplina (25, 'Istorie','Lostun')
        stud3 = Disciplina (12, 'Chimie', 'Fronea')
        if stud1 == stud2:
            assert False
        if stud2 == stud3:
            assert False
        if stud1 == stud3:
            assert True