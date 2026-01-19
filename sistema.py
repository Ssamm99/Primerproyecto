import datetime

# 1. Obtener datos del sistema
hora_actual = datetime.datetime.now()

print("=======================================")
print(f"🚀 INICIANDO SISTEMA - {hora_actual.strftime('%Y-%m-%d %H:%M:%S')}")
print("=======================================")

# 2. Interacción con el usuario
usuario = input("Ingrese su nombre de usuario: ")
print(f"\n[+] Usuario '{usuario}' detectado.")

# 3. Una pequeña prueba matemática (estilo Calculus)
print("\n[?] Verificando capacidad de procesamiento...")
numero = float(input("Ingresa un número para calcular su cuadrado: "))
resultado = numero ** 2

print(f"\n✅ RESULTADO: El cuadrado de {numero} es {resultado}")
print("=======================================")
print("SISTEMA FINALIZADO EXITOSAMENTE")