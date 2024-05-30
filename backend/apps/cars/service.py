import requests


def calc(a: int, b: int, operator: str) -> int:
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b


def get_cars():
    res = requests.get('http://owu.linkpc.net/carsAPI/v1/cars')

    if res.status_code == 200:
        return len(res.json())

    return 0
