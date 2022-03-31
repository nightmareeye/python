import json
import sys

def main():
    json_file = "/1.json"
    #create_todo_list(json_file, "my_task")
    todo=TodoJournal.create
    for i in range(1, 5):
        add_todo(json_file, f"task{i}")

    remove_todo(json_file, 1)

class TodoJournal:
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def create(self):
        with open(self.path, "w") as todo_file:
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
             ensure_ascii=False,
         )

    def add_entry(self, new_entry):
     data=self._parse()

     name = data["name"]
     todos = data["todos"]

     todos.append(new_entry)

     new_data = {
         "name": name,
         "todos": todos,
     }

     self._update(new_data)



    def remove_entry(self, index):
         data = self._parse()
         name = data["name"]
         todos = data["todos"]

         todos.remove(todos[index])

         new_data = {
             "name": name,
             "todos": todos,
         }

         self._update(new_data)



    # def parse_todo(path_todo):
    #     try:
    #         with open(path_todo, 'r') as todo_file:
    #             data = json.load(todo_file)
    #         return data
    #     except FileNotFoundError as e:
    #         print(f"{e}")
    #         # или свое исключение
    #         print(f"Не существует такой тудушки: {path_todo}")
    #         sys.exit(1)
    #
    #
    #
    # def add_todo(path_todo, new_todo):
    #     with open(path_todo, 'r') as todo_file:
    #         data = json.load(todo_file)
    #
    #     name = data["name"]
    #     todos = data["todos"]
    #
    #     todos.append(new_todo)
    #
    #     new_data = {
    #         "name": name,
    #         "todos": todos,
    #     }
    #
    #     update_todo(path_todo, new_data)
    #
    #

    #
    # if __name__ == '__main__':
    #     main()
