def es_primo(num):
    # Verificar si es booleano
    if isinstance(num, bool):
        raise TypeError("El valor debe ser un número entero.")
    
    # Verificar si es float y está muy cerca de un entero
    if isinstance(num, float):
        if num.is_integer():
            num = int(num)
        else:
            # Verificar si está muy cerca de un entero
            rounded = round(num)
            if abs(num - rounded) < 1e-10:
                num = rounded
            else:
                raise TypeError("El valor debe ser un número entero.")
    
    # Verificar otros tipos no numéricos
    if not isinstance(num, int):
        raise TypeError("El valor debe ser un número entero.")
        
    # Lógica para determinar si es primo
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True




