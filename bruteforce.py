import itertools
import string
import time

password = input("ingrese la contraseña para verificar que tan segura es: ")
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%"
start = time.time()  
attempts = 0

for length in range(1, 9):  
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        attempt = ''.join(guess)
        if attempt == password:
            elapsed = time.time() - start
            print(f"Contraseña encontrada: {attempt}")
            print(f"Intentos: {attempts}")
            print(f"Tiempo: {elapsed:.4f} segundos")
            exit()

print("No se encontró la contraseña en el rango definido.")