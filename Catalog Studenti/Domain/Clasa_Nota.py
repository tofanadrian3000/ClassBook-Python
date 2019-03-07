'''
Created on Nov 15, 2017

@author: ad
'''


class Nota(object):
    
    
    def __init__(self, ids, idd, nota):
        '''
        Initializeaza o nota
        '''
        self.__ids = ids 
        self.__idd = idd 
        self.__nota = nota
        
    def __add__(self, other):
        pass

    def GetIdsNota(self):
        '''
        Returneaza id-ul studentului cui apartine nota
        '''
        return self.__ids


    def GetIddNota(self):
        '''
        Returneaza id-ul disciplinei la care este obtinuta nota
        '''
        return self.__idd


    def GetNota(self):
        '''
        Returneaza nota ce a fost obtinuta
        '''
        return self.__nota


    def SetIdsNota(self, ids):
        '''
        Seteaza id-ul studentului pentru o anumita nota
        '''
        self.__ids = ids


    def SetIddNota(self, idd):
        self.__idd = idd


    def SetNota(self, nota):
        self.__nota = nota


    def __eq__(self, other):
        '''
        Returneaza True daca doua note sunt egale si False in caz contrar
        '''
        if isinstance(other, self.__class__):
            return self.GetIdsNota() == other.GetIdsNota() and self.GetIddNota() == other.GetIddNota()
        else:
            return False
        
    def __lt__(self, other):
        '''
        Returneaza True daca prima nota este mai mica decat a doua si False in caz contrar
        '''
        if isinstance(other, self.__class__):
            return self.__nota < other.__nota 
        else:
            return False
        
    def __str__(self):
        '''
        Returneaza modul in care o nota urmeaza sa fie afisata
        '''
        return str(self.GetNota())


