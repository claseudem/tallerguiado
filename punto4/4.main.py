alcancia = [100, 200, 500]
meta = 1000

total = sum(alcancia)

if total >= meta:
    print("¡Felicidades! Alcanzaste tu meta de ahorro.")
else:
    falta = meta - total
    print(f"Te faltan {falta} pesos para alcanzar tu objetivo.")