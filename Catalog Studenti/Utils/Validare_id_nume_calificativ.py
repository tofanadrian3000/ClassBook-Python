'''
Created on Nov 15, 2017

@author: ad
'''
class Validator:
    
    def ValidareNume (self, nume):
        '''
        Valideaza un nume
        '''
        corect = True
        for i in nume:
            if i in ['0','1','2','3','4','5','6','7','8','9']:
                corect = False
        if corect == True:
            nume_corect = nume.split ()
            if len (nume_corect) == 0:
                return False
        else:
            return False
        return True
    
    def ValidareId (self,idg):
        '''
        Valideaza un id
        '''
        try:
            if int (idg) < 0:
                return False
        except ValueError:
            return False
        return True
    
    def ValidareCalificativ (self, nota):
        '''
        Valideaza un calificativ
        '''
        try:
            n = float(nota)
            if n <= 0 or n > 10:
                return False
            else:
                return True
        except ValueError:
            return False