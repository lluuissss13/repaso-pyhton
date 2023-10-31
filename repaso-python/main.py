print("Hola mundo, soy el amigo del Vega")
print("Hola mundo 1!!")


# Soy un comentario

print("Hola mundo2!!")

"""
Texto que no se va a interpretar
Texto que no se va a interpretar
Texto que no se va a interpretar
"""

#variables

texto = "Repaso de Python"
nombre = "Lluis Espinar"
altura = "190cm"
year = 2023

print(f"{texto} - {nombre} - {altura} {str(year)}")
print(texto + " - " + nombre + " - " + altura " - " + str(year))

#entrada
sitioweb = input("¿Cual es tu página web?: ")
print("El sitio web del usuario es: ") + sitioweb

#Condiciones
altura = 190

if altura >= 180:
    print("Eres una persona alta!!")

else: 
    print("Eres BAJITO!!")

# Funciones

def mostrarAltura():
    altura = int(input("Cual estu altura?: "))

    if altura>= 180:
        print("Eres una persona alta!!")
    else: 
    print("Eres BAJITO!!")