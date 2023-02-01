print("Tervetuloa heittämään noppia! Voit heittää neljä-, kuusi-, kahdeksan-, kymmen-, kaksitoista- ja kaksikymmensivuista noppaa")


def heitä_noppaa():
    valinnat = input("Heittääksesi erilaisia noppia, kirjoita d4, d6, d8, d10, d12 tai d20: ")

    if valinnat == "d4":
        import random
        min = 1
        max = 4
        print ("Heitit neljäsivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    if valinnat == "d6":
        import random
        min = 1
        max = 6
        print ("Heitit kuusisivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    if valinnat == "d8":
        import random
        min = 1
        max = 8
        print ("Heitit kahdeksansivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    if valinnat == "d10":
        import random
        min = 1
        max = 10
        print ("Heitit kymmensivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    if valinnat == "d12":
        import random
        min = 1
        max = 12
        print ("Heitit kaksitoistasivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    if valinnat == "d20":
        import random
        min = 1
        max = 20
        print ("Heitit kaksikymmensivuista noppaa, silmäluku on:")
        print (random.randint(min, max))
    uusi_heitto


#else:#
    #print("Kirjoita oikea komento, d4, d6, d8, d10, d12, d20")#

valinnat = input("Heittääksesi erilaisia noppia, kirjoita d4, d6, d8, d10, d12 tai d20: ")
if valinnat == "d4":
    import random
    min = 1
    max = 4
    print ("Heitit neljäsivuista noppaa, silmäluku on:")
    print (random.randint(min, max))
if valinnat == "d6":
    import random
    min = 1
    max = 6
    print ("Heitit kuusisivuista noppaa, silmäluku on:")
    print (random.randint(min, max))
if valinnat == "d8":
    import random
    min = 1
    max = 8
    print ("Heitit kahdeksansivuista noppaa, silmäluku on:")
    print (random.randint(min, max))
if valinnat == "d10":
    import random
    min = 1
    max = 10
    print ("Heitit kymmensivuista noppaa, silmäluku on:")
    print (random.randint(min, max))
if valinnat == "d12":
    import random
    min = 1
    max = 12
    print ("Heitit kaksitoistasivuista noppaa, silmäluku on:")
    print (random.randint(min, max))
if valinnat == "d20":
    import random
    min = 1
    max = 20
    print ("Heitit kaksikymmensivuista noppaa, silmäluku on:")
    print (random.randint(min, max))

uusi_heitto = input("heitetäänkö uudelleen? kyllä, ei? :")
    

if uusi_heitto == "kyllä":
    heitä_noppaa()

if uusi_heitto == "ei":
    print("Kiitos ja hei!")

