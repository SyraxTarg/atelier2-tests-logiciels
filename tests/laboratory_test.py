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