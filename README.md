# TaskFlow

## Descrição

O TaskFlow é um sistema de gerenciamento de tarefas desenvolvido em Python para a disciplina de Engenharia de Software. O sistema permite cadastrar, listar e concluir tarefas por meio de um menu executado no terminal.

## Funcionalidades

- Cadastrar tarefas
- Listar tarefas
- Concluir tarefas
- Definir prioridade (Baixa, Média ou Alta)
- Identificação automática das tarefas por ID

## Estrutura do Projeto

```
TaskFlow/
│
├── .github/
│   └── workflows/
│       └── python.yml
├── docs/
├── src/
│   ├── app.py
│   ├── gerenciador.py
│   └── tarefas.py
├── tests/
│   └── test_tarefas.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Tecnologias Utilizadas

- Python 3
- PyTest
- GitHub
- GitHub Actions

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o programa:

```bash
python src/app.py
```

3. Execute os testes:

```bash
pytest
```

## Autor

Projeto desenvolvido para a disciplina de Engenharia de Software.