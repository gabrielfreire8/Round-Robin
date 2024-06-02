from processo import Processo
import random

class Escalonador:
    def __init__(self, quantum):
        self.quantum = quantum
        self.fila = []

    def adicionar_processo(self, processo):
        self.fila.append(processo)

    def criarProcesso(self, num_processos, perc_alto_proc, min_alto_proc, max_alto_proc, min_baixo_proc=0, max_baixo_proc=24):
        for pid in range(1, num_processos+1):
            if(random.random() < perc_alto_proc / 100):
                processamento = random.randint(min_alto_proc, max_alto_proc)
            else:
                processamento = random.randint(min_baixo_proc, max_baixo_proc)
            novo_processo = Processo(pid, tempo_processamento=processamento)
            self.adicionar_processo(novo_processo)
            print(f"Criado: {novo_processo}")

    def proximo_processo(self):
        if self.fila:
            return self.fila.pop(0)
        return None
    
    def retorna_processo(self, processo):
        if processo.tempo_restante > 0:
            self.fila.append(processo)
    
