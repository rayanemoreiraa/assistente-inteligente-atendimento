import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Assistente Inteligente de Atendimento",
    page_icon="💬",
    layout="centered",
)

st.title("💬 Assistente Inteligente de Atendimento")
st.caption("Projeto de portfólio • Python • atendimento digital")
st.info(
    "Este é um protótipo de demonstração. Ele não consulta pedidos, contas ou sistemas reais. "
    "Não informe senhas, códigos de segurança ou dados bancários."
)

with st.sidebar:
    st.header("Sobre o projeto")
    st.write("O assistente identifica temas comuns de atendimento e sugere próximos passos.")
    st.caption("Modo gratuito: as respostas simuladas funcionam sem chave de API.")

SYSTEM_PROMPT = """
Você é um assistente de atendimento cordial, claro e objetivo.
Responda em português do Brasil e organize respostas em passos curtos quando útil.
Não invente preços, prazos, políticas, status de pedidos ou dados que não foram fornecidos.
Não afirme que consultou sistemas reais. Não solicite senhas, códigos de autenticação ou dados bancários completos.
Para ações que exigem acesso à conta, cobrança, cancelamento, reembolso ou dados pessoais, oriente a pessoa a usar o canal oficial da empresa.
Se o caso exigir análise humana, recomende atendimento humano. Seja breve e acolhedor.
"""

INTENTS = [
    {
        "name": "Entrega atrasada ou não recebida",
        "keywords": ["atraso", "atrasada", "atrasado", "não chegou", "nao chegou", "cadê meu pedido", "cade meu pedido", "entrega", "entregue mas não recebi", "entregue mas nao recebi", "rastreamento", "rastrear"],
        "reply": "Entendi — você precisa de ajuda com a entrega.\n\n1. Abra o aplicativo ou site oficial e confira o status do pedido.\n2. Veja se há uma atualização de entrega ou orientação do estabelecimento.\n3. Se o prazo informado já passou, entre em contato pelo suporte oficial e informe o número do pedido somente naquele canal.\n\nEste protótipo não consegue rastrear pedidos reais. Posso ajudar você a escrever uma mensagem para o suporte.",
    },
    {
        "name": "Reembolso ou estorno",
        "keywords": ["reembolso", "estorno", "devolver meu dinheiro", "dinheiro de volta", "não recebi o reembolso", "nao recebi o reembolso", "cobrado duas vezes", "cobrança duplicada", "cobranca duplicada"],
        "reply": "Vamos organizar o pedido de reembolso.\n\n1. Confira o status da solicitação no canal oficial da empresa.\n2. Separe o comprovante da compra e o número do pedido.\n3. Se o reembolso não aparecer ou houver cobrança duplicada, fale com o suporte oficial e peça o protocolo.\n\nNão consigo consultar pagamentos neste protótipo. Evite enviar aqui dados bancários ou documentos.",
    },
    {
        "name": "Problema com pedido ou item",
        "keywords": ["pedido errado", "veio errado", "faltou", "item faltando", "produto errado", "danificado", "veio quebrado", "qualidade", "reclamação", "reclamacao"],
        "reply": "Sinto muito pelo problema com o pedido.\n\n1. Confira as opções de ajuda relacionadas ao pedido no aplicativo ou site oficial.\n2. Descreva objetivamente o que veio errado ou faltou.\n3. Se for permitido pelo canal oficial, anexe fotos que mostrem o problema.\n\nNão consigo alterar pedidos reais, mas posso ajudar a preparar uma mensagem clara para o atendimento.",
    },
    {
        "name": "Cancelamento",
        "keywords": ["cancelar", "cancelamento", "quero cancelar", "desistir do pedido"],
        "reply": "Para verificar se é possível cancelar, abra o pedido no aplicativo ou site oficial e procure a opção de cancelamento ou ajuda. A possibilidade de cancelar depende do status do pedido e das regras da empresa.\n\nEste protótipo não consegue cancelar pedidos. Se a opção não aparecer, entre em contato com o suporte oficial.",
    },
    {
        "name": "Acesso ou senha",
        "keywords": ["senha", "login", "entrar na conta", "não consigo entrar", "nao consigo entrar", "acesso", "recuperar conta", "esqueci a senha", "código de verificação", "codigo de verificacao"],
        "reply": "Vamos tentar recuperar seu acesso com segurança.\n\n1. Use a opção oficial “Esqueci minha senha”.\n2. Siga as instruções enviadas pelo próprio serviço.\n3. Se aparecer uma mensagem de erro, anote o texto sem compartilhar códigos ou dados pessoais.\n\nNunca envie sua senha ou código de verificação nesta conversa.",
    },
    {
        "name": "Falar com uma pessoa",
        "keywords": ["atendente", "pessoa real", "humano", "falar com alguém", "falar com alguem", "suporte humano", "reclamar com atendente"],
        "reply": "Se você prefere falar com uma pessoa, procure as opções “Ajuda”, “Fale conosco” ou “Atendimento” no aplicativo ou site oficial da empresa. Se já tentou resolver o problema, tenha em mãos o protocolo anterior.\n\nEste protótipo não consegue transferir a conversa para um atendente real.",
    },
]


def demo_reply(message: str) -> str:
    text = " ".join(message.lower().strip().split())
    for intent in INTENTS:
        if any(keyword in text for keyword in intent["keywords"]):
            return intent["reply"]
    return (
        "Quero ajudar você a encontrar o próximo passo. Para eu orientar melhor, conte um pouco mais sobre o problema.\n\n"
        "Você pode escolher um dos temas na lateral ou escrever, por exemplo: “minha entrega está atrasada” ou “quero pedir um reembolso”.\n\n"
        "Lembrete: não tenho acesso a pedidos ou contas reais."
    )


def ai_reply(message: str) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content or "Não consegui preparar uma resposta agora."


if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.subheader("Experimente um tema")
    examples = {
        "Entrega atrasada": "Minha entrega está atrasada. O que devo fazer?",
        "Pedir reembolso": "Quero pedir um reembolso.",
        "Pedido com problema": "Meu pedido veio com um item faltando.",
        "Problema de acesso": "Não consigo entrar na minha conta.",
        "Falar com atendente": "Quero falar com uma pessoa do suporte.",
    }
    for label, example in examples.items():
        if st.button(label, use_container_width=True):
            st.session_state.pending_prompt = example
    if st.button("Limpar conversa", use_container_width=True):
        st.session_state.history = []
        st.session_state.pending_prompt = ""
        st.rerun()

for item in st.session_state.history:
    with st.chat_message(item["role"]):
        st.markdown(item["content"])

prompt = st.chat_input("Digite sua dúvida de atendimento…")
if not prompt and st.session_state.get("pending_prompt"):
    prompt = st.session_state.pop("pending_prompt")

if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # O projeto permanece no modo gratuito, sem chamada de API.
        answer = demo_reply(prompt)
        st.markdown(answer)

    st.session_state.history.append({"role": "assistant", "content": answer})

st.divider()
st.caption("Demonstração educacional. Não representa uma empresa específica e não acessa sistemas ou pedidos reais.")
