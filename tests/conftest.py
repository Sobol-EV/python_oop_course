import pytest
from classes_and_objects.lesson_1_1 import DataBase
from classes_and_objects.lesson_1_2 import Goods


@pytest.fixture(scope='session')
def restore_database(test_data):
    original_values = test_data['database']
    yield original_values

    for attr, value in original_values.items():
        setattr(DataBase, attr, value)


@pytest.fixture(scope='session')
def restore_goods(test_data):
    original_values = test_data['goods']['original']
    yield original_values

    for attr, value in original_values.items():
        setattr(Goods, attr, value)

