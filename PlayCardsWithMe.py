import random
me=[]
you=[]
mez=0
youz=0
cards_deck=["K", "Q", "J", "9", "10", "A", "5", "8", "1", "7", "2", "4", "3", "6"]
cards_decks=cards_deck.copy()
nums = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
ans=input("Hi! Wanna play cards with me (Yes or No)? ")
ans=ans.lower()
if ans == "yes":
    print("Awsome! Now lets play!")
    print("A>K>Q>J>10>9>8>7>...You get the picture...")
    z=2
else:
    print("Come on- give it a go!")
    for g in range(2):
        ans = input("PLEASE play cards with me (Yes or No)? ")
        ans = ans.lower()
        if ans == "yes":
            print("Yay! I changed your mind! Now lets play!")
            print("A>K>Q>J>10>9>8>7>...You get the picture...")
            z=2
            break
        else:
            z=1
if z==2:
    for i in range(14):
        x=random.choice(cards_decks)
        if len(me) < 7:
            me.append(x)
            cards_decks.remove(x)
        else:
            you.append(x)
            cards_decks.remove(x)
    print(you)
    print("Those are your cards")
    for s in range(7):
        while True:
                playze = input("Your play: ")
                print("You don't have that card. Please try again.")
                if playze not in you:
                    continue
                else:
                    k=0
                    break
        if k==0:
            you.remove(playze)
            print(you, "-Your cards after the last play")
            mhmm = nums.index(playze)
            funi=""
            samp = nums[mhmm+1:]
            for r in me:
                if r in samp:
                    funi=r
                else:
                    funi=""
            if funi == "":
                print(me[0])
                me.remove(me[0])
                print("Your point.")
                youz += 1
            else:
                print(funi)
                mez += 1
                print("My point!")
                me.remove(funi)
    if youz>mez:
        print("Good Game, you win")
    elif youz<mez:
     print("WOHOO! I WIN")
    print("Your point(s):",youz,"My point(s):",mez)
elif z==1:
    print("PlayGPT kicked you out of the server")