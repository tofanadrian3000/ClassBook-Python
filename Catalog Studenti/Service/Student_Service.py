'''
Created on Nov 8, 2017

@author: ad
'''
from Repository.Repository import RepositoryExceptions

class StudentService:
    
    def __init__(self, repository):
        '''
        Initializeaza controlorul pentru studenti
        '''
        self.__repo = repository
    
    def adaugaStudent(self, stud):
        '''
        Adauga un student nou la lista de studenti
        '''
        try:
            self.__repo.add(stud)
        except RepositoryExceptions as ve:
            raise RepositoryExceptions (ve)
        
    
    def updateStudent(self, studVechi, studNou):
        '''
        Modifica un datele unui student din lista
        '''
        try:
            self.__repo.update(studVechi, studNou)
        except RepositoryExceptions as ve:
            raise RepositoryExceptions (ve)
        
    def removeStudent(self, stud):
        '''
        Sterge un student din lista de studenti
        '''
        try:
            self.__repo.removeEl(stud)
        except RepositoryExceptions as ve:
            raise RepositoryExceptions (ve)
            
    def findStudent(self, stud):
        '''
        Verifica daca un student se regaseste in lista de studenti
        '''
        try:
            return self.__repo.find(stud)
        except RepositoryExceptions as ve:
            raise RepositoryExceptions (ve)
            
    def numarStudenti(self):
        '''
        Returneaza numarul de studenti
        '''
        return len(self.__repo)
    
    def getStudenti(self):
        '''
        Returneaza intreaga lista de studenti
        '''
        return self.__repo.getAll()
    
    def getStudentiOrdonati(self):
        '''
        Returneaza lista de studenti sortati astfel:
            - daca id-ul studentului este par - alfabetic crescator
            - daca id-ul studentului este impar - dupa id descrescator
        '''
        stud = self.getStudenti()
        for i in range (len(stud)-1):
            if int (stud[i].GetIdStudent()) % 2 == 1:
                for j in range (i+1, len(stud)):
                    if int(stud[j].GetIdStudent()) % 2 == 1:
                        if int(stud[i].GetIdStudent()) < int(stud[j].GetIdStudent()):
                            aux = stud[i]
                            stud[i] = stud[j]
                            stud[j] = aux  
            elif int (stud[i].GetIdStudent()) % 2 == 0:
                for j in range(i+1, len(stud)):
                    if int (stud[j].GetIdStudent()) % 2 == 0:
                        if stud[i].GetNumeStudent() > stud[j].GetNumeStudent():
                            aux = stud[i]
                            stud[i] = stud[j]
                            stud[j] = aux
        return stud