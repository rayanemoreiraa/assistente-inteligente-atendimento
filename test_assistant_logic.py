import unittest
from assistant_logic import demo_reply


class AssistantLogicTests(unittest.TestCase):
    def test_delivery(self):
        self.assertIn("status", demo_reply("Minha entrega está atrasada").lower())

    def test_refund(self):
        self.assertIn("reembolso", demo_reply("Meu reembolso não caiu").lower())

    def test_human_request_takes_priority(self):
        answer = demo_reply("Minha entrega atrasou e quero falar com uma pessoa de verdade")
        self.assertIn("não consegue transferir", answer.lower())

    def test_human_without_accents(self):
        answer = demo_reply("quero falar com alguem, ja tentei resolver")
        self.assertIn("atendimento", answer.lower())
        self.assertIn("protocolo", answer.lower())

    def test_access_safety(self):
        answer = demo_reply("Esqueci minha senha e não consigo entrar")
        self.assertIn("Nunca envie sua senha", answer)

    def test_unknown_message_is_transparent(self):
        answer = demo_reply("Qual é a previsão do tempo?")
        self.assertIn("ainda não identifiquei", answer)
        self.assertIn("não acessa sistemas reais", answer)


if __name__ == "__main__":
    unittest.main()
