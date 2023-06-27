from os import path


all_data = []
last_id = 0
file_base = "base.txt"

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as f:
        pass
def read_records():
    global all_data, last_id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []



def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data!\n")


def add_new_record():
    global last_id

    array = ["surname", "name", "patronymic", "phone number"]
    string = ""

    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Imp\Exp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_record()
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("sorry but try again!\n")

main_menu()
