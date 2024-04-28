def check_palindrome(string):
    # Paso 1: Filtrar la cadena para conservar solo caracteres alfanuméricos
    # isalnum() es un método de las cadenas de texto en Python que retorna True si todos los caracteres en la cadena  son alfanuméricos (es decir, letras o números), y False en caso contrario.
    filtered_string = ''.join(char for char in string if char.isalnum())
    
    # Paso 2: Convertir la cadena filtrada a minúsculas
    filtered_string = filtered_string.lower() 
    
    # Paso 3: Sustituir los caracteres acentuados por sus equivalentes sin acento
    filtered_string = filtered_string.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    
    # Paso 4: Verificar si la cadena filtrada es igual a su imagen reflejada
    return filtered_string == filtered_string[::-1]

#pide una frase al usuario 
phrase = input("Enter a phrase to check if it is a palindrome: ")

#verifica si es palindromo
if check_palindrome(phrase):
    print(f'"{phrase}" is a palindrome.')
else:
    print(f'"{phrase}" is not a palindrome.')
