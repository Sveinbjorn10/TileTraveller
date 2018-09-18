# Í þessum kóða nota ég while lykkju sem er alltaf sönn. 
# Ég mun brjóta hana þegar ég er kominn með userinn í stöðu 3.1.
# Inn í þeirri lykkju er ég með if setningar fyrir hvern og einn glugga í völundarhúsinu.
# Þar á eftir prenta ég út þær hreyfingar sem notandi má taka í hverjum og einum glugga.
# Þar inn í set ég inn while lykkju sem biður um áttina sem aðilinn vill fara í.
# í þessum lykkjum athuga ég hvort leyfileg átt hefur verið valin. Ef ekki þá kemur villumelding
# og lykkjan fer annan hring og biður um nýja átt. Ef rétt átt er valin þá hækkar núverandi staða
# í samræmi við  þá átt sem notandinn vill taka.
# Svo loks þegar einstaklingur hefur komist í reit 3.1 þá brýt ég aðal while lykkjuna og tilkynni
# notanda að hann hafi unnið!

# https://github.com/Sveinbjorn10/TileTraveller

user = 1.1

North = "nN"
East = "eE"
South = "sS"
West = "wW"

user_input = ""

while True:
    if user == 1.1:
        print("You can travel: (N)orth.")
        while True:
            user_input = input("Direction: ")
            if user_input in North:
                user += 0.1
                user = round(user, 2)
                break
            else:
                print("Not a valid direction!")

    if user == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        while True:
            user_input = input("Direction: ")
            if user_input in North:
                user += 0.1
                user = round(user, 2)
                break
            elif user_input in East:
                user += 1
                user = round(user, 2)
                break
            elif user_input in South:
                user -= 0.1
                user = round(user, 2)
                break
            else:
                print("Not a valid direction!")

    if user == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        while True:
            user_input = input("Direction: ")
            if user_input in East:
                user += 1
                user = round(user, 2)
                break
            elif user_input in South:
                user -= 0.1
                user = round(user, 2)
                break
            else:
                print("Not a valid direction!")

    if user == 2.1:
        print("You can travel: (N)orth.")
        while True:
            user_input = input("Direction: ")
            if user_input in North:
                user += 0.1
                user = round(user, 2)
                break
            else:
                print("Not a valid direction!")

    if user == 2.2:
        print("You can travel: (S)outh or (W)est.")
        while True:
            user_input = input("Direction: ")
            if user_input in South:
                user -= 0.1
                user = round(user, 2)
                break
            elif user_input in West:
                user -= 1
                user = round(user, 2)
                break
            else:
                print("Not a valid direction!")

    if user == 2.3:
        print("You can travel: (E)ast or (W)est.")
        while True:
            user_input = input("Direction: ")
            if user_input in East:
                user += 1
                user = round(user, 2)
                break
            elif user_input in West:
                user -= 1
                user = round(user, 2)
                break
            else:
                print("Not a valid direction!")

    if user == 3.1:
        break

    if user == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        while True:
            user_input = input("Direction: ")
            if user_input in North:
                user += 0.1
                user = round(user, 2)
                break
            elif user_input in South:
                user -= 0.1
                user = round(user, 2)
                break
            else:
                print("Not a valid direction!")

    if user == 3.3:
        print("You can travel: (S)outh or (W)est.")
        while True:
            user_input = input("Direction: ")
            if user_input in South:
                user -= 0.1
                user = round(user, 2)
                break
            elif user_input in West:
                user -= 1
                user = round(user, 2)
                break
            else:
                print("Not a valid direction!")

print("Victory!")