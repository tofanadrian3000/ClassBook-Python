'''Created on Nov 15, 2017

@author: ad
'''
from Domain.Clasa_Nota import Nota

class TesteNota:
    
    def run(self):
        '''
        Ruleaza testele pentru functiile din clasa nota
        '''
        self.TestInit()
        self.TestEq()
        self.TestStr()
        self.TestLt()
        
        
    def TestInit(self):
        '''
        Testeaza functiile de initializare, get-urile si set-urile a unei note 
        '''
        n = Nota (1, 2, 9.5)
        assert n.GetIdsNota() == 1
        assert n.GetIddNota() == 2
        assert n.GetNota() == 9.5
        n.SetIddNota(4)
        assert n.GetIddNota() == 4
        n.SetIdsNota(10)
        assert n.GetIdsNota() == 10
        n.SetNota(7.4)
        assert n.GetNota() == 7.4
        
    def TestEq (self):
        '''
        Testeaza functia de egalitate intre doua note
        '''
        assert Nota(1, 1, 10) != Nota (2, 5, 10)
        assert Nota(1, 1, 5) == Nota (1, 1, 7)
        
    def TestStr (self):
        '''
        Testeaza functia de conversie in string a unei nota
        '''
        n = Nota (1,1,10)
        assert str (n) == '10'
        
    def TestLt (self):
        '''
        Testeaza functia de stabilire a unei note mai mici decat alta
        '''
        assert Nota(1,2,8) < Nota (5,6,8.1)
        assert Nota(1,1,10) > Nota (1,1,9.9)