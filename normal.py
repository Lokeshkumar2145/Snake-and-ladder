import random
counter = 0
# def occur():
#     return random(ladder(),snake())
def ladder():
    return random.randint(1,3)
    
def snake():
    return random.randint(1,3)
def dice():
    global counter
    counter +=1
    return random.randint(1,6)

def switch():
    return random.randint(1,3)
    

def generate_play(type, pos):
    match type:
        case 1 :
            if snake()==1 and pos<99:
                # snake()
                if pos!=0:
                    print("pos----> ",pos)
                    print("snake bit you ----roll the dice")
                    d1=dice()
                    print("dice value is ------->",d1)
                    pos=pos-d1
                    return pos
            # else:
            #     print("pos----> ",pos)
            #     d1=dice()
            #     print("dice value is ------->",d1)
            #     pos=pos+d1
            #     return pos
        case 2 :
            if ladder()==2 and pos<94:
                # ladder()
                print("pos----> ",pos)
                print("hurray! ladder ----roll the dice")
                d1=dice()
                print("dice value is ------->",d1)
                pos=pos+d1
                return pos
            # else:
            #     print("pos----> ",pos)
            # d1=dice()
            # print("dice value is ------->",d1)
            # pos=pos+d1
            # return pos
        # case _:
    print("pos----> ",pos)
    d1=dice()
    print("dice value is ------->",d1)
    pos=pos+d1
    return pos

def game_play(x):
    pos=0
    result=0
    flag=True
    while flag:
        if result<100:
            result=generate_play(switch(),pos)
            # result=98
            if result<100:
                pos=result
        elif result==100:
            print(result)
            pos=0
            flag=False
        else:
            if result>100:
                # print(result)
                result=pos
                # print(pos)
                continue
    player=x
    return f"{x} won the game"

print("------------player 1 vs player 2--------------")
player1=input("player 1 : Name ------>")
player2=input("player 2 : Name ------>")
print(f"------------{player1} vs {player2}--------------")
print(f"------------{player1} starts the game--------------")
num=random.randint(0,1)
while True:
    if num==0:
        x=game_play(player1)
    else:
        x=game_play(player2)
    break
print(x)
print("The No of times the Dice rolled is --->", counter)
        