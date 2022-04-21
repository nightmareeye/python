"""TodoJournal class"""
import json
import sys

def main():
    """testing functionality of TodoJournal"""
    json_file = "./1.json"
    TodoJournal.create(json_file, "test3")

    todo = TodoJournal(json_file)
    for i in range(1, 5):
        todo.add_entry(f"task{i}")
    for i in todo:
        print(i)
    print(todo[0])
    print(todo.print())
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
    Methods
    -------
    create():
        Creates json-file for todos
    add_entry(new_entry):
        Adds new todo to json-file
    remove_entry(index):
        Removes todo from json-file
    """
    def __init__(self, path_todo):
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
        self.path = path_todo
        self.name = self._parse()["name"]
        self.entries = self._parse()["todos"]

    def __len__(self):
        return len(self.entries)
    def __iter__(self):
        self.itr = 0
        return self

    def __next__(self):
        if self.itr < len(self):
            result = self.entries[self.itr]
            self.itr += 1
            return result
        else:
            raise StopIteration
    def __getitem__(self, key):
        return self.entries[key]
    @staticmethod
    def create(filename, name):
        """
        Creates json-file for todos
        ...
        Parameters
        ----------
        None
        Returning value
        ---------------
        None
        """
        with open(filename, "w", encoding='utf-8') as todo_file:
            json.dump(
                {"name": name, "todos": []},
                todo_file,
                sort_keys=True,
                indent=4,
                ensure_ascii=False,
            )
    def _update(self, new_data):
        with open(self.path, "w", encoding='utf-8') as todo_file:
            json.dump(
                new_data,
                todo_file,
                sort_keys=True,
                indent=4,
                ensure_ascii=False,)

    def print(self):
        """Added beautiful output"""
        str_pr='====TODOs====\n'
        for td_list in self:
            str_pr+=td_list+'\n'
        str_pr+='============='
        return str_pr
    def add_entry(self, new_entry):
        """
        Adds new todo to json-file
        ...
        Parameters
        ----------
        new_entry : str
            Describes new todo
        Returning value
        ---------------
        None
        """
        self.entries.append(new_entry)

        new_data = {
            "name": self.name,
            "todos": self.entries,
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
        Returning value
        ---------------
        None
        """
        new_data = {
            "name": self.name,
            "todos": self.entries,
        }
        self.entries.remove(self.entries[index])
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
        except TimeoutError as error:
            print(f"{error}")
            print("Превышено время ожидания")
        except RuntimeError as error:
            print(f"{error}")
            print("Превышено время ожидания 2")

if __name__ == '__main__':
    main()
