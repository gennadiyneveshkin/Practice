import os


def build_note(note_name: str, note_text: str):
    """Создает заметку"""
    try:
        with open(f'{note_name}.txt', 'w', encoding="utf-8") as file:
            file.write(note_text)
        print(f'Заметка "{note_name}" создана.')
    except PermissionError:
        print("Нет прав для записи. Проверьте папку и имя файла.")
    except OSError as e:
        print(f"Не удалось сохранить файл: {e}")


def create_note():
    """Запрашивает заметку"""
    try:
        note_name = input('Название заметки: ')
        note_text = input('Текст заметки: ')
        build_note(note_name, note_text)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def read_note():
    """Выводит заметку"""
    try:
        created_note_name = input('Название заметки которую нужно найти: ')
        if os.path.isfile(f'{created_note_name}.txt'):
            with open(f'{created_note_name}.txt', 'r', encoding="utf-8") as file:
                note = file.read()
                print(note)
        else:
            print('Заметка не найдена')
    except PermissionError:
        print("Нет прав для чтения этого файла.")
    except OSError as e:
        print(f"Ошибка при работе с файлом: {e}")


def edit_note():
    """Редактирует заметку"""
    try:
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
    except PermissionError:
        print("Нет прав для чтения / записи файла.")
    except OSError as e:
        print(f"Ошибка при работе с файлом («{edit_note_name}.txt»): {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def delete_note():
    """Удаляет заметку"""
    try:
        delete_note_name = input('Название заметки которую нужно удалить: ')
        if os.path.isfile(f'{delete_note_name}.txt'):
            os.remove(f'{delete_note_name}.txt')
            print('Заметка удалена')
        else:
            print('Заметка не найдена')
    except PermissionError:
        print("Нет прав для удаления этой заметки.")
    except OSError as e:
        print(f"Ошибка при удалении («{delete_note_name}.txt»): {e}")


def display_notes():
    """Выводит список всех заметок, по увеличению длины текста"""
    try:
        notes = [file for file in os.listdir('.') if file.endswith('.txt')]
        sorted_notes = sorted(notes, key=lambda note: len(open(note, encoding="utf-8").read()))
        for note in sorted_notes:
            print(note)
    except PermissionError:
        print("Нет доступа к папке с заметками.")
    except OSError as e:
        print(f"Ошибка при чтении папки: {e}")


def display_sorted_notes():
    """Выводит список всех заметок, по уменьшению длины текста"""
    try:
        notes = [file for file in os.listdir('.') if file.endswith('.txt')]

        # Сортируем список с названиями заметок по длине их содержания
        sorted_notes = sorted(notes, key=lambda note: len(open(note, encoding="utf-8").read()), reverse=True)
        for note in sorted_notes:
            print(note)
    except PermissionError:
        print("Нет доступа к папке с заметками.")
    except OSError as e:
        print(f"Ошибка при чтении папки: {e}")


def main():
    """Управляет работой приложения: показывает меню и выполняет выбранные действия"""
    while True:
        try:
            todo = input('1 - Новая заметка \n'
                         '2 - Найти заметку \n'
                         '3 - Изменить заметку \n'
                         '4 - Удалить заметку \n'
                         '5 - Список заметок по возрастанию длины текста \n'
                         '6 - Сортировка заметок по убыванию длины текста \n'
                         '7 - Выход \n'
                         'Введите число: ')

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

        except (EOFError, KeyboardInterrupt):
            print('Ввод прерван. Работа завершена.')
            break


# Точка входа
if __name__ == '__main__':
    main()
