num=random.randint(0,1)
while True:
    if num==0:
        x=game_play(player1)
    else:
        x=game_play(player2)
    break
print(x)