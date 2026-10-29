import streamlit as st
from assistant_logic import demo_reply

st.set_page_config(page_title="Assistente de Atendimento", page_icon="💬", layout="centered")
st.title("💬 Assistente Inteligente de Atendimento")
st.caption("Projeto de portfólio • Python • Streamlit")
st.info(
    "Protótipo educacional: não consulta pedidos, contas ou pagamentos reais. "
    "Não envie senhas, códigos de segurança, dados bancários ou documentos pessoais."
)

with st.sidebar:
    st.header("Sobre o projeto")
    st.write("Um protótipo que reconhece temas comuns de atendimento e sugere próximos passos.")
    st.caption("Modo gratuito: as respostas são geradas por regras locais, sem API externa.")
    st.subheader("Experimente um tema")
    examples = {
        "Entrega atrasada": "Minha entrega está atrasada. O que devo fazer?",
        "Pedir reembolso": "Solicitei um reembolso, mas o dinheiro ainda não caiu.",
        "Pedido com problema": "Meu pedido veio com um item faltando.",
        "Problema de acesso": "Não consigo entrar na minha conta.",
        "Falar com atendente": "Quero falar com uma pessoa de verdade, porque já tentei resolver e não consegui.",
    }
    for label, example in examples.items():
        if st.button(label, use_container_width=True):
            st.session_state.pending_prompt = example
    if st.button("Limpar conversa", use_container_width=True):
        st.session_state.history = []
        st.session_state.pop("pending_prompt", None)
        st.rerun()

if "history" not in st.session_state:
    st.session_state.history = []

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
    answer = demo_reply(prompt)
    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.history.append({"role": "assistant", "content": answer})

st.divider()
st.caption("Demonstração educacional. Não representa uma empresa específica e não acessa sistemas ou pedidos reais.")
