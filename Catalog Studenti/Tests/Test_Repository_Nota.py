'''
Created on Nov 10, 2017

@author: ad
'''
from Repository.Repository_Nota import RepositoryNota

class TesteRepositoryNota:
    '''
    Contine testele pentru functiile din Repository
    '''
    
    def run(self):
        '''
        Ruleaza toate testele pentru functiile din Repository
        '''
        self.TestAdd()
        self.TestInit()
        self.TestRemove()
        self.TestLen()

    def TestInit (self):
        '''
        Testeaza functia de initializare 
        '''
        repo = RepositoryNota ()
        assert repo.getAll() == []
                
    def TestAdd (self):
        '''
        Testeaza functia de adaugare a unui element 
        '''
        repo = RepositoryNota ()
        repo.add(1)
        assert repo.getAll() == [1]
        repo.add(2)
        assert repo.getAll() == [1,2]
        repo.add(1)
        assert repo.getAll() == [1,2,1]
            
    def TestRemove(self):
        '''
        Testeaza functia de adaugare a unui element
        '''
        repo = RepositoryNota ()
        repo.add(1)
        repo.add(2)
        repo.removeEl(1)
        assert repo.getAll() == [2]
        repo.removeEl(2)
        assert repo.getAll() == []
        
    def TestLen(self):
        '''
        Testeaza functia de lungime a listei de elemente 
        '''
        repo = RepositoryNota ()
        assert len(repo) == 0
        repo.add(1)
        assert len(repo) == 1