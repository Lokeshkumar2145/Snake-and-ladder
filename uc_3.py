
def generate_play(type, pos):
    match type:
        case 1 :
            if move()==1 and pos<99:
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