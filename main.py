from processo import Processo
from escalonador import Escalonador
from processador import Processador
import time

#criar uma instancia do escalonador com um quantum
escalonador = Escalonador(quantum=75)

#adicionar processos na fila do escalonador

#escalonador.adicionar_processo(Processo(2, 125))
escalonador.criarProcesso(num_processos=1000, perc_alto_proc=30, min_alto_proc=100, max_alto_proc=200, min_baixo_proc=10, max_baixo_proc=60)


#criar o processador
processador = Processador(escalonador)

#medir tempo de execucao
inicio = time.perf_counter()
processador.executar()
fim = time.perf_counter()

#calcular e imprimir o tempo de execucao
tempo_execucao = fim - inicio
print(f"Tempo de execucao do escalonamento: {tempo_execucao:.4f} segundos")