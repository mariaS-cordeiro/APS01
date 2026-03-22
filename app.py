import streamlit as st

st.title("📝 Bloco de Notas (até 200 palavras)")

texto = st.text_area("Escreva seu texto aqui:")

palavras = texto.split()
num_palavras = len(palavras)

st.write(f"Palavras: {num_palavras}/200")

if num_palavras > 200:
    st.error("Você ultrapassou o limite de 200 palavras!")
else:
    st.success("Texto dentro do limite permitido.")

if st.button("Salvar texto"):
    st.write("Texto salvo:")
    st.write(texto)
