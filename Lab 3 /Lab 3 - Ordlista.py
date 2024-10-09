# Skapa en ordlista
# Alt 1: Två stycken listor av strängar. Den första listan innehåller ordet vi vill slå upp, och den andra listan 
# innehåller beskrivningen för det ordet, på motsvarande position.

# Alt 2: En lista av tupler. En enda lista som består av par, där första delen av varje par är ordet vi vill slå upp, 
# och den andra är beskrivningen. Observera här alltså att datastrukturen ska vara en lista, varje element i denna lista 
# ska i sin tur vara ett par (en tupel med två element).

# Alt 3: Ett dictionary. Ett dictionary som innehåller ordet vi vill slå upp som "nyckel" och tillhörande beskrivning 
# som "värde".

def main(): # Huvudfunktionen som visar användar alternativ och hanterar olika inputs med två stycken sepparata listor
    ordlista = []
    beskrivning = []

    print(f"\nMeny till ordlista:")
    while True:
        print(f"\n1: Lägg till")
        print("2: Slå upp")
        print("3: Avsluta program")
        val = input("Välj ett alternativ: ")

        if val == "3": # En loop för det olika användar alternativen
            break # Avslutar programet enligt berskivningen
        elif val == "1":
            läggTill(ordlista,beskrivning)
        elif val == "2":
            slåUpp(ordlista,beskrivning)
        else:
            print("Inte ett alternativ")

def läggTill(ordlista, beskrivning): # En funktion som tillåter anändaren att lägga till ord i ordlistan med en beskrivning
    
    tillagtOrd = input(f"\nVilket ord vill du lägga till?: ")
    if tillagtOrd in ordlista:
        print("Det ordet finns redan")
        return
    
    nyBeskrivning = input("Beskrivning av ordet: ")
   
    ordlista.append(tillagtOrd)
    beskrivning.append(nyBeskrivning)

def slåUpp(ordlista, beskrivning): # En funktion som tillåter användaren att slå upp ett ord från ordlistan
    sökOrd = input("Vilket ord vill du slå upp?: ")
    if sökOrd in ordlista:
        print(f"{sökOrd}\n{beskrivning[ordlista.index(sökOrd)]}") # Skriver ut beskrivningen för sökordet med det indexet i ordlistan
    else:
        print("Ordet finns inte i ordlistan")

def main2(): # Huvudfunktion som visar användar alternativ och hanterar olika inputs med listor av tuples
    listaTuple = []

    print(f"\nMeny till ordlista:")
    while True:
        print(f"\n1: Lägg till")
        print("2: Slå upp")
        print("3: Avsluta program")
        val = input("Välj ett alternativ: ")

        if val == "3": # En loop för det olika användar alternativen
            break # Avslutar programet enligt berskivningen
        elif val == "1":
            läggTill2(listaTuple)
        elif val == "2":
            slåUpp2(listaTuple)
        else:
            print("Inte ett alternativ")

def läggTill2(listaTulpe): # En funktion som tillåter användaren att lägga till ett ord med beskrivning i ordlistan
    
    tillagtOrd = input(f"\nVilket ord vill du lägga till?: ")
    for i in listaTulpe: # Funktionen kontrollerar att första elementet av tuple inte redan finns genom att kolla första positionen i varje tuple
        if i[0] == tillagtOrd: # i[0] är då första elementet i tuple och printar failsafe om det redan finns
            print("Det ordet finns redan")
            return
    
    nyBeskrivning = input("Beskrivning av ordet: ")
    listaTulpe.append((tillagtOrd,nyBeskrivning))

def slåUpp2(listaTuple): # En funktion som tillåter användaren att slå upp ett ord från ordlistan
    sökOrd = input(f"\nVilket ord vill du slå upp?: ")
    for i in listaTuple:
        if i[0] == sökOrd:
            print(f" {i[0]} \n {i[1]}")
            break
    else:
        print("Ordet finns inte i ordlistan")

def main3(): # Huvudfunktion som visar användar alternativ och och hanterar olika inputs med dictonary funktionen
    ordListaDic = {}

    print(f"\nMeny till ordlista:")
    while True:
        print(f"\n1: Lägg till")
        print("2: Slå upp")
        print("3: Avsluta program")
        val = input("Välj ett alternativ: ")

        if val == "3": # En loop för det olika användar alternativen
            break # Avslutar programet enligt berskivningen
        elif val == "1":
            läggTill3(ordListaDic)
        elif val == "2":
            slåUpp3(ordListaDic)
        else:
            print("Inte ett alternativ")

def läggTill3(ordListaDic): # En funktion som tillåter användaren att lägga till ett ord i ordlistan med en beskrivning
    tillagtOrd = input(f"\nVilket ord vill du lägga till?: ")

    if tillagtOrd in ordListaDic:
        print("Det ordet finns redan")
        return
    
    nyBeskrivning = input("Beskrivning av ordet: ")
    ordListaDic.update({tillagtOrd:nyBeskrivning})

def slåUpp3(ordListaDic): # En funktion som tillåter användaren att slå upp ett ord från ordlistan
    sökOrd = input("Vilket ord vill du slå upp?: ")

    if sökOrd not in ordListaDic:
        print("Det ordet finns inte")
    else:
        x = ordListaDic[sökOrd]
        print(sökOrd)
        print(x)

#main()
#main2()
#main3()