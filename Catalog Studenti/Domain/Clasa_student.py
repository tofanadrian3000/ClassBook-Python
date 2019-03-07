'''
Created on Nov 7, 2017

@author: ad
'''
class Student:
    '''
    student : <Nume_student> , <id_Student>
    '''
    __Numar_studenti = 0
    
    def __init__(self, ids, nume):
        '''
        Initializeaza un student
        '''
        self.__ids = ids
        self.__nume = nume
        Student.__Numar_studenti += 1
        
    def __str__(self):
        '''
        Returneaza modul in care se afiseaza un student
        '''
        return str (str (self.__ids) + '.' + self.__nume)
    
    def __eq__ (self, other):
        '''
        Verifica daca id-urile a doi studenti sunt egale
        '''
        if isinstance (other, self.__class__):
            return self.__ids == other.__ids
        return False
        
    def GetNumeStudent (self):
        '''
        Returneaza numele studentului
        '''
        return str(self.__nume)
           
    def GetIdStudent (self):
        '''
        Returneaza id-ul studentului
        '''
        return self.__ids
    
    def SetNumeStudent (self, nume):
        '''
        Atribuie un nume studentului
        nume - numele studentului ce va fi atribuit acestuia
        '''
        self.__nume = str(nume)
        
    def SetIdStudent(self, ids):
        '''
        Atribuie un id studentului
        ids - id-ul studentului ce va fi atribuit acestuia
        '''
        self.__ids = int (ids)
