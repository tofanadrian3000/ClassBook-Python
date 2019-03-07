'''
Created on Nov 8, 2017

@author: ad
'''
from Repository.Repository import RepositoryExceptions

class DisciplinaService:
    
    def __init__(self, repository):
        '''
        Initializeaza controlorul pentru discipline
        '''
        self.__repo = repository
    
    def adaugaDisciplina (self, disc):
        '''
        Adauga o noua disciplina la lista existenta
        '''
        try:
            self.__repo.add(disc)
        except RepositoryExceptions as ve:
            raise RepositoryExceptions (ve)
        
    def updateDisciplina(self, discVeche, discNoua):
        '''
        Modifica o disciplina existenta in lista
        '''
        try:
            self.__repo.update(discVeche, discNoua)
        except RepositoryExceptions as ve:
            raise RepositoryExceptions (ve)

    def removeDisciplina(self, disc):
        '''
        Sterge o disciplina din lista de disciplini
        '''
        try:
            self.__repo.removeEl(disc)
        except RepositoryExceptions as ve:
            raise RepositoryExceptions (ve)
        
    def findDisciplina(self, disc):
        '''
        Verifica daca o disciplina se regaseste in lista de discipline
        '''
        try:
            return self.__repo.find(disc)
        except RepositoryExceptions as ve:
            raise RepositoryExceptions (ve)
        
    def numarDiscipline(self):
        '''
        Returneaza numarul de discipline existente in lista
        '''
        return len(self.__repo)
    
    def getDiscipline(self):
        '''
        Returneaza intreaga lista de discipline
        '''
        return self.__repo.getAll()
    
    def getDisciplineSortate (self):
        '''
        Determina disciplinele ordonate alfabetic
        '''
        disc = self.getDiscipline()
        disciplineOrdonate = sorted (disc, key = lambda Disciplina: Disciplina.GetNumeDisciplina())
        return disciplineOrdonate[:]