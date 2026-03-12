import random
def rollFunc(bet,amount):
    symbols=[
        "first.png",
        "second.png",
        "third.png",
        "fourth.png",
        "fifth.png"
    ]
    slot_result=random.choices(symbols,k=3)

    X=1
    complement="xyz"
    new_amount=amount

    fcount=0
    scount=0
    tcount=0
    focount=0
    ficount=0

    for symbol in slot_result:
        if symbol=="first.png":
            fcount=fcount+1
        elif symbol=="second.png":
            scount=scount+1
        elif symbol=="third.png":
            tcount=tcount+1
        elif symbol=="fourth.png":
            focount=focount+1
        else:
            ficount=ficount+1

    if fcount==3 or fcount==2:
        X=0
    if fcount==1:
        X=X/1.7
    if ficount==3:
        X=X*5
    if ficount==2:
        X=X*3
    if ficount==1:
        X=X*2
    if tcount==2 or tcount==3:
        X=X*1.3
    if   scount==2 or scount==3:
        X=X/3
    if focount==2 or focount==3:
        X=X*3
    if X==1:
        X=0
        
    
    if X<=1.5:
        X=0
    if X>=5:
        X=5


    if X==0:
        complement="All your bet money is Gone"
        new_amount=amount-bet
    elif X>0 and X<=1:
        complement="That was a okaish bet."
        new_amount=amount+((bet*X))
    elif X>1 and X<=2:
        complement="Good Roll."
        new_amount=amount+((bet*X))
    elif X>2 and X<=3:
        complement="That was a okaish bet."
        new_amount=amount+((bet*X))
    elif X>3 and X<=4:
        complement="Voooooooooo! HAHAHAHAAHAHHAH"
        new_amount=amount+((bet*X))
    elif X>4 and X<=4.5:
        complement="BIIIIIIIG bet coming."
        new_amount=amount+((bet*X))
    elif X>4.5 and X<=5:
        complement="5XXXXXXXXXXXX BABAY"
        new_amount=amount+((bet*X))
    else:
        complement=None
        new_amount=amount

    return complement,X,new_amount,slot_result