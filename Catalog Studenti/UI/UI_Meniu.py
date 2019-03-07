'''
Created on Nov 8, 2017

@author: ad
'''
from Domain.Clasa_student import Student
from Domain.Clasa_disciplina import Disciplina
from Domain.Clasa_Nota import Nota
from Utils.Validare_Disciplina import ValidatorDisciplina, ValidationDisciplinaException
from Utils.Validare_Student import ValidatorStudent, ValidationStudentException
from Utils.Validare_Nota import ValidatorNota, ValidationNotaException
from Repository.Repository import RepositoryExceptions

class ComandaMeniu:
    '''
    <numeComanda> <functieComanda>
    '''
    def __init__(self, numeComanda, functComanda):
        '''
        Initializeaza o comanda
        '''
        self.__numeCmd= numeComanda
        self.__functCmd = functComanda
    
    def __str__(self):
        '''
        Returneaza forma in care se afiseaza o comanda
        '''
        return str (self.__numeCmd)
    
    def execute(self):
        '''
        Executa functia unei comenzi date
        '''
        self.__functCmd()


class MenuConsole:
    '''
    Consola pentru meniul de comenzi numerice
    '''
    def __init__(self, StudServ, DiscServ, NotaServ):
        '''
        Initializeaza consola
        '''
        self.__StudServ = StudServ
        self.__DiscServ = DiscServ
        self.__NotaServ = NotaServ
        self.__validatorDisciplina = ValidatorDisciplina()
        self.__validatorStudent = ValidatorStudent()
        self.__validatorNota = ValidatorNota()
        
    def __citesteComanda(self):
        '''
        Returneaza o valoare citita
        '''
        try:
            cmd = int ( input('Introduceti urmatoarea comanda: '))
            return cmd 
        except ValueError:
            raise ValueError ('Comanda invalida!')
        
    
    def __uiAddStudent(self):
        '''
        Adauga un student nou la lista de studenti.
        Id-ul si numele studentului se citesc
        '''
        ids = input ('Id: ')
        nume = input ('Nume: ')
        stud = Student(ids, nume)
        try:
            self.__validatorStudent.ValidareStudent(stud)
            try:
                self.__StudServ.adaugaStudent(stud)
                print('Student adaugat cu succes!')
            except RepositoryExceptions as ve:
                print (ve)
        except ValidationStudentException as ve:
            print (ve)
    
    def __uiAddDisciplina(self):
        '''
        Adauga o noua disciplina la lista de discipline
        Id-ul, nume si profesorul disciplinei se citesc
        '''
        idd = input ('Id: ')
        nume = input ('Nume: ')
        profesor = input ('Profesor: ')
        disc = Disciplina (idd, nume, profesor)
        try:
            self.__validatorDisciplina.ValidareDisciplina(disc)
            try:
                self.__DiscServ.adaugaDisciplina(disc)
                print ('Disciplina adaugata cu succes!')
            except RepositoryExceptions as ve:
                print (ve)
        except ValidationDisciplinaException as ve:
            print (ve)
    
    def __uiAddNota(self):
        '''
        Adauga o noua nota in lista de note
        Id-ul studentului, id-ul disciplinei si calificativul se citesc
        '''
        ids = input ('Id student: ')
        idd = input ('Id disciplina: ')
        calificativ = input ('Calificativ: ')
        stud = Student (ids,'asd')
        disc = Disciplina (idd, 'asd', 'asd')
        Erori = ''
        try:
            self.__validatorNota.ValidareNota(Nota (ids, idd, calificativ))
            if stud not in self.__StudServ.getStudenti(): 
                Erori += 'Student inexistent.'
            if disc not in self.__DiscServ.getDiscipline():
                Erori += 'Disciplina inexistenta.'
            if len(Erori) > 0:
                print (Erori)
            else:
                self.__NotaServ.AdaugaNota(Nota (ids, idd, calificativ))
                print ('Nota adaugata cu succes!')
        except ValidationNotaException as ve:
            print (ve)
        
                
    def __uiPrintStudenti(self):
        '''
        Afiseaza toti studentii existenti in lista de studenti
        '''
        studenti = self.__StudServ.getStudenti()
        for x in studenti:
            print(x)       
             
    def __uiPrintDiscipline(self):
        '''
        Afiseaza toate disciplinele existente in lista de discipline
        '''
        discipline = self.__DiscServ.getDiscipline()
        for x in discipline:
            print (x)
            
    def __uiUpdateStudent(self):
        '''
        Modifica un student vechi din lista de studenti
        Se citesc: id-ul vechi, numele vechi, id-ul nou, numele nou
        '''
        idsVechi = input ('Id: ')
        numeNou = input ('Nume nou: ')
        studVechi = Student (idsVechi, 'asd')
        studNou = Student (idsVechi, numeNou)
        try:
            self.__validatorStudent.ValidareStudent(studVechi)
            self.__validatorStudent.ValidareStudent(studNou)
            try:
                self.__StudServ.updateStudent (studVechi, studNou)
                print('Student modificat cu succes!')
            except RepositoryExceptions as ve:
                print (ve)
        except ValidationStudentException as ve:
            print (ve)
    
    def __uiUpdateDisciplina(self):
        '''
        Actualizeaza o disciplina veche din lista de discipline
        '''
        iddVechi = input ('Id: ')
        numeNou = input ('Nume nou: ')
        profesorNou = input ('Profesor nou: ')
        discVeche = Disciplina (iddVechi, 'ads', 'asd')    
        discNoua = Disciplina (iddVechi, numeNou, profesorNou)
        try:
            self.__validatorDisciplina.ValidareDisciplina(discVeche)
            self.__validatorDisciplina.ValidareDisciplina(discNoua)
            try:
                self.__DiscServ.updateDisciplina(discVeche, discNoua)
                print ('Disciplina modificata cu succes!')
            except RepositoryExceptions as ve:
                print (ve)
        except ValidationDisciplinaException as ve:
            print (ve)
            
    def __uiRemoveStudent(self):
        '''
        Sterge un student dupa id din lista de studenti
        Id-ul se citeste
        '''
        ids = input ('Id: ')
        stud = Student (ids, 'asd')
        try: 
            self.__validatorStudent.ValidareStudent(stud)
            try:
                self.__StudServ.removeStudent (stud)
                self.__NotaServ.RemoveNoteStudent(ids)
                print('Stergerea s-a efectuat cu succes!')
            except RepositoryExceptions as ve:
                print (ve)
        except ValidationStudentException as ve:
            print (ve)
    
    def __uiRemoveDisciplina(self):
        '''
        Sterge o disciplina dupa id din lista de discipline
        Id-ul se citeste
        '''
        idd = input ('Id: ')
        disc = Disciplina (idd, 'asd', 'asd')
        try:
            self.__validatorDisciplina.ValidareDisciplina(disc)
            try:
                self.__DiscServ.removeDisciplina(disc)
                self.__NotaServ.RemoveNoteDisciplina(disc.GetIdDisciplina())
                print ('Stergerea disciplinei s-a realizat cu succes!')
            except RepositoryExceptions as ve:
                print (ve)
        except ValidationDisciplinaException as ve:
            print (ve)
            
    def __uiFindStudent(self):
        '''
        Cauta un student dupa id in lista de studenti
        Id-ul se citeste
        '''
        ids = input ('Id: ')
        stud = Student(ids, 'asd')
        try :
            self.__validatorStudent.ValidareStudent(stud)
            try:
                studCautat = self.__StudServ.findStudent(stud)
                print ('Student cautat: ' + str (studCautat))
            except RepositoryExceptions as ve:
                print (ve)
        except ValidationStudentException as ve:
            print (ve)
    
    def __uiFindDisciplina (self):
        '''
        Cauta o disciplina dupa id in lista de discipline
        Id-ul se citeste
        '''
        idd = input ('Id: ')
        disc = Disciplina (idd, 'asd', 'asd')
        try:
            self.__validatorDisciplina.ValidareDisciplina(disc)
            try:
                discCautata = self.__DiscServ.findDisciplina(disc)
                print ('Disciplina cautata: ' + str (discCautata))
            except RepositoryExceptions as ve:
                print (ve)
        except ValidationDisciplinaException as ve:
            print (ve)       
    
    def __uiPrintDisciplineOrdonate (self):
        '''
        Afiseaza toate disciplinele ordonate dupa nume
        '''
        discOrdonate = self.__DiscServ.getDisciplineSortate()
        for i in range (len (discOrdonate)):
            print(discOrdonate[i])
            
    def __uiPrintNoteStudentiDisciplinaAlfabetic (self):
        '''
        Afiseaza notele tuturor studentilor la o anumita disciplina ordonati in ordine alfabetica
        '''
        idd = input ('Id-ul disciplinei: ')
        try:
            self.__validatorDisciplina.ValidareDisciplina(Disciplina (idd, 'asd', 'asd'))
            listStudenti = self.__StudServ.getStudenti()
            listNoteStudenti = self.__NotaServ.GetNoteStudDiscAlfabetic(idd, listStudenti)
            n = len (listNoteStudenti)
            listStudAlfabetic = sorted(listStudenti, key = lambda Student: Student.GetNumeStudent())
            for stud in range(n):
                noteStud = ''
                for nota in listNoteStudenti[stud]:
                    noteStud += str(nota)
                    noteStud += ' '
                print (listStudAlfabetic[stud], ': ', noteStud)
        except ValidationDisciplinaException as ve:
            print (ve)
            
    def __uiPrintMedieStudent (self):
        '''
        Afiseaza media unui student dupa id
        Id-ul se citeste
        '''
        ids = input ('Id-ul studentului: ')
        stud = Student (ids, 'asd')
        try:
            self.__validatorStudent.ValidareStudent(stud)
            medie = self.__NotaServ.GetMedieStudent(stud)
            print (medie)
        except ValidationStudentException as ve:
            print (ve)
            
    def __uiPrintStudentiSortati (self):
        '''
        Afiseaza lista studentilor sortati astfel:
            - alfabetic crescator dupa nume, daca id-ul studentului este par
            - dupa id descrescator, daca id-ul studentului este impar
        '''
        stud = self.__StudServ.getStudentiOrdonati()
        for i in range (len(stud)):
            print (stud[i])
             
    def __uiPrintTopStudentiMedie(self):
        '''
        Afiseaza top ~20% din studenti dupa media lor
        '''
        listStud = self.__StudServ.getStudenti()
        topStudMedii = self.__NotaServ.GetTopStudentiMedie(listStud)
        for stud in topStudMedii:
            print (stud)
            
    def __uiPrintDiscStud(self):
        '''
        Afiseaza disciplinele la care participa un student
        '''
        ids = input ('Id student: ')
        stud = Student (ids, 'asd')
        try:
            self.__validatorStudent.ValidareStudent(stud)
            listDiscip = self.__DiscServ.getDiscipline()
            listDisc = self.__NotaServ.GetDiscStud(ids, listDiscip)
            if len (listDisc):
                for disc in listDisc:
                    print (disc)
        except ValidationStudentException as ve:
            print (ve)
        
    def __uiPrintMenu(self):
        '''
        Afiseaza meniul de comenzi posibile
        '''
        print ('0. Exit')
        for comanda in self:
            print (self[comanda])
        print ('100. Reafisare meniu')
            
    def run(self):
        '''
        Incepe rularea programului
        '''
        
        comenzi = { 1:ComandaMeniu('1. Adauga un student nou',self.__uiAddStudent), 2:ComandaMeniu ('2. Adauga o disciplina noua',self.__uiAddDisciplina), 
                    3:ComandaMeniu('3. Adauga o nota unui student la o anumita disciplina', self.__uiAddNota),
                    4:ComandaMeniu('4. Modifica datele unui student', self.__uiUpdateStudent), 5:ComandaMeniu('5. Modifica datele unei discipline',self.__uiUpdateDisciplina),
                    6:ComandaMeniu('6. Sterge un student',self.__uiRemoveStudent), 7:ComandaMeniu('7. Sterge o disciplina',self.__uiRemoveDisciplina),
                    8:ComandaMeniu('8. Afiseaza lista de studenti', self.__uiPrintStudenti), 9:ComandaMeniu('9. Afiseaza lista de discipline', self.__uiPrintDiscipline),
                    10:ComandaMeniu('10. Cauta un anumit student dupa id',self.__uiFindStudent), 11:ComandaMeniu('11. Cauta o disciplina dupa id', self.__uiFindDisciplina),
                    12:ComandaMeniu('12. Afiseaza discipline ordonate alfabetic', self.__uiPrintDisciplineOrdonate),
                    13:ComandaMeniu('13. Afiseaza toate notele tuturor studentilor la o anumita disciplina in ordine alfabetica', self.__uiPrintNoteStudentiDisciplinaAlfabetic),
                    14:ComandaMeniu('14. Afiseaza media unui student la toate disciplinele', self.__uiPrintMedieStudent),
                    15:ComandaMeniu('15. Afiseaza studentii ordonati (alfabetic crescator daca id-ul lor este par si dupa id descrescator daca id-ul lor este impar', self.__uiPrintStudentiSortati),
                    16:ComandaMeniu('16. Afiseaza topul studentilor dupa medie', self.__uiPrintTopStudentiMedie),
                    17:ComandaMeniu('17. Afiseaza disciplinele la care un student are note', self.__uiPrintDiscStud)
                    }
        
        MenuConsole.__uiPrintMenu (comenzi)
        
        while True:
            try:
                cmd = self.__citesteComanda()
            except ValueError as ve:
                print (ve)
                continue
            if (cmd == 0):
                break
            if (cmd == 100):
                MenuConsole.__uiPrintMenu(comenzi)
                continue
            if cmd in comenzi:
                comenzi[cmd].execute()
            else:
                print("Comanda indisponibila!")
                
        print ('Rularea programului s-a incheiat cu succes.')
        print ('Programul se va inchide in:')
        import time
        i = 5
        while i:
            print (str(i) , end ='\r')
            time.sleep(1)
            i -= 1
        return