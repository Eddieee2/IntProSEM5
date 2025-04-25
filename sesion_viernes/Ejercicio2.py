sueldo = float(input("Ingrese el sueldo del empleado: "))
if sueldo > 3000:
    bono = sueldo * 0.10
elif sueldo > 1500:
    bono = sueldo * 0.05
else:
    bono = 0
    
print("El bono del empleado es:", bono)
print(f"Sueldo: {sueldo:.2f}, Bono: {bono:.2f}")
print(f"Salario total: {sueldo + bono}")