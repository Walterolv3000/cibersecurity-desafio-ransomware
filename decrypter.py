import os
import pyaes

# Nome do arquivo criptografado
encrypted_file_name = "teste.txt.ransomwaretroll"

# Nome do arquivo descriptografado
decrypted_file_name = "teste.txt"

# Chave para descriptografia
key = b"testeransomwares"

try:
    # Abrir e ler o arquivo criptografado
    with open(encrypted_file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Descriptografar os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)

    # Criar o arquivo descriptografado
    with open(decrypted_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    # Remover o arquivo criptografado
    os.remove(encrypted_file_name)

    print(f"Arquivo '{encrypted_file_name}' foi descriptografado e salvo como '{decrypted_file_name}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{encrypted_file_name}' não foi encontrado.")
except PermissionError:
    print(f"Erro: Permissão negada ao acessar '{encrypted_file_name}' ou '{decrypted_file_name}'.")
except Exception as e:
    print(f"Erro inesperado: {e}")
