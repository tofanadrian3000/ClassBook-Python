'''
Created on Nov 8, 2017

@author: ad
'''
class Disciplina:
    '''
     <idDisciplina>, <nume>, <profesor>
    '''
    __Numar_discipline = 0
    
    def __init__(self, idd, nume, profesor):
        '''
        Initializeaza o disciplina
        idd - id-ul disciplinei
        nume - numele disciplinei
        profesor - profesorul disciplinei
        '''
        self.__idd = idd
        self.__nume = nume
        self.__profesor = profesor
        Disciplina.__Numar_discipline += 1
        
    def __str__(self):
        '''
        Returneaza disciplina cautata pentru afisare
        '''
        return str ( str (self.__idd) + ' ' + self.__nume + ' ' + self.__profesor)
    
    def __eq__(self, other):
        '''
        Verifica daca doua elemente sunt egale
        '''
        if isinstance (other, self.__class__):
            return self.__idd == other.__idd
        return False
            
    
    def GetIdDisciplina (self):
        '''
        Obtine si returneaza id-ul unei discipline
        '''
        return self.__idd
    
    def GetNumeDisciplina (self):
        '''
        Obtine si returneaza numele unei discipline
        '''
        return self.__nume
    
    def GetProfesorDisciplina (self):
        '''
        Obtine si returneaza profesorul unei discipline
        '''
        return self.__profesor
    
    def SetIdDisciplina (self, idd):
        '''
        Seteaza id-ul unei discipline
        idd - id-ul disciplinei ce va fi atribuit acesteia
        '''
        self.__idd = idd
        
    def SetNumeDisciplina (self, nume):
        '''
        Seteaza numele unei discipline
        nume - numele disciplinei ce va fi atribuit acesteia
        '''
        self.__nume = nume
        
    def SetProfesorDisciplina (self, profesor):
        '''
        Seteaza profesorul unei discipline
        profesor - profesorul disciplinei ce va fi atribut acesteia
        '''
        self.__profesor = profesor
        
    
            