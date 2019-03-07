'''
Created on Nov 12, 2017

@author: ad
'''
from Repository.Repository import Repository, RepositoryExceptions
from Service.Disciplina_Service import DisciplinaService
from Domain.Clasa_disciplina import Disciplina

class TesteDisciplinaService:
    '''
    Contine toate testele functiilor pentru DisciplinaService
    '''
    def run(self):
        '''
        Ruleaza testele functiilor din RepositoryExceptions
        '''
        self.TestInit()
        self.TestAdaugaDisciplina()
        self.TestUpdateDisciplina()
        self.TestRemoveDisciplina()
        self.TestDeterminareDisciplineOrdonateAlfabetic()
    
    def TestInit(self):
        '''
        Testeaza functia de initializare a unei DisciplinaService 
        '''
        repo = Repository()
        DiscCtrl = DisciplinaService (repo)
        assert DiscCtrl.getDiscipline() == []
        
    def TestAdaugaDisciplina (self):
        '''
        Testeaza functia de adaugare a unei discipline
        '''
        repo = Repository()
        DiscCtrl = DisciplinaService (repo)
        disc = Disciplina (1,'Mate','Nistor')
        DiscCtrl.adaugaDisciplina(disc)
        assert DiscCtrl.getDiscipline() == [disc]
        disc2 = Disciplina (2, 'Istorie', 'Lostun')
        DiscCtrl.adaugaDisciplina(disc2)
        assert DiscCtrl.getDiscipline () == [disc, disc2]
        disc3 = Disciplina (1, 'Fizica', 'Bejan')
        try:
            DiscCtrl.adaugaDisciplina(disc3)
            assert False
        except RepositoryExceptions:
            assert True
            
    def TestUpdateDisciplina (self):
        '''
        Testeaza functia de actualizare a unui discipline
        '''
        repo = Repository ()
        DiscCtrl = DisciplinaService (repo)
        discVeche = Disciplina (1,'Mate','Nistor')
        DiscCtrl.adaugaDisciplina(discVeche)
        discNoua = Disciplina (1, 'Istorie', 'Lostun')
        DiscCtrl.updateDisciplina(discVeche, discNoua)
        assert DiscCtrl.getDiscipline() == [discNoua]
        try:
            DiscCtrl.updateDisciplina(Disciplina(3,'Istorie','Marin'), Disciplina (3,'Mate','Nistor')) 
            assert False
        except RepositoryExceptions:
            assert True
            
    def TestRemoveDisciplina (self):
        '''
        Testeaza functia de stergere a unei discipline
        '''
        repo = Repository ()
        DiscCtrl = DisciplinaService (repo)
        DiscCtrl.adaugaDisciplina(Disciplina (1,'Mate','Lostun'))
        DiscCtrl.removeDisciplina(Disciplina (1,'Mate','Lostun'))
        try:
            DiscCtrl.removeDisciplina( Disciplina (2,'Istorie','Pasvante'))
            assert False
        except RepositoryExceptions:
            assert True
            
    def TestDeterminareDisciplineOrdonateAlfabetic (self):
        '''
        Testeaza functia de determinare a disciplinelor ordonate alfabetic
        '''
        repo = Repository()
        DiscCtrl = DisciplinaService (repo)
        DiscCtrl.adaugaDisciplina(Disciplina (1,'Mate','Nistor'))
        DiscCtrl.adaugaDisciplina(Disciplina (2,'Istorie','Lostun'))
        DiscCtrl.adaugaDisciplina(Disciplina (3,'Analiza','Berinde Stefan'))
        DiscCtrl.adaugaDisciplina(Disciplina (4,'Fizica','Bejan'))
        disciplineOrdonate = DiscCtrl.getDisciplineSortate()
        assert disciplineOrdonate == [Disciplina (3,'Analiza','Berinde Stefan'), Disciplina(4,'Fizica','Bejan'), Disciplina (2,'Istorie','Lostun'), Disciplina (1, 'Mate','Nistor')]