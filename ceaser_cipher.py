import caesar_logo  # Importa el módulo caesar_logo (considera usar minúsculas para los nombres de módulos)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Obtiene el logo del módulo caesar_logo
new_logo = caesar_logo.logo
print(new_logo)

def caesar():
    direction = input("Escribe 'encode' para cifrar, escribe 'decode' para descifrar:\n").lower()  # Pide al usuario la dirección de la operación y conviértela a minúsculas
    text = input("Escribe tu mensaje:\n").lower()  # Pide al usuario el mensaje y conviértelo a minúsculas
    shift = int(input("Escribe el número de desplazamiento:\n"))
    resultado = ""  # Utiliza un nombre de variable más descriptivo que 'string'

    for letter in text:
        if letter not in alphabet:
            resultado += letter  # Agrega caracteres que no están en el alfabeto directamente al resultado
        else:
            indice = alphabet.index(letter)
            if direction == "encode":
                nuevo_indice = (indice + shift) % 26  # Usa el operador módulo para el desplazamiento circular dentro del alfabeto
            elif direction == "decode":
                nuevo_indice = (indice - shift) % 26

            resultado += alphabet[nuevo_indice]

    print(f"Tu mensaje {direction}ado es: {resultado}")  # Ajusta el formato de salida del mensaje

loop = True
while loop:
    caesar()
    preguntar = input("\n¿Quieres cifrar o descifrar de nuevo? Escribe 'yes' o 'no': ").lower()
    if preguntar == "yes":
        continue
    elif preguntar == "no":
        print("ADIOS")
        loop = False

