import random

tajnibroj = random.randint(1,30)
pogodi = 0
for x in range(5):

    pogodi = int(input("Pogodi broj između 1 i 30: "))

    if pogodi == tajnibroj:
        print("Bravo, pogodio si traženi broj!")
        break
    
    elif pogodi > tajnibroj:
        print("Broj je manji od traženog broja!")
        break
    elif pogodi < tajnibroj:
        print("Broj je veći od traženog broja!")

print("Kraj programa..")
print("Traženi broj u ovoj igri bilo je:" + str(tajnibroj))