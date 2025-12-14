# --- Plik: main.py ---
import product727  # Importujemy nasz plik product.py

# Test 1: "1082" -> 1+0+8=9. 9%7=2. Ostatnia cyfra to 2. Zgadza się (True).
print(f'f("1082") returns {product727.f("1082")}')

# Test 2: "2035" -> 2+0+3=5. 5%7=5. Ostatnia cyfra to 5. Zgadza się (True).
print(f'f("2035") returns {product727.f("2035")}')

# Test 3: "1114" -> 1+1+1=3. 3%7=3. Ostatnia cyfra to 4. Nie zgadza się (False).
print(f'f("1114") returns {product727.f("1114")}')

# Test 4: "7071" -> 7+0+7=14. 14%7=0. Ostatnia cyfra to 1. Nie zgadza się (False).
print(f'f("7071") returns {product727.f("7071")}')