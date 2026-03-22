import streamlit as st
import pandas as pd

st.set_page_config(page_title="APS - Ciência e Fake News", layout="centered")

# ---------- FUNÇÃO ----------
def contar_palavras(texto):
    return len(texto.split()) if texto.strip() else 0

# ---------- CABEÇALHO ----------
st.title("📝 Metodologia do Estudo")
st.subheader("APS - Ciência e Fake News")

st.write("**Profa. Maria Sirleidy Cordeiro**")
st.write("**E-mail:** marias.cordeiro@ufpe.br")

st.divider()

# ---------- IDENTIFICAÇÃO ----------
nome_aluno = st.text_input("Nome do(a) aluno(a):")

st.divider()

# ---------- INSTRUÇÕES ----------
st.markdown("### 📌 Produção escrita")
st.write("Responda às questões das páginas 58–59 de Vieira e Faraco (2019).")

perguntas_100 = [
    "1. Como o entrevistado explica o surgimento do termo “pós-verdade”?",
    "2. Segundo ele, devemos checar tudo o que lemos. Que procedimento ele sugere para isso?",
    "3. Que recomendações ele dá aos leitores para evitar a propagação de notícias falsas?",
    "4. Por que é relevante ter cuidado em não repassar notícias falsas?",
    "5. “O fato de existir um termo como pós-verdade mostra que estamos com dificuldade de entender e contextualizar os acontecimentos.” A que acontecimentos ele está se referindo?",
    "6. “Preste atenção também ao uso de adjetivos.” Por que ele faz essa recomendação?",
    "7. “Muitas vezes a certeza das pessoas não se baseia em fatos.” Qual a consequência disso para nós, leitores?"
]

respostas = []

# ---------- QUESTÕES CURTAS ----------
for i, pergunta in enumerate(perguntas_100, start=1):
    st.markdown(f"**{pergunta}**")
    resposta = st.text_area(
        f"Resposta da questão {i}",
        height=120,
        key=f"q_{i}",
        label_visibility="collapsed"
    )

    total_palavras = contar_palavras(resposta)
    st.caption(f"Palavras: {total_palavras}/100")

    if total_palavras > 100:
        st.error(f"A resposta da questão {i} ultrapassou o limite de 100 palavras.")

    respostas.append(resposta)
    st.divider()

# ---------- TEXTO FINAL ----------
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

# ---------- BOTÃO SALVAR E TABELA ----------
if st.button("Salvar respostas"):
    dados = {
        "Aluno(a)": [nome_aluno] * 8,
        "Questão": [
            "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Texto final"
        ],
        "Resposta": [
            respostas[0],
            respostas[1],
            respostas[2],
            respostas[3],
            respostas[4],
            respostas[5],
            respostas[6],
            texto_final
        ]
    }

    df = pd.DataFrame(dados)

    st.success("Respostas registradas com sucesso.")
    st.markdown("### 📊 Visualização das respostas")
    st.dataframe(df, use_container_width=True)
