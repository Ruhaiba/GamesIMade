import random
rps=["Rock", "Paper", "Scissors"]
mem={"Rock":"Scissors", "Scissors":"Paper", "Paper":"Rock"}
userpoint=0
botpoint=0
for i in range(100):
    bot_choice=random.choice(rps)
    user_choice=input("Rock, Paper or Scissors? ")
    if user_choice not in rps:
        print("Invalid Input")
    else:
        print("Bot played", bot_choice)
        give=mem.get(bot_choice)
        if user_choice == give:
            botpoint+=1
            print("1 point to Bot!")
        elif user_choice == bot_choice:
            print("Tie. Nobody's point!")
        else:
            userpoint+=1
            print("1 point to User!")
        print("Bot:", botpoint, "User:", userpoint)
        while True:
            x=input("Would you like to play again (Yes/No)? ")
            x=x.lower()
            if x=="yes":
                s=0
                break
            elif x=="no":
                print("Thank you for playing.")
                s=1
                break
            else:
                print("Invalid input")
        if s==1:
            break