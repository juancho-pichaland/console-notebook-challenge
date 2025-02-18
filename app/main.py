import datetime

class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str, creation_date: datetime):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = creation_date.now()
        self.tags = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date:{self.creation_date}\n{self.title}:{self.text}"


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        code = len(self.notes) + 1
        note = Note(str(code), title, text, importance)
        self.notes.append(note)
        return code

    def delete_note(self, code: int):
        self.notes = [note for note in self.notes if note.code != str(code)]

    def important_notes(self):
        return [note for note in self.notes if note.importance in (Note.HIGH, Note.MEDIUM)]

    def notes_by_tag(self, tag: str):
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self) -> str:
        tag_count = {}
        for note in self.notes:
            for tag in note.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1
        if not tag_count:
            return tag_count


class Console:
    def _init_(self):
        self.notebook = Notebook()

    def show_menu(self):

        print("\nNotebook - Menú Principal")
        print("1. Agregar nota")
        print("2. Listar notas")
        print("3. Agregar etiqueta a nota")
        print("4. Listar notas importantes")
        print("5. Eliminar nota")
        print("6. Mostrar notas por etiqueta")
        print("7. Mostrar etiqueta con más notas")
        print("8. Salir")

    def run(self):

        while True:
            self.show_menu()
            choice = input("choise: ")

            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.list_notes()
            elif choice == "3":
                self.add_tag_to_note()
            elif choice == "4":
                self.list_important_notes()
            elif choice == "5":
                self.delete_note()
            elif choice == "6":
                self.show_notes_by_tag()
            elif choice == "7":
                self.show_most_used_tag()
            elif choice == "8":
                print("exit...")
                break
            else:
                print("Option invalid. try again.")

    def add_note(self):

        title = input("Title: ")
        text = input("Text: ")
        importance = input("Importance (HIGH, MEDIUM, LOW): ").upper()
        if importance not in [Note.HIGH, Note.MEDIUM, Note.LOW]:
            print("Importance invalid.")
            return
        code = self.notebook.add_note(title, text, importance)
        print(f"Note agg whit code {code}.")

    def list_notes(self):

        for note in self.notebook.notes:
            print(note)

    def add_tag_to_note(self):

        code = input("Code of the note: ")
        tag = input("tag: ")
        note = next((n for n in self.notebook.notes if n.code == code), None)
        if note:
            note.add_tag(tag)
            print("tag agg.")
        else:
            print("Not found note.")

    def list_important_notes(self):

        for note in self.notebook.important_notes():
            print(note)

    def delete_note(self):

        code = input("Code of the note to delete: ")
        self.notebook.delete_note(int(code))
        print("Note delete.")

    def show_notes_by_tag(self):
        tag = input("tag: ")
        for note in self.notebook.notes_by_tag(tag):
            print(note)

    def show_most_used_tag(self):

        tag = self.notebook.tag_with_most_notes()
        if tag:
            print(f"the used tag is: {tag}")
        else:
            print("No tag found.")
