import pytest
from classes_and_objects.lesson_1_3 import Car


@pytest.mark.parametrize("attribute, expected_value", [
    ("model", "Тойота"),
    ("color", "Розовый"),
    ("number", "П111УУ77"),
])


def test_car_attributes(attribute, expected_value):
    assert getattr(Car, attribute) == expected_value


def test_car_color_output(capsys):
    print(Car.__dict__["color"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Розовый"