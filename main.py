from rps import rps_match
from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# store RPS print sign in a list call option
option = [rock, paper, scissors]

# Add your code here

print("""

        █████████████████████████████████████████████████████████████
        █▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─▄▄─█
        ██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█████─███─██─█
        ▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀     


    ██████╗░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░███████╗██████╗░
    ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝
    ██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
    ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
    ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

            ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
            ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
            ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
            ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
            ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
            ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
""")
click = input()
print("""

▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ 
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ 
      
    ░█▀▀█ ░█─░█ ░█─── ░█▀▀▀ ░█▀▀▀█ 
    ░█▄▄▀ ░█─░█ ░█─── ░█▀▀▀ ─▀▀▀▄▄ 
    ░█─░█ ─▀▄▄▀ ░█▄▄█ ░█▄▄▄ ░█▄▄▄█
      
    𝓣𝓱𝓮 𝓹𝓵𝓪𝔂𝓮𝓻 𝓱𝓪𝓿𝓮 𝟑 𝓸𝓹𝓽𝓲𝓸𝓷𝓼, 𝓡𝓸𝓬𝓴, 𝓟𝓪𝓹𝓮𝓻, 𝓢𝓬𝓲𝓼𝓼𝓸𝓻𝓼

    𝚈𝚘𝚞 𝚊𝚛𝚎 𝚙𝚕𝚊𝚢𝚒𝚗𝚐 𝚠𝚒𝚝𝚑 𝚋𝚘𝚝. 𝚆𝚑𝚘𝚎𝚟𝚎𝚛 𝚐𝚘𝚝 𝟹 𝚠𝚒𝚗 𝚏𝚒𝚛𝚜𝚝, 𝚆𝚒𝚗 𝚝𝚑𝚎 𝚐𝚊𝚖𝚎 !
      
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ 
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ 
    """)
clickk = input()
while True:
    bot_count = 0
    player_count = 0
    while (player_count < 3 and bot_count < 3):
        print("---------  ScoresBoard  ---------")
        print(f"| 💃🕺 Player: {player_count} || 🤖 Bot: {bot_count}   |")
        print("---------------------------------")
        print("You have 3 options, 0 = Rock[🪨], 1 = Paper[📄], 2 = Scissors [✂︎]")
        try:
            player_choice = int(input("Choose your option Ex: If you want to play rock, please input 0: "))
        except ValueError:
            print("Invaild !! Please make sure your input is correct :) ")
            continue
        bot_choice = randint(0,2)
        print(option[player_choice])
        print("💃🕺's choice")
        print("----------------------- ")
        print(option[bot_choice])
        print("🤖's choice")
        print("----------------------- ")

        round = rps_match(player_choice, bot_choice)
        if round == 1:
            player_count += 1
            print("💃🕺 Player win !! ")
            print("----------------------- ")
            continue
        elif round == -1:
            bot_count += 1
            print("🤖's win !!")
            print("----------------------- ")
            continue
        elif round == 0:
            print("IT'S A TIE !!")
            print("----------------------- ")
            continue
        else:
            print(round)
            continue

    if player_count == 3:
        print("🏆 YOU WINNNNN :))")
    elif bot_count == 3:
        print("🤡 YOU LOSE :'(")
    
    confirmation = input("Would you like to continue the game (Y/N): ").lower()
    if confirmation == "n":
        print("Thank you for playing the game !!")
        quit()
    elif confirmation == "y":
        continue

