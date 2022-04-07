"""TodoJournal class"""
import json
import sys

def main():
    """testing functionality of TodoJournal"""
    json_file = "1.json"
    todo = TodoJournal(json_file, "my_task")
    todo.create()
    for i in range(1, 5):
        todo.add_entry(f"task{i}")
    todo.remove_entry(1)

class TodoJournal:
    """
    Class for Todos
    ...
    Attributes
    ----------
    path : str
        Describes path (where todo-file must be located)
    name : str
        Describes name (name of the todo-file)
    ...
    Methods
    -------
    create():
        Creates json-file for todos
    add_entry(new_entry):
        Adds new todo to json-file
    remove_entry(index):
        Removes todo from json-file
    """
    def __init__(self, path, name):
        """
        Sets all necessary attributes for TodoJournal object
        ...
        Parameters
        ----------
        name : str
            Describes name (name of the todo-file)
        path : str
            Describes path (where todo-file must be located)
        """
        self.path = path
        self.name = name
    def create(self):
        """
        Creates json-file for todos
        ...
        Parameters
        ----------
        None
        ...
        Returning value
        ---------------
        None
        """
        with open(self.path, "w", encoding='utf-8') as todo_file:
            json.dump(
                {"name": self.name, "todos": []},
                todo_file,
                sort_keys=True,
                indent=4,
                )

    def _update(self, new_data):
        with open(self.path, "w", encoding='utf-8') as todo_file:
            json.dump(
                new_data,
                todo_file,
                sort_keys=True,
                indent=4,
                ensure_ascii=False,)
    def add_entry(self, new_entry):
        """
        Adds new todo to json-file
        ...
        Parameters
        ----------
        new_entry : str
            Describes new todo
        ...
        Returning value
        ---------------
        None
        """
        data = self._parse()

        name = data["name"]
        todos = data["todos"]

        todos.append(new_entry)

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)
    def remove_entry(self, index):
        """
        Removes todo from json-file
        ...
        Parameters
        ----------
        index : int
            Describes the index of todo to remove
        ...
        Returning value
        ---------------
        None
        """
        data = self._parse()
        name = data["name"]
        todos = data["todos"]

        todos.remove(todos[index])

        new_data = {
            "name": name,
            "todos": todos,
        }

        self._update(new_data)

    def _parse(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as todo_file:
                data = json.load(todo_file)
            return data
        except FileNotFoundError as error:
            print(f"{error}")
            print(f"Не существует такой тудушки: {self.path}")
            sys.exit(1)
        except PermissionError as error:
            print(f"{error}")
            print(f"Отуствует доступ к файлу: {self.path}")
if __name__ == '__main__':
    main()
