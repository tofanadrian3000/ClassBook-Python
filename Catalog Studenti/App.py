
from Tests.Teste import Teste
from Repository.Repository import Repository
from Service.Student_Service import StudentService
from Service.Disciplina_Service import DisciplinaService
from UI.UI_Meniu import MenuConsole
from Repository.Repository_Nota import RepositoryNota
from Service.Nota_Service import NotaService

teste = Teste()
teste.runTeste()
Repo1 = Repository ()
Repo2 = Repository ()
Repo3 = RepositoryNota ()
ComenziStud = StudentService(Repo1)
ComenziDisc = DisciplinaService (Repo2)
ComenziNota = NotaService (Repo3)
Console = MenuConsole (ComenziStud, ComenziDisc, ComenziNota)
Console.run()