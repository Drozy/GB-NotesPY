from Controller.Controller import Controller
from View.ConsoleView import ConsoleView


def main():
    source_file = "notes.json"
    view = ConsoleView()
    controller = Controller(view, source_file)
    controller.startApp()

if __name__ == '__main__':
    main()