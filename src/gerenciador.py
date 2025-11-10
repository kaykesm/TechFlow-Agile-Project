class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        self.tarefas.append({"descricao": descricao, "concluida": False})

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["concluida"] = True

    def listar_tarefas(self):
        lista = []
        for i, tarefa in enumerate(self.tarefas):
            status = "✔️" if tarefa["concluida"] else "❌"
            lista.append(f"{i+1}. {tarefa['descricao']} {status}")
        return "\n".join(lista)

