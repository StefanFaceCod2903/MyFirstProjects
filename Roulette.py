import random
money = 100

def rd(betmoney, rand):
    glmoney = money
    num = random.randint(1, 36)
    if num in range(1, 36, 3):
        rnd = 1
    elif num in range(2,36,3):
        rnd = 2
    else:
        rnd = 3
    if rand == rnd:
        glmoney += betmoney*2
        print("Felicitari! A picat {} care este in randul {}. Acum ai {} euro.".format(num, rnd, glmoney))
    else:
        glmoney -= betmoney
        print("Ce pacat! A picat {} care este in randul {}. Acum ai {} euro.".format(num, rnd, glmoney))
    return glmoney

def cul(betmoney, culoare):
    glmoney = money
    num = random.randint(0, 1)
    if 1 == num:
        color='rosu'
    else:
        color='negru'
    if(culoare.lower()[0] == color[0] or culoare[0] == color[0]):
        glmoney += betmoney*2
        print("Felicitari! A picat {}. Acum ai {} euro.".format(color, glmoney))
    else:
        glmoney -= betmoney
        print("Ce pacat! A picat {}. Acum ai {} euro.".format(color, glmoney))
    return glmoney

def coloana(betmoney, nr_coloana):
    glmoney = money
    num = random.randint(1,36)
    if num in range(1,13):
        col = 1
    elif num in range(13, 25):
        col = 2
    else:
        col = 3
    if(nr_coloana == col):
        glmoney += betmoney*2
        print("Felicitari! A picat {} care este in coloana {}. Acum ai {} euro.".format(num, col, glmoney))
    else:
        glmoney -= betmoney
        print("Ce pacat! A picat {} care este in coloana {}. Acum ai {} euro.".format(num, col, glmoney))
    return glmoney
def numar(betmoney, nr):
    glmoney = money
    num = random.randint(1,36)
    if num == nr:
        glmoney += betmoney*35
        print("Felicitari! A picat chiar {}. Acum ai {} euro.".format(num,glmoney))
    else:
        glmoney -= betmoney
        print("Ce pacat! A picat {}. Acum ai {} euro.".format(num,glmoney))
    return glmoney

name = input("Cum te cheama?\n")
print("{}, bine ai venit la simulatorul de ruleta! La inceput primesti {} de euro.".format(name, money))
mai_joc = "Da"
while mai_joc[0]=="D" or mai_joc[0]=="d":
    print("Pariezi pe numar, coloana, rand sau culoare?")
    metoda = input()
    if metoda[2] == "m" or metoda[2] == "M":
        betmoney = int(input("Cat vrei sa pariezi?\n"))
        nr = int(input("Ce numar alegi?\n"))
        money = numar(betmoney, nr)
    if metoda[1] == "o" or metoda[1] == "O":
        betmoney = int(input("Cat vrei sa pariezi?\n"))
        nr_coloana = int(input("Care coloana alegi?\n"))
        money = coloana(betmoney, nr_coloana)
    if "CU" in metoda or "cu" in metoda :
        betmoney = int(input("Cat vrei sa pariezi?\n"))
        culoare = input("Care culoare alegi?\n")
        money = cul(betmoney, culoare)
    if metoda[0] =="r" or metoda[0]=="R":
        betmoney = int(input("Cat vrei sa pariezi?\n"))
        rand = int(input("Ce rand alegi?\n"))
        money = rd(betmoney, rand)
    if money == 0:
        break
    else:
        mai_joc = input("Mai vrei sa joci?\n")
sfarsit = input("Sfarsitul jocului!")


