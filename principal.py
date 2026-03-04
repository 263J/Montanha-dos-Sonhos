# Limpeza inicial
from menu import Menu

Menu.limpar()

# Menu principal
while True:

    print(Menu.mensagem)

    # Decisão
    acao = Menu.acoes.get(input("Escolha: ").lower())

    if acao:
        acao()

    else:
        Menu.mensagem = "Ação Inválida!"
    
    # Limpeza Final
    Menu.limpar()