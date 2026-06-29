from src.tarefas import Tarefa


def test_criar_tarefa():
    tarefa = Tarefa(1, "Estudar Python", "Fazer exercícios", "Alta")

    assert tarefa.id == 1
    assert tarefa.titulo == "Estudar Python"
    assert tarefa.descricao == "Fazer exercícios"
    assert tarefa.prioridade == "Alta"
    assert tarefa.concluida is False


def test_concluir_tarefa():
    tarefa = Tarefa(1, "Estudar Python", "Fazer exercícios", "Alta")

    tarefa.concluir()

    assert tarefa.concluida is True