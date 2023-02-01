import random
print("Tervetuloa heittämään noppia! Voit heittää neljä-, kuusi-, kahdeksan-, kymmen-, kaksitoista- ja kaksikymmensivuista noppaa")


def heitä_noppaa():
    valinnat = input("Heittääksesi erilaisia noppia, kirjoita d4, d6, d8, d10, d12 tai d20: ")

    if valinnat == "d4":
        min = 1
        max = 4
        print ("Heitit neljäsivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    elif valinnat == "d6":
        min = 1
        max = 6
        print ("Heitit kuusisivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    elif valinnat == "d8":
        min = 1
        max = 8
        print ("Heitit kahdeksansivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    elif valinnat == "d10":
        min = 1
        max = 10
        print ("Heitit kymmensivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    elif valinnat == "d12":
        min = 1
        max = 12
        print ("Heitit kaksitoistasivuista noppaa, silmäluku on:")
        print (random.randint(min, max))

    elif valinnat == "d20":
        min = 1
        max = 20
        print ("Heitit kaksikymmensivuista noppaa, silmäluku on:")
        print (random.randint(min, max))
    
    else:
        print ("väärä käsky")
        heitä_noppaa()
    
while True:
    heitä_noppaa()
    uusi_heitto = input("heitetäänkö uudelleen? kyllä, ei? :")
    


    if uusi_heitto != "kyllä":
     print("Kiitos ja hei!")
     break