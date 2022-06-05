import random

ladder={1:38,4:14,12:55,16:61,25:50,45:85,49:92,61:96,75:88,82:98}
snake={32:10,34:6,48:26,62:18,88:24,95:56,97:78}
pos1=0
pos2=0

def move(pos):
    dice=random.randint(1,6)
    print(f"Dice:{dice}")
    pos=pos+dice
    if pos in snake:
        print("bitten by snake")
        pos=snake[pos]
        print(f"position:{pos}")
    elif pos in ladder:
        print("climbed by ladder")
        pos=ladder[pos]
        print(f"position:{pos}")
    else:
        print(f"position:{pos}")
    
    print("\n")
    return pos

while True:
    A=input("player 1 enter\"A\" to throw dice:")
    if A=="s":
        pos1=move(pos1)
    else:
        print("Player2 wins")
        break

    if pos1>=100:
        print("Game over!!!---Player 1 wins")
        break

    B=input("player 2 enter\"B\" to throw dice:")
    if B=="s":
        pos2=move(pos2)
    else:
        print("Player1 wins")
        break

    if pos2>=100:
        print("Game over!!!---Player 2 wins")
        break


    


    