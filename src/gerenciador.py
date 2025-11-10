from typing import List, Dict

tarefas: List[Dict] = []

def reset_tarefas():
    """Zera a lista - útil para testes."""
    global tarefas
    tarefas = []

def criar_tarefa(nome: str, prioridade: int = 3) -> Dict:
    """Cria uma tarefa com nome, prioridade e status inicial 'A Fazer'."""
    tarefa = {
        "id": len(tarefas),
        "nome": nome,
        "prioridade": prioridade,
        "status": "A Fazer"
    }
    tarefas.append(tarefa)
    return tarefa

def listar_tarefas() -> List[Dict]:
    """Retorna a lista de tarefas."""
    return tarefas.copy()

def atualizar_status(task_id: int, novo_status: str) -> bool:
    """Atualiza status de uma tarefa. Retorna True se atualizado, False se não encontrado."""
    for t in tarefas:
        if t["id"] == task_id:
            t["status"] = novo_status
            return True
    return False

def excluir_tarefa(task_id: int) -> bool:
    """Exclui a tarefa com id dado. Retorna True se excluiu, False se não encontrou."""
    global tarefas
    nova = [t for t in tarefas if t["id"] != task_id]
    if len(nova) == len(tarefas):
        return False
    # reindexa ids
    for idx, t in enumerate(nova):
        t["id"] = idx
    tarefas = nova
    return True
