import os
import time 
import sys

debug = True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dottime():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")

def ht():
    for _ in range(3):
        print(".", end='\r')
        time.sleep(1)
        print(" ", end='\r')  # Limpa o caractere anterior
        time.sleep(1)

def format_text(text, color_code):
    """
    Aplica formatação ANSI ao texto.
    
    Args:
        text (str): O texto a ser formatado.
        color_code (str): O código ANSI para a formatação desejada.
    
    Returns:
        str: O texto formatado.
    """
    return f"\033[{color_code}m{text}\033[0m"

def lembrancas(type, message):
    if type == "character":
        print("\n" + "="*50)
        print("📜 LEMBRANÇA ADICIONADA 📜")
        print("\n",message)
        print(format_text("*Personagem adicionado à lembrança*", "3;32"))
        print("="*50)
    elif type == "event":
        print("\n" + "="*50)
        print("📜 LEMBRANÇA 📜")
        print(message)
        print("="*50)
    elif type == "notifica":
        print("\n" + "="*50)
        print("📜 NOTIFICAÇÃO 📜")
        print("Seu personagem tem lembranças. Tudo que ele descobre e faz é adicionado às lembranças.")
        print("Você pode acessar as lembranças do seu personagem a qualquer momento escrevendo 'memories'.")
        print("="*50)


def status(fear, sleep, injuries):
    """
    Updates and displays the character's status based on fear, sleep, and injuries levels.
    Applies buffs and nerfs based on the character's current state.
    """
    # Determine the character's state based on thresholds
    if fear > 80:
        state = "assustado"
        nerfs = "Redução na precisão e velocidade de reação."
    elif fear > 50:
        state = "medroso"
        nerfs = "Leve redução na precisão."
    else:
        state = "calmo"
        nerfs = "Nenhum."

    if sleep < 20:
        state = "exausto"
        nerfs = "Redução significativa na energia e foco."
    elif sleep < 50:
        state = "cansado"
        nerfs = "Leve redução na energia."

    if injuries > 80:
        state = "incapacitado"
        nerfs = "Impossível realizar ações físicas."
    elif injuries > 50:
        state = "ferido"
        nerfs = "Redução na mobilidade e força."

    # Display the character's status
    print("\n" + "="*50)
    print("📜 STATUS DO PERSONAGEM 📜")
    print(f"Medo: {fear}/100")
    print(f"Sono: {sleep}/100")
    print(f"Ferimentos: {injuries}/100")
    print(f"Estado: {state}")
    print(f"Efeitos: {nerfs}")
    print("="*50)

# Valores iniciais do personagem
# Esses valores podem ser alterados durante o jogo
fear = 0
sleep = 0
injuries = 0
# Example usage of the status function
# status(10, 20, 40)  # Exibindo o status do personagem redefinindo os valores
# status(+20, +10, +50)  # Exibindo o status do personagem com base em valores aritméticos

def notification(type, message):
    if type == "found_item":
        print("\n" + "="*50)
        print("📜 ITEM ENCONTRADO 📜")
        print(message)
        print("="*50)
    elif type == "character_status":
        print("*Status do personagem atualizado*")


def sms_message (number, message):
    print(format_text("NOVA MENSAGEM SMS", "1;35"))
    print(f"De: {number}")
    mess = input("Abrir a mesnagem? (s/n): ")
    if mess.lower() == 's':
        print(format_text("Você abriu a mensagem.", "3;33"))
        print(format_text(message, "1;32"))
        print(format_text("Mensagem recebida com sucesso!", "1;32"))
    else:
        print("Você ignorou a mensagem.")

# sms_message("555-1234", "Oi amor, sou eu, tenho saudades.")  # Exemplo de mensagem SMS
# Example usage of the notification function
# notification("found_item", "Você encontrou uma lanterna! Isso pode ser útil para iluminar a escuridão.")
# notification("character_status",status(10,20,40))  # Exemplo de status do personagem

def display_gameintro ():
    clear_screen()
    dottime()
    clear_screen()
    print("\033[1;34mEstados Unidos, Califórnia , 2010\033[0m")  # Narração da cena
    ht()
    print("\nMeu nome é Jhon Dalton, tenho 23 anos e... desempregado.")
    ht()
    print("Depois de me formar em engenharia de software, não consegui um emprego.")
    ht()
    print("A crise de 2008 me pegou de jeito e o fato de que o mercado está superfaturado... Ferrou tudo.")
    ht()
    print("\nEntão decidi fazer algo que desse alguma grana, por enquanto.")
    ht()
    print("\nMeu irmão é Park Ranger no Mount San Gorgono. Ele me disse que o parque está cheio de turistas.")
    ht()
    print("E as férias de verão estão chegando... Muitos adolescentes vão para lá acampar e acabam fazendo merda.")
    ht()
    print("Fazem fogueiras em locais não permitidos, fumam, bebem... Por conta disso, o parque nessa época fica com um problema de incêndios.")
    ht()
    print("Para ajudar na fiscalização e sei lá mais  o que, eles remanejam todos os rangers para as patrulhas, incluindo os que ficam nos postos avançados de torre de vigia e combate a incêndios.")
    ht()
    print("\nE é aí que eu entro. Eles estão precisando de gente para ajudar a vigiar esses incêndios, lá de cima da torre.")
    ht()
    print("Meu irmão me recomendou para trabalhar nessas torres, me ligaram oferecendo e eu topei.")
    ht()
    print("A grana é boa, e eu vou ter um lugar para ficar. Lá em cima, na torre, por 3 semanas. Vai ser um trabalho chato, mas é melhor do que nada.")
    ht()
    print("Terei que fazer umas semanas de treinamento de sobrevivência e de procedimentos básicos das torres.")
    ht()
    print("Vou ter que ficar lá em cima, sozinho, sem ninguém por perto. Vamos ver como vai ser.")
    ht()
    print("\nAmanhã vou pegar a estrada e ir para o parque.")
    ht()

def gameplay_epilogue():
    clear_screen()
    print("\033[1;34mRodovia que liga Los Angeles ao Mount San Gorgonio, 07:38 da manhã.\033[0m")  # Narração da cena
    ht()
    print("\nDepois de 2 horas dirigindo, finalmente cheguei ao parque.")  # Narração do personagem
    ht()
    print("O parque é lindo. Montanhas, árvores, lagos, tudo muito bonito.")
    ht()
    print("O clima é bom, o sol está brilhando e a temperatura está agradável.")
    ht()
    print("Depois de passar pela entrada do parque, peguei a estrada de terra que leva até o posto avançado.")
    ht()
    print("O posto avançado é um pequeno prédio de madeira, com uma torre de vigia ao lado. É baixa, feita de madeira também.")
    ht()
    print("\033[1;32mPark Ranger:\033[0m Oi, você deve ser o Jhon. Eu sou o Matt, vou estar com você nesse período. Você lá em cima e eu aqui embaixo.")
    time.sleep(2)
    lembrancas("character", "Você conheceu o Park Ranger Matt.")
    ht()
    print(format_text("Você: ", "1;32") + "Ah... Oi Mat. Sim, eu sou o Jhon...")

if debug == True:
    gameplay_epilogue()

def gameplay_loop():
    while True:
        print("Você está na torre de vigia. O que você quer fazer?")
        print("1. Olhar pela luneta")
        print("2. Fazer uma pausa")
        print("3. Sair do jogo")
        
        choice = input("Escolha uma opção (1/2/3): ")
        
        if choice == '1':
            print("Você olha pela luneta e vê uma bela paisagem.")
            dottime()
        elif choice == '2':
            print("Você faz uma pausa e relaxa um pouco.")
            dottime()
        elif choice == '3':
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if debug == False:
    display_gameintro()