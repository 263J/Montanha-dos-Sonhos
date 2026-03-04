# Importando bibliotéca para ações no prompt
import subprocess
import sys

# Funções
def limpar():
    subprocess.run("cls", shell=True)

def atacar():
    Jogo.mensagem = "Você atacou!"

def defender():
    Jogo.mensagem = "Você defendeu!"

def correr():
    Jogo.mensagem = "Você fugiu!"

def fechar():
    sys.exit()

acoes = {
    "atacar": atacar,
    "defender": defender,
    "correr": correr,
    "fechar": fechar
}

# Classes
class Jogo:
    mensagem = "Bem-vindo ao jogo!"

# Limpeza inicial
limpar()

# Menu principal
while True:

    print(Jogo.mensagem)

    # Decisão
    acao = acoes.get(input("Escolha: ").lower())

    if acao:
        acao()

    else:
        Jogo.mensagem = "Ação Inválida!"
    
    # Limpeza Final
    limpar()