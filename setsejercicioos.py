afiliados={"marla","paul","indira","piero","ruperto","luz",
           "miguel","esteban","monica","eladio","liz",
           "carla","jazmin","cirilo","leda","teofilo"}

deudores = {"leyla","rafael","marla","teofilo","gustavo",
            "ruperto","vera","eladio"}

extranjeros={"marla","eladio","indira","vera","gustavo","liz"}

# la empresa quiere saber cuales son los
# afiliadosque tienen deudad para eniviarles un memorando y allamado de atencion
# print( afiliados & deudores)

# # imprimir los afiliados que no son deudores
# print( afiliados - deudores)

# afiliados que sean deudores y extranjeros
# print(afiliados & deudores & extranjeros)

# lista de deudore que no son afiliados y tampoco extranjeros
print(deudores - extranjeros - afiliados)