calificacion = float(input("Ingrese la calificacion del estudiante (0-10): "))

if calificacion >=9 and calificacion <=10:
    print("La calificacion es A")
elif calificacion >=7 and calificacion <=8:
    print("La calificacion es B")
elif calificacion >=5 and calificacion <=6:
    print("La calificacion es C")
elif calificacion >=3 and calificacion <=4:
    print("La calificacion es D")
elif calificacion >=0 and calificacion <=1:
    print("La calificacion es F")
else: 
    print("La calificacion no es valida")