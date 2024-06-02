class Processo:
    def __init__(self, pid, tempo_processamento):
        self.pid = pid
        self.tempo_processamento = tempo_processamento
        self.tempo_restante = tempo_processamento

    def __str__(self):
        return f"Processo {self.pid}, Tempo de Processamento {self.tempo_processamento}, Tempo Restante {self.tempo_restante}"
    