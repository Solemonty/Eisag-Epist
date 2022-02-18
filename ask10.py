from unicodedata import decimal

f = open("demofile.txt", "r")
demoline = f.read()
templine = ""
clearline = []
for i in demoline:
    binary = bin(ord(i))
    #ποσα μηδενικα πρεπει να προσθεσω στην αρχη
    add = 9 - len(binary)

    #προσθετει μηδενικα
    for i in range(add):
        templine += "0"

    #προσθετει ολα στοιχεια στην templine
    for i in range(2,len(binary)):
        templine += binary[i]

    #προσθετει τελικα στοιχεια στην λιστα
    for i in range(2):
        clearline.append(templine[i])
    for i in range(-2,0):
        clearline.append(templine[i])
    
    templine = ""

finish = False
number = ""

#counter για μεταβλητες που διαιρουνται με 2,3,5,7 χωρις υπολοιπο
meto2 = 0
meto3 = 0
meto5 = 0
meto7 = 0
sumnumbers = 0
while not finish:
    try:
        #περνει 16 πρωτα στοιχεια και τα βαζει για επεξεργασια
        for i in range(16):
            number += str(clearline.pop(0))

        #μετατρεπει την σειρα στην κανονικη μορφη
        number = int(number, 2)
        sumnumbers += 1
        #ελεγχει εαν διαρειται χωρις υπολοιπο
        if number%2 == 0:
            meto2 += 1
        if number%3 == 0:
            meto3 += 1
        if number%5 == 0:
            meto5 += 1
        if number%7 == 0:
            meto7 += 1
            
        number = ""

    except:
        #μετατρεπει οτι εχει μεινει και κανει ελεγχους
        try:
            number = int(number, 2)
            sumnumbers += 1
            if number%2 == 0:
                meto2 += 1
            if number%3 == 0:
                meto3 += 1
            if number%5 == 0:
                meto5 += 1
            if number%7 == 0:
                meto7 += 1

        except:
            finish = True

        finally:
            finish = True

print ("There are:")
print (int(meto2/sumnumbers*100),"% Even numbers")
print (int(meto3/sumnumbers*100),"% Which divide by 3")
print (int(meto5/sumnumbers*100),"% Which divide by 5")
print (int(meto7/sumnumbers*100),"% Which divide by 7")
