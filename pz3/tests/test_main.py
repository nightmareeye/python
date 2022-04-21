"""TodoJournal tests"""
import json
import pytest
from src.TodoJournal import TodoJournal

def test_init():
    """Проверка корректности инициализации TodoJournal"""
    todo = TodoJournal("1.json")
    entries = todo.entries
    name = todo.name
    expected_entries = ["task1","task2","task3","task4"]
    expected_name = "test3"
    assert entries == expected_entries
    assert name == expected_name
def test_create_journal(tmpdir):
    """Проверка корректности создания TodoJournal"""
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
    """Проверка корректности добавления entries в TodoJournal"""
    todo_filename = "test_todo"
    todo = tmpdir.join(todo_filename)
    TodoJournal.create(todo, "test")
    todo_jrnl = TodoJournal(todo)
    todo_jrnl.add_entry("Go buy milk")

    expected_todo = json.dumps(
        {
        "name": "test",
        "todos": ["Go buy milk"]
        },
        indent=4,
        ensure_ascii=False,)
    assert expected_todo == todo.read()
@pytest.fixture()
def todo_journal_with_3_entries(tmpdir):
    """3 entries"""
    todo_filename = "test_todo"
    todo_path = tmpdir.join(todo_filename)
    with open(todo_path, "w",encoding="utf-8") as file:
        json.dump(
            {
                "name": "test",
                "todos": ["first entry", "second_entry", "third entry"]
            },
            file,
            indent=4,
            ensure_ascii=False, )
    return todo_path
@pytest.fixture()
def todo_json_after_remove_second_entry():
    """remove second etry"""
    return json.dumps(
        {
            "name": "test",
            "todos": ["first entry", "third entry"]
        },
        indent=4,
        ensure_ascii=False, )
@pytest.fixture()
def todo_object_with_with_3_entries(todo_journal_with_3_entries):
    """object with 3 entries"""
    return TodoJournal(todo_journal_with_3_entries)
def test_remove_entry(todo_object_with_with_3_entries, todo_json_after_remove_second_entry):
    """testing removal of entries"""
    todo_object_with_with_3_entries.remove_entry(1)
    expected_todo_json_after_remove_second = todo_json_after_remove_second_entry
    assert expected_todo_json_after_remove_second == todo_object_with_with_3_entries.path.read()
def test_parse():
    """testing parse"""
    with pytest.raises(SystemExit):
        TodoJournal("./data/ggg")
def test_printt(tmpdir):
    """Testing nice output"""
    todo_filename = "test_todo"
    todo = tmpdir.join(todo_filename)
    TodoJournal.create(todo,"print")
    todo_jrnl=TodoJournal(todo)
    todo_jrnl.add_entry("test ent")
    expected_output='====TODOs====\ntest ent\n============='
    assert expected_output == todo_jrnl.print()
