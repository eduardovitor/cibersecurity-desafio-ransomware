from cryptography.fernet import Fernet

# Lendo o arquivo
nome_arquivo_cripto = "teste.txt"
with open(nome_arquivo_cripto,"rb") as arq:
    arquivo_cripto = arq.read()

# Lendo a chave criptográfica
nome_chave = "chave_cript.key"
with open(nome_chave,"rb") as chave:
    conteudo_chave = chave.read()

# Inicializando o fernet
fernet = Fernet(conteudo_chave)

# Conteúdo do arquivo descriptografado
conteudo_arq_descripto = fernet.decrypt(arquivo_cripto)

# Escrevendo o conteúdo original de volta
with open(nome_arquivo_cripto,"wb") as arq:
    arq.write(conteudo_arq_descripto)
