import re
import sys

_COORD_RE = re.compile(
    r"(?<!\d)(?P<lat>-?\d{1,3}\.\d+)\s*,\s*(?P<lon>-?\d{1,3}\.\d+)(?!\d)"
)

def is_valid_coord(text: str) -> bool:
    match = _COORD_RE.fullmatch(text.strip())
    if not match:
        return False

    lat = float(match.group("lat"))
    lon = float(match.group("lon"))

    if not (-90.0 <= lat <= 90.0):
        return False
    if not (-180.0 <= lon <= 180.0):
        return False

    return True

def find_coords(text: str) -> list[str]:
    results = []
    for match in _COORD_RE.finditer(text):
        coord_str = match.group(0)
        if is_valid_coord(coord_str):
            results.append(coord_str)
    return results


def _interactive() -> None:
    print("Поиск GPS-координат")
    print("1) Проверить координаты")
    print("2) Найти координаты в файле")
    print("3) Найти координаты на сайте")

    choice = input("Выберите режим: ").strip()

    try:
        if choice == "1":
            coord = input("Введите координаты (например, 55.7558, 37.6173): ").strip()
            if is_valid_coord(coord):
                print("Результат: Координаты корректны.")
            else:
                print("Результат: Координаты НЕкорректны.")

        elif choice == "2":
            path = input("Введите путь к файлу: ").strip()
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            coords = find_coords(text)
            print(f"Найдено координат: {len(coords)}")
            for c in coords:
                print(" -", c)

        elif choice == "3":
            import requests
            url = input("Введите URL (http://...): ").strip()
            response = requests.get(url, timeout=10)
            coords = find_coords(response.text)
            print(f"Найдено координат: {len(coords)}")
            for c in coords[:5]:
                print(" -", c)
        else:
            print("Неверный выбор.")

    except Exception as exc:
        print(f"Ошибка: {exc}")

if __name__ == "__main__":
    _interactive()