from cryptography.fernet import Fernet

# Lendo o arquivo
nome_arquivo = "teste.txt"
with open(nome_arquivo,"rb") as arq:
    arquivo = arq.read()

# Gerando uma chave criptográfica
chave = Fernet.generate_key()
nome_chave = "chave_cript.key"

# Escrevendo a chave para um arquivo
with open(nome_chave,"wb") as arq_chave:
    arq_chave = arq_chave.write(chave)

# Lendo a chave criptográfica
with open(nome_chave,"rb") as chave:
    conteudo_chave = chave.read()

# Abrindo o Fernet com a chave gerada
fernet = Fernet(conteudo_chave)

# Criptografando o arquivo
conteudo_cripto = fernet.encrypt(arquivo)

# Escrevendo o arquivo criptografado
with open(nome_arquivo,"wb") as arq_criptografado:
    arq_criptografado = arq_criptografado.write(conteudo_cripto)



