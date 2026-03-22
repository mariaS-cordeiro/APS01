# APS01
Escrita_atividade
st.title("📝 Bloco de Notas (até 200 palavras)")

# Área de texto
texto = st.text_area("Escreva seu texto aqui:")

# Contagem de palavras
palavras = texto.split()
num_palavras = len(palavras)

# Exibir contagem
st.write(f"Palavras: {num_palavras}/200")

# Verificação do limite
if num_palavras > 200:
    st.error("Você ultrapassou o limite de 200 palavras!")
else:
    st.success("Texto dentro do limite permitido.")

# Botão para salvar (simples)
if st.button("Salvar texto"):
    st.write("Texto salvo:")
    st.write(texto)
