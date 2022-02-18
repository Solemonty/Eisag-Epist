from unicodedata import decimal


#μετραει σειρα
def counter(line):
    zero = 0
    one = 0
    length = 1
    #τρεχει την γραμμη ελεγχοντας καθε στοιχιο με το επομενο (εαν ειναι ιδια τοτε πρσθετει 1 στο length,εαν οχι μηδενιζει)
    for i in range(len(line)):
        try:
            if line[i] != line [i+1]:
                if line[i] == "0" and zero < length:
                    zero = length
                elif line[i] == "1" and one < length:
                    one = length
                length = 1
            else:
                length += 1
        except:
            if line[i] == "0" and zero < length:
                zero = length
            elif line[i] == "1" and one < length:
                one = length
            break
        
    return zero,one

f = open("demofile.txt", "r")
demoline = f.read()
clearline = ""
for i in demoline:
    binary = bin(ord(i))
    #ποσα μηδενικα πρεπει να προσθεσω στην αρχη
    add = 9 - len(binary)

    #προσθετει μηδενικα
    for i in range(add):
        clearline += "0"

    #προσθετει στοιχια στην τελικη γραμμη
    for i in range(2,len(binary)):
        clearline += binary[i]
    
    
zero,one = counter(clearline)
print ("Longest row from 0 is ",zero)
print ("Longest row from 1 is ",one)

