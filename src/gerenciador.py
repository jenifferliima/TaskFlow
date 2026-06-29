# Classe responsável pelo gerenciamento das tarefas.
from tarefas import Tarefa


class Gerenciador:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def cadastrar(self, titulo, descricao, prioridade):
        tarefa = Tarefa(self.proximo_id, titulo, descricao, prioridade)
        self.tarefas.append(tarefa)
        self.proximo_id += 1

    def listar(self):
        return self.tarefas

    def concluir(self, codigo):
        for tarefa in self.tarefas:
            if tarefa.id == codigo:
                tarefa.concluir()
                return True
        return False