#Jeu Porte Dragons / Boucles
import random
playagain = "a"
print("***")
print("Player,Welcome in this New Fantastic Adventure...")
input("Each time you see ***, please press -ENTER-")
print("Yes, well done, like that!:)")
input("***")
print("Each time you have a question (?), please answer to the narrator.")
input("***")
print("Just to be aware of...")
print("We don't have the budget for musics and images for the moments...")
print("You'll be pleased by using your mind and imagination. THANK YOU !")
input("***")
print("So, you are just in front of a HUGE castel with a BIG door...")
print("You decide to go inside this mysterious place..")
input("***")
print("Toc toc toc...toc")
input("***")
print("...")
input("***")
print("<<SOMEBODY HERE...!?>>")
username=input("<<FOREIGNER, what's your name ?>>(name)(?)")
danger = "d"
while playagain != "EXIT":
    while danger != "yes":
        danger=input("<<Do you have an weapon with you?>> (?)")
        if danger == "yes":
            print("***")
            print("GRRRRRRR...Door is opening...")
        elif danger == "no":
            print("<<Come back when you'll have one, unaware !>>")
        else:
            print("<<I only know TWO words, sorry.. it's yes or no !>>")
    input("***")
    print("It's really DARK inside...")
    print("You're not really reassured to be honest...")
    input("***")
    print("In front of you, 2 differents doors.")
    door = "dd"
    #while door != "A" or "B":
    while door not in ["A", "B"]:
        door=input("In which one would you like to go? A or B ? (?)")
        if door == "A":
            print("Your chose door number A.")
            print("There is a sleeping DRAGON in this room..")
            input("***")
            print("You have two choices:")
            print("1)Try to steal its gold.")
            print("2)Try to escape to him.")
            dragonchoice = "dragonchoice"
            while dragonchoice not in ["1", "2"]:
                dragonchoice = input("What's your choice?")
                if dragonchoice == "1":  
                    print("You woke up the TERRIBLE DRAGON..")
                    input("***")
                    print("GAME OVER",username)
                elif dragonchoice == "2":
                    print("You escape the dragon and leave the castle!")
                    input("***")
                    print("WELL DONE, YOU SURVIVED",username,"!")
                else:
                    print("Answer 1 or answer 2 ?")
        elif door == "B":
            print("You chose door number B.")
            print("There is a MAGICIAN in this room..")
            input("***")
            print("<<STRANGER, I think about a number between 1 to 3..>>")
            print("<<If you find it, you're FREE. If you don't, you DIE..>>")
            number = int(input("1, 2 or 3 (?)"))
            b = random.randint(1,3)
            if number == b:
                print("<<TRUE, same number. I choosed",number,"too !>>")
                print("<<You're FREE..>>")
                input("***")
                print("You escape the MAGICIAN and leave the castle!")
                input("***")
                print("WELL DONE, YOU SURVIVED",username,"!")
            else:
                print("<<It's not the good answer, it was",b,"...>>")
                input("***")
                print("GAME OVER",username)              
        else:
            print("No, it's A or B, PLEASE..")
    playagain = input("*** to play again, or write EXIT to quit. (?)")

          



    
