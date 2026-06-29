class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade="Média"):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return (
            f"[{self.id}] {self.titulo}\n"
            f"Descrição: {self.descricao}\n"
            f"Prioridade: {self.prioridade}\n"
            f"Status: {status}\n"
        )