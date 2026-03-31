quantidades = [10, 2, 30, 4, 15]
item_critico = []
for n in quantidades:
     if n < 5:
        item_critico.append(n)
        print(f"Ítem Crítico: {item_critico}")