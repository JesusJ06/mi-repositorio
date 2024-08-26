# lista = [3,5,4,7,8,23]
# tupla = (3,5,4,7,8,23)
# sets = {3,5,4,7,8,23}
# diccionarios = {'x':2,'y':4}


# lista [2]=12
# print (lista)


# lista = [3,5,4,7,8,23]
# fibo = []
# fibo.append(7)
# print (fibo)


# lista = [3,5,4,7,8,23]
# fibo = [0,1]
# for i in range(9):
#     fibo.append (fibo[i]+fibo[i+1])
# print (fibo)



# numero=[]
# for i in range(5):
#     x=int("escriba el numero: ")
#     if x>10:
#         numero.append(x)
# print(numero)



# numeros=[4,5,2,7,21,32]
# numeros.insert(2,33)
# print(numeros)


# Ganadores=["CALIXTO","RUPERTO","CATARCIA","CALIXTO","CALIXTO",
#            "PLUTARDO","RUPERTO","CALIXTO","RUPERTO","CALIXTO"]
# Vendedores=["GABRIELA","LINDSAY","ANDRES","STEFHANIA","WILIAN","LUZ"]

# Vendedores.sort()
# print(Vendedores)

# print(Ganadores.count("CALIXTO"))
# podio=(Vendedores.index("LINDSAY"))
# if podio+1<3:
#     print(f"lindsay si esta en el podio con el puesto {podio+1}")
# else:
#     print(f"lindsay no esta en el podio con el puesto {podio+1}")


import random
P1=[]
P2=[]
for i in range(6):
    P1.append (random.randint(1,6))
    P2.append (random.randint(1,6))
contP1=P1.count(3)
contP2=P2.count(3)

if contP1 > contP2:
    print("El jugador 1 es el ganador con", contP1, "números 3")
elif contP2 > contP1:
    print("El jugador 2 es el ganador con", contP2, "números 3")
else:
    print("Es un empate", contP1, "números 3.")

print("Lista del jugador 1:", P1)
print("Lista del jugador 2:", P2)