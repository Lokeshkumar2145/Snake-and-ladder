import random
def ladder():
    return random.randint(1,3)
    
def move():
    return random.randint(1,3)
def dice():
    global counter
    counter +=1
    return random.randint(1,6)

def switch():
    return random.randint(1,3)

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