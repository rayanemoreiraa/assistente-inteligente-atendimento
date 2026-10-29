"""Regras locais do assistente de atendimento; não usa API externa."""
import unicodedata

INTENTS = [
    {
        "name": "atendimento_humano",
        "keywords": [
            "atendente", "pessoa real", "pessoa de verdade", "falar com uma pessoa",
            "falar com alguem", "quero falar com alguem", "humano", "suporte humano",
            "atendimento humano", "quero um atendente", "nao consegui resolver",
            "ja tentei resolver", "falar com o suporte", "falar com uma pessoa do suporte",
            "quero falar com uma pessoa", "quero falar com uma pessoa de verdade",
            "reclamar com atendente", "atendimento de verdade", "operador humano",
        ],
        "reply": (
            "Entendi. Você quer falar com uma pessoa, e não continuar tentando resolver por aqui.\n\n"
            "1. Abra o aplicativo ou site oficial da empresa.\n"
            "2. Procure “Ajuda”, “Fale conosco” ou “Atendimento”.\n"
            "3. Se já houve uma tentativa anterior, tenha o protocolo em mãos.\n\n"
            "Este protótipo não consegue transferir a conversa nem abrir um chamado real."
        ),
    },
    {
        "name": "entrega",
        "keywords": ["atraso", "atrasada", "atrasado", "nao chegou", "cadê meu pedido", "cade meu pedido", "entrega", "pedido nao recebido", "pedido não recebido", "rastreamento", "rastrear", "entregue mas nao recebi"],
        "reply": (
            "Entendi — você precisa de ajuda com a entrega.\n\n"
            "1. Confira o status no aplicativo ou site oficial.\n"
            "2. Veja se há uma atualização ou orientação do estabelecimento.\n"
            "3. Se o prazo já passou, procure o suporte oficial e informe o número do pedido somente naquele canal.\n\n"
            "Não consigo rastrear pedidos reais por este protótipo."
        ),
    },
    {
        "name": "reembolso",
        "keywords": ["reembolso", "estorno", "devolver meu dinheiro", "dinheiro de volta", "cobrado duas vezes", "cobranca duplicada", "cobrança duplicada", "reembolso nao caiu", "reembolso não caiu", "nao recebi o reembolso", "não recebi o reembolso"],
        "reply": (
            "Vamos organizar os próximos passos para o reembolso.\n\n"
            "1. Confira o status da solicitação no canal oficial.\n"
            "2. Separe o comprovante da compra e o número do pedido.\n"
            "3. Se o valor não aparecer ou houver cobrança duplicada, fale com o suporte e peça um protocolo.\n\n"
            "Não consigo consultar pagamentos. Não envie dados bancários ou documentos nesta conversa."
        ),
    },
    {
        "name": "pedido_com_problema",
        "keywords": ["pedido errado", "veio errado", "faltou", "item faltando", "produto errado", "danificado", "veio quebrado", "problema com o pedido", "reclamacao", "reclamação", "comida fria", "pedido incompleto"],
        "reply": (
            "Sinto muito pelo problema com o pedido.\n\n"
            "1. Abra o pedido no aplicativo ou site oficial e procure a opção de ajuda.\n"
            "2. Explique o que veio errado ou faltou.\n"
            "3. Anexe fotos apenas se o canal oficial solicitar e permitir.\n\n"
            "Não consigo alterar pedidos reais, mas posso ajudar a organizar uma mensagem para o suporte."
        ),
    },
    {
        "name": "cancelamento",
        "keywords": ["cancelar", "cancelamento", "quero cancelar", "desistir do pedido"],
        "reply": (
            "Para verificar se é possível cancelar, abra o pedido no aplicativo ou site oficial e procure a opção de cancelamento ou ajuda.\n\n"
            "A possibilidade depende do status do pedido e das regras da empresa. Este protótipo não cancela pedidos reais."
        ),
    },
    {
        "name": "acesso",
        "keywords": ["senha", "login", "entrar na conta", "nao consigo entrar", "não consigo entrar", "acesso", "recuperar conta", "esqueci a senha", "codigo de verificacao", "código de verificação", "conta bloqueada"],
        "reply": (
            "Vamos tentar recuperar seu acesso com segurança.\n\n"
            "1. Use a opção oficial “Esqueci minha senha”.\n"
            "2. Siga as instruções do próprio serviço.\n"
            "3. Se houver erro, anote a mensagem sem compartilhar códigos ou dados pessoais.\n\n"
            "Nunca envie sua senha ou código de verificação nesta conversa."
        ),
    },
]


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.lower())
    value = "".join(char for char in value if not unicodedata.combining(char))
    return " ".join(value.strip().split())


def demo_reply(message: str) -> str:
    text = normalize_text(message)
    # Pedidos explícitos de pessoa são prioritários, mesmo se também mencionarem outro problema.
    human = next(item for item in INTENTS if item["name"] == "atendimento_humano")
    if any(normalize_text(keyword) in text for keyword in human["keywords"]):
        return human["reply"]

    for intent in INTENTS:
        if intent["name"] == "atendimento_humano":
            continue
        if any(normalize_text(keyword) in text for keyword in intent["keywords"]):
            return intent["reply"]

    return (
        "Quero ajudar, mas ainda não identifiquei o tema da sua dúvida.\n\n"
        "Você pode perguntar sobre entrega atrasada, reembolso, problema com pedido, cancelamento, acesso à conta ou atendimento humano.\n\n"
        "Este protótipo usa regras de demonstração e não acessa sistemas reais."
    )
