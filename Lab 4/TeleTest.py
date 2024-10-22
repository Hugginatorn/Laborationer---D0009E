class Phonebook:
    def __init__(self):
        self.phonebook = {}

    def add_contact(self, name, number):
        if name in self.phonebook:
            print("Namnet finns redan i telefonboken.")
        else:
            self.phonebook[name] = number
            print(f"{name} har lagts till i telefonboken med nummer {number}.")

    def lookup_contact(self, name):
        if name in self.phonebook:
            number = self.phonebook[name]
            print(f"Numret till {name} är {number}.")
        else:
            print(f"{name} finns inte i telefonboken.")

    def alias_contact(self, name, new_name):
        if name in self.phonebook:
            number = self.phonebook[name]
            self.phonebook[new_name] = number
            print(f"{name} har fått ett nytt namn: {new_name}.")
        else:
            print(f"{name} finns inte i telefonboken.")

    def change_number(self, name, new_number):
        if name in self.phonebook:
            self.phonebook[name] = new_number
            print(f"Numret till {name} har ändrats till {new_number}.")
        else:
            print(f"{name} finns inte i telefonboken.")

    def save_phonebook(self, filename):
        with open(filename, "w") as file:
            for name, number in self.phonebook.items():
                file.write(f"{name},{number}\n")
        print("Telefonboken har sparats.")

    def load_phonebook(self, filename):
        self.phonebook.clear()
        with open(filename, "r") as file:
            for line in file:
                name, number = line.strip().split(",")
                self.phonebook[name] = number
        print("Telefonboken har lästs in.")
        print(self.phonebook)

    def run(self):
        while True:
            command = input("phonebook> ").lower()

            if command == "add":
                name = input("Namn: ")
                number = input("Nummer: ")
                self.add_contact(name, number)

            elif command == "lookup":
                name = input("Namn: ")
                self.lookup_contact(name)

            elif command == "alias":
                name = input("Namn: ")
                new_name = input("Nytt namn: ")
                self.alias_contact(name, new_name)

            elif command == "change":
                name = input("Namn: ")
                new_number = input("Nytt nummer: ")
                self.change_number(name, new_number)

            elif command == "save":
                filename = input("Filnamn: ")
                self.save_phonebook(filename)

            elif command == "load":
                filename = input("Filnamn: ")
                self.load_phonebook(filename)

            elif command == "quit":
                print("Tack för att du använde telefonboken!")
                break

            else:
                print("Ogiltigt kommando. Försök igen.")


if __name__ == "__main__":
    phonebook = Phonebook()
    phonebook.run()