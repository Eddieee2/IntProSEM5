capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
cantidad_años = int(input("Ingrese la cantidad de años: "))

tasa_decimal = tasa_interes_anual / 100
valor_compuesto = (1 + tasa_decimal) ** cantidad_años
monto_final = capital_inicial * valor_compuesto
interes_ganado = monto_final - capital_inicial

print("\nCapital inicial:", capital_inicial)
print("Tasa de interés anual:", tasa_interes_anual, "%")
print("Cantidad de años:", cantidad_años)
print("Monto final:", round(monto_final, 2))
print("Interés ganado:", round(interes_ganado, 2))