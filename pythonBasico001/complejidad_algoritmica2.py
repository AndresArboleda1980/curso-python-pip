'''
En esta función vamos a contar lo que esta pasando dentro de este programa
Contamos los pasos
'''
def f(x)
    respuesta = 0 # 1     paso
#tenemos un loop que no depende de X asi que se ejecuta siempre 1000
    for i in range(1000):# 1000   pasos
        respuesta += 1
#tenemos este loop que depende del valor de X 
    for i in range(x):# X pasos
        respuesta += x
 #tenemos loop anidados que eso significa X.X   
    for i in range(x): # x pasos
        for j in range(x): # x pasos 
            respuesta += 1#1 OPERACIÓN
            respuesta += 1#1 OPERACIÓN
        # 2X**2
    return respuesta  # 1 OPERACIÓN
    '''
    Sumamos las operaciones menos las que ya se contaron en 2x**2
    1002 operaciones
    sumamos  las X
    1002+X+2X**2
    el siguiente paso es darle un valor a X para saber que tiene mas peso en la FORMULA  dada 
    de analisar las funciones
                    1002+X+2X**2

    '''    
