'''
Created on Nov 7, 2017

@author: ad
'''

from Tests.Test_Validare_Disciplina import TesteValidareDisciplina
from Tests.Test_Validare_Student import TesteValidareStudent
from Tests.Test_Validare_Nota import TesteValidareNota
from Tests.Test_Validare_Date import TesteValidareDate
from Tests.Test_Clasa_Student import TesteStudent
from Tests.Test_Clasa_Disciplina import TesteDisciplina
from Tests.Test_Repository import TesteRepository
from Tests.Test_Student_Service import TesteStudentService
from Tests.Test_Disciplina_Service import TesteDisciplinaService
from Tests.Test_Clasa_Nota import TesteNota
from Tests.Test_Nota_Service import TesteNotaService
from Tests.Test_Repository_Nota import TesteRepositoryNota

class Teste ():
    '''
    Contine toate functiile de test din cadrul programului
    '''
    def __init__(self):
        '''
        Initializeaza testele
        '''
        self.__testeValidareDate = TesteValidareDate()
        self.__testeValidareDisciplina = TesteValidareDisciplina()
        self.__testeValidareStudent = TesteValidareStudent()
        self.__testeValidareNota = TesteValidareNota()
        self.__testeClasaStudent = TesteStudent ()
        self.__testeClasaDisciplina = TesteDisciplina ()
        self.__testeRepository = TesteRepository ()
        self.__testeStudentService = TesteStudentService ()
        self.__testeDisciplinaService = TesteDisciplinaService ()
        self.__testeClasaNota = TesteNota ()
        self.__testeRepositoryNota = TesteRepositoryNota ()
        self.__testeNotaService = TesteNotaService()
        
    def runTeste(self):
        '''
        Ruleaza toate testele
        '''
        self.__testeValidareDate.run()
        self.__testeValidareDisciplina.run()
        self.__testeValidareStudent.run()
        self.__testeValidareNota.run()
        self.__testeClasaStudent.run()
        self.__testeClasaDisciplina.run()
        self.__testeRepository.run()
        self.__testeStudentService.run()
        self.__testeDisciplinaService.run()
        self.__testeClasaNota.run()
        self.__testeRepositoryNota.run()
        self.__testeNotaService.run()