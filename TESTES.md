# Registro de testes

Os testes automatizados podem ser executados com `python -m unittest test_assistant_logic -v`.

| Área | Verificação | Resultado esperado |
|---|---|---|
| Entrega | Mensagem sobre atraso | Orientação para conferir status no canal oficial |
| Reembolso | Mensagem sobre estorno não recebido | Orientação para consultar solicitação e falar com suporte |
| Atendimento humano | Pedido de falar com pessoa junto com problema de entrega | O pedido humano tem prioridade |
| Variações de escrita | Mensagem sem acentos | Intenção reconhecida |
| Segurança | Mensagem sobre senha | Aviso para não compartilhar senha ou códigos |
| Mensagem desconhecida | Pergunta fora dos temas | O sistema informa o limite e não inventa uma resposta |

Este registro descreve os cenários cobertos pelos testes do projeto. O resultado real deve ser confirmado executando a suíte de testes no ambiente de desenvolvimento.
