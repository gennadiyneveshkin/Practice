import os

def build_note(note_name: str, note_text: str):
    """Создает заметку"""
    with open(f'{note_name}.txt', 'w', encoding="utf-8") as file:
        file.write(note_text)
    print(f'Заметка "{note_name}" создана.')


def create_note():
    """Запрашивает заметку"""
    note_name = input('Название заметки: ')
    note_text = input('Текст заметки: ')
    build_note(note_name, note_text)


def read_note():
    """Выводит заметку"""
    created_note_name = input('Название заметки которую нужно найти: ')
    if os.path.isfile(f'{created_note_name}.txt'):
        with open(f'{created_note_name}.txt', 'r', encoding="utf-8") as file:
            note = file.read()
            print(note)
    else:
        print('Заметка не найдена')

def edit_note():
    """Редактирует заметку"""
    edit_note_name = input('Название заметки которую нужно изменить: ')
    if os.path.isfile(f'{edit_note_name}.txt'):
        with open(f'{edit_note_name}.txt', 'r', encoding="utf-8") as file:
            note = file.read()
            print(note)
        with open(f'{edit_note_name}.txt', 'w', encoding="utf-8") as file:
            text = input('Новый текст заметки: ')
            file.write(text)
    else:
        print('Заметка не найдена')

def delete_note():
    """Удаляет заметку"""
    delete_note_name = input('Название заметки которую нужно удалить: ')
    if os.path.isfile(f'{delete_note_name}.txt'):
        os.remove(f'{delete_note_name}.txt')
        print('Заметка удалена')
    else:
        print('Заметка не найдена')

def main():

    while True:

        todo = input('1 - Новая заметка: \n'
                     '2 - Найти заметку: \n'
                     '3 - Изменить заметку: \n'
                     '4 - Удалить заметку: \n'
                     '5 - Список заметок: \n'
                     '6 - Сортировки по длине заметки по убыванию \n'
                     '7 - Выход:')

        if todo == '1':
            create_note()
        elif todo == '2':
            read_note()
        elif todo == '3':
            edit_note()
        elif todo == '4':
            delete_note()
        elif todo == '5':
            display_notes()
        elif todo == '6':
            display_sorted_notes()
        elif todo == '7':
            print('Работа завершена')
            break
        else:
            print('Некорректный ввод')

def display_notes():
        notes = [file for file in os.listdir('.') if file.endswith('.txt')]
        notes.sort(key=len)
        for note in notes:
            print(note)

def display_sorted_notes():
    notes = [file for file in os.listdir('.') if file.endswith('.txt')]
    notes.sort(key=len, reverse=True)



