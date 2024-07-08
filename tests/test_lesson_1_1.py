import pytest
from classes_and_objects.lesson_1_1 import DataBase


@pytest.mark.parametrize("attribute, expected_value, expected_type", [
    ('pk', 1, int),
    ('title', "Классы и объекты", str),
    ('author', "Сергей Балакирев", str),
    ('views', 14356, int),
    ('comments', 12, int),
], ids=[
    "pk is 1",
    "title is 'Классы и объекты'",
    "author is 'Сергей Балакирев'",
    "views are 14356",
    "comments are 12"
])
def test_database_attributes_and_types(attribute, expected_value, expected_type, restore_database):
    assert getattr(DataBase, attribute) == expected_value
    assert isinstance(getattr(DataBase, attribute), expected_type)

