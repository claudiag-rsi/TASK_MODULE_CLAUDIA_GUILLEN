import pytest

from func import es_primo
# 8. Pruebas adicionales
@pytest.mark.parametrize("num, resultado", [
    (37, True),    # Número primo pequeño
    (1001, False), # Número compuesto grande (1001 = 7 * 11 * 13)
    (101, True),   # Número primo grande
    (0, False),    # Cero
    (1, False)     # Uno
])
def test_pruebas_adicionales(num, resultado):
    assert es_primo(num) == resultado, f"Error: {num} debería ser {'primo' if resultado else 'no primo'}"

@pytest.mark.parametrize("num, resultado", [
    (600851475143, False),  # Número compuesto grande (tiene factores primos como 71, 839, etc.)
])
def test_numero_compuesto_grande(num, resultado):
    assert es_primo(num) == resultado, f"Error: {num} debería ser {'primo' if resultado else 'no primo'}"

@pytest.mark.parametrize("num, resultado", [
    (1000000000, False)  # Número compuesto grande (mil millones, que es 2^9 * 5^9)
])
def test_numero_compuesto_muy_grande(num, resultado):
    assert es_primo(num) == resultado, f"Error: {num} debería ser {'primo' if resultado else 'no primo'}"

@pytest.mark.parametrize("num, resultado", [
    (982451653, True)  # Número primo grande (982451653 es un número primo cercano a mil millones)
])
def test_primo_extremadamente_grande(num, resultado):
    assert es_primo(num) == resultado, f"Error: {num} debería ser {'primo' if resultado else 'no primo'}"