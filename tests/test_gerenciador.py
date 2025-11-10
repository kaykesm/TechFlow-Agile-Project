import unittest
from src.gerenciador import GerenciadorTarefas

class TestGerenciadorTarefas(unittest.TestCase):
    def setUp(self):
        self.g = GerenciadorTarefas()

    def test_adicionar_tarefa(self):
        self.g.adicionar_tarefa("Estudar Python")
        self.assertEqual(len(self.g.tarefas), 1)

    def test_concluir_tarefa(self):
        self.g.adicionar_tarefa("Estudar GitHub")
        self.g.concluir_tarefa(0)
        self.assertTrue(self.g.tarefas[0]["concluida"])

    def test_listar_tarefas(self):
        self.g.adicionar_tarefa("Aprender testes automatizados")
        resultado = self.g.listar_tarefas()
        self.assertIn("Aprender testes automatizados", resultado)

if __name__ == "__main__":
    unittest.main()
