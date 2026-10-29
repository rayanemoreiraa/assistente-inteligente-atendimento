# Assistente Inteligente de Atendimento

Protótipo de portfólio feito com Python e Streamlit. O aplicativo reconhece dúvidas comuns e sugere próximos passos usando regras locais, sem exigir uma chave de API ou pagamento.

## O que o projeto demonstra

- Interface de chat com Streamlit.
- Reconhecimento de temas: entrega, reembolso, pedido com problema, cancelamento, acesso à conta e pedido de atendimento humano.
- Normalização de texto para reconhecer variações com ou sem acentos.
- Priorização do pedido de atendimento humano quando ele aparece junto de outro problema.
- Respostas transparentes para mensagens que o protótipo não reconhece.
- Testes automatizados das principais regras.
- Avisos de privacidade e limites do protótipo.

## Limites e privacidade

Este é um protótipo educacional independente. Não representa uma empresa específica, não consulta pedidos, pagamentos ou contas reais e não transfere conversas para atendentes. Não insira senhas, códigos de autenticação, dados bancários ou documentos pessoais.

## Executar localmente

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
```

No Windows:

```powershell
.venv\Scripts\activate
```

No macOS/Linux:

```bash
source .venv/bin/activate
```

Instale e execute:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Executar os testes

```bash
python -m unittest test_assistant_logic -v
```

## Cenários de teste manuais

| Cenário | Entrada de exemplo | Comportamento esperado |
|---|---|---|
| Entrega | “Minha entrega está atrasada” | Orienta a consultar o canal oficial e o status |
| Reembolso | “Meu reembolso não caiu” | Orienta a consultar a solicitação e procurar suporte |
| Pedido com problema | “Meu pedido veio incompleto” | Orienta a descrever o problema no canal oficial |
| Cancelamento | “Quero cancelar meu pedido” | Explica que deve verificar as opções oficiais |
| Acesso | “Esqueci minha senha” | Recomenda recuperação oficial e protege códigos |
| Atendimento humano | “Quero falar com uma pessoa de verdade” | Reconhece a intenção e explica que não transfere a conversa |
| Mensagem desconhecida | “Qual é a previsão do tempo?” | Não inventa uma resposta; pede que a pessoa escolha um tema suportado |

## Tecnologias

Python • Streamlit • unittest • Git • GitHub

## Próximas evoluções possíveis

- Conectar uma base de conhecimento validada.
- Integrar um provedor de IA, se houver orçamento e necessidade.
- Criar transferência real para atendimento humano por meio de um sistema autorizado.
- Adicionar métricas agregadas sem guardar dados pessoais.
