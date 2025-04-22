distancia_recorrida = float(input("Ingrese la distancia recorrida en kilómetros: "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos: "))

rendimiento = distancia_recorrida / litros_consumidos

precio_por_litro = 1.5 
gasto_total = litros_consumidos * precio_por_litro

print("\nDistancia recorrida:", distancia_recorrida, "km")
print("Litros consumidos:", litros_consumidos, "litros")
print("Precio por litro:", precio_por_litro, "moneda")

print("Rendimiento del vehículo:", round(rendimiento, 2), "km/l")
print("Gasto total en combustible:", round(gasto_total, 2), "moneda")