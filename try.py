# try:
#     resultado= 10/0
# except ZeroDivisionError:
# #     print("Error:No se puede división por cero")

# def iniciar_sesion(usuario, contraseña):
#     # Datos de inicio de sesion
#     ususario_correcto = "admin"
#     contraseña_correcta = "1234"
#     try: 
#         # Validar los datos del usuario
#         if usuario != ususario_correcto:
#             raise ValueError("El nombre de usuario incorrecto")
#         elif contraseña != contraseña_correcta:
#             raise ValueError("La contraseña incorrecta")
#         else:
#          print("Sesión iniciada correctamente")

#     except ValueError as e:
#         print(e)

# #  Ejemplo de uso:
# iniciar_sesion =("admin", "password") # Deberia iniciar esion corectamente
# iniciar_sesion =("usuario_incorrecto", "password") # deberia mostrar un mensaje de error
