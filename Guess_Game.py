import random    
print()                                     
print(" _____                    _____")               
print("|   __|_ _ ___ ___ ___   |   __|___ _____ ___ ")
print("|  |  | | | -_|_ -|_ -|  |  |  | .'|     | -_|")
print("|_____|___|___|___|___|  |_____|__,|_|_|_|___|  Created By: BlitzIQ")
print()                                            
number=int(input("Guess Any Number From 1 to 10: "))
randomnum=random.randint(1,10) #You can change the limit here
if number == randomnum:
    print("you Guessed it right")
else:
    print(">_< OOps Wrong Answer")
    print("The Number is "+str(randomnum) )