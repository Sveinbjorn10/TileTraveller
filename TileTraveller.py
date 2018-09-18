# 1) Það var auðveldara að nota functions þar sem maður þurfti ekki að skrifa það sama
#    aftur og aftur. Ég náði að helminga kóðann minn með því að bæta bara inn 2 functionum.
#    sérstaklega með movement() functioninu. options() var meira notað til að hafa forritið 
#    stílhreinna.
# 2) Klárlega auðveldara að lesa seinna versionið. Bæði útaf functionunum og fáeinum breytingum
#    sem ég gerði. Í staðin fyrir að hafa einhverja langloku fyrir hvern og einn reit, þá get
#    ég útskýrt hvern og einn reit með variables og unnið út frá því á sama hátt fyrir alla
#    reiti. Aðal ástæðan er þó sú að maður er ekki endalaust að lesa hér um bil sama texta.
# 3) Ég gat búið til function sem ákvarðaði hreyfinguna á notandanum miðað við þann reit sem
#    hann er í nú þegar. Einnig bjó ég til print function sem er nú hálf tilgangslaus en vegna
#    þess að við erum að æfa okkur í functions fannst mér viðeigandi að bæta því við.
#    Hefði vilja búa til function sem gat ákvarðað hvaða Tile væri um að ræða án þess að nota
#    Endalaust af if setningum. En ég fann ekki leið til þess. Allavega ekki leið sem við
#    eigum að vera búinn að læra.

user = 11

T = "You can travel: "
N = "(N)orth"
E = "(E)ast"
S = "(S)outh"
W = "(W)est"
OR = " or "
P = "."

Tile11 = T + N + P
Tile12 = T + N + OR + E + OR + S + P
Tile13 = T + E + OR + S + P
Tile21 = T + N + P
Tile22 = T + S + OR + W + P
Tile23 = T + E + OR + W + P
Tile31 = T
Tile32 = T + N + OR + S + P
Tile33 = T + S + OR + W + P

def options(tilenr):
    print(tilenr)

def movement(tilenr):
    while True:
        user_input = input("Direction: ").capitalize()
        if user_input in tilenr:
            if user_input == "N":
                return 1
            elif user_input == "E":
                return 10
            elif user_input == "S":
                return -1
            else: #"West"
                return -10
        else:
            print("Not a valid direction!")

tilenum = Tile11 

while True:
    if user == 11:
        tilenum = Tile11
    elif user == 12:
        tilenum = Tile12
    elif user == 13:
        tilenum = Tile13
    elif user == 21:
        tilenum = Tile21
    elif user == 22:
        tilenum = Tile22
    elif user == 23:
        tilenum = Tile23
    elif user == 32:
        tilenum = Tile32
    elif user == 33:
        tilenum = Tile33
    else:
        break

    options(tilenum)
    user += movement(tilenum)

print("Victory!")    