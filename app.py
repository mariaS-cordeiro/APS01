import streamlit as st
import pandas as pd

st.set_page_config(page_title="APS - Ciência e Fake News", layout="centered")

# ---------- FUNÇÃO ----------
def contar_palavras(texto):
    return len(texto.split()) if texto.strip() else 0

# ---------- CABEÇALHO CENTRALIZADO ----------
st.markdown("""
<div style='text-align: center;'>

    <h1 style='color: black;'>Metodologia do Estudo</h1>

    <h3 style='color: #ff6600;'>APS - Ciência e Fake News</h3>

    <p style='color: black; font-weight: bold;'>
        Profa. Maria Sirleidy Cordeiro
    </p>

    <p style='color: #ff6600;'>
        marias.cordeiro@ufpe.br
    </p>

</div>
""", unsafe_allow_html=True)

st.divider()

# ---------- IDENTIFICAÇÃO ----------
nome_aluno = st.text_input("Nome do(a) aluno(a):")

st.divider()

# ---------- INSTRUÇÕES ----------
st.markdown("### 📝 Produção escrita")
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

# ---------- TEXTO FINAL ----------
st.markdown("### 📌 Consolidando os estudos")

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
        "Aluno(a)": [nome_aluno]*8,
        "Questão": ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Texto final"],
        "Resposta": respostas + [texto_final]
    }

    df = pd.DataFrame(dados)

    st.success("Respostas registradas!")
    st.dataframe(df, use_container_width=True)
