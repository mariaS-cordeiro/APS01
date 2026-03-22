import streamlit as st
import pandas as pd

st.set_page_config(page_title="APS - Ciência e Fake News", layout="centered")

# ---------- FUNÇÕES ----------
def contar_palavras(texto):
    return len(texto.split()) if texto and texto.strip() else 0

def resumir_texto(texto, limite=80):
    if isinstance(texto, str) and len(texto) > limite:
        return texto[:limite] + "..."
    return texto

# ---------- ESTADO ----------
if "respondido" not in st.session_state:
    st.session_state["respondido"] = False

if "df_respostas" not in st.session_state:
    st.session_state["df_respostas"] = None

if "txt_respostas" not in st.session_state:
    st.session_state["txt_respostas"] = ""

# ---------- CABEÇALHO ----------
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: black; margin-bottom: 0;'>Metodologia do Estudo</h1>
        <h3 style='color: #e65100; margin-top: 8px;'>APS - Ciência e Fake News</h3>
        <p style='color: black; font-weight: bold; margin-bottom: 0;'>Profa. Maria Sirleidy Cordeiro</p>
        <p style='color: #e65100; margin-top: 4px;'>marias.cordeiro@ufpe.br</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------- IDENTIFICAÇÃO ----------
nome_aluno = st.text_input("Nome do(a) aluno(a):")

st.divider()

# ---------- INSTRUÇÕES ----------
st.markdown("### ✏️ Produção escrita")
st.write("Responda às questões das páginas 58–59 de Vieira e Faraco (2019).")

perguntas_100 = [
    "1. Como o entrevistado explica o surgimento do termo “pós-verdade”?",
    "2. Segundo ele, devemos checar tudo o que lemos. Que procedimento ele sugere para isso?",
    "3. Que recomendações ele dá aos leitores para evitar a propagação de notícias falsas?",
    "4. Por que é relevante ter cuidado em não repassar notícias falsas?",
    "5. O fato de existir um termo como pós-verdade mostra dificuldade de contextualização. A que acontecimentos ele se refere?",
    "6. Por que é importante prestar atenção ao uso de adjetivos?",
    "7. Qual a consequência de crenças não baseadas em fatos para os leitores?"
]

respostas = []

# ---------- QUESTÕES ----------
for i, pergunta in enumerate(perguntas_100, start=1):
    st.markdown(f"**{pergunta}**")
    resposta = st.text_area(
        label=f"Resposta da questão {i}",
        height=120,
        key=f"q_{i}",
        label_visibility="collapsed"
    )

    total = contar_palavras(resposta)
    st.caption(f"Palavras: {total}/100")

    if total > 100:
        st.error(f"A resposta da questão {i} ultrapassou o limite de 100 palavras.")

    respostas.append(resposta)
    st.divider()

# ---------- TEXTO FINAL ----------
st.markdown("### ✏️ Produção escrita final")
st.write(
    "A partir das discussões de Lungarzo (1993) e Chalmers (1993) sobre o que é ciência, "
    "elabore um texto dissertativo de até 200 palavras, explicando de que forma a ciência "
    "pode ser afetada ou prejudicada pela disseminação de fake news, com base no texto "
    "de Vieira e Faraco (2019, p. 50–63)."
)

st.write("**Para construir sua resposta, considere:**")
st.write("- o conceito de ciência apresentado pelos autores;")
st.write("- a relação entre conhecimento científico, validação e verdade;")
st.write("- os impactos das fake news na credibilidade e circulação do conhecimento científico.")

texto_final = st.text_area(
    "Texto final",
    height=220,
    key="texto_final"
)

total_final = contar_palavras(texto_final)
st.caption(f"Palavras: {total_final}/200")

if total_final > 200:
    st.error("O texto final ultrapassou o limite de 200 palavras.")

st.divider()

# ---------- SALVAR ----------
if st.button("Salvar respostas"):
    dados = {
        "Aluno(a)": [nome_aluno] * 8,
        "Questão": ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Texto final"],
        "Resposta completa": respostas + [texto_final]
    }

    df = pd.DataFrame(dados)
    df["Resposta"] = df["Resposta completa"].apply(lambda x: resumir_texto(x, 80))

    # conteúdo para download em txt
    conteudo_txt = f"Aluno(a): {nome_aluno}\n\n"
    for i, r in enumerate(respostas, start=1):
        conteudo_txt += f"Q{i}:\n{r}\n\n"
    conteudo_txt += f"Texto final:\n{texto_final}\n"

    st.session_state["respondido"] = True
    st.session_state["df_respostas"] = df
    st.session_state["txt_respostas"] = conteudo_txt

# ---------- STATUS E VISUALIZAÇÃO ----------
if st.session_state["respondido"]:
    st.success("Status: respondido")

    st.markdown("### 📊 Visualização das respostas")
    st.dataframe(
        st.session_state["df_respostas"][["Aluno(a)", "Questão", "Resposta"]],
        use_container_width=True
    )

    st.download_button(
        label="Baixar bloco de notas",
        data=st.session_state["txt_respostas"],
        file_name=f"respostas_{nome_aluno.replace(' ', '_')}.txt" if nome_aluno else "respostas.txt",
        mime="text/plain"
    )
