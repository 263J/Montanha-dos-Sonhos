import subprocess
import sys

class Menu:
    mensagem = "Bem-vindo ao jogo!"

    def limpar():
        subprocess.run("cls", shell=True)

    def atacar():
        Menu.mensagem = "Você atacou!"

    def defender():
        Menu.mensagem = "Você defendeu!"

    def correr():
        Menu.mensagem = "Você fugiu!"

    def fechar():
        sys.exit()

    acoes = {
        "atacar": atacar,
        "defender": defender,
        "correr": correr,
        "fechar": fechar
    }