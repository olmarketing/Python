import csv

class Phonebook:
    def __init__(self):
        self.contacts = []

    def load(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.contacts.append(row)

    def save(self, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            for contact in self.contacts:
                writer.writerow(contact)

    def add_contact(self, last_name, first_name, patronymic, phone_number):
        self.contacts.append([last_name, first_name, patronymic, phone_number])

    def search_contact(self, last_name):
        for contact in self.contacts:
            if contact[0] == last_name:
                return contact
        return None

    def update_contact(self, last_name, first_name, patronymic, phone_number):
        for contact in self.contacts:
            if contact[0] == last_name:
                contact[1] = first_name
                contact[2] = patronymic
                contact[3] = phone_number
                return True
        return False

    def delete_contact(self, last_name):
        for contact in self.contacts:
            if contact[0] == last_name:
                self.contacts.remove(contact)
                return True
        return False

phonebook = Phonebook()
phonebook.load('phonebook.txt')

# Добавляем новый контакт
phonebook.add_contact('Иванов', 'Иван', 'Иванович', '123-456-7890')

# Ищем контакт
contact = phonebook.search_contact('Иванов')

# Изменяем контакт
phonebook.update_contact('Иванов', 'Петр', 'Иванович', '098-765-4321')

# Удаляем контакт
phonebook.delete_contact('Иванов')

# Сохраняем контакты в файл
phonebook.save('phonebook.txt')
