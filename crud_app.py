import argparse

parser = argparse.ArgumentParser()
parser.add_argument("command")
args = parser.parse_args()

command = args.command
print(command)



data = {
    "Satanael": "Cost: Lucifer, Satan, Micheal, Ishtar, Anzu, and Arsene",
    "Jack Frost": "Cost: Silky, and Mandrake",
    "Angel": "Cost: Succubus, and Arsene",
}


def read_data():

    name = input("What name do you want to get data for?: ")
    print(data[name])


def create_data():
    
    name = input("What name do you want to get create data for?:")

    if name in data:
        print("Already have Data")
        print(data[name])
    else:
        Personasneeded = input("What Personas are needed?")
        data[name] = Personasneeded
        print(data[name])


def update_data():
    
    name = input("What name do you want to update data for?: ")
    print(data[name])
    PersonaUpdate = input("What is needed?")
    data[name] = PersonaUpdate
    print(data[name])
        

def delete_data():
    name = input("What data do you want to delete?")
    if name in data:
        del data[name]
        print("Data Deleted")


if command == "create":
    print("you want to create an entry?")
    create_data()
elif command == "read":
    print("reading entry..")
    read_data()

elif command == "update":
    print("reading entry..")
    update_data()

elif command == "delete":
    print("deleting entry..")
    delete_data()
    print(data)