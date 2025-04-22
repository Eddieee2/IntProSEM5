total_litros_consumidos = float(input("Ingrese el total de litros consumidos en un mes en la vivienda: "))
cantidad_personas = int(input("Ingrese la cantidad de personas que viven en la casa: "))

consumo_mensual_por_persona = total_litros_consumidos / cantidad_personas
consumo_diario_por_persona = consumo_mensual_por_persona / 30

print("\nConsumo total del mes:", total_litros_consumidos, "litros")
print("Cantidad de personas en la vivienda:", cantidad_personas)
print("Consumo mensual por persona:", round(consumo_mensual_por_persona, 2), "litros")
print("Consumo diario por persona:", round(consumo_diario_por_persona, 2), "litros")