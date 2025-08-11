import itertools
import string
import time

# Senha correta para o brute force tentar descobrir
senha_correta = "abc12"

# Função que simula uma tentativa de login
def tentar_senha(tentativa):
    time.sleep(0.1)  # simula delay de verificação
    return tentativa == senha_correta

def gerar_senhas(possiveis_chars, max_tamanho):
    for tamanho in range(1, max_tamanho + 1):
        for tentativa in itertools.product(possiveis_chars, repeat=tamanho):
            yield "".join(tentativa)

def brute_force(max_tamanho=5):
    possiveis_chars = string.ascii_lowercase + string.digits
    tentativas = 0

    for senha_tentativa in gerar_senhas(possiveis_chars, max_tamanho):
        tentativas += 1
        print(f"Tentando senha #{tentativas}: {senha_tentativa}")
        if tentar_senha(senha_tentativa):
            print(f"Senha encontrada: {senha_tentativa} após {tentativas} tentativas")
            return senha_tentativa
    print("Senha não encontrada.")
    return None

if __name__ == "__main__":
    brute_force()
