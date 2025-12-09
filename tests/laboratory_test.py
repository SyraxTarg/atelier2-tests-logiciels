import pytest
from main import Laboratory

def test_init_labo_empty():
    #Arrange
    substances = []

    # Act
    with pytest.raises(Exception) as result:
        Laboratory(substances)

    # Assert
    assert str(result.value) == "List can't be empty"


def test_get_quantity():
    #Arrange
    substances = ["toto", "tata"]
    l = Laboratory(substances)

    # Act
    result = l.getQuantity("toto")
    # Assert
    assert result == 0


def test_get_quantity_error():
    #Arrange
    substances = ["toto", "tata"]
    l = Laboratory(substances)

    # Act
    with pytest.raises(Exception) as result:
        l.getQuantity("totjo")

    # Assert
    assert str(result.value) == "No such substance in stock"


def test_add():
    #Arrange
    substances = ["toto", "tata"]
    l = Laboratory(substances)

    # Act
    quantity = l.add("toto", 12)

    # Assert
    assert quantity == {"name": "toto", "quantity": 12}


def test_add_unknown_substance():
    #Arrange
    substances = ["toto", "tata"]
    l = Laboratory(substances)

    # Act
    with pytest.raises(Exception) as result:
        l.add("vsfd", 12.456)

    # Assert
    assert str(result.value) == "No such substance in stock"


def test_add_negative_number():
    #Arrange
    substances = ["toto", "tata"]
    l = Laboratory(substances)

    # Act
    with pytest.raises(Exception) as result:
        l.add("toto", -854)

    # Assert
    assert str(result.value) == "Impossible to add negative quantities"


def test_add_too_precise_number():
    #Arrange
    substances = ["toto", "tata"]
    l = Laboratory(substances)

    # Act
    with pytest.raises(Exception) as result:
        l.add("toto", 8.785412569854)

    # Assert
    assert str(result.value) == "The quantity must be rounded to a maximum of four decimal places."


def test_add_invalid_parameter_type():
    #Arrange
    substances = ["toto", "tata"]
    l = Laboratory(substances)

    # Act
    with pytest.raises(Exception) as result:
        l.add("toto", "2")

    # Assert
    assert str(result.value) == "The quantity must be a float and substance must be string"