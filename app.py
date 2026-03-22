import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="APS - Ciência e Fake News", layout="centered")

def contar_palavras(texto):
    return len(texto.split()) if texto.strip() else 0

col1, col2 = st.columns([1, 3])

with col1:
    logo_path = Path("logo.png")
    if logo_path.exists():
        st.image(str(logo_path), width=120)
    else:
        st.warning("Logo não encontrada.")

with col2:
    st.title("Metodologia do Estudo")
    st.subheader("APS - Ciência e Fake News")
    st.write("Profa. Maria Sirleidy Cordeiro")
    st.write("marias.cordeiro@ufpe.br")

st.divider()

nome_aluno = st.text_input("Nome do(a) aluno(a):")

st.divider()

st.markdown("### 📌 Produção escrita")
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

for i, pergunta in enumerate(perguntas_100, start=1):
    st.markdown(f"**{pergunta}**")
    resposta = st.text_area(
        f"Resposta {i}",
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

st.markdown("### ✍️ Produção escrita final")
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
    key="texto_final",
    label_visibility="visible"
)

total_final = contar_palavras(texto_final)
st.caption(f"Palavras: {total_final}/200")

if total_final > 200:
    st.error("O texto final ultrapassou o limite de 200 palavras.")

st.divider()

if st.button("Salvar respostas"):
    dados = {
        "Aluno(a)": [nome_aluno] * 8,
        "Questão": ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Texto final"],
        "Resposta": respostas + [texto_final]
    }

    df = pd.DataFrame(dados)

    st.success("Respostas registradas!")
    st.dataframe(df, use_container_width=True)
