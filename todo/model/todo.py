class Todo:
    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str]):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []
    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
         if tag not in self.tags:
            self.tags.append(tag)

    # terminar
    # def __str__(self):

class TodoBook:
    def __init__(self, todos: dict[1, Todo]):
        self.todos = {}

    # def add_todo(self):



