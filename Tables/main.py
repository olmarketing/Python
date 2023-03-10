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


# import os,sys

def main_import_contacts():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
    # with open(os.path.join(sys.path[0],'phonebook.txt'), 'r', encoding='utf-8') as data:
        s=data.readlines()
        for i in range(len(s)):
            phonebook[i]=s[i].split()
       
def import_contacts(some_string):
    finded_contacts=list()
    for i in phonebook:
        if some_string in phonebook[i]:
            finded_contacts.append(*phonebook[i])
    return finded_contacts
    

def export_contacts(new_contact):
    with open('phonebook.txt', 'a+', encoding='utf-8') as data:
    # with open(os.path.join(sys.path[0],'phonebook.txt'), 'a+', encoding='utf-8') as data:
        s=' '.join(new_contact)
        data.writelines(s+'\n')
        phonebook[len(phonebook)+1]=new_contact
       

def input_contacts():
    new_contact=list()
    new_contact.append(input("surname: "))
    new_contact.append(input("name: "))
    new_contact.append(input("given name: "))
    new_contact.append(input("phonenumber: "))
    
    print(new_contact)
    export_contacts(new_contact)

def find_contacts():
    s=input("Введите номер или имя: ")
    with open ('phonebook.txt','r', encoding='utf-8') as fc:
         p=0
         for i in fc:
            if s in i:
                 print(i)
                 action=input('\nЧто вы хотите сделать?\n1    Удалить контакт\n2    Переименовать контакт')
                 if action==1:
                      return delete_contact(i)
                 elif action==2:
                      return replace_contact(i)
                            
         print("Такого контакта нет")

def delete_contact(el):
    with open('phonebook.txt', 'r', encoding='utf-8') as rpb:
        lines=rpb.readlines()
    with open('phonebook.txt', 'w', encoding='utf-8') as wpb:
         for line in lines:
              if el not in line:
                   wpb.write(line)
    print('Deleted')    

def replace_contact(el):
     with open('phonebook.txt', 'r', encoding='utf-8') as rpb:
        lines=rpb.readlines()
     with open('phonebook.txt', 'w', encoding='utf-8') as wpb:
          for line in lines:
               if el in line:
                    line=line.split()
                    for part in line:
                         new_cont=part.replace(part, input('Введите новую информацию:   '))
                         wpb.writelines(new_cont + '')
                         print('Готово')
               else: 
                    wpb.write(str(line))


def user_interface():
    main_import_contacts()
    print('Phonebook\nЧто вы хотите сделать?\n1    Добавить контакт\n2    Найти контакт\n3 Распечатать книгу\n0   Закончить действия\n4   Удалить контакт')    
    user_input=input('Ваш выбор: ')
    if user_input=='1':
            input_contacts()
    elif user_input=="2":
            find_contacts()
    elif user_input=="4":
            delete_contact()
    elif user_input=='3':
            print()
            for i in phonebook:
                print(*phonebook[i])
    elif user_input=='0':
         exit()    
    user_input=input('Ваш выбор: ')
   


    
    print('bye')

phonebook=dict()
user_interface()
delete_contact()


