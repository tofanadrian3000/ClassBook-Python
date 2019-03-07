'''
Created on Nov 15, 2017

@author: ad
'''

from Service.Nota_Service import NotaService
from Repository.Repository_Nota import RepositoryNota
from Domain.Clasa_Nota import Nota
from Domain.Clasa_student import Student
from Service.Student_Service import StudentService
from Repository.Repository import Repository
class TesteNotaService:
    
    def run(self):
        '''
        Ruleaza testele pentru functiile din NotaService
        '''
        self.TestAdaugaNota()
        self.TestRemoveNoteStudent()
        self.TestRemoveNoteDisciplina()
        self.TestGetNoteDisciplinaStudent()
        self.TestGetNoteStudent()
        self.TestGetMedieStudent()
        self.TestGetMedieStudentDisciplina()
        self.TestGetTopMedii()        
        
    def TestAdaugaNota(self):
        '''
        Testeaza functia de initializare a NotaService
        '''
        repo = RepositoryNota ()
        NoteServ = NotaService(repo)
        nota1 = Nota (1,4,7)
        NoteServ.AdaugaNota(nota1)
        assert NoteServ.GetNote() == [nota1]
        nota2 = Nota (2,4,9)
        NoteServ.AdaugaNota(nota2)
        assert NoteServ.GetNote() == [nota1, nota2]
        
    def TestRemoveNoteStudent(self):
        '''
        Testeaza functia de stergere a tuturor notelor unui student
        '''
        repo = RepositoryNota ()
        NoteServ = NotaService (repo)
        nota1 = Nota (1,2,9)
        nota2 = Nota (1,5,10)
        nota3 = Nota (1,2,7)
        nota4 = Nota (1,5,7)
        nota5 = Nota (1,2,8)
        nota6 = Nota (2,2,9)
        nota7 = Nota (2,2,8)
        NoteServ.AdaugaNota(nota1)
        NoteServ.AdaugaNota(nota2)
        NoteServ.AdaugaNota(nota3)
        NoteServ.AdaugaNota(nota4)
        NoteServ.AdaugaNota(nota5)
        NoteServ.AdaugaNota(nota6)
        NoteServ.AdaugaNota(nota7)
        NoteServ.RemoveNoteStudent(1)
        assert NoteServ.GetNote() == [nota6, nota7]
        NoteServ.RemoveNoteStudent(2)
        assert NoteServ.GetNote() == []
    
    def TestRemoveNoteDisciplina(self):
        '''
        Testeaza functia de stergere a tuturor notelor de la o anumita disciplina
        '''
        repo = RepositoryNota ()
        NoteServ = NotaService (repo)
        nota1 = Nota (1,2,9)
        nota2 = Nota (1,5,10)
        nota3 = Nota (1,2,7)
        nota4 = Nota (1,5,7)
        nota5 = Nota (1,2,8)
        nota6 = Nota (2,2,9)
        nota7 = Nota (2,2,8)
        NoteServ.AdaugaNota(nota1)
        NoteServ.AdaugaNota(nota2)
        NoteServ.AdaugaNota(nota3)
        NoteServ.AdaugaNota(nota4)
        NoteServ.AdaugaNota(nota5)
        NoteServ.AdaugaNota(nota6)
        NoteServ.AdaugaNota(nota7)
        NoteServ.RemoveNoteDisciplina(2)
        assert NoteServ.GetNote() == [nota2, nota4]
        NoteServ.RemoveNoteDisciplina(5)
        assert NoteServ.GetNote() == []
    
    def TestGetNoteDisciplinaStudent (self):
        '''
        Testeaza functia de obtinere a tuturor notelor pentru un student la o anumita disciplina
        '''
        repo = RepositoryNota ()
        NoteServ = NotaService (repo)
        nota1 = Nota (1,2,9)
        nota2 = Nota (1,5,10)
        nota3 = Nota (1,2,7)
        nota4 = Nota (1,5,7)
        nota5 = Nota (1,2,8)
        nota6 = Nota (2,2,9)
        nota7 = Nota (2,2,8)
        NoteServ.AdaugaNota(nota1)
        NoteServ.AdaugaNota(nota2)
        NoteServ.AdaugaNota(nota3)
        NoteServ.AdaugaNota(nota4)
        NoteServ.AdaugaNota(nota5)
        NoteServ.AdaugaNota(nota6)
        NoteServ.AdaugaNota(nota7)
        assert NoteServ.GetNoteStudentDisciplina(2, 1) == [nota1, nota3, nota5]
        assert NoteServ.GetNoteStudentDisciplina(5,1) == [nota2, nota4]
        assert NoteServ.GetNoteStudentDisciplina(2, 2) == [nota6, nota7]
        assert NoteServ.GetNoteStudentDisciplina(5,5) == []
        assert NoteServ.GetNoteStudentDisciplina(10, 1) == []
        assert NoteServ.GetNoteStudentDisciplina(17, 20) == []
        
    def TestGetNoteStudent (self):
        '''
        Testeaza functia de obtiere a tuturor notelor unui student 
        '''
        repo = RepositoryNota ()
        nota1 = Nota (1,2,9)
        nota2 = Nota (1,5,10)
        nota3 = Nota (1,2,7)
        nota4 = Nota (1,5,7)
        nota5 = Nota (1,2,8)
        nota6 = Nota (2,2,9)
        nota7 = Nota (2,2,8)
        NoteServ = NotaService (repo)
        NoteServ.AdaugaNota(nota1)
        NoteServ.AdaugaNota(nota2)
        NoteServ.AdaugaNota(nota3)
        NoteServ.AdaugaNota(nota4)
        NoteServ.AdaugaNota(nota5)
        NoteServ.AdaugaNota(nota6)
        NoteServ.AdaugaNota(nota7)
        assert NoteServ.GetNoteStudent(Student(1,'Paul')) == [nota1, nota2, nota3, nota4, nota5]
        assert NoteServ.GetNoteStudent(Student(2,'Adi')) == [nota6, nota7]
        
    def TestGetMedieStudent (self):
        '''
        Testeaza functia de obtinere a mediei unui student 
        '''
        repo = RepositoryNota ()
        NoteServ = NotaService (repo)
        nota1 = Nota (1,2,9)
        nota2 = Nota (1,5,10)
        nota3 = Nota (1,2,7)
        nota4 = Nota (1,5,7)
        nota5 = Nota (1,2,8)
        nota6 = Nota (2,2,9)
        nota7 = Nota (2,2,8)
        NoteServ.AdaugaNota(nota1)
        NoteServ.AdaugaNota(nota2)
        NoteServ.AdaugaNota(nota3)
        NoteServ.AdaugaNota(nota4)
        NoteServ.AdaugaNota(nota5)
        NoteServ.AdaugaNota(nota6)
        NoteServ.AdaugaNota(nota7)
        assert NoteServ.GetMedieStudent(Student(1,'asd')) == 8.2
        assert NoteServ.GetMedieStudent(Student(2,'asd')) == 8.5
        
    def TestGetMedieStudentDisciplina (self):
        '''
        Testeaza functia de obtinere a mediei unui student la o anumita disciplina 
        '''
        repo = RepositoryNota ()
        NoteServ = NotaService (repo)
        nota1 = Nota (1,2,9)
        nota2 = Nota (1,5,10)
        nota3 = Nota (1,2,7)
        nota4 = Nota (1,5,7)
        nota5 = Nota (1,2,8)
        nota6 = Nota (2,2,9)
        nota7 = Nota (2,2,8)
        NoteServ.AdaugaNota(nota1)
        NoteServ.AdaugaNota(nota2)
        NoteServ.AdaugaNota(nota3)
        NoteServ.AdaugaNota(nota4)
        NoteServ.AdaugaNota(nota5)
        NoteServ.AdaugaNota(nota6)
        NoteServ.AdaugaNota(nota7)
        assert NoteServ.GetMedieStudentDisc(1, 2) == 8
        assert NoteServ.GetMedieStudentDisc(1,5) == 8.5
        assert NoteServ.GetMedieStudentDisc(2,2) == 8.5
        
    def TestGetTopMedii (self):
        '''
        Testeaza functia de obtinere a mediilor in ordine descrescatoare
        '''
        repo = RepositoryNota ()
        NoteServ = NotaService (repo)
        StudServ = StudentService(Repository())
        StudServ.adaugaStudent(Student(1,'asd'))
        StudServ.adaugaStudent(Student(2,'asd'))
        nota1 = Nota (1,2,9)
        nota2 = Nota (1,5,10)
        nota3 = Nota (1,2,7)
        nota4 = Nota (1,5,7)
        nota5 = Nota (1,2,8)
        nota6 = Nota (2,2,9)
        nota7 = Nota (2,2,8)
        NoteServ.AdaugaNota(nota1)
        NoteServ.AdaugaNota(nota2)
        NoteServ.AdaugaNota(nota3)
        NoteServ.AdaugaNota(nota4)
        NoteServ.AdaugaNota(nota5)
        NoteServ.AdaugaNota(nota6)
        NoteServ.AdaugaNota(nota7)
        listNote = NoteServ.GetNote()
        listStud = StudServ.getStudenti()
        assert NoteServ.GetTopMedii(listNote, listStud) == [8.5, 8.2]
  