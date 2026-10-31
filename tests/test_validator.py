from src.gps_validator.validator import is_valid_coord, find_coords

def test_all_valid_fixture_coords(valid_coords):
    for coord in valid_coords:
        assert is_valid_coord(coord) is True, f"должен быть валидным: {coord!r}"

def test_all_invalid_fixture_coords(invalid_coords):
    for coord in invalid_coords:
        assert is_valid_coord(coord) is False, f"должен быть невалидным: {coord!r}"

def test_find_coords_in_text():
    text = "Точка А: 55.7558, 37.6173. Точка Б: -33.8688, 151.2093."
    expected = ["55.7558, 37.6173", "-33.8688, 151.2093"]
    assert find_coords(text) == expected

def test_find_ignores_invalid_bounds():
    text = "Ошибка: 100.0, 200.0. Норма: 10.0, 20.0"
    assert find_coords(text) == ["10.0, 20.0"]