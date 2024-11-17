import random
words = ["TIGER", "UMBRELLA", "PLATES", "WARM", "YELLOW", "APPLE", "BRAIN", "DONUTS", "CUPCAKES", "LOLIPOPS", "WATER", "BREAD", "KANGAROO", "FLOWER", "QUEEN", "GARLIC", "PARTY", "TIME", "MOUNTAINS", "WRONG", "WRITE", "ERASE", "PENCIL", "PIPE"]
word=random.choice(words)
wor=""
for l in word:
    wor+=l
strike=0
hidd=""
head="(-_-)"
body="|"
leg2="\ "
leg1=" /"
arm="--"
for i in range(len(word)):

    lay=str(i)
    hidd+=lay
print(hidd)
z=0
for t in range(100):
    if hidd == wor:
        break
    ans=input("Guess away! : ")
    if len(ans)>1:
        while True:
            ans = input("Please try again! : ")
            if len(ans)==1:
                z=1
                break
            else:
                continue
    elif len(ans)==1 or z==1:
        if ans in word:
            ha=word.count(ans)
            for ss in range(ha):
                y=word.index(ans)
                yz=str(y)
                hidd=hidd[:y]+ans+hidd[y+1:]
                word=word[:y]+"_"+word[y+1:]
            print(hidd)
        else:
            if strike==0:
                strike+=1
                print(head)
            elif strike==1:
                strike+=1
                print(head)
                print(" ",body)
            elif strike==2:
                strike+=1
                print(head)
                print("-",body)
            elif strike==3:
                strike+=1
                print(head)
                print("-",body,"-")
            elif strike==4:
                strike+=1
                print(head)
                print("-",body,"-")
                print(leg1)
            elif strike==5:
                strike+=1
                print(head)
                print("-",body,"-")
                print(leg1, leg2)
                break
if strike != 6:
    print("Bravo! You got the word!")
else:
    print("Better luck next time, the word was", wor)