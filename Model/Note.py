from datetime import datetime


class Note(object):
    def __init__(self, note_id: int, title = "Название", body = "Текст заметки", 
                 timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")) -> None:
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

    def get_title(self) -> None:
        return self.title

    def get_body(self) -> None:
        return self.body

    def get_timestamp(self) -> str:
        return str(self.timestamp)

    def edit(self, new_title: str, new_body: str) -> None:
        self.title = new_title
        self.body = new_body
        self.timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def __str__(self) -> str:
        return "{}' {'title': {}, 'body': {}, 'timestamp': {}}"\
            .format(self.note_id, self.title, self.body, self.timestamp)

