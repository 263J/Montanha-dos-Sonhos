# Importando bibliotéca para ações no prompt
import subprocess

# Limpeza inicial
subprocess.run("cls", shell=True)

# Funções
def atacar():
    print("Você atacou!")

def defender():
    print("Você defendeu!")

def correr():
    print("Você fugiu!")

acoes = {
    "atacar": atacar,
    "defender": defender,
    "correr": correr
}

# Laço principal
while True:

    # Decisão
    menuPrincipal = input("Escolha: ").lower()

    #

    acao = acoes.get(menuPrincipal)

    if menuPrincipal == "fechar":
        break

    if acao:
        acao()

    else:
        print("Ação inválida!")
    
    # Limpeza Final
    #subprocess.run("cls", shell=True)