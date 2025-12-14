# --- Plik: calculations.py ---

def f(number1, number2, operator):
    # Sprawdzamy po kolei, jaki to operator
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        # Operator % to reszta z dzielenia
        return number1 % number2
    elif operator == "**":
        # Operator ** to potęgowanie
        return number1 ** number2
    else:
        return None  # Jeśli podano nieznany znak