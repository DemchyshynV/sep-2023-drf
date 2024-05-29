def calc(a: int, b: int, operator: str) -> int:
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
