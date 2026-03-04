# Importando bibliotéca para ações no prompt
import subprocess
import sys

# Limpeza inicial
subprocess.run("cls", shell=True)

# Funções
def atacar():
    print("Você atacou!")

def defender():
    print("Você defendeu!")

def correr():
    print("Você fugiu!")

def fechar():
    print("Você fechou o jogo!")
    sys.exit()

acoes = {
    "atacar": atacar,
    "defender": defender,
    "correr": correr,
    "fechar": fechar
}

# Menu principal
while True:

    # Decisão
    acao = acoes.get(input("Escolha: ").lower())

    if acao:
        acao()

    else:
        print("Ação inválida!")
    
    # Limpeza Final
    #subprocess.run("cls", shell=True)