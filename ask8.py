import random 

def Winner(pospyrgx,pospyrgy,posaksx,posaksy):
    winner = None

    #εαν νικησε ο πυργος
    
    for i in range(8):
        if pospyrgx == posaksx and i == posaksy:
            winner = "P"
            break
        elif winner!= None and i ==posaksx and pospyrgy == posaksy:
            winner = "P"
            break

    #εαν νικησε αξιωματικος
    mult=1
    while posaksx+mult<=7 and winner==None:
        try:
            if posaksy+mult == pospyrgy and posaksx+mult == pospyrgx:
                winner = "A"
                break
        finally:
            try:
                if posaksy-mult == pospyrgy and posaksx+mult == pospyrgx:
                    winner = "A"
                    break
            finally:
                mult+=1
    mult=1
    while posaksx-mult>=0 and winner==None:
        try:
            if posaksy+mult == pospyrgy and posaksx-mult == pospyrgx:
                winner = "A"
                break
        finally:
            try:
                if posaksy-mult == pospyrgy and posaksx-mult == pospyrgx:
                    winner = "A"
                    break
            finally:
                mult+=1

    return winner

#ποσες φορες νικησε ο καθενας
pyrgos = 0
aksiomatikos = 0

for i in range(100):
    #θεσεις πυργου
    pospyrgx = random.randint(0,7)
    pospyrgy = random.randint(0,7)

    #θεσεις αξιωματικου
    posaksx = random.randint(0,7)
    posaksy = random.randint(0,7)

    #να μην εχουν ιδιες θεσεις
    while posaksy == pospyrgy and pospyrgx == posaksx:
        posaksy = random.randint(0,7)
    
    #επεξεργαζει ποιος νικησε
    winner = Winner(pospyrgx,pospyrgy,posaksx,posaksy)
    if winner == "P":
        pyrgos += 1
    elif winner == "A":
        aksiomatikos += 1
   
#αποτελεσματα
print ("Rook won :",pyrgos," times")
print ("Bishop won :",aksiomatikos," times")