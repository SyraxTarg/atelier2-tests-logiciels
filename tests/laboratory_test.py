import pytest
from main import Laboratory

def test_init_labo_empty():
    #Arrange
    substances = []
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }

    # Act
    with pytest.raises(Exception) as result:
        Laboratory(substances, reactions)

    # Assert
    assert str(result.value) == "List can't be empty"


def test_get_quantity():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    result = l.getQuantity("toto")
    # Assert
    assert result == 0


def test_get_quantity_error():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    with pytest.raises(Exception) as result:
        l.getQuantity("totjo")

    # Assert
    assert str(result.value) == "No such substance in stock or reactions"


def test_add():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    quantity = l.add("toto", 12)

    # Assert
    assert quantity == {"name": "toto", "quantity": 12}


def test_add_decimal():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    quantity = l.add("toto", 12.1236)

    # Assert
    assert quantity == {"name": "toto", "quantity": 12.1236}


def test_add_unknown_substance():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    with pytest.raises(Exception) as result:
        l.add("vsfd", 12.456)

    # Assert
    assert str(result.value) == "No such substance in stock or reactions"


def test_add_negative_number():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    with pytest.raises(Exception) as result:
        l.add("toto", -854)

    # Assert
    assert str(result.value) == "Impossible to add negative quantities"


def test_add_too_precise_number():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    with pytest.raises(Exception) as result:
        l.add("toto", 8.785412569854)

    # Assert
    assert str(result.value) == "The quantity must be rounded to a maximum of four decimal places."


def test_add_invalid_parameter_type():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    with pytest.raises(Exception) as result:
        l.add("toto", "2")

    # Assert
    assert str(result.value) == "The quantity must be a float and substance must be string"


def test_add_reaction():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    quantity = l.add("tutu", 2)

    # Assert
    assert quantity == {"name": "tutu", "quantity": 2}


def test_add_reaction_non_existent():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)

    # Act
    with pytest.raises(Exception) as result:
        l.add("vsfd", 12.456)

    # Assert
    assert str(result.value) == "No such substance in stock or reactions"


def test_make():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)
    l.add("toto", 3)
    l.add("tata", 8)

    #Act
    result = l.make("tutu", 2)

    # Assert
    assert result == 2
    assert l.getQuantity("toto") == 1
    assert l.getQuantity("tata") == 4


def test_make_unknown_subs():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)
    l.add("toto", 3)
    l.add("tata", 8)

    # Act
    with pytest.raises(Exception) as result:
        l.make("plop", 2)

    assert str(result.value) == "No such substance in stock or reactions"


def test_make_too_few_ingredients():
    #Arrange
    substances = ["toto", "tata"]
    reactions = {
        "tutu" : [("toto", 1), ("tata", 2)]
    }
    l = Laboratory(substances, reactions)
    l.add("toto", 5)

    # Act
    with pytest.raises(Exception) as result:
        l.make("tutu", 1)

    assert str(result.value) == "Not enough tata, needed 2, possessed 0"