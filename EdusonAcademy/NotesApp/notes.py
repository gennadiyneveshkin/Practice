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
    build_note(note_text, note_name)


def read_note():
    """Выводит заметку"""
    created_note_name = input('Название заметки котороую нужно найти: ')
    if os.path.isfile(f'{created_note_name}.txt'):
        with open(f'{created_note_name}.txt', 'r', encoding="utf-8") as note:
        print(note)
    else:
        print('Не удалось найти заметку')


