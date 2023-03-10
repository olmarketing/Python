# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


def main_import_contacts():
    with open('phonebook.txt', 'w+', encoding='utf-8') as data:
    # with open(os.path.join(sys.path[0],'phonebook.txt'), 'r', encoding='utf-8') as data:
        s=data.readlines()
        for i in range(len(s)):
            phonebook[i]=s[i]
        print(phonebook)

def import_contacts(some_string):
    finded_contacts=list()
    for i in phonebook:
        if some_string in phonebook[i]:
            finded_contacts.append(*phonebook[i])
    return finded_contacts
    

def export_contacts(new_contact):
    with open('phonebook.txt', 'a+', encoding='utf-8') as data:
    
        s=' '.join(new_contact)
        data.writelines(s+'\n')
        phonebook[len(phonebook)]=new_contact
       

def input_contacts():
    new_contact=list()
    new_contact.append(input("surname: "))
    new_contact.append(input("name: "))
    new_contact.append(input("given name: "))
    new_contact.append(input("phonenumber: "))
    
    # print(new_contact)
    export_contacts(new_contact)

def find_contacts():
    s=import_contacts(input("wadda we search?: "))
    print(*s)

def delete_name():
    new_contact={}
    del new_contact['key']

def user_interface():
    main_import_contacts()
    print('Phonebook\nwant?\n1    add contact\n2    find contact\n3 print whole book\n4   any other input - end program\n5   delete')    
    user_input=input('your choise: ')
    while user_input in ('1','2','3'):
        if user_input=='1':
            input_contacts()
        elif user_input=="2":
            find_contacts()
        elif user_input=="5":
            delete_name()
        elif user_input=='3':
            print()
            for i in phonebook:
                print(*phonebook[i])    
        user_input=input('your choise: ')
    
    print('bye')

phonebook=[]
user_interface()


