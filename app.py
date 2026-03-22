import streamlit as st

st.set_page_config(page_title="APS - Ciência e Fake News", layout="centered")

# ---------- ESTILO ----------
st.markdown("""
<style>
    .main {
        background-color: #f3f4f6;
    }

    .a4-sheet {
        background: white;
        width: 210mm;
        min-height: 297mm;
        margin: 20px auto;
        padding: 25mm 20mm 25mm 20mm;
        box-shadow: 0 0 10px rgba(0,0,0,0.12);
        border-radius: 6px;
        font-family: Arial, sans-serif;
    }

    .titulo-disciplina {
        text-align: center;
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .subinfo {
        text-align: center;
        font-size: 15px;
        margin-bottom: 2px;
    }

    .secao {
        font-size: 22px;
        font-weight: 700;
        margin-top: 24px;
        margin-bottom: 18px;
    }

    .instrucao {
        font-size: 16px;
        font-weight: 600;
        margin-top: 18px;
        margin-bottom: 8px;
    }

    .questao {
        font-size: 16px;
        margin-top: 12px;
        margin-bottom: 8px;
        line-height: 1.5;
    }

    .destaque {
        font-weight: 700;
    }

    .caixa-label {
        font-size: 13px;
        color: #555;
        margin-top: -6px;
        margin-bottom: 8px;
    }

    hr {
        margin-top: 28px;
        margin-bottom: 28px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- FUNÇÃO ----------
def contar_palavras(texto: str) -> int:
    return len(texto.split()) if texto.strip() else 0

# ---------- CONTAINER A4 ----------
st.markdown('<div class="a4-sheet">', unsafe_allow_html=True)

st.markdown('<div class="titulo-disciplina">Metodologia do estudo</div>', unsafe_allow_html=True)
st.markdown('<div class="subinfo">Profa. Maria Sirleidy Cordeiro</div>', unsafe_allow_html=True)
st.markdown('<div class="subinfo">marias.cordeiro@ufpe.br</div>', unsafe_allow_html=True)

st.markdown('<div class="secao">📝 Produção escrita</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="instrucao">📌 Responda às questões das páginas 58–59 de Vieira e Faraco (2019).</div>',
    unsafe_allow_html=True
)

perguntas_100 = [
    '(1) Como o entrevistado explica o surgimento do termo “pós-verdade”?',
    '(2) Segundo ele, devemos checar tudo o que lemos. Que procedimento ele sugere para isso?',
    '(3) Que recomendações ele dá aos leitores para evitar a propagação de notícias falsas?',
    '(4) Por que é relevante ter cuidado em não repassar notícias falsas?',
    '(5a) “O fato de existir um termo como pós-verdade mostra que estamos com dificuldade de entender e contextualizar os acontecimentos.” À que acontecimentos ele está se referindo?',
    '(5b) “Preste atenção também ao uso de adjetivos.” Por que ele faz essa recomendação?',
    '(5c) “Muitas vezes a certeza das pessoas não se baseia em fatos.” Qual a consequência disso para nós, leitores?'
]

respostas_100 = {}

for i, pergunta in enumerate(perguntas_100, start=1):
    st.markdown(f'<div class="questao">{pergunta}</div>', unsafe_allow_html=True)
    resposta = st.text_area(
        label=f"Resposta {i}",
        height=120,
        key=f"q100_{i}",
        label_visibility="collapsed",
        placeholder="Escreva sua resposta aqui..."
    )
    total = contar_palavras(resposta)
    respostas_100[f"q{i}"] = resposta

    if total <= 100:
        st.markdown(f'<div class="caixa-label">Palavras: {total}/100</div>', unsafe_allow_html=True)
    else:
        st.error(f"Você ultrapassou o limite de 100 palavras. Total atual: {total}")

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    '<div class="instrucao">📌 A partir das discussões de Lungarzo (1993) e Chalmers (1993) sobre o que é ciência, elabore um texto dissertativo de até 200 palavras, explicando de que forma a ciência pode ser afetada ou prejudicada pela disseminação de fake news, com base no texto de Vieira e Faraco (2019, p. 50–63).</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="questao">
<span class="destaque">Para a construção da resposta, considere:</span><br>
• o conceito de ciência apresentado pelos autores Lungarzo (1993) e Chalmers (1993);<br>
• a relação entre conhecimento científico, validação e verdade;<br>
• os impactos das fake news na credibilidade e circulação do conhecimento científico.
</div>
""", unsafe_allow_html=True)

texto_final = st.text_area(
    "Texto final",
    height=220,
    key="texto_200",
    label_visibility="collapsed",
    placeholder="Escreva seu texto dissertativo aqui..."
)

total_final = contar_palavras(texto_final)

if total_final <= 200:
    st.markdown(f'<div class="caixa-label">Palavras: {total_final}/200</div>', unsafe_allow_html=True)
else:
    st.error(f"Você ultrapassou o limite de 200 palavras. Total atual: {total_final}")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Salvar respostas"):
    st.success("Respostas registradas na sessão.")
    st.write("Pré-visualização:")
    st.write(respostas_100)
    st.write({"texto_final": texto_final})

st.markdown("</div>", unsafe_allow_html=True)
