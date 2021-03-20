"""
Nombre: Divisores 
Entrada: Num
Salida: resultado de la división
Restricción<: Número entero positivo
"""
def divisores(num):
    if(isinstance(num,int) and num>0):
        return divisores_aux(num,num)
    else:
        return "El número debe ser mayor a cero y positivo"

def divisores_aux(num,contador):   
    if contador==0:
        return None
    else:
        if(num%contador)==0:
            print(contador)
        return divisores_aux(num,contador-1)
#------------------------------------------------------------------------------------------------------    
"""
Nombre: Multiplicar Recursivo 
Entrada: Num,factor
Salida: El factor de los número 
Restricción: Número entero positivo
"""
def multiplicarRecursivo(num,factor):
    if(isinstance(num,int) and isinstance(factor,int)):
        return multiplicar_aux(num,factor)
    else:
        return "El número debe ser un entero positivo"

def multiplicar_aux(num,factor):
    if(factor==0):
        return 0
    else:
        return num+multiplicar_aux(num,factor-1)
#--------------------------------------------------------------------------------------------------------

"""
Nombre: división Recursivo
Entrada: divisor,dividendo 
Salida: La división entera de los números
Restricción<: Número entero positivo
"""
def divisionRecursivo(divisor,dividendo):
    if(isinstance(divisor,int) and isinstance(dividendo,int)):
        return divisionRecursivo_aux(divisor,dividendo,0)
    else:
        return "El número debe ser entero positivo"

def divisionRecursivo_aux(divisor,dividendo,contador):
    if(contador<=divisor):
        return 0
    elif(contador>divisor):
        return -1
    else:
        return 1+divisionRecursivo_aux(divisor,dividendo,contador+dividendo)

    
    
    
