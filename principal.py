# Importando bibliotéca para ações no prompt
import subprocess

# Limpeza inicial
subprocess.run("cls", shell=True)

# Variáveis
finalizado = False

# Funções
def atacar():
    print("Você atacou!")

def defender():
    print("Você defendeu!")

def correr():
    print("Você fugiu!")

def fechar():
    global finalizado
    print("Você Fechou!")
    finalizado = True

acoes = {
    "atacar": atacar,
    "defender": defender,
    "correr": correr,
    "fechar": fechar
}

# Laço principal
while not finalizado:

    # Decisão
    opcao = input("Escolha: ")

    acao = acoes.get(opcao)
    if acao:
        acao()
    else:
        print("Opção inválida")
    
    # Limpeza Final
    #subprocess.run("cls", shell=True)