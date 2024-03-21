nombre = input("Por favor escriba su nombre: ")

edad = input("Escriba su edad: ")

print ("Bienvenido {} Usted tiene {} años".format(nombre, edad))

_MAYORIA_EDAD = 16

# Esta constante sirve para conocer la edad máxima para acceder a taza preferencial para jovenes
_EDAD_MAXIMA_TAZA_PREF_JOVENES = 25

if int(edad) >= _MAYORIA_EDAD:
    print ("Usted es mayor de edad, puede obtener un crédito")
else:
    print ("Usted es menor de edad, NO puede obtener un crédito")

if int(edad) >= _MAYORIA_EDAD and int(edad) < _EDAD_MAXIMA_TAZA_PREF_JOVENES:
    print ("Por favor pregunte por la taza preferencial para jovenes")
    
if int(edad) >= _MAYORIA_EDAD:
    print ("Usted es mayor de edad, puede obtener un crédito")
    if int(edad) < _EDAD_MAXIMA_TAZA_PREF_JOVENES:
        print ("Por favor pregunte por la taza preferencial para jovenes")


