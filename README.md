# Assistente Inteligente de Atendimento

MVP educacional de portfólio que demonstra uma interface de atendimento com respostas em português, tratamento de dúvidas comuns e integração opcional com um modelo de IA via API.

> **Transparência:** este projeto independente não é afiliado ao iFood, não acessa pedidos reais e não deve receber senhas, códigos de autenticação, dados bancários ou dados pessoais sensíveis.

## O que demonstra

- Interface de chat com Streamlit.
- Organização do código em funções.
- Respostas de demonstração para temas como entrega, reembolso e acesso.
- Integração opcional com API de modelo de linguagem.
- Instruções de sistema para reduzir respostas inventadas e proteger informações.
- Configuração por variável de ambiente; a chave da API não deve ser publicada.

## Como executar no computador

É necessário ter Python 3.10 ou superior.

1. Baixe ou clone este repositório.
2. Abra um terminal dentro da pasta do projeto.
3. Crie um ambiente virtual (recomendado):

   **Windows**
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Inicie o aplicativo:
   ```bash
   streamlit run app.py
   ```

O app abre no navegador em modo demonstração sem exigir uma chave de API.

## Ativar respostas com IA

1. Copie `.env.example` para um arquivo chamado `.env`.
2. Adicione sua chave em `OPENAI_API_KEY` no arquivo `.env`.
3. Se necessário, ajuste `OPENAI_MODEL`.
4. Reinicie o aplicativo e ative **Usar IA real (API)** na barra lateral.

A utilização da API pode gerar custos e depende de uma conta e de acesso à API. **Nunca coloque sua chave de API no código nem a envie ao GitHub.** O arquivo `.env` está incluído no `.gitignore`.

## Como testar

Experimente perguntas como:
- "Minha entrega está atrasada. O que faço?"
- "Quero pedir um reembolso."
- "Não consigo acessar minha conta."
- "Qual é a política de troca?"

No modo demonstração, as respostas são regras simples, não respostas geradas por IA. No modo IA, as respostas são geradas pelo modelo configurado, mas ainda precisam ser verificadas.

## Próximas melhorias

- Criar uma base de conhecimento com políticas fictícias e claramente identificadas.
- Adicionar testes automatizados.
- Registrar métricas sem armazenar dados pessoais.
- Implementar transferência para atendimento humano.
- Criar fluxo equivalente em n8n.

## Tecnologias

Python • Streamlit • API de modelo de linguagem • python-dotenv • Git/GitHub

## Sobre o projeto

Projeto de aprendizagem desenvolvido para praticar conceitos de Python, integração com IA generativa e construção de um protótipo de atendimento. O escopo atual é intencionalmente pequeno e pode ser ampliado conforme o aprendizado.
