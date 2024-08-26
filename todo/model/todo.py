# TODO: Add code here
class Todo:
    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags: list[str]):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = False
        self.tags = []
    def mark_completed(self):
        self.completed = True
