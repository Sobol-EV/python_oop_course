import pytest
from classes_and_objects.lesson_1_2 import Goods

@pytest.mark.parametrize("attribute, expected_value, expected_type", [
    ('title', "Мороженое", str),
    ('weight', 154, int),
    ('tp', "Еда", str),
    ('price', 2048, int),
    ('inflation', 100, int),
], ids=[
    "title is 'Мороженое'",
    "weight is 154",
    "tp is 'Еда'",
    "price is 2048",
    "inflation is 100"
])

def test_goods_attributes_and_types(attribute, expected_value, expected_type, restore_goods):
    assert getattr(Goods, attribute) == expected_value
    assert isinstance(getattr(Goods, attribute), expected_type)

