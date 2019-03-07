'''
Created on Nov 15, 2017

@author: ad
'''


class NotaService:
    
    def __init__(self, repo):
        '''
        Initializeaza NotaService
        '''
        self.__repo = repo 

    
    def AdaugaNota(self, nota):
        '''
        Adauga o noua nota la lista de note
        '''
        self.__repo.add (nota)
        
    def GetNote(self):
        '''
        Returneaza toate notele
        '''
        return self.__repo.getAll()
    
    def GetNoteStudent(self, stud):
        '''
        Returneaza toate notele unui student
        '''
        note = self.GetNote()
        note_stud = []
        for nota in note:
            if nota.GetIdsNota() == stud.GetIdStudent():
                note_stud.append(nota)
        return note_stud
    
    def GetNoteStudentDisciplina (self, idd, ids):
        '''
        Returneaza toate notele tuturor studentilor la o anumita disciplina
        idd - id-ul disciplinei 
        '''
        note = self.GetNote()
        noteStud = []
        for nota in note:
            if nota.GetIddNota() == idd and nota.GetIdsNota() == ids:
                noteStud.append (nota)
        noteStud = sorted(noteStud, reverse = True, key = lambda Nota: Nota.GetNota())
        return noteStud
    
    def GetNoteStudDiscAlfabetic (self, idd, listStudenti):
        '''
        Returneaza toate notele tuturor studentilor ordonati alfabetic la o anumita disciplina
        '''
        listStudAlfabetic = sorted (listStudenti, key = lambda Student: Student.GetNumeStudent())
        listStudNote = []
        for stud in listStudAlfabetic:
            studNote = self.GetNoteStudentDisciplina(idd, stud.GetIdStudent())
            listStudNote.append(studNote)
        return listStudNote
    
    def RemoveNoteStudent(self, ids):
        '''
        Sterge toate notele pentru un anumit student
        '''
        note = self.GetNote()
        for nota in note:
            if nota.GetIdsNota() == ids:
                self.__repo.removeEl(nota)
                
    def RemoveNoteDisciplina(self,idd):
        '''
        Sterge toate notele pentru o anumita disciplina
        '''
        note = self.GetNote()
        for nota in note:
            if nota.GetIddNota() == idd:
                self.__repo.removeEl(nota)
    
    def GetMedieStudent (self, stud):
        '''
        Returneaza media unui student la toate disciplinele
        '''
        note = self.GetNoteStudent(stud)
        Suma = 0
        for nota in note:
            Suma += float (nota.GetNota())
        if len(note):
            Suma /= len(note)
        return Suma
    
    def GetMedieStudentDisc(self, ids, idd):
        '''
        Returneaza media unui student la o anumita disciplina 
        '''
        noteStudDisc = self.GetNoteStudentDisciplina(idd, ids)
        Suma = 0
        for nota in noteStudDisc:
            Suma += float(nota.GetNota())
        return Suma/(len(noteStudDisc))
    
    def GetTopMedii (self, listNote, listStud):
        '''
        Returneaza mediile in ordine descrescatoare
        '''
        medii = []
        for stud in listStud:
            medii.append(self.GetMedieStudent(stud))
        medii = sorted (medii,reverse = True, key = lambda medii: medii)
        return medii

    def GetTopStudenti (self, listStud):
        '''
        Returneaza studentii ordonati dupa medie dupa medie
        '''
        for i in range (len(listStud)-2):
            for j in range (i+1, len(listStud)-1):
                if self.GetMedieStudent(listStud[i]) < self.GetMedieStudent(listStud[j]):
                    aux = listStud[i]
                    listStud[i] = listStud[j]
                    listStud[j] = aux
        return listStud
    
    def GetTopStudentiMedie (self, listStud):
        '''
        Returneaza primii ~20% din studenti ordonati dupa medie, continuand numele si media lor 
        '''
        note = self.GetNote()
        topStud = self.GetTopStudenti(listStud)
        topMedii = self.GetTopMedii(note, listStud)
        topStudMedii = []
        for i in range (len(topStud)//5 + 1):
            topStudMedii.append(str(topStud[i])+ ': '+ str (topMedii[i]))
        return topStudMedii
    
    def GetIddDiscStud (self, ids):
        '''
        Returneaza lista de id-uri ale disciplinelor la care un student are note
        '''
        note = self.GetNote()
        listIddDisc = []
        for nota in note:
            if nota.GetIdsNota() == ids:
                if nota.GetIddNota() not in listIddDisc:
                    listIddDisc.append(nota.GetIddNota())
        return listIddDisc
    
    def GetDiscStud (self, ids, listDiscip):
        '''
        Returneaza lista de discipline la care un student are note
        '''
        listIddDisc = self.GetIddDiscStud(ids)
        listDisc = []
        for iddDisc in listIddDisc:
            for Discip in listDiscip:
                if Discip.GetIdDisciplina() == iddDisc:
                    listDisc.append(Discip)
        return listDisc
                        