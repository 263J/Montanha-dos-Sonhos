import ollama
import random

player_hp = 30
goblin_hp = 20

def narrar(texto):
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": "Você é um narrador de RPG medieval sombrio, use menos de 20 palavras para escrever, seja detalhista e apenas narre o ocorrido."},
            {"role": "user", "content": texto}
        ]
    )
    return response["message"]["content"]

print("Um goblin selvagem aparece na floresta!")

while player_hp > 0 and goblin_hp > 0:
    acao = input("\nO que você faz? ")

    if "atac" in acao.lower():
        dano = random.randint(4, 8)
        goblin_hp -= dano
        texto = f"O jogador ataca o goblin e causa {dano} de dano."
        print(narrar(texto))
    
    elif "magia" in acao.lower():
        dano = random.randint(6, 12)
        goblin_hp -= dano
        texto = f"O jogador conjura uma magia poderosa e causa {dano} de dano."
        print(narrar(texto))
    
    else:
        print("Ação não reconhecida.")

    if goblin_hp > 0:
        dano = random.randint(3, 6)
        player_hp -= dano
        print(f"O goblin contra-ataca e causa {dano} de dano!")

    print(f"\nSua vida: {player_hp}")
    print(f"Vida do goblin: {goblin_hp}")

if player_hp <= 0:
    print("Você morreu...")
else:
    print("O goblin foi derrotado!")