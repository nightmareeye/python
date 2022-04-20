from base64 import encode
from encodings import utf_8
import json
from src.TodoJournal import TodoJournal

def test_init():
    """Проверка корректности инициализации TodoJournal"""
    # TODO проблема. чтобы сейчас протестировать нужно знать путь до тудушки, ее имя.
    todo = TodoJournal("1.json")
    entries = todo.entries
    name = todo.name
    expected_entries = ["task1","task2","task3","task4"]
    expected_name = "test3"
    assert entries == expected_entries
    assert name == expected_name

def test_create_journal(tmpdir):
    todo_filename = "test_todo"
    todo = tmpdir.join(todo_filename)
    TodoJournal.create(todo, "test")

    expected_todo = json.dumps(
        {
        "name": "test",
        "todos": []
        },
        indent=4)
    assert expected_todo == todo.read()

def test_add_entry(tmpdir):
    todo_filename = "test_todo"
    todo = tmpdir.join(todo_filename)
    TodoJournal.create(todo, "test")
    todo_jrnl = TodoJournal(todo)
    todo_jrnl.add_entry("Сходить за молоком")

    expected_todo = json.dumps(
        {
        "name": "test",
        "todos": ["Сходить за молоком"]
        },
        indent=4,
        ensure_ascii=False,)
    assert expected_todo == todo.read()
