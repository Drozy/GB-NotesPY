class ConsoleView(object):
    def __init__(self) -> None:
        pass

    def mainMenu(self) -> int:
        while True:
            try:
                choice = int(input('\nВыберите действие:\n' +
                    '(1) - Показать все заметки\n' +
                    '(2) - Открыть заметку\n' +
                    '(3) - Изменить заметку\n' +
                    '(4) - Добавить новую заметку\n' +
                    '(5) - Удалить заметку\n' +
                    '(0) - Выход\n'))
                if -1 < choice < 6:
                    break
                else:
                    print('Неверный ввод, попробуйте ещё раз.\n')
            except Exception:
                print('Неверный ввод, попробуйте ещё раз.\n')
        print()
        return choice

    def userInput(self) -> str:
        return input()

    def userOutput(self, message: str) -> None:
        print(message)

    def showNote(self, note_id: int, title: str, body: str, timestamp: str) -> None:
        print('\nID: {}\nЗаголовок: {}\
              \n-----------------------------------------\
              \n{}\
              \n-----------------------------------------\
              \nОтредактировано {}'.format(note_id, title, body, timestamp))
