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
st.caption("MVP de portfólio • Python • IA generativa • boas práticas de atendimento")

with st.sidebar:
    st.header("Configuração")
    use_ai = st.toggle("Usar IA real (API)", value=bool(os.getenv("OPENAI_API_KEY")))
    st.caption("Sem chave de API, o app funciona em modo demonstração.")
    st.divider()
    st.markdown("**Projeto de portfólio**")
    st.write("Demonstra um fluxo simples de atendimento, com orientação para não inventar informações.")

SYSTEM_PROMPT = """
Você é um assistente de atendimento cordial, claro e objetivo.
Regras:
- Responda em português do Brasil.
- Não invente preços, prazos, políticas ou dados que não foram fornecidos.
- Se faltar informação, diga isso com transparência e faça uma pergunta objetiva.
- Não peça senhas, códigos de autenticação nem dados bancários completos.
- Se o caso exigir acesso à conta, cobrança, reembolso ou dados pessoais, oriente a pessoa a procurar o canal oficial da empresa.
- Seja breve e útil.
"""

def demo_reply(message: str) -> str:
    text = message.lower()
    if any(word in text for word in ["reembolso", "estorno", "devolver meu dinheiro"]):
        return (
            "Posso ajudar com orientações gerais sobre reembolso. Como não tenho acesso "
            "ao seu pedido nem à política de uma empresa específica, confira o pedido no "
            "canal oficial de atendimento. Não envie aqui dados bancários ou senhas. "
            "Você quer ajuda para escrever uma mensagem solicitando o reembolso?"
        )
    if any(word in text for word in ["atraso", "atrasado", "não chegou", "nao chegou", "entrega"]):
        return (
            "Entendi que você precisa de ajuda com uma entrega. Eu não consigo consultar "
            "pedidos reais neste protótipo. Verifique o status no aplicativo ou canal oficial "
            "da empresa. Se quiser, posso ajudar a redigir uma mensagem objetiva para o suporte."
        )
    if any(word in text for word in ["senha", "login", "acessar", "acesso"]):
        return (
            "Para recuperar o acesso, use a opção oficial de recuperação de senha do serviço. "
            "Não compartilhe sua senha nem códigos de verificação nesta conversa. "
            "Se você me disser qual mensagem de erro aparece (sem dados pessoais), posso ajudar "
            "a entender o próximo passo."
        )
    return (
        "Obrigado por entrar em contato! Este protótipo está em modo demonstração e não tem "
        "acesso aos sistemas de uma empresa. Conte um pouco mais sobre o que aconteceu e "
        "posso ajudar a organizar as informações ou preparar uma mensagem para o atendimento."
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
    return response.choices[0].message.content or "Não consegui gerar uma resposta agora."

if "history" not in st.session_state:
    st.session_state.history = []

for item in st.session_state.history:
    with st.chat_message(item["role"]):
        st.markdown(item["content"])

prompt = st.chat_input("Digite uma dúvida de atendimento…")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if use_ai:
            if not os.getenv("OPENAI_API_KEY"):
                answer = "Para usar a IA real, configure OPENAI_API_KEY no arquivo .env. Não publique essa chave no GitHub."
                st.warning(answer)
            else:
                try:
                    with st.spinner("Preparando resposta…"):
                        answer = ai_reply(prompt)
                    st.markdown(answer)
                except Exception as exc:
                    answer = (
                        "Não consegui acessar a IA agora. Confira a chave de API, a conexão "
                        "e os limites da sua conta. Detalhe técnico: " + str(exc)
                    )
                    st.error(answer)
        else:
            answer = demo_reply(prompt)
            st.markdown(answer)

    st.session_state.history.append({"role": "assistant", "content": answer})

st.divider()
st.caption(
    "Aviso: demonstração educacional. Não representa o iFood, não consulta pedidos reais "
    "e não deve receber dados pessoais, senhas ou informações financeiras."
)
