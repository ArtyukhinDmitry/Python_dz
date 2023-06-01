

from os import path

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
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
        print("Empty base!\n")


# 2 ++


def add_record():
    global last_id
    print("Add record:")
    array = ['lastname', 'name', 'surname', 'phone number']
    answers = []
    for i in array:
        answers.append(data_collection(i))
    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, "a", encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Record add in phone book\n")
        print('\n')
    else:
        print("Record error")


def data_collection(num):
    answer = input(f"Go {num}: ")
    while True:
        if num in 'lastname' 'name' 'surname':
            if answer.isalpha():
                break
        if num == 'phone number':
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f'Record is not correct')
    return answer


def exist_contact(rec_id, data):
    if rec_id:
        popitka = [i for i in all_data if rec_id in i.split()[0]]
    else:
        popitka = [i for i in all_data if data in i]
    return popitka
        


# 3 +


def search_record():
    search_data = exist_contact(0, input('What search record? :'))
    if search_data:
        print(*search_data, sep='\n')
    else:
        print('Record is not correct')


# 4 ++


def change_record(data_tuple):
    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple
    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, ' '.join(v[1:])):
                print('Record discovered')
                return
            all_data[i] = ' '.join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print('Record changed\n')


def edit_menu():
    add_dict = {'1': 'lastname', '2': 'name', '3': 'surname', '4': 'phone number'}
    show_all()
    record_id = input('What ID edit?: ')

    if exist_contact(record_id, ''):
        while True:
            print('\nEdit: ')
            change = input('1: lastname\n'
                           '2: name\n'
                           '3: surname\n'
                           '4: phone number\n'
                           '5: exit\n')
            match change:
                case '1' | '2' | '3' | '4' :
                    return record_id, change, data_collection(add_dict[change])
                case '5':
                    return 0
                case _:
                    print('Edit error')
    else:
        print('Record not correct')


# 5++


def delete_record():
    global all_data
    symbol = "\n"
    del_rec = input('What record delete?: ')

    if exist_contact(del_rec, ''):
        all_data = [k for k in all_data if k.split()[0] !=del_rec]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print('Record deleted\n')
    else:
        print('Not delete - error')

# 6 +


def exp_imp_menu():
    while True:
        print('\nExp/Imp menu: ')
        move = input('1: Import\n'
                     '2: Export\n'
                     '3: Exit\n')
        match move:
            case '1' :
                import_record(input('What record?: '))
            case '2':
                export_record(input('What record?: '))
            case '3':
                return 0
            case _:
                print('Edit error')

def import_record(name):
    global file_base
    if path.exists(name):
        file_base = name
        read_records()

def export_record(name):
    symbol = '\n'
    change_name = f'{name}.txt'
    if not path.exists(change_name):
        with open(change_name, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')


# menu ++


def main_menu():
    work = True
    while work:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all\n"
                       "2. Add\n"
                       "3. Search\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_record()
            case "3":
                search_record()
            case "4":
                work = edit_menu()
                if work:
                    change_record(work)
            case "5":
                delete_record()
            case "6":
                exp_imp_menu()
            case "7":
                work = False
            case _:
                print("Try again!\n")

main_menu()
