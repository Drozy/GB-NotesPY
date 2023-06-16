import json
from Model.Note import Note
from Model.Notebook import NoteBook
from View.ConsoleView import ConsoleView


class Controller(object):
    def __init__(self, view: ConsoleView, source: str) -> None:
        self.view = view
        self.source = source
        self.notebook = NoteBook()

    def loadNotes(self) -> None:
        with open(self.source, 'r') as file:
            notes_json = json.load(file)
            for note_id, note in notes_json.items():
                self.notebook.recall(int(note_id), 
                                     note['title'], 
                                     note['body'], 
                                     note['timestamp'])

    def saveNotes(self) -> None:
        notes_json = {}
        all_notes = self.notebook.show()
        for note_id in all_notes:
            notes_json[note_id] = {
                'title': all_notes[note_id].get_title(),
                'body': all_notes[note_id].get_body(),
                'timestamp': all_notes[note_id].get_timestamp()
            }
        with open(self.source, 'w') as file:
            json.dump(notes_json, file)

    def startApp(self) -> None:
        self.loadNotes()
        self.view.userOutput('\nПриложение Заметки')
        while True:
            self.doAction(self.view.mainMenu())

    def doAction(self, user_choiсe: int) -> None:
        actions = {
            1: self.showAllNotes,
            2: self.showNote,
            3: self.editNote,
            4: self.addNote,
            5: self.delNote,
            0: 'exit'
        }
        action = actions.get(user_choiсe)
        if action == 'exit':
            self.saveNotes()
            exit()
        else:
            action()

    def showAllNotes(self) -> None:
            output = ''
            all_notes = self.notebook.show()
            for note_id in all_notes:
                output = output + str(note_id) + '\t' + \
                    all_notes[note_id].get_title() + '   \t' + \
                    all_notes[note_id].get_timestamp() + '\n'
            self.view.userOutput(output)

    def showNote(self) -> None:
        self.view.userOutput("Введите ID заметки: ")
        note_id = int(self.view.userInput())
        if self.notebook.contains(note_id):
            note = self.notebook.get(note_id)
            self.view.showNote(note_id, 
                                note.get_title(), 
                                note.get_body(), 
                                note.get_timestamp())
        else:
            self.view.userOutput("Заметка с ID {} не найдена"
                                 .format(note_id))

    def editNote(self) -> None:
        self.view.userOutput("Введите ID заметки: ")
        note_id = int(self.view.userInput())
        if self.notebook.contains(note_id):
            self.view.userOutput("Введите новый заголовок заметки: ")
            new_title = self.view.userInput()
            self.view.userOutput("Введите текст заметки: ")
            new_body = self.view.userInput()
            self.notebook.edit(note_id, new_title, new_body)
        else:
            self.view.userOutput("Заметка с ID {} не найдена"
                                 .format(note_id))
        
    def addNote(self) -> None:
        self.view.userOutput("Введите заголовок заметки: ")
        title = self.view.userInput()
        self.view.userOutput("Введите текст заметки: ")
        body = self.view.userInput()
        self.view.userOutput("Создана заметка с ID {}"
                             .format(self.notebook.add(title, body)))

    def delNote(self) -> None:
        self.view.userOutput("Введите ID заметки: ")
        note_id = int(self.view.userInput())
        if self.notebook.contains(note_id):
            self.notebook.remove(note_id)
        else:
            self.view.userOutput("Заметка с ID {} не найдена"
                                 .format(note_id))