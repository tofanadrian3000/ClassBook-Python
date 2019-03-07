'''
Created on Nov 10, 2017

@author: ad
'''
from Repository.Repository import Repository, RepositoryExceptions

class TesteRepository:
    '''
    Contine testele pentru functiile din Repository
    '''

    def TestInit (self):
        '''
        Testeaza functia de initializare 
        '''
        repo = Repository ()
        assert repo.getAll() == []
        
    def run(self):
        '''
        Ruleaza toate testele pentru functiile din Repository
        '''
        self.TestAdd()
        self.TestInit()
        self.TestRemove()
        self.TestUpdate()
        self.TestFind()
        
    def TestAdd (self):
        '''
        Testeaza functia de adaugare unui element 
        '''
        repo = Repository ()
        repo.add(1)
        assert repo.getAll() == [1]
        repo.add(2)
        assert repo.getAll() == [1,2]
        try:
            repo.add(1)
            assert False
        except RepositoryExceptions:
            assert True
            
    def TestRemove (self):
        '''
        Testeaza functia de stergere a unui element din Repository
        '''
        repo = Repository ()
        try:
            repo.removeEl(1)
            assert False
        except RepositoryExceptions:
            assert True
        repo.add (1)
        repo.add (2)
        repo.add (3)
        repo.removeEl(1)
        assert repo.getAll() == [2,3]
        repo.removeEl(3)
        assert repo.getAll() == [2]
    
    def TestUpdate (self):
        '''
        Testeaza functia de actualizare a unui element din Repository
        '''
        repo = Repository ()
        try:
            repo.update(1,2)
            assert False
        except RepositoryExceptions:
            assert True
        repo.add (1)
        repo.add (2)
        repo.add (3)
        repo.update (1,5)
        assert repo.getAll() == [5,2,3]
        repo.update (2,9)
        assert repo.getAll() == [5,9,3]
        
    def TestFind (self):
        '''
        Testeaza functia de cautare a unui element din Repository
        '''
        repo = Repository ()
        try:
            repo.find(1)
            assert False
        except RepositoryExceptions:
            assert True
        repo.add (1)
        assert repo.find(1) == 1
    