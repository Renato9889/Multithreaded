#Renato Luiz de Almeida - Trabalho 1 de Sistemas Operacionais
#É importada a bliblioteca nativa do Python de Threadings
import threading
#Variavel Global para realizar os calculos
global var
var = 3
#É feita um classe de modelo de thread
class modelothread(threading.Thread):
    def __init__(self, indent, palavra, ctd):
        threading.Thread.__init__(self)
        self.indent = indent
        self.palavra = palavra
        self.ctd = ctd
    def run(self):
        print ("Iniciando thread %s com %d processos " % (self.palavra,self.ctd))
        processo(self.palavra, self.ctd,self.indent)
        print ("Finalizando " + self.palavra)
#Aqui é feito uma função que é o processo da thread
def processo(palavra, cont,calq):
    while cont:
        if calq == 1:
            print("A Thread %s está realizando o processo %d : (%d x %d = %d )" % (palavra, cont,var,cont,(var*cont)))
            cont -= 1
        elif calq == 2:
            print("A Thread %s está realizando o processo %d : (%d ^ %d = %d )" % (palavra, cont,cont,var,(cont**var)))
            cont -= 1
        else:
            print("A Thread %s está realizando o processo %d: (%d / %d = %.2f)" % (palavra, cont,cont,var,(cont/var)))
            cont -= 1

# Nessa parte será criada as threads
thread1 = modelothread(1, "Multiplicação", 230)
thread2 = modelothread(2, "Potenciação", 190)
thread3 = modelothread(3, "Divisão", 200)
# Aqui elas são inicializadas
thread1.start()
thread2.start()
thread3.start()
# Aqui elas são Finalizadas e o programa encerrado
threads = []
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
for t in threads:
    t.join()
print ("Todos os Processos Finalizados")