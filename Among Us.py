import random
emergency=0
print("Welcome to Among Us ඞ")
roles=["Crewmate", "Imposter"]
Istrike=0
names=["Amanda", "Diana", "Elenore", "Harry", "Isak", "Jack"]
foods=["Pizza", "Fries", "Cheese", "Chocolate", "Chicken Nuggets", "Ice Cream"]
imp=[]
taskCount=0
places=["Navigator", "Electrical", "Kitchen"]
y=1
user_name=input("What shall we call you? ")
names.append(user_name)
namess=names.copy()
print("Hi", user_name, ", Welcome to Among Us!")
for i in range(len(names)):
    mhm=random.choice(roles)
    if mhm=="Imposter":
        if Istrike != y:
            Istrike+=1
            imp.append(names[i])
    else:
        continue
if user_name in imp:
    print("You are: Imposter")
    print("Try to sabatoge when no one is around!  Emergency meeting will be held every 1 tasks you do")
else:
    print("You are: Crewmate")
    print("Finish all your Tasks. After your done, Search for the imposter, Emergency meeting will be held every 3 tasks you do")
print(names, ": Those are all the players.")
print("Chapter 1: PLayers Introduce themselves")
for z in names:
    fav = random.choice(foods)
    if z not in imp:
        print(z,": Hi I'm", z, ", and my favourite food is", fav)
        print(" ")
    else:
        print(z, ": Hi I'm", z, ", and my fav food is`", fav )
        print(" ")
Navigator=[]
Electrical=[]
Kitchen=[]
for f in names:
    assign=random.choice(namess)
    namess.remove(assign)
    place=random.choice(places)
    if assign == user_name:
        myplace=assign
    if place == "Navigator":
        if assign == user_name:
            myplace = Navigator
        Navigator.append(assign)
    elif place == "Electrical":
        Electrical.append(assign)
        if assign == user_name:
            myplace = Electrical
    else:
        Kitchen.append(assign)
        if assign == user_name:
            myplace = Kitchen
print("Kitchen:", Kitchen)
print("Electrical:", Electrical)
print("Navigator:", Navigator)
print(myplace, ": Tasks done:", taskCount)
if user_name in imp:
    print("You only have to do 1 task.")
    ask=int(input("701+260= "))
    if ask != 961:
        while True:
            ask = int(input("701+260= "))
            if ask == 961:
                print("EMERGENCY MEETING!")
                emergency = 1
                break
            else:
                continue
    else:
        print("EMERGENCY MEETING!")
        emergency=1
else:
    print("Finish 3 tasks to start Emergency meeting.")
    ask=input("Type 3 words about yourself: ")
    print("EMERGENCY MEETING!")
    taskCount+=1
    emergency = 1
if emergency == 1:
    print("Any suspects?")
    ha=input("Who do you vote out? ")
    haa=random.randint(3, 6)
    if haa > 3:
        print(haa, "people voted", ha)
        if ha in imp:
            print(ha, "was a imposter. Crewmates Win!")
            end="End"
            names.remove(ha)
        else:
            print(ha, "was not a imposter.")
            end="No"
            names.remove(ha)
    else:
        print(7-haa, "skipped")
        end="No"
if end != "End":
    if user_name in imp:
        print("Who would you like to sabatoge? ")
        aha=input("Enter name: ")
        names.remove(aha)
        emergency=0
        print("EMERGENCY MEETING!")
        emergency = 1
        if emergency == 1:
            print("Any suspects?")
            ha = input("Who do you vote out? ")
            haa = random.randint(3, len(names))
            if haa > 3:
                print(haa, "people voted", ha)
                if ha in imp:
                    print(ha, "was a imposter. Crewmates win")
                    end="End"
                else:
                    print(ha, "was not a imposter.")
                    end="No"
            else:
                print(7 - haa, "chose you, Crewmates win!")
                end="End"
                print("Imposters were:", print(imp))
    else:
        print("MALFUNCTION-Finish 1 task to emergetite a meetingggg---")
        print("ANOTHER MALFUNCTIOOONN--EMERGENCY MEETING-")
        emergency = 1
        if emergency == 1:
            print("Time to vote out once...and for all.")
            ha = input("Who do you vote out? ")
            haa = random.randint(3, len(names))
            if haa > 3:
                print(haa, "people voted", ha)
                if ha in imp:
                    print(ha, "was a imposter. Crewmates win")
                    end = "End"
                else:
                    print(ha, "was not a imposter.")
                    end = "No"
            else:
                print(7 - haa, "chose you, Crewmates win!")
                end = "End"
                print("Imposters were:", print(imp))