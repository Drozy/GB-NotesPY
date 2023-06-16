from Model.Note import Note


class NoteBook(object):

    def __init__(self) -> None:
        self.all_notes = {}
        self.index = 1

    def add(self, title: str, body: str) -> int:
        self.index += 1
        self.all_notes[self.index] = Note(self.index, title, body)
        return self.index
    
    def recall(self, note_id: int, title: str, body: str, timestamp: str) -> None:
        self.all_notes[note_id] = Note(note_id, title, body, timestamp)
        if self.index < note_id: self.index = note_id

    def get(self, note_id: int) -> Note:
        return self.all_notes[note_id]

    def remove(self, note_id: int) -> None:
        del self.all_notes[note_id]

    def contains(self, note_id: int) -> bool:
        return note_id in self.all_notes
        
    def edit(self, note_id: int, title: str, body: str) -> None:
        self.all_notes[note_id].edit(title, body)

    def show(self) -> dict:
        return self.all_notes