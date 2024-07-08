import pytest
from classes_and_objects.lesson_1_4 import Notes


@pytest.mark.parametrize("attribute, expected_value", [
    ("uid", 1005435),
    ("title", "Шутка"),
    ("author", "И.С. Бах"),
    ("pages", 2),
])
def test_notes_attributes(attribute, expected_value):
    assert getattr(Notes, attribute) == expected_value


def test_getattr_author(capsys):
    author = getattr(Notes, "author")
    print(author)
    captured = capsys.readouterr()
    assert captured.out.strip() == "И.С. Бах"