class Individ: # Gör en klass för varje individ i telefonboken
    def __init__(self, nummer, namn = []):
        self.namn = namn    # byter namn på variabeln
        self.nummer = nummer # byter namn på variabeln

class Telefonbok: #
    def __init__(self):
        self.telefonkatalog = {} # skapar en tom telefonbok i form av en dictionary

    def main(self): # Huvudfunktionen som kör programmet och interagerar med användaren
        while True:
            user_input = input("phonebook> ").split()
            if user_input[0] == "add":
                if len(user_input) == 3:
                    self.läggTillnamn(user_input[1], user_input[2])
            elif user_input[0] == "lookup":
                if len(user_input) == 2:
                    self.lookup(user_input[1])
            elif user_input[0] == "alias":
                if len(user_input) == 3:
                    self.läggTillalias(user_input[1], user_input[2])
            elif user_input[0] == "change":
                if len(user_input) == 3:
                    self.ändraNummer(user_input[1], user_input[2])
            elif user_input[0] == "load":
                if len(user_input) == 2:
                    self.load(user_input[1])
            elif user_input[0] == "save":
                if len(user_input) == 2:
                    self.save(user_input[1])
            elif user_input[0] == "quit":
                print("Tack för att du använde telefonboken!")
                break
            else:
                print("Felaktig inmatning. Försök igen.")
    
    def läggTillnamn(self, namn, nummer): # Lägger till en ny individ i telefonboken
        if namn in self.telefonkatalog: # Kollar om namnet redan finns i telefonboken
            print(f"{namn} finns redan i telefonboken.")
            return
        for individ in self.telefonkatalog.values(): # Kollar om numret redan finns i telefonboken
            if individ.nummer == nummer:
                print(f"{nummer} finns redan i telefonboken.")
                return
        else:
            nyIndivid = Individ(nummer, [namn]) # Skapar en varibel för den nya individen
            self.telefonkatalog[namn] = nyIndivid # Lägger till den nya individen i telefonboken
            print(f"{namn} är tillagt i telefonkatalogen")

    def lookup(self, namn): # Kollar om en individ finns i telefonboken
        if namn in self.telefonkatalog: # Kontrollerar om namnet finns i telefonboken
            print(f"{namn}: {self.telefonkatalog[namn].nummer}")
        else:
            print(f"{namn} finns inte i telefonboken.")

    def läggTillalias(self, namn, alias): # Lägger till ett alias för en individ i telefonboken
        if namn not in self.telefonkatalog: # Kontrollerar om namnet finns i telefonboken
            print(f"{namn} finns inte i telefonboken.")
            return
        if alias in self.telefonkatalog: # Kontrollerar om aliaset redan finns i telefonboken
            print(f"{alias} finns redan i telefonboken.")
            return
        else:
            self.telefonkatalog[alias] = self.telefonkatalog[namn] # Lägger till aliaset i telefonboken
            print(f"{alias} är tillagt i telefonboken under {namn}")

    def ändraNummer(self, namn, nyttNummer): # Ändrar numret för en individ i telefonboken
        if namn not in self.telefonkatalog: # Kontrollerar om namnet finns i telefonboken
            print(f"{namn} finns inte i telefonboken.")
            return
        for individ in self.telefonkatalog.values(): # Kontrollerar om numret redan finns i telefonboken
            if individ.nummer == nyttNummer:
                print(f"{nyttNummer} finns redan i telefonboken.")
                return
            
        individ = self.telefonkatalog[namn]
        individ.nummer = nyttNummer # Ändrar numret för individen
        print(f"Numret för {namn} har ändrats till {nyttNummer}")
                

    def load(self, filnamn): # Laddar in en filen
        try:
            self.telefonkatalog.clear()  # använder telefonbok.clear för att rensa boken
            with open(filnamn, "r") as fil: # Öppnar filen för att läsa
                for rad in fil: # Kolla om "rad" funktar lika bra som "line"
                    nummer, namn, _= rad.strip().split(";") # Tar bort mellanslag och delar upp raden i en lista
                    #rad.pop() # tar bort sista elementet i listan
                    self.läggTillnamn(namn, nummer) # Lägger till namn och nummer i telefonboken
        except FileNotFoundError: # Om filen inte finns så ska inte programmet krascha utna skriva ut förljande
            print("Filen finns inte.")

    def save(self, filnamn): # Sparar filen
        with open(filnamn, "w") as fil: # Öppnar filen för att skriva
            for namn, individ in self.telefonkatalog.items(): # Loopar igenom telefonboken så att varje namn och nummer sparas och får en egen rad
                fil.write(f"{individ.nummer};{namn};\n") # Skriver in den nya raden i filen

phonebook = Telefonbok()
phonebook.main()