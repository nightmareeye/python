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
