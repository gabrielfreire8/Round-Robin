from escalonador import Escalonador

class Processador:
    def __init__(self, escalonador):
        self.escalonador = escalonador

    def executar(self):
        tempo_atual = 0
        processo = self.escalonador.proximo_processo()

        while processo:
            tempo_executado = min(processo.tempo_restante, self.escalonador.quantum)
            processo.tempo_restante -= tempo_executado
            tempo_atual += tempo_executado

            print(f"Executando {processo}")
            processo.tempo_processamento = processo.tempo_restante

            if processo.tempo_restante > 0:
                self.escalonador.retorna_processo(processo)

            processo = self.escalonador.proximo_processo()